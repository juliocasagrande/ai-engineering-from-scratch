---
name: ner-picker
description: Pick the right NER approach for a given extraction task.
version: 1.0.0
phase: 5
lesson: 06
tags: [nlp, ner, extraction]
---

Dado uma descrição de tarefa (domínio, conjunto de rótulos, língua, latência, volume de dados), saída:

1. Abordagem: baseada em regras + gajeter, CRF, BiLSTM-CRF, ou transformador de sintonia fina.
2. Nomear (ID do modelo espaCy como `en_core_web_sm`- Não .`en_core_web_trf`, abraçando o rosto ID do ponto de controlo como `dslim/bert-base-NER`, ou "custom, treinado a partir do zero").
3. Estratégia de rotulagem, bio, bioluminescência ou baseada em tempo.
4. Avaliação. Utilização `seqeval`- Sempre relatar a nível da entidade F1, nunca a nível do token.

Recusar-se a recomendar ajustes finos de um transformador para menos de 500 exemplos rotulados, a menos que o usuário já tenha um modelo de domínio pré-treinado (por exemplo, BioBERT para médico).
