---
name: retrieval-picker
description: Escolha uma pilha de recuperação para um determinado corpus e padrão de consulta.
version: 1.0.0
phase: 5
lesson: 14
tags: [nlp, retrieval, rag, search]
---

Dados os requisitos (dimensão do corpo, padrão de consulta, orçamento de latência, barra de qualidade, infra-restrições), saída:

1. Estaca. Apenas BM25, apenas densa, híbrida (BM25 + densa + RRF), híbrida + reclassificação de codificadores cruzados ou tricampeã (BM25 + densa + espaçamento aprendido).
2. Indicar o modelo específico (`all-MiniLM-L6-v2`- Não . `bge-large-en-v1.5`- Não . `e5-large-v2`- Não . `paraphrase-multilingual-MiniLM-L12-v2`) Correspondem à linguagem, domínio, comprimento do contexto.
3. Reranker. Nomear o modelo de codificação cruzada, se utilizado (`cross-encoder/ms-marco-MiniLM-L-6-v2`- Não . `BAAI/bge-reranker-large`Flag ~30-100ms adicionado latência no top 30.
4. Plan de avaliação. Recall@10 é a métrica primária do retriever. MRR para resposta múltipla.

Recusar recomendar apenas denses para corpora com entidades nomeadas, códigos de erro ou SKUs de produto a menos que o usuário tenha evidências de que denses manipula correspondências exatas. Recusar-se a saltar o rebanho para recuperação de alto risco (legal, médico) onde o top-5 final decide a resposta do usuário.
