---
name: orchestration-picker
description: Escolha uma topologia de orquestração (supervisor, enxame, hierárquica, debate ou nenhuma) para um determinado problema e implementa-a minimamente.
version: 1.0.0
phase: 14
lesson: 28
tags: [orchestration, supervisor, swarm, hierarchical, debate]
---

Dado um domínio de produto e uma classe de tarefas, escolha a topologia mínima.

Decisão:

1. 1 agente + padrões de fluxo de trabalho (Lessão 12) são suficientes? -> não usar topologia em tudo.
2. - 2 a 4 especialistas com responsabilidades distintas? **supervisor-worker**- Não .
3. Os especialistas de latência e críticos podem dar-nos a volta? **swarm**- Não .
4. 10+ especialistas, orçamento de supervisão em situação de falha? -> **hierarchical**- Não .
5. A precisão importa mais do que o custo, o multi-proponente + crítica ajuda? -> **debate** (Lessão 25).

Produzir:

1. O andaime de topologia escolhido.
2. Contador de salto no enxame; limite de profundidade de nidificação no hierárquico; tampa redonda no debate.
3. Anéis de observabilidade por transferência ou por passo (OTel GenAI, lição 23).
4. Uma seção "por que isto, não aquilo".

Rejeitos duros:

- Chamando três chamadas de LLM em sequência "multi-agente".
- A massa sem contador de saltos é uma certeza.
- Hierárquico que se reduz a um especialista por ramo.

Regras de recusa:

- Se o usuário quiser multi-agente para uma tarefa que um único loop ReAct lida, recusar e sugerir a lição 01.
- Se o utilizador quiser um supervisor para uma tarefa de 2 etapas, recuse e sugira a encadeamento imediato (Lessão 12).
- Se o domínio tiver requisitos de conformidade / auditoria, rejeite o enxame e sugira supervisor ou hierarquica.

Resultado: andamio topológico + README com base na decisão. Terceira: "o que ler a seguir" apontando para a lição 13 (LangGraph) para implementação de supervisores, lição 16 (OpenAI Agents SDK) para entrega como ferramentas ou lição 25 para detalhes do debate.
