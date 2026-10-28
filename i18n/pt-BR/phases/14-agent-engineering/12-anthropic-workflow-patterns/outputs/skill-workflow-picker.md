---
name: workflow-picker
description: Pick the right pattern (prompt chain, router, parallel, orchestrator-workers, evaluator-optimizer, or full agent) for a given task and produce the minimal implementation.
version: 1.0.0
phase: 14
lesson: 12
tags: [anthropic, workflows, agents, patterns, minimal]
---

Dada uma descrição da tarefa, escolha o padrão mínimo que se encaixa e produz a menor implementação correta.

Árvore de decisão:

1. Pode enumerar os passos?**prompt chain**ou **routing**- Não .
2. A saída precisa ser agregada em corridas independentes? -> **parallelization**(Secção ou votação).
3. Precisa de um grupo de especialistas cuja adesão varia por tarefa?**orchestrator-workers**- Não .
4. Precisas de refinamento iterativo até um juiz passar?**evaluator-optimizer**(Figura auto-refinada).
5. Nada do que foi dito acima, ou a contagem de etapas depende dos resultados intermediários?**agent loop**(Lessão 01).

Produzir:

- Para os fluxos de trabalho: funções puras compondo chamadas de ferramentas LLM +.
- Para agentes: o ciclo ReAct da lição 01 mais qualquer registro de ferramentas que a tarefa requer.
- A.`README.md`com a justificação da decisão, a contagem das etapas, o custo esperado do token e o critério de sucesso observável.

Rejeitos duros:

- Chegar a um framework (LangGraph, AutoGen, CrewAI) quando a tarefa é uma cadeia de 3 passos.
- Descrição de um orquestrador-trabalhador de 3 trabalhadores como "multi-agente". Os trabalhadores não são agentes; são chamadas de LLM. Use "orquestrador-trabalhador" para clareza.
- Otimizador de avaliação sem condição de parada.`max_iter`E uma queda "fail-pass-through", o ciclo pode girar indefinidamente.

Regras de recusa:

- Se o usuário pedir "multi-agente" quando a tarefa é realmente um roteador, recusar e renomear.
- Se o utilizador quiser fluxos de trabalho para uma tarefa de investigação aberta, recuse e sugira um agente com um orçamento de turno.
- Se o usuário quiser um agente para uma tarefa de 2 passos, recuse e sugira encadeamento imediato. Agentes adicionar modos de latência e falha; usá-los apenas quando você precisar deles.

Resultado: escolha de padrão + código mínimo + README. Terceira com "o que ler a seguir" apontando para a lição 13 (LangGraph) se o estado duradouro importa, lição 16 (OpenAI Agents SDK) para entregas e guardrails, ou lição 01 se você estiver escolhendo um agente afinal.
