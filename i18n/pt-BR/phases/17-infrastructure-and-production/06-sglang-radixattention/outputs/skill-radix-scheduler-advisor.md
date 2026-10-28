---
name: radix-scheduler-advisor
description: Aconselhar sobre a adoção de SGLang e a disciplina de ordenação rápida para cargas de trabalho pesadas de prefixos que desejam a reutilização do cache da RadixAttention.
version: 1.0.0
phase: 17
lesson: 06
tags: [sglang, radixattention, prefix-caching, scheduler, prompt-ordering]
---

Dada uma descrição da carga de trabalho (forma do modelo de instrução, padrão de recuperação, comprimento da conversa, número de inquilinos simultâneos, hardware), produzir um aviso de adoção SGLang / RadixAttention.

Produzir:

1. Carga de trabalho impressão digital. Classificar como prefixo pesado (RAG com preâmbulo repetido, agentes com esquemas de ferramentas repetidas, voz com contexto repetido) ou prefixo-luz (impulsações únicas de um só tiro). Nomear o comprimento do prefixo compartilhado e a taxa de repetição.
2. Auditoria de ordens de prompt. Siga o modelo de prompt atual de cima para baixo. Marque qualquer conteúdo dinâmico entrelaçado na seção imutável. Recomenda ordem canônica: sistema → ferramentas / esquemas → contexto de recuperação → histórico de conversa → entrada do usuário.
3. Taxa de hits esperada. A partir da impressão digital da carga de trabalho, estimar a taxa de hits no cache alcançável. Chat geral 10-30%. RAG com modelo consistente 60-85%. Voz/visão com preâmbulo fixo 80-95%.
4. Se a taxa de impacto esperada for superior a 40% e a carga de trabalho não for única, recomendamos a SGLang. `--enable-prefix-caching` Se for 30-40%, dê uma amostra e escolha.
5. Plano de implantação. SGLang de 48 horas de referência sombra com modelo de prompt atual. Registo de taxa de hits. Corrigir problemas de ordens de prompt. Re-referência. Envio se a taxa de hits limpa o alvo.

Rejeitos duros:
- Recomendar SGLang sem medir a partilha de préfixos no tráfego.
- Reclamar o número de 6,4x sem citar a forma da carga de trabalho.
- Ignorar a disciplina de ordenação rápida. O modelo é a chave de cache; sem ele o agendador não pode ajudar.

Regras de recusa:
- Se a carga de trabalho for única (sem pedido repetido do sistema), recuse o SGLang e recomenda o vLLM.
- Se a equipe não puder controlar o modelo de solicitação (consumidor de terceiros), recusar e recomendar a normalização do modelo de nível proxy antes de revisitar.
- Se o isolamento de vários inquilinos requer pools separados de KV por inquilino, note que a SGLang o apoia, mas o despejo de ramos de árvores pode matar de fome inquilinos menores; recomendo a alocação de orçamento por inquilino.

Resultado: uma lista de um SGLang de uma página de impressão digital de carga de trabalho, correções de ordenação de prompt, taxa de acidente esperada, escolha do motor e plano de implantação.
