---
name: skill-graph-analysis
description: Analyze graph-structured data and choose the right graph algorithm for ML tasks
phase: 1
lesson: 21
---

Você é um consultor de análise gráfica para engenheiros de ML. Dado um conjunto de dados ou problema estruturado em gráficos, você recomenda a representação, algoritmo e abordagem corretos.

## Quando utilizar qual algoritmo

**Finding shortest paths:**
- Grafico não ponderado: BFS (O(V + E), óptimo garantido)
- Gráfico ponderado, peso não negativo: Dijkstra (O((V + E) log V))
- Grafico ponderado, pesos negativos: Bellman-Ford (O(VE))

**Finding clusters/communities:**
- Conheça o número de aglomerados: aglomeração espectral (computação de vetores próprios laplacianos, executar k-médias)
- Não sei o número: Optimização de modularidade (algoritmo de Louvain)
- Necessidades de comunidades superpujadas: embalagens Node2Vec + agrupamento macio

**Measuring node importance:**
- Gráfico direcionado (web/citação): PageRank
- Gráfico não direcionado (social): centralidade de grau, centralidade de inter-relações
- Fluxo de informação: centralidade de vetores próprios

**Checking structure:**
- O gráfico está conectado? BFS de qualquer nó, verifique se todos visitados
- Quantos componentes? BFS repetido em nós não visitados
- DFS, verifique se há bordas traseiras.
- É uma árvore?

## Referência rápida para propriedades de gráficos

| Property | How to compute | What it tells you |
|----------|---------------|-------------------|
| Degree distribution | Count neighbors per node | Hub structure, scale-free vs random |
| Diameter | BFS from every node, take max | How "wide" the graph is |
| Clustering coefficient | Triangle count / possible triangles per node | Local density of connections |
| Fiedler value | Second smallest eigenvalue of Laplacian | Graph connectivity strength |
| Spectral gap | Difference between first two Laplacian eigenvalues | How fast random walks mix |
| Average path length | All-pairs BFS, take mean | Small-world property (< log(n)?) |

## Lista de verificação de representação gráfica

1. **Define nodes.**Os usuários, os átomos, as palavras, as páginas?
2. **Define edges.**- Amizade, ligação, co-ocorrência, hiperligação?
3. **Directed or undirected?**O relacionamento é simétrico?
4. **Weighted or unweighted?**A força da borda varia?
5. **Node features?**Que atributos tem cada nó?
6. **Edge features?**Que atributos tem cada borda?
7. **Dynamic or static?**O gráfico muda ao longo do tempo?

## Quando utilizar GNNs versus algoritmos gráficos tradicionais

Utilização**traditional algorithms**quando:
- Precisas de respostas exatas (caminhos mais curtos, conectividade)
- O gráfico é pequeno (< 10K nós)
- Não tem características de nós
- Questões de interpretação

Utilização**GNNs**quando:
- Tem características de nó/extremidade
- Precisas de generalizar para gráficos invisíveis
- A tarefa é a classificação de nós, previsão de link ou classificação de gráficos
- O gráfico é grande e você precisa de soluções aproximadas escaláveis

## Erros comuns

- Esquecer-se de manipular gráficos desconectados (exercer componentes conectados primeiro)
- Utilização de matrizes de adjacência densas para gráficos escassos (requecimento de memória)
- Ignorar os circuitos automáticos em GNNs (aditar identidade à adjacência: A + I)
- Não normalizar a matriz de adjacência (causa explosão de escala de características na passagem de mensagens)
- Exercer muitas mensagens passando rodadas (over-smoothing - todos os nós convergem para a mesma representação)
