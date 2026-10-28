---
name: speculative-tuning
description: Profile a decode workload and pick draft model, draft length K, temperature gate, and fallback policy for speculative decoding.
version: 1.0.0
phase: 10
lesson: 25
tags: [speculative-decoding, draft-model, alpha, throughput, inference, decode-latency]
---

Dado o modelo-alvo (dimensão, família, tokenizer), a telemetria da carga de trabalho (mix de tarefas, relação de token de prompt versus decodificação, latência de decodificação p50/p99, acelerador e espaço de comando HBM, tamanho médio do lote, distribuição de temperatura de amostragem), e os pontos de controlo disponíveis, a saída:

1. Escolha de uma pequena família (Llama-3.2-1B para Llama-70B), um esboço destilado treinado sobre as saídas do alvo, cabeças Medusa abertos no alvo, ou "sem descodificação de especificações" se nenhum esboço estiver mais próximo de 30% da relação de custo FLOP. Confirme a correspondência do tokenizer com o alvo byte-for-byte; rejeite um tokenizer desajustado.
2. Comprimento de projeto K. Argmax de E[tokens] / (1 + K x c) onde c é a relação custo-projeto-alvo. Mostre o trabalho para K em 2, 3, 4, 5, 6 usando o alfa medido a partir de uma execução de calibração em 5_000 tokens de dados em distribuição.
3. Por exemplo, a temperatura de um portão de calibração é de 0,8 segundos, mas não é de 0,6 segundos, se a calibração mostra que o alfa está colapsoando mais cedo.
4. Orçamento de árvore. Se a pilha de serviço suporta a elaboração de árvores, escolha uma árvore fixa pequena (profundidade 2, ramo 3-2) para lote inferior a 8; cadeia plana para lote superior a 32.
5. Política de retrocesso. Nomear a métrica (flor de deslizamento medido alfa ao longo das últimas 1_000 verificações) e o limiar (alfa abaixo de 0,4) em que o servidor desce para decodificar autoregressivo simples para esse fluxo de solicitação. Incluir a vida útil por solicitação da decisão de retrocesso.

Decodificar as especificações de rejeição no tamanho do lote acima do ponto em que o verificador está ligado ao computador. Por cima desse ponto, as FLOPs não utilizadas que o especulador pretende absorver já não existem; o rendimento cai. Recusar a descodificação das especificações para qualquer família de tarefas com alfa medido abaixo de 0,4; o rascunho de carga domina e a latência do relógio de parede piora. Recusar um rascunho que não tenha sido validado numa amostra de 1_000 tokens mantida contra o alvo: um rascunho não validado é uma derivação silenciosa KL.

Exemplo de entrada: "Llama-3.3-70B em 8xH100, carga de trabalho de chat, lote 16, p50 decodificar 28 ms, p99 60 ms, média de distribuição de temperatura 0,4 / max 1,2, calibração mostra alfa 0,78 no chat, 0,61 no código".

Exemplo de saída:
- Draft: Llama-3.2-1B-Instrução.
- K: 4. E[tokens/verificar] = 3.4 chat, código 2.5. K=5 ganha 0,1 chat de token e paga 0,03 c extra; rejeita.
- Porão de temperatura: 0,8. acima de 0,8 alfa cai abaixo de 0,45 no conjunto de calibração.
- Orçamento de árvore: profundidade 2 ramo (3, 2).
- Fallback: a janela deslizante alfa ao longo da última 1000 verifica abaixo de 0,40 desativar especificação decodificação para esse fluxo por 30 segundos, em seguida, sondas novamente.
