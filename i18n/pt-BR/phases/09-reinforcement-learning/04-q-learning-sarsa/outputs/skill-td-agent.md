---
name: td-agent
description: Escolha entre Q-learning, SARSA, esperado SARSA para uma tarefa de RL tabuleira ou de pequena dimensão.
version: 1.0.0
phase: 9
lesson: 4
tags: [rl, td-learning, q-learning, sarsa]
---

Em um ambiente de tabela ou de pequenas características, a saída:

1. Algoritmo. Q-learning / SARSA / Expected SARSA / n-step variant. Razão de uma frase ligada à política vs. fora da política e à variância.
2. Hiperparametros. α, γ, ε, calendário de decomposição.
3. Inicialização. Valor Q_0 (optimista vs zero) e justificação.
4. Diagnóstico de convergência. `|Q - Q*|` Verifique se o DP é possível.
5. Como será a exploração se comportar na inferência?

Recusar a aplicação de TD tabuleiro a espaços de estado > 106. Recusar a envio de um agente de aprendizagem Q sem uma advertença de viés máximo. Marcar qualquer agente treinado com ε mantido em 1,0 durante toda a fase (sem fase de exploração).
