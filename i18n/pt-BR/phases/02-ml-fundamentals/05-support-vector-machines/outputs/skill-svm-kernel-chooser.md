---
name: skill-svm-kernel-chooser
description: Escolha o kernel SVM certo e sintonize C e gamma para o seu problema
version: 1.0.0
phase: 2
lesson: 5
tags: [svm, kernel, classification, hyperparameter-tuning]
---

# Guia de seleção do kernel SVM

Os SVM são definidos por duas opções: o kernel (que determina a forma do limite de decisão) e os parâmetros de regularização (que controlam o comércio entre largura de margem e erros de classificação).

## Lista de verificação das decisões

1. Os dados são linearmente separáveis (ou próximos a eles)?
   - Sim: usar o núcleo linear. É mais rápido e mais interpretável.
   - Não, vai para o passo 2.

2. Quantas características contra amostras?
   - Características >> amostras (por exemplo, texto com TF-IDF): usar kernel linear. Dados de alta dimensão são muitas vezes linearmente separaveis. RBF adiciona complexidade sem ganho.
   - amostras >> características (por exemplo, dados tabuleiros com 10-50 características): o kernel RBF é a escolha padrão.

3. Espera-se que o limite da decisão seja suave?
   - Limite liso e contínuo: núcleo RBF
   - Fronteira em forma de polinômio: núcleo polinômio (comece com grau 2 ou 3)
   - Conhecimento de domínio sugere termos de interação específicos: núcleo polinômio com grau correspondente

4. Quão grande é o conjunto de dados?
   - Menos de 10.000 amostras: qualquer kernel funciona, RBF é o padrão seguro
   - 10.000 a 100.000: núcleo linear ou LinearSVC (formulação primária, O(n) por época)
   - Mais de 100.000: não use o SVM do núcleo. Passe para SVM linear, aumento de gradiente ou redes neurais.

5. Escalate as características?
   - Os SVM exigem a escalação de características. Sempre padronize (média zero, variância unitária) antes de ser montado.

## Diagrama de fluxo de seleção do núcleo

```
Start
  |
  v
Features > 1000 or features >> samples?
  Yes --> Linear kernel (LinearSVC for speed)
  No  --> Dataset < 10k samples?
            Yes --> Try RBF first (best general-purpose kernel)
            No  --> Linear kernel (kernel SVMs are O(n^2) to O(n^3))
```

Se o RBF não funcionar bem, tente o grau polinômio 2-3.

## Apontação C (regularização)

C controla a penalidade por classificações erradas.

| C value | Effect | When to use |
|---------|--------|-------------|
| 0.001 - 0.01 | Wide margin, many violations allowed | Noisy data, want generalization |
| 0.1 - 1.0 | Balanced | Good starting range |
| 10 - 1000 | Narrow margin, few violations | Clean data, need high accuracy |

Estratégia de sintonização:
- Comece com C=1.0
- Pesquisa em escala de registro: [0,001, 0,01, 0,1, 1, 10, 100, 1000]
- Use a validação cruzada para escolher o melhor valor
- Se o melhor C estiver na borda do seu alcance, estenda o alcance nessa direção

## Gamma de sintonização (núcleo RBF)

Gamma controla o alcance da influência de um único ponto de treinamento.

| gamma value | Effect | When to use |
|-------------|--------|-------------|
| Small (0.001) | Each point influences a large area. Smooth, simple boundary | Underfitting or few features |
| Medium (auto: 1/n_features) | sklearn default. Reasonable starting point | General use |
| Large (10+) | Each point influences only nearby points. Complex, wiggly boundary | Risk of overfitting |

Estratégia de sintonização:
- Comece com gama="escala" (1 / (n_features * X.var()), o sklearn padrão)
- Pesquisa em escala de registro: [0,001, 0,01, 0,1, 1, 10]
- Baixo gama + alto C tende a ser super ajustado
- Gamma alta + baixa C tende a ser inferior

## Apontação conjunta C e gama

C e gama interagem, sempre sintonizando-os, não de forma independente.

abordagem recomendada:
1. Pesquisa de rede grosseira: C em [0,01, 0,1, 1, 10, 100], gama em [0,001, 0,01, 0,1, 1, 10] (25 combos)
2. Encontrar a melhor região
3. Pesquisa de rede fina em torno da melhor região (por exemplo, C em [5, 10, 20, 50], gama em [0,05, 0,1, 0,2])
4. Utilize uma validação cruzada de 5 vezes durante todo o período

## Erros comuns

- Usando kernel RBF em dados escassos de alta dimensão (linear é melhor e 100 vezes mais rápido)
- Esquecer as características de escala (o único erro mais comum no SVM)
- Apontação de C muito alta em dados barulhentos (memora o ruído em vez de aprender o limite)
- Utilização de SVM do kernel em conjuntos de dados com mais de 50 mil amostras (tempo de treinamento é proibitivo)
- Não sintonizar C e gamma (compensa-se mutuamente)
- Defaulting para o grau polinômio 5+ (overfits agressivamente, tente 2 ou 3 primeiro)

## Referência rápida

| Kernel | When to use | Key parameters | Training complexity |
|--------|------------|----------------|-------------------|
| Linear | Text/TF-IDF, many features, large data | C only | O(n) per epoch |
| RBF | General-purpose, under 10k samples | C, gamma | O(n^2) to O(n^3) |
| Polynomial | Known polynomial relationships | C, degree, coef0 | O(n^2) to O(n^3) |
| Sigmoid | Rarely useful (equivalent to two-layer neural net) | C, gamma, coef0 | O(n^2) to O(n^3) |
