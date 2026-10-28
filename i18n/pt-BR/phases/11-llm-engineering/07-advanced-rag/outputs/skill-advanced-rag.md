---
name: skill-advanced-rag
description: Construir RAG de nível de produção com pesquisa híbrida, re-ranqueamento e avaliação
version: 1.0.0
phase: 11
lesson: 7
tags: [rag, hybrid-search, bm25, reranking, hyde, evaluation]
---

# Padrão RAG Avançado

RAG básico: inserir consulta -> busca vetorial -> top-k -> gerar.
RAG avançado: inserir consulta + BM25 -> fusíveis de classificação -> rerank -> top-k -> gerar.

```
query -> [vector search (top-50)] -+-> RRF fusion -> reranker (top-5) -> prompt -> LLM
                                   |
query -> [BM25 search (top-50)]  --+
```

## Quando atualizar a partir do RAG básico

- Qualidade de recuperação cai abaixo de 70% Recall@5
- Os utilizadores relatam respostas erradas ou irrelevantes
- O corpo cresce para além de 100 mil pedaços .
- As consultas usam um vocabulário diferente dos documentos
- As perguntas de múltiplos hop falham consistentemente

## Lista de verificação da execução

1. Adicionar índice BM25 ao lado do índice vetorial
2. Execute ambas as pesquisas em paralelo (top-50 cada)
3. Fusão com fusão de grau recíproco (k=60)
4. Rencontre os candidatos mais importantes com um codificador cruzado
5. Tome o top 5 para a última pergunta .
6. Adicionar avaliação de fidelidade a um conjunto de testes

## Guia de selecção técnica

- **Hybrid search**A utilização de um produto em produção é sempre adequada.
- **Reranking**A recall@5 é ruim, adiciona 50-200ms de latência.
- **HyDE**A aplicação de um programa de licenciamento é mais eficaz quando as consultas são vagas ou utilizam um vocabulário diferente do do doc.
- **Parent-child chunks**A utilização de pequenos pedaços não tem contexto, mas os grandes diluem a relevância.
- **Metadata filtering**: quando o corpus tiver categorias claras (data, tipo de fonte, departamento).
- **Query decomposition**A utilização para perguntas multi-hop que exigem informações de vários documentos.

## Erros comuns

- Exercício de BM25 e pesquisa vetorial com diferentes conjuntos de partes (devem procurar o mesmo corpus)
- Usar um grupo de candidatos muito pequeno para a re-ranqueação (o top-10 é muito pouco; use o top-50)
- Adicionar HyDE para cada consulta (apenas ajuda quando o desajuste de vocabulário é o gargalo)
- Não avaliação de alterações (medida Recall@k antes e após cada técnica)
- Super-engenharia do gasoduto antes de medir onde falha

## Fluxo de trabalho de avaliação

1. Crie mais de 50 perguntas de teste com fragmentos de respostas conhecidos
2. Medida Recall@5 e Recall@10 para cada método de recuperação
3. Para perguntas em que a recuperação é bem-sucedida, medir a fidelidade das respostas geradas
4. Seguir as métricas semanalmente à medida que o corpo cresce
5. Investigar falhas individuais antes de adicionar mais técnicas
