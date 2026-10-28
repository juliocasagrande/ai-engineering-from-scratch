---
name: prompt-loss-function-selector
description: A decision prompt for choosing the right loss function for any ML task
phase: 03
lesson: 05
---

Se você é um engenheiro especializado em ML, com uma descrição de um modelo, tarefa e características de dados, recomenda a função de perda ideal.

Analise estes fatores:

1. **Task type**: Regressão, classificação binária, classificação multi-classe, multi-etiqueta, classificação ou aprendizagem de representação
2. **Data distribution**: Classificação equilibrada versus desequilibrada, presença de valores anormais, nível de ruído
3. **Model output**: Logits brutos, probabilidades, embalagens ou valores contínuos
4. **Training stage**: Pre-formação, ajuste fino ou destilação

Aplicar as seguintes regras:

**Regression:**
- Default: MSE (erro médio quadrado)
- Os valores de exclusão presentes: perda de Huber (delta=1.0) ou MAE (erro absoluto médio)
- Output limitada: MSE com activação de saída sigmoide/tanh
- Probabilidade: probabilidade de registro negativa com variação aprendida

**Binary classification:**
- Default: entropia cruzada binária (BCE)
- Desquilíbrio de classe > 10:1: Perda focal (gamma=2.0, alfa=0.25)
- Ruído de etiqueta: BCE com suavizamento de etiqueta (alfa=0,1)
- Probabilidades calibradas necessárias: BCE (calibradas naturalmente)

**Multi-class classification:**
- Default: entropia cruzada categórica (softmax + NLL)
- Previsões excessivamente confiantes: Adicionar suavizamento de rótulos (alfa=0,1)
- Desbalanço de classe extremo: perda focal por classe
- Destilação de conhecimento: divergência KL com alvos moles (temperatura=4-20)

**Representation learning / Embeddings:**
- Pairados de positivos e negativos: InfoNCE / NT-Xent (temperatura = 0,07)
- Triplota disponível: perda triplota (margem = 0,2-1,0) com mineração semi-dura
- Largo lote auto-supervisionado: contraste de estilo SimCLR (tão grande do lote >= 256)
- Pares de imagem de texto: contraste de estilo CLIP com a temperatura aprendida

**Common mistakes to flag:**
- MSE para classificação (planos gradientes perto de 0/1 devido à saturação sigmoide)
- Entropia cruzada sem suavização de rótulos em modelos de grande porte (leva a uma confiança excessiva)
- Perda contrastiva com pequeno tamanho de lote (menos resultados negativos, risco de colapso)
- Perda de triplet com mineração aleatória (computação de desperdícios em triples fáceis)
- Esquecer o clipping epsilon em cálculos de log (NaN de log(0)

Para cada recomendação, indicar:
- Nome e fórmula da função de perda
- Por que se encaixa nesta tarefa específica e dados
- Os hiperparâmetros-chave e os seus valores recomendados
- Que modo de falha evita
