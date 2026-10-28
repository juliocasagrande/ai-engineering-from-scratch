---
name: skill-svd
description: Apply SVD to real problems including compression, denoising, recommendations, and least-squares solving
phase: 1
lesson: 11
---

Você é especialista em aplicar a decomposição de valores singulares a problemas práticos de engenharia. Quando lhe é dada uma tarefa que envolve matrizes, compressão de dados, ruído, dados faltantes ou sistemas lineares, determine se o SVD é a ferramenta certa e como aplicá-lo.

## Quadro de decisão

### Passo 1: Identificar o tipo de problema

- **Data compression / dimensionality reduction**Use SVD truncado. Mantenha os valores singulares superiores k. Escolha k por limiar de energia (95% é um objetivo comum) ou por desempenho de tarefa a jusante.
- **Noise reduction**Calcule o SVD completo. Procure uma lacuna no espectro de valores singulares. Truncate abaixo da lacuna. A lacuna separa o sinal do ruído.
- **Missing data / recommendations**Encher as entradas faltantes (médias ou zeros de linha), calcular SVD, reconstruir com baixo grau. Na produção, use ALS ou SVD incremental que lidem com os dados faltantes de forma nativa.
- **Least-squares / pseudoinverse**Compute SVD. Inverte valores singulares não-zero. Multiplica V Sigma + U^T pelo vetor alvo. Mais estável do que as equações normais.
- **Text similarity / topic modeling**A partir de agora, o sistema de cálculo pode ser aplicado a partir de um ponto de vista de base.
- **Numerical rank determination**Calcule SVD. Conte valores singulares acima de um limiar (relativo ao maior).
- **Matrix norm computation**A norma espectral = maior valor singular. A norma de Frobenius = sqrt ((suma dos valores singulares ao quadrado).
- **Condition number**Sigma_max / sigma_min. Diz-lhe o quão sensível o sistema é às perturbações.

### Passo 2: Escolha a variante certa

| Situation | Method | Why |
|-----------|--------|-----|
| Dense matrix, full decomposition needed | `np.linalg.svd(A)` / `svd(A)` in Julia | Standard algorithm, numerically stable |
| Only top k components needed | `scipy.sparse.linalg.svds(A, k)` | Faster than full SVD when k is small |
| Sparse matrix | `scipy.sparse.linalg.svds` | Handles sparse storage efficiently |
| Streaming data | Incremental SVD / online SVD | Updates decomposition without recomputing from scratch |
| Missing data (recommendations) | ALS, Funk SVD, or NMF | Standard SVD requires a complete matrix |
| Very large matrix (millions of rows) | Randomized SVD (`sklearn.utils.extmath.randomized_svd`) | O(mn log k) instead of O(mn min(m,n)) |
| PCA on centered data | SVD of centered data matrix | Equivalent to eigendecomposition of covariance, but more stable |

### Passo 3: Escolha a classificação k

- **Energy threshold**: Calcule a energia acumulada = soma ((sigma_1^2 ... sigma_k^2) / soma ((todas as sigmas^2).
- **Gap detection**A diferença entre o sinal e o ruído indica o limite.
- **Cross-validation**Para as tarefas a seguir, varrer k e medir o desempenho em dados mantidos.
- **Elbow method**O cotovelo é onde adicionar mais componentes deixa de ajudar.
- **Domain knowledge**Se você sabe que os dados têm d fatores subjacentes, use k = d.

### Passo 4: Validação dos resultados

- **Reconstruction error**Computação de dados: A_k_rõ_rõ_rõ_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_r_
- **Explained variance**Para PCA/compressão, indicar a fracção da variância total (energia) capturada.
- **Downstream task performance**Se o SVD for uma etapa de pré-processamento, medir a métrica de ponta a ponta.
- **Visual inspection**Para as imagens, compare a imagem original e a imagem reconstruída visualmente.

## Erros comuns

- Computação de SVD através da própria composição de A^T A. Isto quadrata o número de condição e perde a precisão numérica.
- Usar SVD completo quando apenas os componentes de topo k são necessários. Para matrizes grandes, use SVD truncado ou aleatório.
- Aplicar SVD diretamente a uma matriz com entradas faltantes. SVD padrão requer uma matriz completa. Use métodos de conclusão de matriz (ALS, Funk SVD) em vez disso.
- Ignorando o centramento. Para PCA, os dados devem ser centrados (média subtraída) antes do SVD. Sem centramento, o primeiro componente capta a média, não a variância.
- Se mantermos valores singulares muito poucos, perdemos o sinal, se mantermos muitos, mantemos o ruído, usamos limites de energia ou validação cruzada.
- Confonder SVD com a própria composição. SVD funciona em qualquer matriz (qualquer forma, qualquer grau).

## Padrões de código

### Compressão rápida
```python
U, S, Vt = np.linalg.svd(A, full_matrices=False)
k = np.searchsorted(np.cumsum(S**2) / np.sum(S**2), 0.95) + 1
A_compressed = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
```

### Pseudoinversos para os mínimos quadrados
```python
U, S, Vt = np.linalg.svd(A, full_matrices=False)
S_inv = np.array([1/s if s > 1e-10 else 0 for s in S])
x = Vt.T @ np.diag(S_inv) @ U.T @ b
```

### Denúncia
```python
U, S, Vt = np.linalg.svd(noisy_data, full_matrices=False)
k = find_gap(S)
clean_data = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
```

### APA de grande escala
```python
from sklearn.utils.extmath import randomized_svd
U, S, Vt = randomized_svd(X_centered, n_components=50, random_state=42)
explained_variance = S**2 / (n_samples - 1)
```

## Quando NÃO utilizar SVD

- A matriz é muito escassa e só precisamos de alguns componentes.
- Se precisar de fatores não negativos (modelagem de tópicos, desmesura espectral), use NMF em vez disso.
- Os dados têm uma estrutura não linear forte que os métodos lineares não podem capturar.
- Precisam de atualizações em tempo real sobre os dados de streaming e a matriz muda constantemente.
- A matriz se encaixa na memória, mas é tão grande que até mesmo a SVD aleatória é muito lenta.

## Custo computacional

| Method | Time | Space |
|--------|------|-------|
| Full SVD of m x n matrix | O(mn min(m,n)) | O(mn) |
| Truncated SVD (top k) | O(mnk) | O((m+n)k) |
| Randomized SVD (top k) | O(mn log k) | O((m+n)k) |
| Power iteration (1 vector) | O(mn * iters) | O(m+n) |

Para uma matriz 10000 x 5000:
- Total de SVD: ~ 250 mil milhões de operações
- SVD truncado (k=50): ~ 2,5 mil milhões de operações
- SVD aleatório (k=50): ~ 500 milhões de operações

Escolha o método que corresponda às suas exigências de escala e precisão.
