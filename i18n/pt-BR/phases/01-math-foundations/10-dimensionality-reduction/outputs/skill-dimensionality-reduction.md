---
name: skill-dimensionality-reduction
description: Escolha a técnica de redução de dimensionalidade certa para uma determinada tarefa com base no tamanho dos dados, no objetivo e no uso a jusante
phase: 1
lesson: 10
---

É um especialista na selecção e aplicação de métodos de redução de dimensões.

## Quadro de decisão

### Passo 1: Identifique o objetivo

- **Preprocessing for a model** (classificação, regressão, agrupamento): Utilize PCA. É rápido, determinista e produz características classificadas por conteúdo de informação.
- **2D visualization of cluster structure**: Use UMAP (default) ou t-SNE (se o conjunto de dados for pequeno e desejar agrupamentos locais apertados).
- **Noise removal**: Utilize PCA com um limiar de variância (conserva componentes que explicem 95% da variância).
- **Feature compression for storage or speed**Use PCA. Escolha k por desempenho de tarefa a jusante, não apenas variância.

### Passo 2: Verificar as restrições

| Constraint | Recommendation |
|------------|---------------|
| Dataset > 100k samples | PCA or UMAP. Avoid t-SNE (O(n^2) without approximation). |
| Need deterministic results | PCA. t-SNE and UMAP are stochastic. |
| Nonlinear manifold structure | UMAP or t-SNE. PCA only captures linear relationships. |
| Need to transform new data | PCA (has an exact transform). UMAP supports approximate transform. t-SNE does not transform new points. |
| Interpretable components | PCA. Each component is a weighted combination of original features. |
| High-dimensional input (>1000 features) | Apply PCA first to 50-100 dimensions, then t-SNE or UMAP for visualization. |

### Passo 3: Configurar parâmetros

**PCA:**
- `n_components`Para a visualização, use 2. Para o pré-processamento, varrer k e medir a precisão a jusante.

**t-SNE:**
- `perplexity`Os valores de baixa (5-10) para grupos pequenos e apertados. Os valores de alta (30-50) para estrutura mais ampla. Tente valores múltiplos.
- `n_iter`Pelo menos 1000.
- Aplicar sempre o PCA primeiro para reduzir para 50 dimensões antes de t-SNE.

**UMAP:**
- `n_neighbors`5-50. Baixo para detalhes locais, alto para layout global.
- `min_dist`Os valores baixos são agrupados com força.
- `metric`: "Euclídico" para dados densos, "cosino" para inserções de texto.

### Passo 4: Validação

- Para PCA: verifique a curva de variância explicada. Um cotovelo afiado confirma a dimensionalidade intrínseca baixa.
- Para t-SNE/UMAP: executar várias vezes com sementes diferentes. Aglomerados que aparecem consistentemente são reais. Aglomerados que se movem são artefatos.
- Para pré-processamento: medir o desempenho da tarefa a jusante. Se a precisão não diminuir após a redução, você manteve o sinal.

## Erros comuns

- Usando a saída t-SNE como características de entrada para um modelo. t-SNE é apenas para visualização.
- Interpretação das distâncias entre os clusters t-SNE como significativas.
- Aplicar PCA sem centrar.
- A escolha dos componentes PCA por contagem em vez de por variação explicada. 50 componentes num conjunto de dados é muito diferente de 50 noutro.
- A execução de t-SNE em dados de alta dimensão crus.
