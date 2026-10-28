---
name: lm-baseline
description: Construir um modelo de base de linguagem n-gram reproduzível antes de treinar um LM neural.
phase: 5
lesson: 16
---

Dado um corpus e uso alvo (previsão da próxima palavra, rescoring, linha de base de perplexidade), saída:

1. Trigrama para inglês geral, 4 gramas se o corpo é grande, 5 gramas para rescoring de fala.
2. O Kneser-Ney modificado é o padrão, Laplace só para ensino.
3. Biblioteca. `kenlm` para a produção, `nltk.lm` Para ensinar, faça o seu só para aprender matemática.
4. Avaliação: perplexidade mantida com tokenização consistente entre os conjuntos de treinamento e de teste.

Recusar-se a relatar perplexidade calculada com tokenization diferente entre sistemas a ser comparada  números de perplexidade são comparáveis apenas sob tokenization idêntica. `<UNK>` - Sim, durante o treinamento.
