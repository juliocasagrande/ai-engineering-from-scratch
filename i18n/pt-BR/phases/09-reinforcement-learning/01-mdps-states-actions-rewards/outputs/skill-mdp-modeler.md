---
name: mdp-modeler
description: Dado uma descrição da tarefa, produzir uma especificação do processo de decisão de Markov e os riscos de formulação de bandeira antes do treinamento.
version: 1.0.0
phase: 9
lesson: 1
tags: [rl, mdp, modeling]
---

Dada uma tarefa (controle / jogo / recomendação / ajuste fino do LLM), saída:

1. Estado, vetor de características exato ou tensor especifica justificar propriedade Markov.
2. Ação, conjunto discreto ou intervalo contínuo, dimensão.
3. Transição, determinista, estocástica com modelo conhecido, ou apenas amostra.
4. Recompensa, função e fonte, Sparse vs. Formulário, Terminal vs.
5. Desconto, valor e justificação do horizonte.

Recusar-se a enviar qualquer MDP onde o estado não é marcovia sem menção explícita de frame-stacking ou estado recorrente. Recusar qualquer recompensa que não foi definida em termos do resultado alvo. `γ ≥ 1.0` Marque qualquer intervalo de recompensa > 100x a recompensa típica de passo como uma fonte provável de explosão de gradiente.
