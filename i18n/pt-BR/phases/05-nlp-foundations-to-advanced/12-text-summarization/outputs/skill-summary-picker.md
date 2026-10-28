---
name: summary-picker
description: Pick extractive or abstractive, name the library, add a factuality check.
version: 1.0.0
phase: 5
lesson: 12
tags: [nlp, summarization]
---

Em função de uma tarefa (tipo de documento, exigência de conformidade, duração, orçamento de cálculo), saída:

1. Abstração ou extração, explica em uma frase porquê.
2. - O modelo de inicialização / biblioteca.`sumy.TextRankSummarizer`- Não .`facebook/bart-large-cnn`- Não .`google/pegasus-pubmed`, ou um LLM.
3. Plano de avaliação: ROUGE-1, ROUGE-2, ROUGE-L (utilização `rouge-score`- E a verificação de factualidade, se é abstracto.
4. Um modo de falha para sondar. O swap de entidades é o mais comum na resumo de notícias abstractivas; amostras de bandeira onde as entidades de origem não aparecem no resumo.

Rejeitar a resumo abstrato para conteúdo médico, legal, financeiro ou regulamentado sem um portal de factualidade.
