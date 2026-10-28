---
name: training-budget-estimator
description: Estimação (N, D, horas, número de GPUs) de uma nova formação de transformador dada a limitação do orçamento computacional e da implantação.
version: 1.0.0
phase: 7
lesson: 13
tags: [scaling-laws, training, chinchilla]
---

Dado um objetivo de formação (perda de meta / MMLU meta / métrica de meta a jusante), orçamento de cálculo (dolares ou FLOPs), volume de inferência (tokens/mês) e restrições (dispositivo-alvo, memória, latência), saída:

1. O regime de computação. Chinchilla-ótimo, sobre-treinado (inferência-ótimalizado), sub-treinado (prototipo). Razão de uma frase ligada ao volume de inferência.
2. N e D. Valores concretos. `D/N` Se estiveres treinado demais, nota a penalidade de perda contra o Chinchilla-optimo.
3. O treinamento de relógio de parede. Horas × GPU-conta dado o teor de treinamento assumido (MFU ≈ 40% para denso, ~ 30% para MoE).
4. Fontes de dados: corporações denominadas ou orçamento sintético. `D` excede os tokens de alta qualidade disponíveis.
5. Nota de risco: um modo de falha específico: contaminação de dados, instabilidade do optimizador em escala, desajuste do tokenizer de comprimento de contexto, saturação da suíte de avaliação.

Recusar a formação de um modelo denso >8B sob Chinchilla-óptimo se servir um volume de inferência elevado  os compostos de custo de inferência. Recusar-se a definir a perda-alvo sem uma série de avaliações definida. A marca de qualquer gasto de planos > 1% do orçamento para pesquisa de arquitetura em vez de curatividade de dados  os retornos são conhecidos por serem pequenos. Requer uma execução de 1% do orçamento em escala para validar as suposições antes de se comprometer o orçamento completo.
