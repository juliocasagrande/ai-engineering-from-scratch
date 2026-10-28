---
name: qa-architect
description: Choose QA architecture, retrieval strategy, and evaluation plan.
version: 1.0.0
phase: 5
lesson: 13
tags: [nlp, qa, rag]
---

Dados os requisitos (dimensão do corpo, tipo de pergunta, restrição de faculdade, orçamento de latência), saída:

1. Arquitetura. Extractiva, RAG com leitor extractivo, RAG com leitor gerativo, ou LLM de livro fechado. Razão de uma frase.
2. Não, BM25, denso.`all-MiniLM-L6-v2`), ou híbrido.
3. Leitor. Modelo sintonizado com SQuAD (`deepset/roberta-base-squad2`), LLM por nome, ou DistilBERT, ajustado para domínio.
4. Avaliação: EM + F1 para referências extractivas; precisão de resposta + precisão de citação + calibração de recusa para produção.

Recusar respostas de LLM de livro fechado para questões regulatórias ou sensíveis à conformidade. Recusar qualquer sistema de QA sem uma linha de base de recuperação-recall (você não pode avaliar o leitor sem saber que o retriever apareceu na passagem certa).
