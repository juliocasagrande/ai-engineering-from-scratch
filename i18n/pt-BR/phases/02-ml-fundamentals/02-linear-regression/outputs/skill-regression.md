---
name: skill-regression
description: Choose the right regression approach based on data characteristics and problem constraints
version: 1.0.0
phase: 2
lesson: 2
tags: [regression, linear-regression, polynomial-regression, ridge, regularization]
---

# Guia de estratégia de regressão

A regressão prevê valores contínuos. A abordagem correta depende da relação entre características e alvo, do número de características e do risco de sobreajuste.

## Lista de verificação das decisões

1. A relação entre características e alvo é aproximadamente linear?
   - Sim: comece com regressão linear ordinária
   - Não: tente características polinómicas ou um modelo não linear

2. Quantas características tem em relação às amostras?
   - Poucas características, muitas amostras: regressão linear comum funciona bem
   - Muitas características, poucas amostras: utilização de regularização (Ridge ou Lasso)
   - Mais características do que amostras: Lasso (L1) para selecionar características, ou Ridge (L2) para encolher todos os pesos

3. Precisas de interpretação?
   - Sim: regressão linear com poucas características, ou Lasso para seleção automática de características
   - Não: características polinómicas ou passar para modelos baseados em árvores ou redes neurais

4. O seu conjunto de dados é pequeno (menos de 10.000 filas)?
   - Use a equação normal (solução de forma fechada) para a velocidade
   - A validação cruzada é essencial para uma avaliação confiável

5. O seu conjunto de dados é grande (milhões de linhas)?
   - Utilize descida de gradiente estocástica (SGD) ou descida de gradiente de mini lote
   - A equação normal é muito lenta devido à inversão de matriz O ((n^3)

## Quando utilizar cada abordagem

**Ordinary Linear Regression**Se R-quadrado é aceitável e o modelo é simples, parar aqui.

**Polynomial Regression**A partir de 1°C, o número de pontos de correção é de 0,00 mm.

**Ridge Regression (L2)**Todos os pesos diminuem para zero, mas nenhum se torna exatamente zero.

**Lasso Regression (L1)**O Lasso leva os pesos de características irrelevantes a zero exatamente, realizando a seleção automática de características.

**Elastic Net**Utilize quando você tem muitos recursos correlacionados e deseja alguma seleção de recursos.

## Erros comuns

- Salto de características de escala antes da descida de gradiente (convergência torna-se extremamente lenta)
- Utilização de desempenho do conjunto de testes para ajustar os hiperparâmetros (conjunto de validação de uso ou validação cruzada)
- A instalação de polinômios de alto grau sem verificar o erro de validação (a formação R^2 aumenta sempre com o grau)
- Ignorar as parâmetros residuais (R^2 pode ser enganoso se os resíduos apresentarem padrões)
- Tratar R^2 como a única métrica (verificar a distribuição residual, a MAE e os limiares específicos do domínio)

## Referência rápida

| Method | When to use | Regularization | Feature selection |
|--------|------------|---------------|-------------------|
| OLS | Baseline, few features | None | Manual |
| Ridge | Many features, all relevant | L2 (shrink) | No |
| Lasso | Many features, few relevant | L1 (zero out) | Automatic |
| Elastic Net | Many correlated features | L1 + L2 | Partial |
| Polynomial | Nonlinear relationship | Add Ridge/Lasso on top | Manual degree choice |
