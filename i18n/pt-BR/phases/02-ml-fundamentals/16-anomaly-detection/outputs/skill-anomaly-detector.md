---
name: skill-anomaly-detector
description: Choose the right anomaly detection approach for your problem
phase: 2
lesson: 16
---

Quando alguém precisa encontrar padrões incomuns em dados, ajude-o a escolher a abordagem certa e a configurá-la corretamente.

## Quadro de decisão

### Passo 1: Que tipo de anomalias?

- **Point anomalies**(valores singulares incomuns) -> Z-score, IQR, Isolation Forest ou LOF
- **Contextual anomalies**(contexto dado incomum como tempo) -> Adicionar características de contexto, em seguida, usar qualquer método
- **Collective anomalies**(seqüências incomuns) -> Características da janela deslizante + qualquer método ou modelos de sequência

### Passo 2: Tem rótulos?

- **No labels at all**-> Não supervisionados: Isolamento florestal, LOF, pontuação Z, IQR, autoencodadores
- **Some labels (few anomaly examples)**-> Semisupervisão: treinar apenas com dados normais, testar em tudo
- **Many labels**-> Supervisionado: trata-o como classificação desequilibrada (mas os tipos de anomalia em que você treinou são os únicos que você vai pegar)

### Passo 3: Quais são as suas limitações?

| Constraint | Best Method |
|-----------|------------|
| Must explain why it is anomalous | Z-score (which feature, how many stds) or IQR (which feature, how far from bounds) |
| Very high-dimensional data (50+ features) | Isolation Forest (handles irrelevant features) |
| Multiple clusters of different densities | LOF (local density comparison) |
| Real-time, single-pass processing | Z-score with running statistics (Welford's algorithm) |
| Large dataset (millions of rows) | Isolation Forest (subsamples) or Z-score (O(n)) |
| Must minimize false alarms | Higher thresholds, tune on precision, use ensemble of methods |

### Passo 4: Como avaliar

- Não usem precisão, com anomalias de 0,1%, sempre prever "normal" dá 99,9% de precisão.
- Utilização**Precision@k**Dos pontos mais suspeitos, quantos são as anomalias reais?
- Utilização**AUPRC**: área abaixo da curva de recomposição de precisão.
- Utilização**Recall at fixed FPR**A taxa de falsos positivos que se pode tolerar, que fracção de anomalias se detecta?
- Comparar sempre com uma linha de base: a pontuação aleatória deve dar a Precision@k igual à taxa de anomalia.

### Passo 5: Erros comuns

1. **Training on contaminated data.**Se o seu conjunto de treinamento contém anomalias, o modelo aprende-as como normal.
2. **Using AUROC with extreme imbalance.**O AUROC pode ser de 0,99, mesmo quando o modelo detecta apenas 10% das anomalias em limiares práticos.
3. **Ignoring temporal context.**Um uso de CPU de 90% é normal durante a implantação, anormal às 3 da manhã.
4. **Fixed thresholds in production.**A distribuição de dados varia, um limiar que funciona hoje pode não funcionar no próximo mês.
5. **Univariate detection on multivariate data.**Verificar cada característica de forma independente evita anomalias que são incomuns apenas quando consideradas juntas.

## Referência rápida

| Method | Speed | Interpretability | Multivariate | Robust to Outliers in Training |
|--------|-------|-----------------|-------------|-------------------------------|
| Z-score | Very fast | High | Per-feature only | No |
| IQR | Very fast | High | Per-feature only | Somewhat |
| Isolation Forest | Fast | Low | Yes | Somewhat |
| LOF | Slow | Medium | Yes | No |
| Autoencoder | Medium | Low | Yes | No |
| One-Class SVM | Medium | Low | Yes | No |
