---
name: coref-picker
description: Escolha uma abordagem de base, um plano de avaliação e uma estratégia de integração.
version: 1.0.0
phase: 5
lesson: 24
tags: [nlp, coref, information-extraction]
---

Dado um caso de uso (doc único / multi-doc, domínio, língua), saída:

1. Abordagem. baseada em regras / baseada em espaços neurais / LLM-promptado / híbrido. Razão de uma frase.
2. Modelo, ponto de controlo nomeado, se neuronal.
3. Integração. Ordem de operações: tokenize → NER → coref → downstream task.
4. Avaliação: CoNLL F1 (MUC + B3 + CEAF-φ4 média) sobre conjunto de trabalhos realizados + revisão manual de cluster de 20 documentos.

Recusar o coref exclusivo para documentos com mais de 2.000 tokens sem fusão de janela deslizante. Recusar qualquer pipeline que execute o coref sem um relatório de recall de precisão de nível de menção.
