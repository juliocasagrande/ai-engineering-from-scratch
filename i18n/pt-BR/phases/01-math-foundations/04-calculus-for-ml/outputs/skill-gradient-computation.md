---
name: skill-gradient-computation
description: Compute gradients of common ML loss functions and choose the right derivative approach
version: 1.0.0
phase: 1
lesson: 4
tags: [calculus, gradients, backpropagation]
---

# Computação de gradientes para ML

Referência prática para a computação de gradientes de funções de perda, funções de ativação e operações de camadas usadas em redes neurais.

## Lista de verificação das decisões

1. A função é composta por primitivas simples (potência, exp, log, trig)?
2. A função é uma operação personalizada ou caixa negra? Use diferenciação numérica: `(f(x+h) - f(x-h)) / (2h)`com h = 1e-7.
3. A função é construída a partir de operações de tensor em PyTorch / JAX? Deixe o autograd lidar com ele. Verifique com verificação numérica.
4. Você precisa do gradiente de uma perda escalar w.r.t. uma matriz de pesos? Aplique a regra da cadeia através do gráfico de cálculo, um nó por vez.
5. Existe uma operação não diferenciável (argmax, arredondamento, amostragem)?

## Quando utilizar cada abordagem

| Approach | When to use | Cost |
|---|---|---|
| Analytical (hand-derived) | Simple functions, verifying autograd output | Free at runtime |
| Numerical (finite differences) | Debugging, gradient checking, black-box functions | 2n forward passes for n parameters |
| Automatic differentiation | Any differentiable computation graph (the default) | One backward pass |
| Symbolic (SymPy, Mathematica) | Deriving closed-form gradients for papers | Compile time only |

## Referência rápida: derivados comuns

| Function | f(x) | f'(x) | ML context |
|---|---|---|---|
| MSE loss | (1/n) sum(y_hat - y)^2 | (2/n)(y_hat - y) | Regression |
| Cross-entropy (binary) | -(y log(p) + (1-y) log(1-p)) | p - y (after sigmoid) | Binary classification |
| Cross-entropy (multi) | -log(p_true_class) | p - one_hot(y) (after softmax) | Multi-class classification |
| Sigmoid | 1 / (1 + e^(-x)) | sigma(x) * (1 - sigma(x)) | Output gates, binary output |
| Tanh | (e^x - e^(-x)) / (e^x + e^(-x)) | 1 - tanh(x)^2 | Hidden activations (legacy) |
| ReLU | max(0, x) | 1 if x > 0, 0 if x < 0 | Default hidden activation |
| Leaky ReLU | max(0.01x, x) | 1 if x > 0, 0.01 if x < 0 | Avoiding dead neurons |
| GELU | x * Phi(x) | Phi(x) + x * phi(x) | Transformers |
| Softmax_i | e^(x_i) / sum(e^(x_j)) | s_i(1 - s_i) for i=j, -s_i*s_j for i!=j | Output layer (Jacobian) |
| Log-softmax | x_i - log(sum(e^(x_j))) | 1 - softmax(x_i) for the i-th entry | Numerically stable CE |
| Linear layer | y = Wx + b | dL/dW = dL/dy * x^T, dL/db = dL/dy | Every layer |
| L2 regularization | lambda * sum(w^2) | 2 * lambda * w | Weight decay |
| L1 regularization | lambda * sum(\|w\|) | lambda * sign(w) | Sparsity |

## Erros comuns

- O factor 1/n em perdas médias de lote (MSE, entropia cruzada) é escalado pelo tamanho do lote.
- Computação de gradiente de softmax como um vetor quando é realmente uma matriz jacobiana. Para entropia cruzada + softmax combinada, o gradiente se simplifica para (p - y), o que evita o jacobiano completo.
- Aplicação da regra da cadeia na ordem errada. Trabalhar para trás da perda: dL/dW = dL/dy * dy/dW.
- Usando h que é muito grande (h = 0,1) ou muito pequeno (h = 1e-15) para derivadas numéricas.
- Esquecendo que a ReLU tem gradiente não definido em exatamente x = 0. Na prática, definir para 0 ou 0,5.

## Recepta de verificação de gradientes

```
For each parameter w:
  numeric_grad = (loss(w + h) - loss(w - h)) / (2h)
  auto_grad = backward pass value
  relative_error = |numeric - auto| / max(|numeric|, |auto|, 1e-8)
  assert relative_error < 1e-5
```

Erro relativo acima de 1e-3 significa que algo está errado.
