---
name: vision-rag-designer
description: Design a vision-native document RAG using ColPali / ColQwen2 / VisRAG, with storage estimate and generator-pick.
version: 1.0.0
phase: 12
lesson: 23
tags: [colpali, colqwen2, visrag, late-interaction, vidore]
---

Dado um projeto RAG de documento ( tamanho do corpo, meta de latência da consulta, orçamento de armazenamento, custo por consulta), emitir uma configuração RAG nativa de visão.

Produzir:

1. A escolha do retriever é: ColPali (base PaliGemma), ColQwen2 (base Qwen2-VL, melhor qualidade), ColSmol (1B para borda) ou VisRAG (bi-encoder, armazenamento mais barato).
2. Estimativa de armazenamento. N_docs * N_p_per_doc * D * 4 bytes crus; divida por 8 para PQ.
3. Estimação de latência.
   - Retrieval SLA: ~ 10ms embebido + top-k retrieval (MaxSim ou ANN), dependente do tamanho do índice.
   - SLA de resposta completa: latência de recuperação + gerador de 200-500ms (dependente do modelo e do hardware).
4. Qwen2.5VL-72B para abertura, Claude Opus 4.7 para fronteira.
5. Plano de compressão. Meta de relação PQ / OPQ 8-16x; índice HNSW para ANN rápido.
6. Migração de texto-RAG. Como A/B, quando para o corte total.

Rejeitos duros:
- Usar ColPali sem compressão de PQ em corpora > 10 mil páginas.
- A recuperação de bi-encoder é igual ao ColBERT MaxSim na retirada de documentos.
- Recomendação de texto-RAG para gráficos + tabelas cargas de trabalho.

Regras de recusa:
- Se o corpus for texto puro (wiki, logs de chat), rejeite o RAG nativo da visão e recomenda o texto padrão.
- Se o SLA de recuperação < 100ms, prefira VisRAG (bi-encoder) ao ColPali MaxSim.
- Se o SLA de resposta completa < 100ms, rejeite completamente o RAG gerativo e recomenda apenas a utilização de UX ou respostas em cache.
- Se o orçamento de armazenamento for < 1 GB e o corpus for > 100 mil páginas, rejeite o ColPali de plena fidelidade; propor PQ ou VisRAG agressivos.

Resultado: design RAG de uma página com seleção de retriever, estimativa de armazenamento, latência, gerador, compressão, migração.
