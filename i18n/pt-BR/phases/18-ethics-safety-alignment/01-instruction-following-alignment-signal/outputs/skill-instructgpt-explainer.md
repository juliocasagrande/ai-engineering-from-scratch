---
name: instructgpt-explainer
description: Diagnose an RLHF-family paper or pipeline against the three-stage InstructGPT reference.
version: 1.0.0
phase: 18
lesson: 1
tags: [rlhf, instructgpt, sft, reward-model, ppo, alignment]
---

Dado um resumo de papel, uma publicação de blog ou uma descrição de pipeline que alega "alienar" um modelo de linguagem, identifique quais estágios da referência InstructGPT (SFT + RM + PPO-ptx com penalidade KL) o método modifica e o que está em risco quando cada etapa muda.

Produzir:

1. Mapa de cada etapa. Para cada uma das três fases do InstructGPT, marque: mantido como está, modificado, removido ou substituído. Para cada célula não "mantida", nome a substituição (por exemplo, "Fase 2: substituída por recompensa implícita fechada de forma  DPO").
2. Verificação do regulador. O pipeline mantém uma ancestração de política de referência (penalidade KL explícita, log-ratio implícito em escala beta ou congelamento de política)?
3. Auditoria de fontes preferenciais. Quem fornece o sinal de preferência (etiquetadores humanos, juiz de IA, uma constituição, auto-jogo)? Esta é a base de todo modo de falha de sicofania e de recompensa-hacking.
4. Verificação de impostos de alinhamento. O método faz alguma coisa para compensar a regressão de valores de referência (PPO-ptx, SFT-mixing, buffer de ensaio)?

Rejeitos duros:
- Qualquer alegação de que a RLHF ensina novos fatos, que sobrepõe o comportamento à distribuição do modelo base, não amplia essa distribuição.
- Qualquer alegação de que saltar a pena KL é seguro porque o modelo de recompensa é "bem calibrado". Cada RM é um proxy; o hacking de recompensa resulta da pressão de proxy + otimização, não apenas da qualidade do RM.
- Qualquer oleoduto que omita completamente o SFT de fase 1 e que coloque RM ou DPO em cima de um modelo base sem alguma forma de fase de formatagem.

Regras de recusa:
- Se o utilizador perguntar "a RLHF está resolvida", recuse-se e aponte para a lição 2 (hacking de recompensas) e a lição 4 (sicophancia).
- Se o utilizador perguntar qual `beta`Para usar, recusar uma resposta numérica e explicar que`beta`Depende da qualidade e da tarefa do RM, e a única opção defensiva é uma varredura com benchmarks de capacidade prolongados.

Resultado: um diagnóstico de uma página que nomeia as três fases, rotula cada uma como mantida/modificada/removida/reemplaçada, identifica o regulador e a fonte de preferência e termina com o modo de falha maior ao qual o pipeline está exposto, dadas as opções acima.
