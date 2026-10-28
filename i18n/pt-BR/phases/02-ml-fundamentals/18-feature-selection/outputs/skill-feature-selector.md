---
name: skill-feature-selector
description: Árvore de decisão de referência rápida para escolher o método de seleção de recursos correto
version: 1.0.0
phase: 2
lesson: 18
tags: [feature-selection, mutual-information, rfe, lasso, tree-importance]
---

# Estratégia de seleção de características

Uma referência rápida para escolher e aplicar o método de selecção adequado.

## Passo 1: Comece com a limpeza

Antes de aplicar qualquer método, remova características obviamente inúteis:

- **Constant features**: variância = 0. Remova-os.
- **Near-constant features**A variância < 0,01 (ou o seu limiar)
- **Duplicate features**- As colunas são idênticas.
- **ID columns**A informação não é generalizável.

Isto leva segundos e pode eliminar 10-30% das características em conjuntos de dados do mundo real confusos.

## Passo 2: Escolha um método baseado na sua situação

### Árvore de decisão rápida

1. **< 50 features?** Comece com a classificação de informações mútuas.
2. **50 - 500 features?** Use primeiro o limiar de variância, em seguida, L1 (Lasso) se usar um modelo linear, ou a importância de árvore se usar árvores.
3. **> 500 features?** Métodos de cadeia: limiar de variância -> filtro de informação mútua (top 50%) -> RFE sobre sobreviventes.
4. **Need interpretability?** A regularização L1 dá-lhe zero exato/não zero.
5. **Need to capture nonlinear relationships?** Informações mútuas ou importância baseada em árvores. Evite L1 (apenas linear).
6. **Need feature interactions?** Os métodos de filtragem não têm interações.

### Referência de método

| Method | When to Use | When to Avoid |
|--------|------------|---------------|
| Variance threshold | Always, as a first step | Never skip this |
| Mutual information | Quick ranking, nonlinear relationships | When you need feature interaction detection |
| RFE | Thorough selection, moderate feature count | Very expensive models, > 1000 features |
| L1 / Lasso | Linear models, fast embedded selection | Nonlinear problems, highly correlated features |
| Tree importance | Nonlinear relationships, feature interactions | Biased by high-cardinality features |
| Permutation importance | Model-agnostic validation, final check | Too slow for initial screening |

## Passo 3: Valida a seleção

- Compare o desempenho do modelo com características selecionadas versus todas as características
- Utilize validação cruzada, não uma única divisão de trem/teste
- Se o desempenho cair em mais de 1-2%, pode ter sido eliminado o recurso útil
- Se o desempenho melhorar, você remover com sucesso o ruído

## Passo 4: lidar com as armadilhas comuns

### Características correlacionadas
- L1 escolhe arbitrariamente um de um grupo correlacionado e zeros os outros
- Calcule a matriz de correlação primeiro e decida quais características correlacionadas manter
- A importância da árvore espalha a importância entre as características correlacionadas

### Fugas de dados
- Seleção de funções adequadas apenas com base em dados de formação
- Aplicar a mesma selecção aos dados de ensaio
- Na validação cruzada, a selecção de características deve ocorrer dentro de cada dobra

### Super-ajustamento à selecção de características
- RFE com muitas iterações pode overfit para o conjunto de treinamento
- Validação em dados mantidos, não em dados utilizados para a seleção
- Utilize a seleção de estabilidade (repetir em sub-mostras) para obter resultados mais robustos

## Passo 5: Lista de verificação da produção

- [ ] Prazo de variação aplicado como primeiro filtro
- [ ] Selecção de características montadas apenas em dados de formação
- [ ] Características selecionadas documentadas (nome, método utilizado, pontuação)
- [ ] Performance comparada: características selecionadas versus todas as características
- [ ] Avaliação cruzada, não dividida
- [ ] Selecção de características integrada no processo de formação (não feita manualmente)
- [ ] Monitoramento em vigor para a deriva de características (as características selecionadas podem ficar obsoletas)
