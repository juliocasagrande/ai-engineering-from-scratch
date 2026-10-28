---
name: dualpipe-planner
description: Plan a pipeline parallelism strategy (1F1B, Zero Bubble, DualPipe, DualPipeV) for a training cluster.
version: 1.0.0
phase: 10
lesson: 19
tags: [pipeline-parallelism, dualpipe, dualpipev, zero-bubble, expert-parallelism, distributed-training]
---

Dado o número total de camadas de treinamento (contagem de GPU, topologia de interconexão, modelo de acelerador, memória por GPU), uma forma do modelo (parâmetros totais, parâmetros ativos, MoE ou densidade, número esperado de camadas) e um volume de dados de treinamento-alvo, recomendamos uma estratégia de paralelismo de pipeline e confirmamos a fração de bolha esperada.

Produzir:

1. Profundeza do pipeline P. Selecionar com base no orçamento de memória da GPU (deve caber um estágio do pipeline por classificação), MoE vs densidade e largura de banda de interconexão.
2. Contagem de micro-parceiras M. Deve ser divisível por 2 para DualPipe e DualPipeV. Relação típica M/P entre 8 e 16.
3. Seleção de programação. Escolha entre 1F1B, Zero Bubble, DualPipe, DualPipeV. Tabela de decisão: treinamento denso sob 500 GPUs -> Zero Bubble. MoE com paralelismo especialista -> DualPipe. Treinamento denso acima de 500 GPUs sem pesado tudo para tudo -> DualPipeV. Pequenas corridas sob 100 GPUs -> 1F1B está bem.
4. Fração de bolha esperada. Calcule o horário escolhido no objetivo P e M. Relata como percentagem e como horas de GPU absolutas economizadas em relação a 1F1B no orçamento total de treinamento.
5. Plano de replicação de parâmetros (apenas DualPipe). Confirme que a replicação de parâmetros 2x se encaixa na VRAM disponível. Relate a densidade de parâmetros efetiva por GPU dada a P escolhida.

Rejeitos duros:
- A duplicação de 2x não é justificada sem comunicações pesadas para EP.
- P > 64 em qualquer curso de treinamento.
- A contagem de micro-partidas não divisível por 2 para DualPipe/DualPipeV. O cronograma não será encerrado.
- Paralelamente de pipeline quando o modelo se encaixa na memória de uma GPU.

Regras de recusa:
- Se a interligação for de 200Gbps ou mais lenta por GPU, rejeite o DualPipe e recomenda o DualPipeV. A janela de sobreposição de tudo para tudo é muito estreita para justificar a replicação.
- Se o usuário não puder fornecer um kernel personalizado completo adequado à sua topologia de cluster, recomenda a Zero Bubble em vez do DualPipe.
- Se a execução de treinamento for inferior a tokens 1B, rejeite completamente o planejamento de paralelismo de pipeline e recomenda o paralelismo de dados mais o paralelismo tensor.

Resultado: um plano de uma página listando P, M, cronograma, fração de bolha esperada, custo de replicação de parâmetros (se DualPipe), e uma recomendação de kernel total. Terceiro com um parágrafo "gato de retorno" nomeando a métrica de utilização específica (percentagem de utilização de GPU agregada, medida durante as primeiras 1000 etapas) que justificaria a mudança para um cronograma mais simples se o número-alvo não for atingido.
