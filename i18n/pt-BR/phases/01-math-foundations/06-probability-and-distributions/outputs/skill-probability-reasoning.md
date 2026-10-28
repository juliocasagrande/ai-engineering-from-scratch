---
name: skill-probability-reasoning
description: Choose the right probability distribution for a given ML problem
version: 1.0.0
phase: 1
lesson: 6
tags: [probability, distributions, modeling]
---

# Seleção de Distribuição de Probabilidade

Como escolher a distribuição certa ao modelar dados, projetar funções de perda ou definir prioridades.

## Lista de verificação das decisões

1. O resultado é discreto (categorias, contagens) ou contínuo (medidas, pontuações)?
2. O resultado é limitado (por exemplo, [0, 1]) ou ilimitado?
3. Quantos resultados possíveis existem?
4. Os dados são simétricos ou distorcidos?
5. Os eventos são independentes ou correlacionados?
6. Está a modelar uma taxa, uma contagem, uma proporção ou uma medição?

## Árvore de decisão de distribuição

```
Is the variable discrete?
  Yes --> Only 2 outcomes? --> Bernoulli (p)
     |    k outcomes, one trial? --> Categorical (p1...pk)
     |    k outcomes, n trials? --> Multinomial (n, p1...pk)
     |    Count of successes in n trials? --> Binomial (n, p)
     |    Count of events per interval? --> Poisson (lambda)
     |    Count of trials until first success? --> Geometric (p)
     |    Count of trials until r successes? --> Negative Binomial (r, p)
  No --> Symmetric, bell-shaped? --> Normal (mu, sigma)
     |   Positive values, right-skewed? --> Log-normal or Exponential
     |   Bounded in [0, 1]? --> Beta (alpha, beta)
     |   Positive values, flexible shape? --> Gamma (alpha, beta)
     |   Time between events? --> Exponential (lambda)
     |   Heavy tails needed? --> Student's t (nu) or Cauchy
     |   Multivariate, bell-shaped? --> Multivariate Normal
     |   On a simplex (sums to 1)? --> Dirichlet (alpha)
```

## Mapeamento de cenários de ML do mundo real para distribuições

| Scenario | Distribution | Parameters |
|---|---|---|
| Binary classification output | Bernoulli | p = sigmoid(logit) |
| Multi-class classification output | Categorical | p = softmax(logits) |
| Token prediction in language models | Categorical over vocab | p from softmax |
| Pixel intensity (normalized) | Beta or Uniform [0, 1] | Depends on image stats |
| Word count in a document | Poisson | lambda = avg word count |
| Time between user requests | Exponential | lambda = request rate |
| Measurement error | Normal | mu = 0, sigma from data |
| Weight initialization | Normal or Uniform | Kaiming/Xavier rules |
| VAE latent space prior | Standard Normal | mu = 0, sigma = 1 |
| Bayesian prior on proportions | Beta | alpha, beta from belief |
| Bayesian prior on category weights | Dirichlet | alpha vector |
| Noise in regression targets | Normal | mu = 0, sigma estimated |
| Outlier-robust regression | Student's t | low degrees of freedom |
| Duration/lifetime modeling | Weibull or Gamma | shape and scale |
| Topic distribution per document (LDA) | Dirichlet | alpha < 1 for sparse |

## Quando as distribuições vão mal

- Usando Normal quando os dados têm um limite inferior duro (por exemplo, preços, distâncias). O normal atribui probabilidade não zero a valores negativos. Use log-normal ou gama em vez disso.
- Usando Poisson quando a variância é diferente da média. Poisson assume que a média = variância. Se a variância > média, use o binomio negativo.
- Usando Bernoulli para problemas de várias classes. Bernoulli é estritamente binário. Use categorical para k > 2.
- Assumir independência quando as observações estão correlacionadas. Série de tempo, dados espaciais e dados agrupados violam a independência. Use modelos autoregressivos ou hierárquicos.

## Erros comuns

- Confusão de valores PDF com probabilidades. Um PDF pode exceder 1.
- Esquecendo que as saídas de softmax são probabilidades categóricas, não probabilidades independentes de Bernoulli.
- Usando um prévio uniforme quando você tem conhecimento de domínio.
- Tratar log-probabilidades como probabilidades. log-probs são sempre negativos (ou zero). Eles não somam a 1.

## Referência rápida: propriedades de distribuição

| Distribution | Support | Mean | Variance | Key property |
|---|---|---|---|---|
| Bernoulli(p) | {0, 1} | p | p(1-p) | Simplest discrete |
| Binomial(n, p) | {0..n} | np | np(1-p) | Sum of n Bernoulli |
| Poisson(lam) | {0, 1, 2, ...} | lam | lam | Mean = variance |
| Normal(mu, s^2) | (-inf, inf) | mu | s^2 | Max entropy for given mean/var |
| Exponential(lam) | [0, inf) | 1/lam | 1/lam^2 | Memoryless |
| Beta(a, b) | [0, 1] | a/(a+b) | ab/((a+b)^2(a+b+1)) | Conjugate to Binomial |
| Gamma(a, b) | (0, inf) | a/b | a/b^2 | Conjugate to Poisson |
| Dirichlet(alpha) | Simplex | alpha_i/sum | (see formula) | Conjugate to Categorical |
