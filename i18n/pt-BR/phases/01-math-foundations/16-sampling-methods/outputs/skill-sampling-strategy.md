---
name: skill-sampling-strategy
description: Escolha o método de amostragem adequado para geração, estimativa ou inferência
version: 1.0.0
phase: 1
lesson: 16
tags: [sampling, mcmc, generation]
---

# Seleção da estratégia de amostragem

Como escolher o método de amostragem certo para geração de texto, inferência bayesiana, estimativa de Monte Carlo e treinamento.

## Lista de verificação das decisões

1. Está a gerar resultados (texto, imagens) ou a estimar uma quantidade (integral, expectativa)?
2. Pode tomar amostras diretamente da distribuição alvo, ou apenas avaliar a sua densidade?
3. A distribuição-alvo é discreta ou contínua?
4. Qual é a dimensão do espaço de amostra? baixo (< 5), médio (5-100) ou alto (> 100)?
5. Precisa de amostras exatas ou aproximadas?
6. Precisas de gradientes para a amostragem?

## Quando utilizar cada método

| Method | When to use | Complexity | Exact? |
|---|---|---|---|
| Direct sampling | You have the CDF or can use a library function | O(1) per sample | Yes |
| Inverse CDF | Known closed-form CDF inverse (exponential, Cauchy) | O(1) per sample | Yes |
| Box-Muller | Need normal samples without a library | O(1) per sample | Yes |
| Rejection sampling | Can evaluate target PDF, low dimension (1-3) | O(1/acceptance) per sample | Yes |
| Importance sampling | Need expectations, not individual samples | O(n) for n samples | Approximate |
| Stratified sampling | Monte Carlo estimation, want lower variance | O(n) for n samples | Approximate |
| Metropolis-Hastings | High-dimensional, can evaluate unnormalized density | O(1) per step + burn-in | Asymptotically |
| Gibbs sampling | Can sample from each conditional distribution | O(d) per full sweep | Asymptotically |
| HMC/NUTS | High-dimensional continuous, smooth density | O(L * d) per step | Asymptotically |
| Temperature sampling | LLM text generation, control creativity | O(V) for vocab size V | N/A |
| Top-k sampling | LLM generation, remove unlikely tokens | O(V log k) | N/A |
| Top-p (nucleus) | LLM generation, adaptive candidate set | O(V log V) | N/A |
| Reparameterization | Need gradients through Gaussian sampling (VAEs) | O(d) | Yes |
| Gumbel-Softmax | Need gradients through categorical sampling | O(k) for k classes | Approximate |

## Configurações de geração de MLL

| Use case | Temperature | Top-p | Top-k | Notes |
|---|---|---|---|---|
| Factual Q&A | 0.0 (greedy) | -- | -- | Deterministic, no randomness |
| Code generation | 0.2-0.5 | 0.9 | -- | Low creativity, high coherence |
| General chat | 0.7 | 0.9 | -- | Balanced |
| Creative writing | 0.9-1.2 | 0.95 | -- | Higher diversity |
| Brainstorming | 1.0-1.5 | 0.95 | -- | Maximum diversity, may lose coherence |

Temperatura e top-p podem ser combinados. Aplique primeiro temperatura (logits de escala), depois aplique filtragem top-p.

## Seleção do método MCMC

| Property | Metropolis-Hastings | Gibbs | HMC/NUTS |
|---|---|---|---|
| Dimension | Any | Any (best < 100) | High (100+) |
| Requires conditionals | No | Yes | No |
| Requires gradient | No | No | Yes |
| Acceptance rate | Tune to ~23% | Always 100% | Tune to ~65% |
| Correlation | High (random walk) | Moderate | Low |
| Burn-in | Long | Moderate | Short |
| Best for | Exploration, simple models | Conjugate models, Bayesian networks | Continuous posteriors, deep probabilistic models |

## Erros comuns

- Usando amostragem de rejeição em dimensões altas. A taxa de aceitação cai exponencialmente com a dimensão.
- Definição de variação de proposta MCMC muito alta ou muito baixa. Muito alta: a maioria das propostas rejeitadas, cadeia presa. Muito baixa: todas as propostas aceitas, cadeia se move lentamente. Meta ~23% aceitação para caminhada aleatória MH.
- Esquecer a queima-in. As primeiras amostras N do MCMC são tendenciosas pelo ponto de partida.
- A análise de importância é feita com uma proposta muito diferente da meta. Algumas amostras têm pesos enormes, o que torna a estimativa pouco confiável.
- Usar temperatura > 0 para tarefas que necessitam de saída determinista (por exemplo, classificação, extração estruturada).
- Não combinar top-p com temperatura. A temperatura sozinha não remove os tokens de lixo da cauda longa.
- Propagação para trás através de uma operação padrão de amostragem.

## Referência rápida: técnicas de redução de variância

| Technique | How it works | Variance reduction |
|---|---|---|
| Stratified sampling | Divide space into strata, sample each | Always <= standard MC |
| Antithetic variates | Use both U and 1-U | Works for monotone functions |
| Control variates | Subtract a known-mean variable | Proportional to correlation |
| Importance sampling | Reweight samples from a better proposal | Depends on proposal quality |
| Latin hypercube | Stratify each dimension independently | Better than stratified in high-d |
