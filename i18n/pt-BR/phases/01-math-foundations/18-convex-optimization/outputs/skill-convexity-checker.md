---
name: skill-convexity-checker
description: Determine se um problema de otimização é convexo e escolha o solucionador certo
version: 1.0.0
phase: 1
lesson: 18
tags: [optimization, convexity, solvers]
---

# Verificador de convexidade

Como verificar se um problema de otimização é convexo e o que fazer com a resposta.

## Lista de verificação das decisões

1. A função objetiva é convexa? (Cheque a semidefinição positiva de Hessian ou use regras de composição.)
2. São todas as restrições de desigualdade da forma g_i(x) <= 0 onde cada g_i é convexa?
3. São todas as restrições de igualdade afinas (lineares)?
4. Se todos os três forem sim, o problema é convexo. Use um solvente convexo com garantias de convergência.
5. Se não, o problema não é convexo.

## Como testar a convexidade de uma função

| Test | Applies to | Method |
|---|---|---|
| Second derivative >= 0 | Scalar functions f(x) | Compute f''(x). If f''(x) >= 0 for all x, convex. |
| Hessian is PSD | Multivariate functions f(x) | Compute H(x). If all eigenvalues >= 0 everywhere, convex. |
| Definition test | Any function | Check f(tx + (1-t)y) <= t*f(x) + (1-t)*f(y) for sampled x, y, t. |
| Composition rules | Composed functions | See composition table below. |
| Restriction to a line | Multivariate f | f is convex iff g(t) = f(x + tv) is convex in t for all x, v. |

## Regras de composição (preservando a convexidade)

| Operation | Result |
|---|---|
| f + g (both convex) | Convex |
| c * f (c > 0, f convex) | Convex |
| max(f, g) (both convex) | Convex |
| f(Ax + b) where f is convex | Convex |
| g(f(x)) where g is convex non-decreasing and f is convex | Convex |
| g(f(x)) where g is convex non-increasing and f is concave | Convex |
| sum of convex functions | Convex |
| pointwise supremum of convex functions | Convex |

## Objectivos comuns da ML: convexos ou não?

| Objective | Convex? | Reason |
|---|---|---|
| MSE: (1/n) sum(y - Xw)^2 | Yes | Quadratic in w, Hessian = (2/n) X^T X is PSD |
| Logistic loss: sum(log(1 + exp(-y_i * w^T x_i))) | Yes | Sum of convex functions (log-sum-exp family) |
| Hinge loss: sum(max(0, 1 - y_i * w^T x_i)) | Yes | Max of convex (linear) functions |
| L2 regularization: lambda * \|\|w\|\|^2 | Yes | Quadratic, Hessian = 2*lambda*I |
| L1 regularization: lambda * \|\|w\|\|_1 | Yes | Sum of absolute values (convex but not differentiable) |
| Ridge regression: MSE + L2 | Yes | Sum of two convex functions |
| LASSO: MSE + L1 | Yes | Sum of two convex functions |
| Elastic net: MSE + L1 + L2 | Yes | Sum of convex functions |
| SVM (primal): hinge + L2 | Yes | Sum of convex functions |
| Cross-entropy with softmax | Yes (in logits) | Log-sum-exp is convex |
| Neural network (any loss) | No | Nonlinear activations create non-convex composition |
| k-means objective | No | Discrete assignment step |
| Matrix factorization: \|\|X - UV^T\|\|^2 | No | Bilinear in U and V |
| GAN loss | No | Minimax, non-convex in generator |
| Contrastive loss (InfoNCE) | No | Log of ratio of exponentials with negative samples |

## Seleção de solventes com base na convexidade

| Problem type | Solver | Convergence guarantee |
|---|---|---|
| Convex, smooth, unconstrained | Gradient descent | O(1/k) to global minimum |
| Convex, smooth, unconstrained | L-BFGS | Superlinear to global minimum |
| Convex, smooth, unconstrained | Newton's method | Quadratic near minimum (if Hessian tractable) |
| Convex, smooth, constrained | Interior point method | Polynomial time |
| Convex, non-smooth (L1) | Proximal gradient / ISTA | O(1/k) to global minimum |
| Convex, non-smooth (L1) | ADMM | Flexible, handles constraints |
| Convex, quadratic | Conjugate gradient | Exact in n steps |
| Non-convex, smooth | SGD / Adam | Converges to local minimum |
| Non-convex, smooth | SGD + restarts | Better local minimum on average |
| Non-convex, smooth | Overparameterize + SGD | Flat minima, good generalization |

## Erros comuns

- Suponha que um problema seja convexo porque a função de perda é convexa. A perda deve ser convexa nos parâmetros que você está otimizando. A entropia cruzada é convexa nos logits, mas o mapeamento completo da rede neural de entradas para logits não é convexo.
- Usando o método de Newton em um problema não convexo. O Hessiano pode ter valores próprios negativos, fazendo com que Newton se mova em direção a pontos de sela ou máximas em vez de mínimos.
- Esquecer que a regularização L1 torna o objetivo não diferenciável em zero. A descida de gradiente padrão não funciona bem. Use métodos de descida de gradiente proximal ou subgradiente.
- Quadratando o número da condição formando A^T A. Se você precisar resolver um problema de mínimos quadrados e A é mal condicionado, use QR ou SVD em vez das equações normais.
- Declarar um problema não convexo sem verificar. Muitos problemas de ML (modelos lineares, SVMs, regressão logística) são convexos e beneficiam de soluções mais fortes.

## Teste rápido: o meu problema é convexo?

```
1. Write out the objective: minimize f(w) subject to constraints
2. For each term in f(w):
   - Is it quadratic with PSD matrix? -> Convex
   - Is it a norm? -> Convex
   - Is it log-sum-exp? -> Convex
   - Does it involve w nonlinearly (sigmoid(w), w1*w2)? -> Likely non-convex
3. Are all constraints linear or convex inequalities?
4. If ALL terms are convex and constraints are convex/linear -> problem is convex
5. If ANY term is non-convex -> problem is non-convex
```
