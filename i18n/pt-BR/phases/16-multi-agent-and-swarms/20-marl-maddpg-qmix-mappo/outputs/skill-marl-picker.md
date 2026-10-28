---
name: marl-picker
description: Escolha um algoritmo MARL (MADDPG, QMIX, MAPPO, IQL ou extensões) para uma determinada tarefa multi-agente. Considere cooperativa versus competitiva, tipo de espaço de ação, heterogeneidade, estrutura de recompensa e escala.
version: 1.0.0
phase: 16
lesson: 20
tags: [multi-agent, MARL, MADDPG, QMIX, MAPPO, CTDE]
---

Dada uma descrição de tarefa multi-agente, escolha o algoritmo MARL.

Produzir:

1. **Task taxonomy.** Completamente cooperativa (recompensa partilhada), totalmente competitiva (sumada zero), mista, sumada geral. Número de agentes. Homogéneo versus heterogéneo.
2. **Observability.** Pleno (cada agente vê o estado global), parcial (cada um vê apenas a sua própria observação) ou habilitado para comunicação.
3. **Action space.** Discreto (como Atari, SMAC) ou contínuo (mundo de partículas, MuJoCo). Afeta a escolha do algoritmo.
4. **Reward structure.** Dense (formado por passo) vs. scarse (apenas terminal). Dense torna o MAPPO prático; scarse necessita de ajuda de atribuição de crédito (decompositividade de valor do QMIX).
5. **Algorithm recommendation.** Comece com o MAPPO como linha de base para Yu et al. 2022.
   - QMIX quando for necessária uma atribuição de crédito cooperativa + homogênea + forte de recompensas escassas
   - MADDPG quando misturado (cooperação + concorrência) + acções contínuas
   - Extensões (QTRAN, QPLEX, FACMAC) quando a restrição de monotonia é demasiado restritiva
6. **Training infrastructure.** Se não tiver, recomenda políticas de nível imediato para os agentes de LLM.
7. **Deployment contract.** CTDE: no momento da implantação, cada agente só vê observação local. Escreva o contrato explicitamente para que o código de tempo de execução o respeite.

Rejeitos duros:

- Escolher uma linha de base não-MAPPO para uma primeira corrida.
- Utilização do QMIX para tarefas mistas cooperativas e competitivas.
- Recomendação de formação MARL para sistemas de agentes LLM que carecem de dados de interação ou de sinal de recompensa.
- Treinar sem registar observações e ações por agente.

Regras de recusa:

- Se a tarefa tiver menos de ~1000 episódios de dados de interação, recomenda políticas de nível imediato ou ajustes finos supervisionados.
- Se a tarefa não for marcovita (requer memória), mas a recomendação não inclui críticos recorrentes, marque a lacuna.
- Se a tarefa for competitiva em suma geral (equilíbrios múltiplos), a MARL não escolhe apenas uma; recomenda a concepção de mecanismos ou a selecção de equilíbrio.

Output: um resumo de uma página. Comece com uma recomendação de uma frase ("linha de base de MAPPO com função de valor centralizada; ator discreto por agente; CTDE na implantação; 5 sementes por experimento. "), em seguida, as sete seções acima. Termine com um pipeline de treinamento para implantação: coleta de dados, treinamento, avaliação, implantação.
