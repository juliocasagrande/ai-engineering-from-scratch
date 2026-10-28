---
name: policy-gradient-trainer
description: Produce a REINFORCE / actor-critic / PPO training config for a given task and diagnose variance issues.
version: 1.0.0
phase: 9
lesson: 6
tags: [rl, policy-gradient, reinforce]
---

Dado um ambiente (ações discretas / contínuas, horizonte, estatísticas de recompensa), saída:

1. Chefe de política: Softmax (discreto) ou Gaussian (contínuo) com contagem de parâmetros.
2. Nenhum (vanilha), correndo médio, aprendido.`V̂(s)`, ou crítico A2C.
3. Controle de variação, recompensas por padrão, normalização de retorno, valor de clip de gradiente.
4. Bónus de entropia, coeficiente β e horário de decomposição.
5. Tamanho do lote, episódios por atualização, contrato de actualização dos dados da política.

Rejeitar o REINFORCE- no- baseline em horizontes > 500 passos. Rejeitar o controlo de ação contínua com uma cabeça softmax.`β = 0`e entropia de política observada < 0,1 como entropia-collapso.
