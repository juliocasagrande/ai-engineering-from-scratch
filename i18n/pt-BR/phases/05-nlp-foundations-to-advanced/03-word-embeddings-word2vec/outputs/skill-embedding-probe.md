---
name: embedding-probe
description: Inspeccionar um modelo Word2vec, fazer análises, encontrar vizinhos, diagnosticar qualidade.
version: 1.0.0
phase: 5
lesson: 03
tags: [nlp, embeddings, debugging]
---

Você analisa as palavras treinadas para verificar se funcionam. `gensim.models.KeyedVectors` Objeto e vocabulário, você corre:

1. Três análises canônicas. `king : man :: queen : woman`- Não . `paris : france :: tokyo : japan`- Não . `walking : walked :: swimming : ?`- Relata o resultado do top 1 e o cosino.
2. Cinco testes de vizinho mais próximo em palavras específicas de domínio que o usuário fornece.
3. Um cheque de simetria. `similarity(a, b) == similarity(b, a)` Para dentro da precisão de flutuação.
4. Se qualquer incorporação tiver uma norma abaixo de 0,01 ou acima de 100, o modelo tem um erro de treinamento.

Recusar-se a declarar um modelo bom apenas com base na precisão da analogia. Os critérios de referência da analogia são jogáveis e não são transferidos para tarefas a jusante. Recomendar uma avaliação intrínseca e a jusante juntamente.
