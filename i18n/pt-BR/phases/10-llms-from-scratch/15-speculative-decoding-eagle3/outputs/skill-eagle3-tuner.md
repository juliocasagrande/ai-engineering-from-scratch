---
name: eagle3-tuner
description: Pick and tune a speculative decoding strategy (vanilla / Medusa / EAGLE-1/2/3 / lookahead) for a new inference workload.
version: 1.0.0
phase: 10
lesson: 15
tags: [speculative-decoding, eagle, eagle-3, medusa, inference, vllm, sglang, tensorrt-llm]
---

Dada uma meta de inferência de produção (modelo de verificador, tamanho de lote, perfil de comprimento de sequência, latência de decodificação de p50/p99, acelerador, intervalo alfa esperado da telemetria, mistura de tarefas), recomendamos uma estratégia de decodificação especulativa e parâmetros de sintonização.

Produzir:

1. Família de projetos. Escolha entre a baunilha, Medusa, EAGLE-1, EAGLE-2, EAGLE-3, ou lookahead. Justifique usando telemetria alfa (ou uma estimativa calibrada), custo de treinamento disponível (nenhum, pequeno SFT, total 60B + token run), e se os verificadores enviam um projeto publicado (existem pontos de verificação EAGLE-3 para Llama 3.1/3.3, DeepSeek-V3, Qwen 2.5, Qwen 3).
2. Longitude de projeto N. Escolha o número inteiro N que minimiza o tempo esperado de parede por token dado alfa e a relação custo projeto-verificador c: minimizar (1 + N*c) / ((1 - alfa^(N+1)) / (1 - alfa)). Mostre o trabalho para três valores N candidatos em torno do ideal.
3. Parâmetros de busca de árvore se EAGLE-2/3. Escolha a profundidade da árvore e o fator de ramificação para permanecer dentro do orçamento de memória.
4. Quando a temperatura > 0,8, o alfa desabate. Recomenda-se desactivar a descodificação das especificações acima de um limiar calibrado, ou mudar para uma árvore mais ampla com ramificação inferior por nó.
5. Plano de retrocesso de KV. Nomear a implementação específica do cache de KV (buffer de arranque do vLLM vs. sequência de comprimento lógico do TensorRT-LLM) e confirmar que suporta rejeição em lote na simultaneidade alvo.

Rejeitos duros:
- Qualquer recomendação que altera a distribuição de saída do verificador (por exemplo, descodificação aproximada das especificações, rejeição relaxada).
- Decodificação de especificações no lote 1 num único modelo pequeno, quando o custo do projecto exceda o custo do verificador economizado.
- A EAGLE com um projeto de ponto de controlo treinado contra um tokenizer ou revisão de modelo base diferente do verificador.
- A execução de descodificação de especificações sem rollback KV  irá corromper silenciosamente os tokens subsequentes.

Regras de recusa:
- Se a telemetria alfa não estiver disponível E o mix de tarefas for escrita criativa de alta temperatura, recuse a recomendação e solicite uma execução de calibração primeiro.
- Se o verificador for menor que os parâmetros densos 7B, recomenda-se desativar o decodificação das especificações em vez de escolher uma estratégia.
- Se a pilha de serviço não suportar a família de projetos escolhida (por exemplo, versão vLLM sem EAGLE-3), rebaixar para EAGLE-2 em vez de pedir ao usuário que reconstruia a pilha.

Resultado: uma recomendação de uma página listando o projeto de família, N, forma da árvore (se aplicável), confirmação de rollback KV e o intervalo de aceleração esperado.
