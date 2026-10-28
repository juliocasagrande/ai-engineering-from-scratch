---
name: mc-evaluator
description: Evaluate a policy via Monte Carlo rollouts and produce a convergence report with DP-comparison if available.
version: 1.0.0
phase: 9
lesson: 3
tags: [rl, monte-carlo, evaluation]
---

Dado um ambiente (episódico, com API de reset+passo) e uma política, saída:

1. Método, primeira visita vs. MC de cada visita.
2. Orçamento do episódio, número de alvo, diagnóstico de variância, erro padrão esperado.
3. Plano de exploração. ε programa (se necessário) ou início de exploração.
4. Comparador padrão de ouro. DP-óptimo V* se tabuleiro; caso contrário, um limite de uma linha de base de Q-learning / PPO.
5. Verificação de terminação, limite máximo de passos, temporadas, manuseio de trajetórias não terminantes.

Recusar-se a executar MC em tarefas não episódicas sem um limite de horizonte finito. Recusar-se a relatar estimativas V^π de menos de 100 episódios por estado para tarefas tabuleiras. Marcar qualquer política com ações de variação zero como um risco de exploração.
