---
name: topic-picker
description: Escolha LDA ou BERTopic para um corpus, especifique biblioteca, botões, avaliação.
version: 1.0.0
phase: 5
lesson: 15
tags: [nlp, topic-modeling]
---

Dado um corpus de descrição (conto de documentos, comprimento de avg, domínio, língua, orçamento de cálculo), saída:

1. Algoritmo: LDA/NMF/BERTopic/Top2Vec/FASTopic. Razão de uma frase.
2. Configuração. Número de tópicos (comece em ~sqrt(n_docs)), `min_df` - Não . `max_df` filtros, modelos de incorporação para abordagens neurais.
3. Avaliação: coerência entre os temas (c_v) `gensim.models.CoherenceModel`, diversidade de tópicos, mais uma leitura humana de 20 amostras.
4. Modo de falha para a sonda. Para LDA, "tópicos lixo" absorvendo palavras de parada e termos frequentes. Para BERTopic, -1 cluster de outlier engolir documentos ambíguos.

Rejeitar BERTopic em documentos mais longos do que a janela de contexto do modelo de incorporação sem uma estratégia de fragmentação. Rejeitar LDA em texto muito curto (tweets, revisões com menos de 10 tokens) à medida que a coerência desmorona. Marcar qualquer escolha de n_topics abaixo de 5 ou acima de 200 como provavelmente errada para dados reais.
