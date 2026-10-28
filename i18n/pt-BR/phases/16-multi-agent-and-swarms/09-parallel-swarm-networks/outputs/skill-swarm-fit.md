---
name: swarm-fit
description: Decidir se uma tarefa se encaixa numa arquitetura swarm (descentralizada) ou numa supervisora (centralizada).
version: 1.0.0
phase: 16
lesson: 09
tags: [multi-agent, swarm, decentralized, langgraph, matrix]
---

Dada uma tarefa e seus requisitos de throughput / determinismo, recomendamos o enxame ou supervisor e listamos as opções específicas de fila e guarda-roupa.

Produzir:

1. **Task independence check.** As subtarefas são independentes ou dependem umas das outras?
2. **Duration distribution.** O Swarm ganha principalmente em cargas de trabalho de duração variável.
3. **Ordering requirement.** Estritamente, relaxado ou nada, o grupo não mantém a ordem, o supervisor sim.
4. **Debuggability need.** Alto (financeiro, médico) → supervisor. Médio → enxame com ID de rastreamento por tarefa.
5. **Queue choice.** Memória interna (`queue.Queue`) para demonstrações; Kafka / Redis Streams / NATS / durável DB-suportado para produção.
6. **Worker design requirements.** Deve ser idempotente, deve emitir traços por tarefa, deve lidar com a pressão de volta.
7. **Anti-starvation plan.** Envelhecimento prioritário, especialização de trabalhadores, fila limitada.
8. **Observability plan.** Identificadores por tarefa, eventos de início/final, esquema de conjunto de resultados.

Rejeitos duros:

- Recomendação de grupo para tarefas com exigências de ordem difíceis.
- Um enxame sem trabalhadores impotentes.
- Enxame sem fila duradoura na produção.

Regras de recusa:

- Se a tarefa tiver menos de 10 unidades independentes por segundo, rejeite o enxame e recomende o supervisor.
- Se os requisitos de observabilidade necessitam de um único rastro coerente (auditoria, conformidade), rejeite o enxame e recomenda um gráfico determinista de LangGraph em vez disso.

Resultado: um resumo arquitetônico de uma página. Abre com o veredicto adequado, feche com a recomendação específica do corretor de mensagens para o throughput de destino.
