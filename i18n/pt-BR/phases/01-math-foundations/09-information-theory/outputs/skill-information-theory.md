---
name: skill-information-theory
description: Aplicar conceitos de teoria da informação às funções de perda de ML, avaliação de modelos e seleção de características
version: 1.0.0
phase: 1
lesson: 9
tags: [information-theory, entropy, loss-functions]
---

# Teoria da informação para ML

Quando utilizar entropia, entropia cruzada, divergência KL e informação mútua em sistemas de aprendizagem automática.

## Lista de verificação das decisões

1. Medir a incerteza numa única distribuição? **entropy**- Não .
2. Medir a aproximação de um modelo com as etiquetas reais? **cross-entropy** (este é o seu classificação perda).
3. Medir a distância entre duas distribuições? **KL divergence**- Não .
4. Verificar se duas variáveis estão relacionadas? **mutual information**- Não .
5. Qualidade do modelo de comunicação de linguagem? **perplexity** (exponencial de entropia cruzada).
6. Destilar um modelo para outro? **KL divergence** De professora a estudante.

## Quando utilizar cada medida

| Measure | Formula | Use case | ML application |
|---|---|---|---|
| Entropy H(P) | -sum(p log p) | How uncertain is this distribution? | Data complexity, maximum entropy models |
| Cross-entropy H(P,Q) | -sum(p log q) | How good is model Q at predicting true P? | Classification loss, language model loss |
| KL divergence D(P\|\|Q) | sum(p log(p/q)) | How different are P and Q? | VAE loss (ELBO), knowledge distillation, RLHF |
| Mutual information I(X;Y) | H(X) - H(X\|Y) | How much does Y tell us about X? | Feature selection, representation learning |
| Perplexity | exp(H(P,Q)) or 2^H | How confused is the model? | Language model evaluation |
| Conditional entropy H(X\|Y) | -sum(p(x,y) log p(x\|y)) | Remaining uncertainty in X after knowing Y | Feature informativeness |

## Relações fundamentais

```
Cross-entropy  = Entropy + KL divergence
H(P, Q)        = H(P)   + D_KL(P || Q)

Since H(P) is constant during training:
  Minimizing cross-entropy = Minimizing KL divergence

Mutual information = Entropy - Conditional entropy
I(X; Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)

Perplexity = exp(cross-entropy in nats)
           = 2^(cross-entropy in bits)
```

## Referência rápida: fórmulas e unidades

| Formula | Bits (log base 2) | Nats (log base e) |
|---|---|---|
| Information: -log(p) | -log2(p) | -ln(p) |
| Entropy: -sum(p log p) | bits | nats |
| 1 nat = | 1.4427 bits | 1 nat |
| PyTorch default | -- | nats |
| Information theory papers | bits | -- |

## Valores de interpretação

| Entropy value | What it means |
|---|---|
| 0 | Deterministic. One outcome has probability 1. |
| log(n) | Maximum uncertainty. Uniform distribution over n outcomes. |
| Low | Distribution is peaked. Model is confident. |
| High | Distribution is flat. Model is uncertain. |

| Perplexity value | Language model quality |
|---|---|
| 1 | Perfect prediction (never happens in practice) |
| 10 | Choosing among ~10 equally likely tokens on average |
| 50 | GPT-2 level on standard benchmarks |
| < 10 | State-of-the-art for well-represented domains |

## Erros comuns

- Para uma medida simétrica, use a divergência Jensen-Shannon: JS = 0,5 * KLPP = 0,5 * KLPP = 0,5 * KLPP = 0,5 * KLPP = 0,5 * KLPP = 0,5 * QQ) onde M = 0,5 * P+Q).
- Esquecer essa entropia cruzada com rótulos de um só-quente simplifica para -log(p_true_class). Você não precisa somar todas as classes quando a distribuição verdadeira é um só-quente.
- Usando log base 2 em código, mas relatando nats (ou vice-versa). PyTorch usa log natural por padrão. Multiplicar por log2(e) = 1.4427 para converter nats em bits.
- Entropia computacional de um evento de probabilidade vazia ou zero. Convenção: 0 * log(0) = 0, porque lim(p->0) p*log(p) = 0.
- Comparar perplexidade entre diferentes vocabulários. Um modelo com tamanho de vocabulário 50k e perplexidade 30 não é diretamente comparável a um com tamanho de vocabulário 10k e perplexidade 30.

## Quando cada conceito aparece na produção ML

| Concept | Where you see it |
|---|---|
| Cross-entropy loss | Every classification model (nn.CrossEntropyLoss) |
| KL divergence | VAE ELBO, PPO clipping, knowledge distillation |
| Entropy regularization | Exploration bonus in RL (higher entropy = more exploration) |
| Mutual information | Feature selection, InfoNCE loss (contrastive learning) |
| Perplexity | Language model benchmarks (lower = better) |
| Label smoothing | Replaces one-hot with soft targets, reduces cross-entropy overconfidence |
| Temperature scaling | Divides logits by T before softmax, controls entropy of output |
