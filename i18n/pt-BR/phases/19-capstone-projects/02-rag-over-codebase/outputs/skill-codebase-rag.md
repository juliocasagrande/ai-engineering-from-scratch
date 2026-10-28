---
name: codebase-rag
description: Build a cross-repo semantic search system with AST-aware chunking, hybrid retrieval, incremental re-index, and cited answers.
version: 1.0.0
phase: 19
lesson: 02
tags: [capstone, rag, code-search, tree-sitter, qdrant, bm25, hybrid-retrieval]
---

Dado que existem mais de 10 repositórios com um total de pelo menos 2 milhões de linhas de código, construam um pipeline de ingestão, um índice híbrido e um agente de consulta com recurso a citações que responda a perguntas de referência cruzada com âncoras verificáveis de arquivo:linha.

Construir um plano:

1. Partilhe todos os arquivos com um tree-sitter, partilhe os limites dos nós de função e classe.`{repo, path, start_line, end_line, symbol, body}`- Não .
2. Resume cada peça com Claude Haiku 4.5 ou Gemini 2.5 Flash usando instruções de sistema em cache imediato.
3. Indicação em três estruturas: Qdrant (denso, Voyage-code-3 ou código-embed-nomic), Tantivy (BM25 com pesos de campo) e kuzu (borda de símbolo para importações, chamadas, herança).
4. Construir um agente de consulta LangGraph com três nós: retrieve (denso paralelo BM25), rerank (Cohere rerank-3 ou bge-reranker-v2-gemma-2b), synth (Claude Sonnet 4.7 com cache rápido e requisito de citação de arquivo: linha).
5. Post-filtramento: rejeitar qualquer alegação sem um verificável `(repo/path:start-end)`Ancorar; re-pedir ou deixar cair.
6. Cable um git push webhook que calcula uma diferença de nível de símbolo e re-embeda apenas os pedaços alterados.
7. Avalie com um conjunto de 100 perguntas mantidas. Relate MRR@10, nDCG@10, fidelidade de citação e percentil de latência.
8. Execute um trabalho semanal de deriva que re-executa a avaliação e alertas em MRR@10 queda > 5%.

Rubrico de avaliação:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | Retrieval quality | MRR@10 and nDCG@10 on a 100-question held-out set |
| 20 | Citation faithfulness | Fraction of answer claims with verifiable file:line anchors |
| 20 | Latency and scale | p95 query latency at 10k QPS on the indexed corpus size |
| 20 | Incremental indexing correctness | Time from git push to searchable on a 50-file commit |
| 15 | UX and answer formatting | Citation clickability, snippet previews, follow-up affordance |

Rejeitos duros:

- O envenenamento de tokens de tamanho fixo em vez de envenenamento de código pesado gerado.
- Só a recuperação de cosina sem BM25 ou re-ranqueamento.
- Respostas sem arquivo obrigatório: citações de linha.
- Re-embedagem de corpo completo em cada empurrão de git; deve ser incremental.

Regras de recusa:

- Recusam-se a indexar os repos sem ler a licença deles.
- Recusar-se a responder a consultas que afirmam citar arquivos que o índice nunca viu; sempre verifique a âncora antes de retornar.
- Recusar a fornecer uma resposta em p95 acima de 4s; retornar um resultado parcial com uma manobra de acompanhamento em vez disso.

Resultado: um repo contendo o pipeline de ingestão, o agente de consulta LangGraph, o conjunto de eval rotulado com 100 perguntas, um link do painel de controle Langfuse e um texto que nomeia os três modos de falha de recuperação que você fixou (envenenamento de código gerado, recall de símbolo de cauda longa, resolução de símbolo de repositório cruzado) e a mudança exata que fixou cada um.
