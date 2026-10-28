---
name: nli-picker
description: Pick an NLI model, label template, and evaluation setup for a classification / faithfulness / zero-shot task.
version: 1.0.0
phase: 5
lesson: 21
tags: [nlp, nli, zero-shot]
---

Dado um caso de utilização (verificação de fidelidade, classificação de tiros zero, inferência a nível de documento), saída:

1. Modelo, ponto de controlo NLI, razão ligada ao domínio, comprimento, língua.
2. Modelo (se não é possível). Padrão de verbalização. Exemplo.
3. Limitação de envolvimento para a regra da decisão.
4. Avaliação, precisão no conjunto de rotulagem, base apenas em hipóteses, subconjunto adversário.

Recusar-se a enviar classificação de tiro zero sem uma verificação de sanidade rotulada de 100 exemplos. Recusar-se a usar um modelo de NLI de nível de frase em instalações de comprimento de documento. Marque qualquer alegação de que a NLI resolve alucinação  ela a reduz; não a elimina.
