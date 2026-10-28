---
name: skill-classification-baseline
description: Establish a strong classification baseline before reaching for complex models
version: 1.0.0
phase: 2
lesson: 3
tags: [classification, logistic-regression, baseline, preprocessing]
---

# Guia de base de classificação

Antes de tentar modelos complexos, estabeleça uma linha de base com regressão logística. Ela treina em segundos, produz probabilidades e é totalmente interpretável. Um número surpreendente de problemas do mundo real nunca precisa de nada mais sofisticado.

## Lista de verificação das decisões

1. É provável que a decisão seja linear?
   - Sim: a regressão logística será provavelmente suficiente
   - Não: ainda quer que seja uma linha de base para medir a melhoria

2. Quantas características tens?
   - Menores de 50 anos: Regressão logística normal funciona bem
   - 50 a 10.000: adicionar regularização de L2 (Ridge)
   - Mais de 10.000 (por exemplo, características de texto TF-IDF): utilizar regularização L1 (Lasso) ou LinearSVC

3. O conjunto de dados está desequilibrado?
   - Ratio abaixo de 5:1: provavelmente bem sem ajuste
   - 5:1 a 50:1: uso `class_weight="balanced"`em sklearn
   - Mais de 50:1: combinar a ponderação da classe com métricas adequadas (precisão, retirada ou F1)

4. Há características em escalas diferentes?
   - Sempre padronize antes da regressão logística. Utiliza otimização baseada em gradientes, e características não escaladas lentamente convergem ou distorcem a fronteira de decisão.

5. Há valores faltantes?
   - Imputa antes de ser montado.
   - Use a imputação mediana para colunas numéricas, modo para categorias.

## Quando a regressão logística é boa o suficiente

- Classificação binária com relações de características principalmente lineares
- Você precisa de probabilidades de saída (não apenas rótulos de classe)
- É necessária a interpretabilidade (os coeficientes indicam a direcção da importância das características e a magnitude relativa após a normalização)
- Os dados de formação são pequenos (centenas a milhares de amostras)
- Você precisa de um modelo rápido para a distribuição em tempo real (produto de ponto único na inferência)
- Requisitos regulamentares ou de conformidade exigem explicabilidade

## Quando atualizar

- A precisão está bem abaixo do alvo e tentou a engenharia de recursos.
- A relação entre características e objetivo é claramente não linear (verifique as parâmetros residuais)
- Você tem grandes dados tabuleiros (10k + linhas): tente aumentar o gradiente (XGBoost ou LightGBM)
- As características têm interações complexas que as características polinômias não podem capturar
- Você tem imagem, texto ou dados sequenciais: regressão logística em entradas brutas não funcionará

## Passo de pré-processamento para uma linha de base de classificação

1. **Train/test split**Primeiro, antes de qualquer pré-processamento. Isto evita vazamento de dados.
2. **Handle missing values**A mediana é numérica, a moda é categórica.
3. **Encode categoricals**A codificação de alvos só se aplica em rolos de treinamento (utilizar a codificação fora de rolos para evitar vazamentos).
4. **Scale numerics**- StandardScaler (média zero, variação unitária).
5. **Fit logistic regression**com`C=1.0`(regularização por defeito).
6. **Evaluate**Matriz de confusão, precisão, recall, F1.
7. **Tune threshold**A definição de um valor de 0,5 é raramente ideal.

## Erros comuns

- Avaliação da precisão apenas em dados desequilibrados (um modelo que prevê que a classe majoritária tem pontuações elevadas, mas é inútil)
- Esquecer as características de escala (regressão logística com características não escaladas se move lentamente e converge para uma solução pior)
- Utilização do conjunto de ensaio para ajustar o limiar de decisão (validação de utilização ou validação cruzada)
- Salto da linha de base e salto direto para XGBoost (perde-se a interpretabilidade e não há ponto de referência)
- Não verificar a multicolinariedade (as características altamente correlacionadas aumentam a variação do coeficiente)

## Referência rápida

| Scenario | Model | Regularization | Key setting |
|----------|-------|---------------|-------------|
| Few features, interpretable | LogisticRegression | L2 (default) | C=1.0 |
| Many features, some irrelevant | LogisticRegression | L1 | penalty="l1", solver="saga" |
| High-dim sparse (text) | SGDClassifier | L1 or ElasticNet | loss="log_loss" |
| Imbalanced classes | LogisticRegression | L2 | class_weight="balanced" |
| Need probabilities | LogisticRegression | L2 | predict_proba() |
| Need class labels only | LinearSVC | L2 | Faster than LR for large data |
