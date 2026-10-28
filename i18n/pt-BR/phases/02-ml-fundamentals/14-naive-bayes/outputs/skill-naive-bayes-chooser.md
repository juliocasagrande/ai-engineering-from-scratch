---
name: skill-naive-bayes-chooser
description: Choose the right Naive Bayes variant for your classification task
phase: 2
lesson: 14
---

Quando alguém precisa escolher uma variante de Bayes ingênua, acompanha-o neste processo de decisão.

## Lista de verificação das decisões

### Passo 1: Quais são as suas características?

- **Word counts or TF-IDF values**-> MultinômioNB
- **Continuous measurements (temperature, height, sensor readings)**-> GaussianNB
- **Binary indicators (word present/absent, checkbox states)**-> BernoulliNB
- **Mixed types**-> Dividir em subconjuntos, ou converter todos em um tipo

### Passo 2: Quantos dados tem?

- **Under 1,000 samples**A sua forte antecedência (assunção de independência) impede o excesso de conexão.
- **1,000 to 50,000 samples**A Comissão considera que a redução da taxa de juro é uma das principais causas de uma redução do preço de juro.
- **Over 50,000 samples**A regressão logística ou o aumento do gradiente provavelmente superarão a NB.

### Passo 3: Almejar

- Comece com alpha=1.0 (Laplace smoothing).
- Se a precisão for baixa e tiver dados suficientes, tente alpha=0,1 ou 0,01.
- Se o modelo estiver em excesso de encaixe (precisão de ensaio do trem), aumentar o alfa para 5,0 ou 10,0.
- Validar sempre o suavizamento com validação cruzada, não uma única divisão de trem/teste.

### Passo 4: Verificar as suposições

- **MultinomialNB**As características devem ser não negativas. Se tiver valores negativos, mude ou use GaussianNB.
- **GaussianNB**Funciona melhor quando as características são aproximadamente em forma de sino dentro de cada classe.
- **BernoulliNB**Selecione o limiar cuidadosamente (para texto: presente = 1, ausente = 0).

## Erros comuns

1. **Using GaussianNB on text data.**As contagens de palavras não são gaussianas.
2. **Forgetting Laplace smoothing.**Uma única palavra invisível elimina toda a probabilidade.
3. **Trusting the probability outputs.**As probabilidades NB são mal calibradas. Use-as para classificação, não como pontuações de confiança.
4. **Ignoring class imbalance.**NB, os antecedentes refletem as frequências de classe. Com 99% negativo e 1% positivo, o anterior supera a probabilidade. Ajustar os antecedentes manualmente ou reanalisar.

## Referência rápida

| Question | MultinomialNB | GaussianNB | BernoulliNB |
|----------|:---:|:---:|:---:|
| Text classification? | Yes | No | Maybe (short text) |
| Continuous features? | No | Yes | No |
| Binary features? | No | No | Yes |
| Very fast training needed? | Yes | Yes | Yes |
| Small training set? | Good | Good | Good |
| Need calibrated probabilities? | No | No | No |

## Quando não usar Bayes ingênuo

- As características são altamente correlacionadas e você tem dados suficientes para um modelo que lida com correlações (regressão logística, aumento de gradiente)
- Precisas da melhor precisão possível e tens muitos dados
- As suas características são imagens, sequências ou gráficos (utilize redes neurais)
- Você precisa de um modelo que capte as interações de características (utilizar métodos baseados em árvores)
