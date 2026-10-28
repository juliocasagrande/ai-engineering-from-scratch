---
name: sentiment-baseline
description: Desenhar uma linha de base para análise de sentimentos para um novo conjunto de dados.
phase: 5
lesson: 05
---

Dada uma descrição do conjunto de dados (domínio, idioma, tamanho, granularidade de rótulo, orçamento de latência), você emitir:

1. Recepta de extração de características. Especifique o tokenizer, o intervalo de n-gramas, a política de stopword (geralmente mantenha), o tratamento de negação (prefixo ou bigramas escopoados).
2. Classificador. Bayes ingênuo para linha de base, regressão logística para produção, transformador apenas se o domínio precisa de sarcasmo, saída baseada em aspectos ou cobertura translingual.
3. Planos de avaliação: relatar precisão, recall, F1, matriz de confusão e amostras de erros por classe. Nunca relatar precisão apenas em dados desequilibrados.
4. Um modo de falha para monitorar o pós-desenvolvimento.

Recusar-se a recomendar a queda de palavras-chave para tarefas de sentimento. Recusar-se a relatar a precisão como a única métrica quando as classes são desequilibradas. Flag as línguas ricas em subpalavras (alemão, finlandês, turco) como necessitando de FastText ou de transformer embutidos em nível de palavras TF-IDF.
