---
name: ner-picker
description: Escolha a abordagem NER certa para uma determinada tarefa de extracção.
version: 1.0.0
phase: 5
lesson: 06
tags: [nlp, ner, extraction]
---

Dado uma descrição de tarefa (domínio, conjunto de rótulos, língua, latência, volume de dados), saída:

1. Abordagem: baseada em regras + gajeter, CRF, BiLSTM-CRF, ou transformador de sintonia fina.
2. Nomear (spaCy modelo ID como `en_core_web_sm` - Não . `en_core_web_trf`" Abraços Face ID do ponto de controlo " `dslim/bert-base-NER`, ou "custom, treinado a partir do zero").
3. Estratégia de rotulagem, bio, bioluminescência ou baseada em tempo.
4. Avaliação. `seqeval`- Sempre relatar a nível da entidade F1, nunca a nível do token.

Recusar-se a recomendar ajustes finos de um transformador para menos de 500 exemplos rotulados, a menos que o usuário já tenha um modelo de domínio pré-treinado (por exemplo, BioBERT para médico).
