---
name: marl-architect
description: Escolha o regime de RL multi-agente certo (IPPO, CTDE, auto-jogue, liga) para uma determinada tarefa.
version: 1.0.0
phase: 9
lesson: 10
tags: [rl, multi-agent, marl, self-play]
---

Dado uma tarefa com `n` Agentes, saída:

1. Classificação do regime: cooperativa/adversária/sumada geral.
2. Algoritmo: IPPO / MAPPO / QMIX / auto-jogo / liga. Razão ligada à aderência e estrutura de recompensa.
3. Acessos à informação: formação centralizada (que informação global vai para o crítico)? execução descentralizada?
4. A atribuição de crédito, base contrafactual, decomposição de valor ou formação de recompensa.
5. Plano de exploração, entropia por agente, treinamento baseado na população, ou liga.

Recusar a aprendizagem Q independente em tarefas cooperativas fortemente ligadas. Recusar recomendar o auto-joio para soma geral com riscos de ciclo. Marcar qualquer pipeline MARL sem uma avaliação fixa do oponente (números de auto-joio escolhidos em cereja são comuns).
