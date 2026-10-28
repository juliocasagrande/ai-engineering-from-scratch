---
name: game-rl-designer
description: Desenhar um canal de treinamento de jogo-RL ou raciocínio-RL (AlphaZero / MuZero / GRPO) para um determinado domínio.
version: 1.0.0
phase: 9
lesson: 12
tags: [rl, alphazero, muzero, grpo, self-play]
---

Dado um alvo (jogo de informação perfeita / informação imperfeita / Atari / raciocínio LLM / combinatório), saída:

1. - Regras conhecidas, Markov, Stochastic, Multi-Agent, informando AlphaZero contra MuZero contra GRPO.
2. Estratégia de busca: MCTS, Gumbel-sampled, best-of-N, ou nenhum.
3. Plano de auto- jogação. Simétrico auto- jogação / liga / dados offline / verificador gerado.
4. O objetivo é o sinal. Resultado do jogo / recompensa do verificador / preferência / modelo aprendido. Incluir um plano de robustez.
5. Diagnóstico: taxa de vitória versus linha de base, curva ELO, taxa de aprovação do verificador, KL para referência.

Rejeitar AlphaZero em jogos de informação imperfeita (ruta para CFR). Rejeitar GRPO sem um verificador confiável. Rejeitar qualquer pipeline de jogo-RL sem um conjunto fixo de oponentes de linha de base (auto-play ELO não é calibrado de outra forma).
