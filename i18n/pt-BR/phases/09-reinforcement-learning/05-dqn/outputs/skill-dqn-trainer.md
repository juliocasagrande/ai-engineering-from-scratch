---
name: dqn-trainer
description: Produce a DQN training config (buffer, target sync, ε schedule, reward clipping) for a discrete-action RL task.
version: 1.0.0
phase: 9
lesson: 5
tags: [rl, dqn, deep-rl]
---

Dado um ambiente de ação discreta (forma de observação, contagem de ação, horizonte, escala de recompensa), saída:

1. Rede. Arquitetura (MLP / CNN / Transformer), características fracas, profundidade.
2. Capacidade, tamanho do minibatch, tamanho do aquecimento.
3. Rede de alvo: estratégia de sincronização (difícil em cada passo C ou suave τ).
4. Exploração. ε começo / fim / comprimento do cronograma.
5. Perda, Huber vs MSE, valor de clip de gradiente, regra de recorte de recompensa.
6. Duplo DQN. Acionado por padrão, a menos que haja razão explícita para desativar.

Recusar o envio de um DQN sem rede-alvo, sem buffer de repetição ou mantido em ε. Recusar tarefas de ação contínua (ruta para SAC / TD3). Marque qualquer intervalo de recompensa > 10x por etapa como necessária de corte ou normalização de escala.
