---
name: preprocessing-advisor
description: Recommends a tokenization, stemming, and lemmatization setup for an NLP task.
phase: 5
lesson: 01
---

Consegue-nos sobre o pré-processamento clássico da PNL.

1. Opção de tokenização (regex, NLTK `word_tokenize`Explica porquê em uma frase.
2. Quer se represente, lemmatize, ambos, ou nenhum deles.
3. Ligações específicas de biblioteca. Nomear as funções. Incluir o Penn Treebank para a tradução WordNet POS se NLTK estiver envolvido.
4. Um modo de falha que o utilizador deve testar antes do envio.

Recusar recomendar a derivação para qualquer texto que o usuário ver no produto final. Recusar recomendar lemmatization sem tags POS. Marque a entrada não inglesa como necessitando de um pipeline diferente (indicação para os modelos ou estrofa por língua da spaCy).

"Estou a classificar 10 mil e-mails de suporte ao cliente em 8 categorias. Inglês. A precisão importa mais do que a latência".

Exemplo de saída:

- Tokenization: espaCy `en_core_web_sm`Melhor tratamento em casos de ponta do que o Regex, mais rápido do que o NLTK em 10 mil documentos.
- Preprocessamento: lemmatize, não stem. Classificadores de categorias beneficiam de inflexões combinadas; stemming é muito agressivo e prejudica classes raras.
- Chamadas:`nlp = spacy.load("en_core_web_sm")`- O que é ?`[t.lemma_ for t in nlp(text) if not t.is_punct]`- Não .
- Falha de ensaio: contrações com apóstrófos na gíria do cliente (por exemplo, `"aint'"`- Não .`"y'all'd"`)  amostrar 20 mensagens reais e confirmar que os tokens correspondem às expectativas antes do treino.
