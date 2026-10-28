---
name: dp-solver
description: Resolva um pequeno MDP tabuleiro exatamente através da iteração de política ou iteração de valor.
version: 1.0.0
phase: 9
lesson: 2
tags: [rl, dynamic-programming, bellman]
---

Dado um MDP com um modelo conhecido, saída:

1. Iteração de política versus iteração de valor. Razão ligada a S, ChoiceA, G.
2. Inicialização, V0 - inicialização, sensibilidade à convergência.
3. Paragem, tolerância supernormal, número esperado de varreduras.
4. Verificação, calculado exatamente, política gananciosa extraída.
5. Utilização: como esta linha de base será utilizada para depurar/avaliação de métodos baseados em amostragem.

Recusar a execução de DP em espaços de estado > 107. Recusar a reivindicação de convergência sem uma verificação de sup-norma. Marcar qualquer γ ≥ 1 em uma tarefa de horizonte infinito como uma violação de garantia.
