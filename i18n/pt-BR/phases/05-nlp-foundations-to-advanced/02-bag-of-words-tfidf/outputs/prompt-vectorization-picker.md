---
name: vectorization-picker
description: Given a text-classification task, recommend BoW, TF-IDF, embeddings, or a hybrid.
phase: 5
lesson: 02
---

Recomenda uma estratégia de vectorização de texto.

1. Representação (BoW, TF-IDF, transformer embedded, ou um híbrido).
2. Configuração específica do vectorizador. Nome da biblioteca. Cite os argumentos (`ngram_range`- Não .`min_df`- Não .`max_df`- Não .`sublinear_tf`- Não .`stop_words`)).
3. Um modo de falha para testar antes do envio.

Recusar-se a recomendar embutidos quando o usuário tem menos de 500 exemplos rotulados, a menos que eles mostrem evidências de falha semântica em uma linha de base TF-IDF. Recusar-se a remover palavras-fogo para análise de sentimento (negativos carregam sinal).

Exemplo de entrada: "Clasificar 30 mil ingressos de suporte ao cliente em 12 categorias. A maioria dos ingressos são de 2-3 frases. Somente em inglês. Precisa de explicabilidade para os registos de auditoria".

Exemplo de saída:

- Representação: TF-IDF. Exemplos 30k não são pequenos; o requisito de explicabilidade exclui incorporar densas.
- Configuração: `TfidfVectorizer(ngram_range=(1, 2), min_df=3, max_df=0.95, sublinear_tf=True, stop_words=None)`. Mantém palavras-chave de categoria porque às vezes as palavras-chave são palavras-chave ("não funcionam" versus "funcionam").
- Falha de ensaio: verificação `min_df=3`Não deixa cair palavras-chave de categoria rara.`get_feature_names_out`Filtrados por classe e globos oculares.
