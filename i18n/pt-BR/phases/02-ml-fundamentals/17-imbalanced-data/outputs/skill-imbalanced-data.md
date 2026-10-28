---
name: skill-imbalanced-data
description: Decision checklist for handling imbalanced classification problems
version: 1.0.0
phase: 2
lesson: 17
tags: [imbalanced-data, smote, class-weights, threshold-tuning, evaluation]
---

# Estratégia de dados desequilibrada

Uma lista de verificação de decisões para lidar com a classificação desequilibrada.

## Passo 1: Medir o desequilíbrio

- Contar amostras por classe
- Calcular o índice de desequilíbrio (maioria / minoria)
- Mild: relação < 3:1 (por exemplo, 70/30)
- Moderado: proporção 3:1 a 20:1 (por exemplo, 95/5)
- Gravidade: relação > 20:1 (por exemplo, 99/1)

## Passo 2: Escolha a métrica certa

Prefira precisão/recolha/F1 em vez de precisão para conjuntos de dados desequilibrados.

| Situation | Primary Metric | Secondary Metric |
|-----------|---------------|-----------------|
| Missing positives is very costly (fraud, disease) | Recall | F2 score |
| False alarms are costly (spam filter, recommendations) | Precision | F0.5 score |
| Both matter roughly equally | F1 score | MCC |
| Need a single ranking metric | AUPRC | AUC-ROC |
| Need to compare across datasets | MCC | AUPRC |

## Passo 3: Escolha uma estratégia de reequilíbrio

### Por gravidade do desequilíbrio

| Imbalance | First Try | Second Try | Avoid |
|-----------|-----------|------------|-------|
| Mild (< 3:1) | Class weights | Threshold tuning | Oversampling (unnecessary) |
| Moderate (3:1 to 20:1) | SMOTE + class weights | Threshold tuning on top | Undersampling (too much data loss) |
| Severe (> 20:1) | SMOTE + class weights + threshold | Ensemble with balanced bagging | Undersampling alone |

### Por tamanho do conjunto de dados

| Dataset Size | Preferred Strategy | Reason |
|-------------|-------------------|--------|
| < 1,000 samples | Oversampling or SMOTE | Cannot afford to lose majority data |
| 1,000 - 10,000 | SMOTE + threshold tuning | Enough minority samples for k-NN |
| > 10,000 | Class weights or undersampling | Fast, sufficient minority data |

## Passo 4: Aplique a técnica

### Peso de classe (tenta sempre primeiro)
- Em sklearn: `class_weight='balanced'`
- Não é necessária modificação de dados
- Funciona com qualquer modelo baseado em perdas
- Equivalente ao excesso de amostragem na expectativa

### SMOTE
- Aplicar apenas para dados de formação (nunca teste/validação)
- Use k=5 vizinhos (default)
- Combine com os pesos de classe para melhores resultados
- Cuidado com pontos sintéticos barulhentos perto da fronteira

### Apontação do limiar
- Modelo de trem, obter probabilidades previstas no conjunto de validação
- Limitações de limpeza de 0,05 a 0,95
- Escolha um limiar maximizando a métrica escolhida
- Sempre sintonizar os dados de validação, nunca os dados de teste

## Passo 5: Valida adequadamente

- Utilize validação cruzada estratificada (preserva as proporções de classes em cada dobra)
- Metricas de relatório sobre o conjunto de ensaio original (não reformulado)
- Nunca aplique SMOTE antes de dividir - apenas em dobras de treinamento
- Comparar com a linha de base "prevê sempre a maioria"

## Passo 6: Erros comuns a evitar

- Aplicação de SMOTE a todo o conjunto de dados antes da divisão de trens/testes (vaga de dados)
- Utilizando a precisão como métrica de avaliação
- Não tentar primeiro pesos de classe (abordagem mais simples, muitas vezes suficiente)
- Super-esampulação e validação cruzada (lequeio de pontos sintéticos através das dobras)
- Ignorar a regulação do limiar (performance livre, não é necessário reformulação)
- Usando sub-esampulação aleatória em pequenos conjuntos de dados (lança fora muitos dados)

## Árvore de decisão rápida

1. A relação de desequilíbrio é < 3:1? -> Experimente apenas pesos de classe
2. O conjunto de dados é > 10.000 amostras? -> Peso de classe + ajustamento de limiar
3. O conjunto de dados é < 1.000 amostras? -> SMOTE + peso de classe
4. Caso contrário -> SMOTE + peso de classe + ajuste de limiar
5. Ainda não é bom o suficiente?
