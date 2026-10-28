---
name: skill-evaluation
description: Lista de verificação da estratégia de avaliação para os modelos de classificação e regressão
version: 1.0.0
phase: 2
lesson: 9
tags: [evaluation, metrics, cross-validation, model-selection]
---

# Estratégia de avaliação modelo

Uma lista de verificação para avaliar corretamente qualquer modelo de ML. Siga esta sequência para evitar os erros de avaliação mais comuns.

## Passo 1: Divide os dados corretamente

- Divisão antes de qualquer pré-processamento (escalada, imputação, codificação)
- Usar divisões estratificadas para tarefas de classificação
- Reserve um conjunto de testes que você toque exatamente uma vez no final
- Para pequenos conjuntos de dados, use a validação cruzada de 5 ou 10 vezes em vez de uma única divisão
- Para as séries temporais, use divisões baseadas no tempo (nunca misturar)

## Passo 2: Escolha a métrica certa

### Classificação

| Situation | Use this metric | Why |
|-----------|----------------|-----|
| Balanced classes, simple comparison | Accuracy | Easy to interpret, meaningful when classes are equal |
| False positives are costly (spam filter, fraud alerts) | Precision | Measures how many flagged items are actually positive |
| False negatives are costly (cancer screening, security) | Recall | Measures how many actual positives you catch |
| Need to balance precision and recall | F1 Score | Harmonic mean, punishes extreme imbalance |
| Comparing models across thresholds | AUC-ROC | Threshold-independent ranking quality |
| Imbalanced data | F1, AUC-ROC, or PR-AUC | Accuracy is misleading with imbalanced classes |

### Regressão

| Situation | Use this metric | Why |
|-----------|----------------|-----|
| Standard regression, outliers acceptable | RMSE | Same units as target, penalizes large errors |
| Outlier-robust evaluation | MAE | Treats all errors equally, not dominated by outliers |
| Comparing models on different scales | R-squared | Normalized 0-1 scale (fraction of variance explained) |
| Business requires dollar amounts | MAE or RMSE | Directly interpretable as error magnitude |

## Passo 3: Estabelecer linhas de base

Antes de avaliar o seu modelo, calcule o desempenho de base:
- Classificação: Preditor de classe majoritária (prevê sempre a classe mais comum)
- Regressão: sempre prever a média do objetivo de formação
- Qualquer modelo que não possa vencer estas linhas de base não está aprendendo

## Passo 4: Validação cruzada

- Utilize K-fold (K=5 ou K=10) para estimativas estáveis
- Utilização de um tapete K estratificado para classificação
- Relatório da média e desvio padrão entre as dobras
- Um modelo com média = 0,85 e std = 0,02 é mais confiável do que média = 0,87 e std = 0,10

## Passo 5: Comparar os modelos estatisticamente

- Não escolha o modelo com a pontuação média mais alta sem verificar a importância
- Utilize um teste de t em par através de dobras de validação cruzada
- Se você não é < 2,78 (para K=5, df=4, p<0,05), a diferença pode ser devido ao acaso
- Considere o modelo mais simples quando as diferenças de desempenho não são significativas

## Passo 6: Verifique se há erros comuns

- Fugas de dados: fluem informações de dados de ensaio para o treinamento? (escalagem antes da divisão, características derivadas de alvos)
- Desquilíbrio de classes: a precisão oculta o desempenho pobre das classes minoritárias?
- O que é o "super-ajustamento"?
- Excesso de avaliações: já olhou para o conjunto de testes mais de uma vez?

## Passo 7: Relatório final

- Trem em trem + validação combinada
- Avaliação no conjunto de testes realizados exactamente uma vez
- Relatar a métrica escolhida com intervalos de confiança, se possível
- Indicar a comparação de referência (quão melhor do que o aleatório/médio)
