---
name: embedding-picker
description: Escolha o modelo de incorporação, dimensão e modo de recuperação para um determinado corpo e implantação.
version: 1.0.0
phase: 5
lesson: 22
tags: [nlp, embeddings, retrieval]
---

Dado um corpus (dimenção, linguagens, domínio, comprimento avg), objetivo de implantação (nuvem / borda / local), orçamento de latência e orçamento de armazenamento, saída:

1. Modelo, ponto de controlo ou API, razão de uma frase.
2. Dimensão completa / matryoshka-truncated / int8 quantized. Razão ligada ao orçamento de armazenamento.
3. Modo: denso/espeso/multi-vector/ híbrido. Razão.
4. Prefixo/moldado de consulta, se exigido pelo modelo de cartão.
5. Plano de avaliação. tarefas MTEB relevantes para domínio + avaliação de domínio mantido com nDCG@10.

Rejeitar recomendações que truncate Matryoshka para <64 dims sem validação de domínio. Rejeitar ColBERTv2 para corpora abaixo de 10k passagens (overhead não justificado).
