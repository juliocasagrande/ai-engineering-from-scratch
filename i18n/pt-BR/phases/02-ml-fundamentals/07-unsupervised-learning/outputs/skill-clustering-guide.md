---
name: skill-clustering-guide
description: Escolha o algoritmo de agrupamento certo com base na forma dos dados, ruído e restrições
version: 1.0.0
phase: 2
lesson: 7
tags: [clustering, k-means, dbscan, hierarchical, gmm, unsupervised]
---

# Guia de seleção de algoritmos de agrupamento

O clustering não tem um único melhor algoritmo. A escolha certa depende da forma do cluster, se você sabe o número de clusters, quanto ruído há nos dados e quão grande é o conjunto de dados.

## Lista de verificação das decisões

1. Sabe o número de aglomerados?
   - Sim: K-Means ou GMM
   - Não: DBSCAN (encontrar automaticamente os aglomerados) ou hierárquico (cortar o dendrograma em diferentes níveis)

2. Que forma têm os aglomerados?
   - Aproximadamente esférica (como uma mancha): K-Means
   - Elíptica de diferentes tamanhos: GMM
   - Formas arbitrárias (crescentes, anéis, cadeias): DBSCAN
   - Aninhados ou hierárquicos: agrupamento hierárquico

3. Os dados contêm ruído ou valores anormais?
   - Sim: DBSCAN (etiquetas de pontos de ruído explicitamente) ou GMM (pontos de baixa probabilidade são anormais)
   - Não , o K-Means está bem .

4. Precisa de atribuições suaves (probabilidades)?
   - Sim: GMM dá P\ cluster \ \ data point) para cada cluster
   - Não: a K-Means ou a DBSCAN dão tarefas difíceis

5. Quão grande é o conjunto de dados?
   - Menos de 10.000: qualquer algoritmo funciona
   - 10.000 a 1.000.000: K-Means (rápido), Mini-Batch K-Means (mais rápido)
   - Mais de 1.000.000: Mini Batch K-Means ou BIRCH.

## Quando utilizar cada abordagem

**K-Means**O método de cotovelo ou a pontuação da silueta para escolher K. Limitações: assume aglomerados esféricos, sensíveis à inicialização (use K-Means++ ou executar várias vezes), não pode lidar bem com diferentes tamanhos de aglomerados.

**DBSCAN**A melhor forma de detectar aglomerados de forma arbitrária e de detectar automaticamente valores anormais. Dois parâmetros: eps (radius de bairro) e min_samples (densidade mínima). Não requer especificar K. Limitações: lutas quando os aglomerados têm densidades muito diferentes, e sintonizar eps pode ser complicado. Use um gráfico de distância k para estimar eps: calcule a distância para o vizinho k-th mais próximo de cada ponto, classifique e procure um cotovelo.

**Hierarchical (Agglomerative)**A ligação de Ward funciona melhor para aglomerados compactos. A ligação única encontra aglomerados alongados, mas é sensível ao ruído. Limitações: memória O(n^2) e tempo O(n^3, tão impraticável para grandes conjuntos de dados.

**GMM (Gaussian Mixture Models)**O método de classificação de dados é um método de classificação de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de

## Avaliação da qualidade do cluster (sem rótulos)

| Metric | What it measures | Range | Use when |
|--------|-----------------|-------|----------|
| Silhouette score | Cohesion vs separation | -1 to 1 (higher is better) | Comparing K values or algorithms |
| Inertia (within-cluster SS) | Tightness of clusters | 0 to inf (lower is better) | Elbow method for K-Means |
| BIC / AIC | Model fit with complexity penalty | Lower is better | Choosing number of GMM components |
| Calinski-Harabasz index | Ratio of between to within variance | Higher is better | Quick comparison |
| Davies-Bouldin index | Average similarity between clusters | Lower is better | Penalizes overlapping clusters |

## Erros comuns

- Funcionamento K-Means sem características de escalagem (funções em escalas maiores dominam o cálculo da distância)
- Selecionar K através da análise de dados em 2D quando os dados reais são de alta dimensão (utilizar pontuações de silueta)
- Utilização de K-Means em aglomerados não esféricos (dados crescentes ou em forma de anel necessitam de DBSCAN)
- Configuração de eps DBSCAN muito grandes (todo em um cluster) ou muito pequenos (todo é ruído)
- Tratar os rótulos de cluster como verdade fundamental (o clusteramento é exploratório; validar com conhecimento do domínio)
- Execução de agrupamentos hierárquicos em conjuntos de dados com mais de 20.000 pontos (explode memória e tempo)

## Referência rápida

| Algorithm | Cluster shape | Finds K | Handles noise | Soft assignments | Scalability |
|-----------|--------------|---------|---------------|-----------------|-------------|
| K-Means | Spherical | No (you set K) | No | No | Millions |
| Mini-Batch K-Means | Spherical | No | No | No | Tens of millions |
| DBSCAN | Arbitrary | Yes | Yes | No | Hundreds of thousands |
| Hierarchical | Any (linkage-dependent) | Flexible (cut dendrogram) | Depends on linkage | No | Under 20k |
| GMM | Elliptical | No (you set K) | Partial (low probability) | Yes | Under 100k |
| HDBSCAN | Arbitrary | Yes | Yes | Partial | Hundreds of thousands |
