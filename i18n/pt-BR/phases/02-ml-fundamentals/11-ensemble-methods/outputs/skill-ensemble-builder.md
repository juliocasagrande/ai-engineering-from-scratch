---
name: skill-ensemble-builder
description: Escolha o método de conjunto certo e configure-o para o seu problema
version: 1.0.0
phase: 2
lesson: 11
tags: [ensemble, bagging, boosting, random-forest, xgboost, stacking]
---

# Ensemble Guia de Seleção de Método

Os conjuntos combinam vários modelos para produzir melhores previsões do que qualquer modelo único.

## Lista de verificação das decisões

1. Qual é o principal problema do seu modelo atual?
   - Alta variação (overfitting): uso de sacos (Foresta aleatória)
   - Alta viés (subconjunto): aumento de utilização (Gradente de aumento, XGBoost)
   - Ambos, ou você quer precisão máxima: usar empilhamento

2. Quantos dados tens?
   - Sob 1.000 fileiras: Forte aleatória (robusto, difícil de configurar mal)
   - 1000 a 100.000: XGBoost ou LightGBM (melhor geral para tabuleiro)
   - Mais de 100.000: LightGBM (a maior velocidade de aumento de gradiente, lida bem com grandes dados)

3. Quanto tempo de sintonização pode investir?
   - Minimo: Floresta aleatória com defeitos (quase sempre funciona)
   - Moderado: XGBoost com taxa de aprendizagem=0,1, ajustar n_estimatores com parada precoce
   - Máximo: LightGBM ou XGBoost com busca de hiperparâmetros bayesianos

4. Precisas de interpretação?
   - Sim: árvore de decisão única ou pequena floresta aleatória com importância característica
   - Partial: aumento de gradiente com valores SHAP
   - Não: empilhadas ou conjuntos profundos

5. Os dados são barulhentos com muitos anormais?
   - Sim: Foresta aleatória (o atraso é robusto ao ruído)
   - Não: aumento do gradiente (pode aumentar a precisão com dados limpos)

## Quando utilizar cada método

**Random Forest (Bagging)**A primeira escolha é segura. Treina muitas árvores em amostras e médias de arranque. Reduz a variância sem aumentar o viés. É quase impossível sobrecarregar em dados moderados. É necessário ajustar o mínimo: definir n_estimators = 100-500 e deixar padrões.

**AdaBoost**A redução da taxa de variação de valores de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de valor de valor de um valor de um valor de

**Gradient Boosting**A solução de um novo árvore é a de cada árvore nova, que se encaixa nos resíduos do conjunto até agora. Reduz o viés. O método mais poderoso para dados tabuleiros. Requer sintonização: taxa de aprendizagem, n_estimatores, max_depth, min_child_weight, sub-sampling.

**XGBoost**A versão de texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de um texto de

**LightGBM**A taxa de crescimento de gradientes é mais rápida do que a de XGBoost em grandes conjuntos de dados.

**CatBoost**Não é necessário codificar um só-quente. bom quando você tem muitos recursos categóricos.

**Stacking**A meta-aprendizaje é treinado sobre as previsões de vários modelos base diversos. Utilize quando você precisa da melhor precisão absoluta e tem computação a sobra. Sempre gerar previsões de modelos base através de validação cruzada para evitar vazamentos.

**Voting**A maioria das pessoas que votam em forma mais simples, mas não necessariamente, podem votar com mais facilidade.

## Erros comuns

- Usando aumento de gradiente sem parar cedo (ele se encaixará se você deixar correr muitas rodadas)
- A definição de taxa de aprendizagem muito alta (acima de 0,3 geralmente causa instabilidade)
- Não ajustar a profundidade máxima para aumentar a gradiência (por defeito, árvores ilimitadas ou muito profundas super ajustadas)
- Estacionamento com modelos que são todos do mesmo tipo (diversidade é o ponto de estacionamento)
- Usando AdaBoost em dados ruidosos (outliers ganham cada vez mais peso a cada rodada)
- Esperar que a Foresta aleatória corrija a falta de encaixe (reduza a variância, não o viés)

## Prioridades de ajuste por método

**Random Forest:**
1. n_estimatores: 100-500 (mais raramente é pior, apenas mais lento)
2. Max_depth: Nenhum (deixe as árvores crescerem completamente) ou tampa de 10-20 para velocidade
3. Max_features: "sqrt" para classificação, "log2" ou n/3 para regressão

**XGBoost / LightGBM:**
1. Taxa de aprendizagem: 0,01-0,3 (menor é melhor se tiver computação para mais árvores)
2. n_estimators: use parar cedo em um conjunto de validação em vez de adivinhar
3. profundidade máxima: 3-8 (comece com 6)
4. min_child_weight / min_data_in_leaf: 1-20 (mais alto impede o sobreajuste)
5. Submuestra: 0,7-1,0
6. colsample_byte: 0,7-1,0
7. Reg_alpha (L1) e reg_lambda (L2): 0-10

## Referência rápida

| Method | Reduces | Speed | Tuning effort | Best for |
|--------|---------|-------|--------------|----------|
| Random Forest | Variance | Fast | Low | Noisy data, quick baseline |
| AdaBoost | Bias | Fast | Low | Simple base learners, clean data |
| Gradient Boosting | Bias | Medium | High | Tabular data, competitions |
| XGBoost | Both | Fast | High | Production tabular ML |
| LightGBM | Both | Fastest | High | Large datasets (50k+ rows) |
| CatBoost | Both | Medium | Medium | Many categorical features |
| Stacking | Both | Slow | High | Maximum accuracy, diverse models |
| Voting | Variance | Fast | None | Quick combination of 2-3 models |
