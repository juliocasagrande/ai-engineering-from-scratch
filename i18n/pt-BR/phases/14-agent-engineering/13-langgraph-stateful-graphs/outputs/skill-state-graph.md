---
name: state-graph
description: Construa uma máquina de estado em forma de LangGraph com estado digitalizado, bordas condicionais, ponto de verificação por nó e currículo duradouro.
version: 1.0.0
phase: 14
lesson: 13
tags: [langgraph, state-machine, durable, checkpointing, human-in-the-loop]
---

Dado um tempo de execução alvo, uma forma de estado, um conjunto de funções de nós e um backend de checkpointer, produzem um gráfico de agente com estado.

Produzir:

1. Uma tipografia `State` Documentar todos os campos. nós ler estado; eles retornam atualizações.
2. A. `StateGraph` com `add_node`- Não . `add_edge`- Não . `add_conditional_edges`- Não . `set_entry`, mais `START`- Não .`END` Sentinelas.
3. A. `Checkpointer` Interface com `save(session_id, node, state)` e `load_latest(session_id)`. Default para SQLite; permitir Postgres/Redis/custom.
4. A. `Runner` que passa através do gráfico, serializa estado após cada nó, pega `PausedAtNode` para humanos no circuito, e apoios `resume_from` com opcional `state_override`- Não .
5. Três auxiliares de topologia: supervisor (routador central), enxame (transmissões de ferramentas compartilhadas), hierárquica (subgrafos).

Rejeitos duros:

- Nodos não deterministas sem captura explícita de semente aleatória ou de relógio de parede. Resume assume que a saída do nó é reprodutível dado o estado de entrada.
- Um ponto de verificação que só salva o estado "resumido", serializa o estado completo ou resume pausas.
- Graficos onde cada borda é condicional.

Regras de recusa:

- Se o usuário pedir um gráfico de estado sem persistência, recuse. O ponto é resumo duradouro; se você não precisa de resumo, use os padrões de fluxo de trabalho na lição 12.
- Se o usuário pedir para "checkpoint apenas no sucesso", recusar. falhas precisam declarar também  é onde o depuração começa.
- Se o gráfico tiver mais de ~ 30 nós, rejeite o layout plano e precise de subgráficos aninhados.

Output: `state.py`- Não . `graph.py`- Não . `checkpointer.py`- Não . `runner.py`- Não . `README.md` Explicando o esquema de estado, a escolha de checkpointer e a semântica de retomada. Terminando com "o que ler a seguir" apontando para a lição 14 para alternativa modelo de ator, lição 16 para camada de entrega / guarda-roupa, ou lição 23 para OTel abrange em etapas de gráfico.
