---
name: skill-statistical-testing
description: Choose the right statistical test for comparing ML models and evaluating experiments
version: 1.0.0
phase: 1
lesson: 15
tags: [statistics, hypothesis-testing, model-comparison]
---

# Testeamento estatístico para ML

Como escolher o teste certo ao comparar modelos, executar experimentos A/B ou validar resultados.

## Lista de verificação das decisões

1. O que você está comparando, meios, proporções, distribuições ou correlações?
2. Quantos grupos? Uma amostra versus referência, dois grupos ou vários grupos?
3. As observações são emparelhadas (o mesmo conjunto de ensaio, as mesmas dobras) ou independentes?
4. Se n < 30 e não for claramente normal, use não-parametral.
5. Os dados são contínuos, ordinários ou categóricos?
6. Quantos testes você está executando? Aplique correção se mais de um.

## Árvore de decisão

```text
Comparing means?
  Two groups?
    Paired (same data splits)? --> Paired t-test (or Wilcoxon signed-rank if non-normal)
    Independent? --> Welch's t-test (or Mann-Whitney U if non-normal)
  Multiple groups?
    Paired? --> Repeated measures ANOVA (or Friedman test)
    Independent? --> One-way ANOVA (or Kruskal-Wallis)

Comparing proportions?
  Two groups? --> Chi-squared test or Fisher's exact test (small n)
  Multiple groups? --> Chi-squared test

Comparing distributions?
  Is one distribution a reference? --> Kolmogorov-Smirnov test
  Are both empirical? --> Two-sample KS test

Measuring association?
  Both continuous, roughly normal? --> Pearson correlation
  Ordinal or non-normal? --> Spearman rank correlation
  Categorical x Categorical? --> Chi-squared test of independence

Running many tests?
  Apply Bonferroni correction: alpha_adjusted = alpha / number_of_tests
  Or use Holm-Bonferroni (less conservative, still controls family-wise error)
```

## Quando utilizar cada teste

| Test | Data type | Assumptions | ML use case |
|---|---|---|---|
| Paired t-test | Continuous, paired | Normal differences | Compare 2 models on same k-fold splits |
| Wilcoxon signed-rank | Continuous/ordinal, paired | None (non-parametric) | Compare 2 models, small k (5-10 folds) |
| Welch's t-test | Continuous, independent | Roughly normal | Compare model on two separate datasets |
| Mann-Whitney U | Continuous/ordinal, independent | None | Compare latency distributions |
| ANOVA | Continuous, 3+ groups | Normal, equal variance | Compare multiple model architectures |
| Kruskal-Wallis | Continuous/ordinal, 3+ groups | None | Compare multiple models, non-normal metrics |
| Chi-squared | Categorical counts | Expected count >= 5 | Compare class distributions, confusion matrices |
| Fisher's exact | Categorical counts | Small samples | Rare event comparison |
| KS test | Continuous | None | Check if predictions follow expected distribution |
| Bootstrap CI | Any statistic | None | Confidence interval for AUC, F1, any metric |
| McNemar's test | Paired binary | None | Compare two classifiers on same test set |

## Recepta de comparação de modelo

1. Defina o nível de métrica e de significância (alfa = 0,05) antes de executar experimentos.
2. Execute ambos os modelos nos mesmos foldos de validação cruzada k-fold (k = 5 ou 10).
3. Recolher pontuações em pares: (a_1, b_1), (a_2, b_2), ..., (a_k, b_k).
4. Diferenças computacionais: d_i = b_i - a_i.
5. Realizar ensaio em par (Wilcoxon para k <= 10, ensaio em par para k > 10 ou diferenças normais).
6. Relatório: valor p, diferença média, intervalo de confiança de 95%, tamanho do efeito (d de Cohen).
7. Se p < alfa E tamanho do efeito é significativo, a diferença é real e vale a pena agir.

## Erros comuns

- Usando um teste independente quando os dados são emparejados. Se ambos os modelos foram avaliados nas mesmas dobras de teste, deve-se usar um teste em par. Os testes independentes descartam o emparejamento e perdem poder estatístico.
- Relatório p < 0,05 sem tamanho de efeito. Uma melhoria de precisão de 0,1% estatisticamente significativa não vale a pena implementar.
- Comparar modelos em diferentes conjuntos de testes. O conjunto de testes DEVE ser idêntico para ambos os modelos.
- Com 20 testes com alfa = 0,05, esperamos um falso positivo por acaso.
- Usando precisão em dados desequilibrados. Em uma classe de maioria de 99%, um classificador trivial atinge 99%. Use F1, AUC de recall de precisão, ou coeficiente de correlação de Matthews.
- Tratar as folhas de validação cruzada como amostras independentes. Eles compartilham dados de treinamento, o que viola a suposição de independência.

## Referência rápida: interpretação do tamanho do efeito

| Cohen's d | Interpretation |
|---|---|
| 0.2 | Small effect |
| 0.5 | Medium effect |
| 0.8 | Large effect |
| > 1.0 | Very large effect |

| What to report | Why |
|---|---|
| p-value | Is the difference real? |
| Confidence interval | How big could the difference be? |
| Effect size (Cohen's d) | Is the difference meaningful? |
| Sample size (n or k folds) | Can we trust the result? |
