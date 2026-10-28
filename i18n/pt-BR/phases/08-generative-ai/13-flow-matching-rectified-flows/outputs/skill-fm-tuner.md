---
name: fm-tuner
description: Convert a diffusion training plan into a flow-matching / rectified-flow config.
version: 1.0.0
phase: 8
lesson: 13
tags: [flow-matching, rectified-flow, diffusion]
---

Dado um plano de formação de estilo difusão (dados, computação, cronograma, contagem de etapas-alvo, barra de qualidade), produzir um equivalente de correspondência de fluxo:

1. Programa + interpolante. Linear (fluxo corrigido), transporte óptimo (Lipman OT-CFM), conservando variância ou cosino. Razão de uma frase.
2. Amostragem de tempo: uniforme, logit-normal (SD3) ou ponderado pelo modo.
3. Meta. Velocidade v = x_1 - x_0 (fluxo corrigido) ou alfa'(t) x_1 + sigma'(t) x_0 (CFM).
4. Otimizador + aquecimento de lr. Incluir AdamW com beta2 = 0,95 para estabilidade na escala do transformador.
5. Plano de reflow. Se executar 0, 1 ou 2 iterações de reflow; orçamento por iteração ~ re-inferência completa sobre um subconjunto curado.
6. Número de etapas: meta de contagem de etapas de treinamento, etapas de inferência esperadas (20, 4, 2, 1), gama de escala de orientação.
7. Eval. FID/ CLIP-score em relação à linha de base de difusão, qualidade do gráfico versus contagem de etapas.

Recusar a fazer refluxo antes de v_1 convergir (refluxo em um modelo ruim apenas se cozinha na direção ruim). Recusar recomendar inferência de 1 passo sem destilação de consistência no topo. Marque qualquer modelo de correspondência de fluxo que visa a inferência de 20 passos - se você precisar de tantos passos, você desperdiçou a reformulação.
