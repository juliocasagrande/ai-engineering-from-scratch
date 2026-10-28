---
name: hybrid-memory
description: Generate a Mem0-shaped three-store memory system (vector + KV + graph) with a fusion scorer, scope taxonomy, and temporal invalidation.
version: 1.0.0
phase: 14
lesson: 09
tags: [memory, mem0, vector, graph, kv, fusion, scope]
---

Dado um tempo de execução alvo, um backend vetorial (Qdrant, pgvector, Chroma, sqlite-vec), um backend KV (Postgres, Redis, dict) e um backend gráfico (Neo4j, bordas de memória), produz um sistema de memória fundido.

Produzir:

1. Três salas de lojas atrás de um`add(text, user_id, session_id, scope, importance, tags)`Quando escrever, o extractor decompõe.`text`Não há loja opcional.
2. Um marcador de fusão .`score = w_rel * relevance + w_imp * importance + w_rec * recency`Expor os três pesos como configuração.
3. Taxonomia de âmbito: `user`- Não .`session`- Não .`agent`Uma consulta de usuário nunca deve vazar os registros de outro usuário.
4. Invalidação temporária. Contradições marcam as antigas bordas/registros inválidos; nunca excluir. Expor `search(query, as_of=timestamp)`Para perguntas históricas.
5. Uma interface de extractor. A definição padrão pode ser orientada por LLM; permite um regresso determinista regex para testes.`add()`Para evitar explosões.

Rejeitos duros:

- Memória de loja única descrita como "em forma de Mem0". Produtos de vetores apenas, KV apenas, gráficos apenas são bem, mas não são memória híbrida. Não os nomear mal.
- Recuperação transversal sem pesos por intervalo ou um explícito `scope=`A fuga de dados é um incidente de conformidade e privacidade.
- A exclusão de contradições, inválido e tempo-estampado, a exclusão esconde bugs e rompe auditorias.

Regras de recusa:

- Se o usuário pedir "sem peso de importância", recusar.
- Se o backend do gráfico não tiver detector de conflito, recuse-se a chamar o sistema resultante de "Mem0-formed".
- Se o produto envolver PII (médico, jurídico, RH), recusar a expedição com um extractor que não tenha sido auditado pelo proprietário do produto.

Resultado: um arquivo por loja mais `memory.py`(facadeira), `config.py`(pesos), `README.md`A lição completa é a seguinte: "O que ler a seguir", apontando para a lição 10 se o agente precisa aprender novas habilidades, lição 23 se os intervalos OTel são necessários em operações de memória, ou lição 27 para o tratamento de entradas não confiáveis na recuperação.
