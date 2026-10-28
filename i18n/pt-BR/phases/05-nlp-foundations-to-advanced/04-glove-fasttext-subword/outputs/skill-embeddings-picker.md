---
name: skill-embeddings-picker
description: Pick a tokenization approach for a new language model or text pipeline.
version: 1.0.0
phase: 5
lesson: 04
tags: [nlp, tokenization, embeddings]
---

Dada uma descrição de tarefa e conjunto de dados, você emitir:

1. Estratégia de tokenização (nivel de palavra, BPE, WordPiece, SentencePiece, BPE de nível de byte). Razão de uma frase.
2. Meta de tamanho do vocabulário. LM apenas em inglês: 32k. Multilingue: 64k-100k. Código: 50k-100k.
3. Liga à biblioteca com o comando de treinamento exato.`tokenizers`- Não .`sentencepiece`O que é que é o problema?
4. Um obstáculo de reprodução. Desajuste do modelo de tokenizer é o bug de produção silenciosa mais comum. Nomear qual par de tokenizer com o qual um checkpoint pré-treinado e advertir contra troca.

Recusar-se a recomendar a formação de um tokenizer personalizado quando o usuário está a ajustar um LLM pré-treinado (o fine-tune deve usar o tokenizer pré-treinado). Recusar-se a recomendar a tokenização a nível de palavras para qualquer caminho de inferência de produção.
