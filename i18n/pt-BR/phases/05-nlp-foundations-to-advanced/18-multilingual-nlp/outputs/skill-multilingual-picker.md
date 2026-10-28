---
name: multilingual-picker
description: Pick source language, target model, and evaluation plan for a multilingual NLP task.
version: 1.0.0
phase: 5
lesson: 18
tags: [nlp, multilingual, cross-lingual]
---

Dados os requisitos (linguagens-alvo, tipo de tarefa, dados marcados disponíveis por língua), saída:

1. Língua fonte para ajuste fino. Inglês padrão; verifique LANGRANK ou qWALS se a língua-alvo tem uma linguagem tipologicamente próxima de alto recurso.
2. Modelo base: XLM-R (classificação), mT5 (geração), NLLB (tradução), Aya-23 (LLM gerativo).
3. Com um orçamento reduzido, com 100 a 500 exemplos de linguagem-alvo, se disponíveis, apenas se a rotulagem for impossível.
4. Plano de avaliação: precisão por língua (não agregada), consistência interlingual, nível de entidade F1 em scripts não latinos.

Recusar-se a enviar um modelo multilingue sem avaliação por idioma  métricas agregadas escondem falhas de cauda longa.
