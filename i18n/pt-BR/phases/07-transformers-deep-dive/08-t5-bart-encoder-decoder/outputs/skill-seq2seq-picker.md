---
name: seq2seq-picker
description: Choose encoder-decoder vs decoder-only for a new sequence-to-sequence task.
version: 1.0.0
phase: 7
lesson: 8
tags: [transformers, t5, bart, seq2seq]
---

Dada uma tarefa seq2seq (tradução / resumo / fala-a-texto / extração estruturada / reescritura), distribuições de comprimento de entrada e saída, e prioridades de qualidade vs latência, saída:

1. Arquitetura. Um dos: encoder-decoder (T5 / BART / estilo Whisper), decoder-só instrução-ajustada, encoder-só + modelo de prompt. Razão de uma frase.
2. Objetivo de pré-treino: corrupção de tempo (T5), denúncia (BART), next-token (apenas para decodificadores) ou "salte pré-treino, ajuste o ponto de verificação existente".
3. Formatação de entrada. String de prefixo de tarefa (estilo T5) vs. system prompt (apenas para decodificadores) vs. tokens brutos (BART). Incluir o manuseio BOS/EOS.
4. Estratégia de decodificação: Penalties de largura e comprimento de pesquisa de feixe (tradução/resumo) ou núcleo/min-p (tarefas semelhantes a bate-papo).
5. Eval. Métrica adequada à tarefa: BLEU / ROUGE / WER / F1 / correspondência exacta. Inclua o tamanho da divisão do teste.

Recusar recomendar apenas o encoder para saídas gerativas. Recusar recomendar encoder-decoder quando a entrada já é uma conversa.
