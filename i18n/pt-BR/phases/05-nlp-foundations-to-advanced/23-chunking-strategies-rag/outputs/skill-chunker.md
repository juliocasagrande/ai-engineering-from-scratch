---
name: chunker
description: Pick a chunking strategy, size, and overlap for a given corpus and query distribution.
version: 1.0.0
phase: 5
lesson: 23
tags: [nlp, rag, chunking]
---

Dado um corpus (tipos de documentos, comprimento de avg, domínio) e distribuição de consulta (factoide / analítica / multi-hop), saída:

1. Estratégia. Recursiva / frase / semântica / documento-mãe / tardia / contextual. Razão.
2. Tamanho do pedaço, contagem de tokens, razão ligada ao tipo de consulta.
3. Superposição. Default 0; justificar se > 0.
4. A aplicação mínima/máxima. `min_tokens`- Não .`max_tokens`Os guardas.
5. Plan de avaliação. Recall@5 no conjunto de avaliação estratificada de 50 perguntas (factoide, analítica, multi-hop).

Rejeitar qualquer estratégia de fragmentação sem a aplicação do tamanho da peça min/max. Rejeitar sobreposição acima de 20% sem uma ablação mostrando que ajuda.
