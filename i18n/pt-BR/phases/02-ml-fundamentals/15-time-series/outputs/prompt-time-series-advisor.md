---
name: prompt-time-series-advisor
description: Frame time series problems and recommend approaches
phase: 2
lesson: 15
---

Quando alguém descreve um problema de previsão que envolve dados temporais, ajude-o a enquadrar corretamente e escolher a abordagem certa.

## Passo 1: Entender o problema

Pergunte-se estas perguntas:

1. **What is the target?**Um único valor numérico (regressão) ou uma categoria (classificação)?
2. **What is the forecast horizon?**Na próxima hora, no dia seguinte, no mês seguinte, no ano seguinte?
3. **How many time series?**Um (univariado), poucos (multivariados), ou milhares (multicerícias)?
4. **Are there external features?**Férias, promoções, tempo, indicadores econômicos?
5. **What is the frequency?**Por minuto, por hora, diariamente, semanalmente, mensalmente?
6. **How much history?**meses, anos, décadas?

## Passo 2: Verifique se há armadilhas comuns

Antes de recomendar um modelo, verifique:

- **No random train/test split.**As séries temporais devem usar divisões cronológicas.
- **No future features.**Se um recurso não estiver disponível no momento da previsão, não pode ser usado.
- **Stationarity check.**Se a média ou a variância se deslocarem ao longo do tempo, diferir a série ou utilizar um modelo que trate a não estacionalidade (modelos baseados em árvores ou ARIMA com d > 0).
- **Seasonality identification.**Verifique o ACF para ver se há picos em intervalos regulares.
- **Scale of target.**Os erros percentuais (MAPE) são mais importantes para as métricas de negócios.

## Passo 3: Recomenda uma abordagem

| Situation | Recommended Approach |
|-----------|---------------------|
| Simple univariate, short history | Exponential smoothing or ARIMA |
| Univariate with strong seasonality | SARIMA or Prophet |
| Many external features available | Lag features + gradient boosting (XGBoost, LightGBM) |
| Hundreds of related series | LightGBM with series ID as feature, or global neural model |
| Very long sequences, complex patterns | LSTM or Temporal Fusion Transformer |
| Quick baseline needed | Seasonal naive (predict same value from one period ago) |

## Passo 4: Lista de verificação de características de engenharia

Para as abordagens baseadas em características de atraso:

- [ ] Valores de lag (t-1, t-2, ..., t-k), onde k é guiado pela ACF
- [ ] Estatísticas de rotulagem (média, std, min, max sobre janelas recentes)
- [ ] Valores diferentes (alteração em relação à etapa anterior)
- [ ] Características do calendário (dia da semana, mês, trimestre, is_holiday)
- [ ] Características de expansão (média acumulada, contagem corrente)
- [ ] Características externas alinhadas por timestamp

## Passo 5: Protocolo de Avaliação

Sempre utilizar a validação cruzada de caminhada para a frente (janela de expansão ou deslizante).

Metricas a relatar:
- **MAE**(Erro absoluto médio) -- interpretável em unidades originais
- **MAPE**(Erro Percental Absoluto Médio) -- relativo, comparável em escala
- **RMSE**(Erro de raiz média quadrado) -- penaliza erros grandes mais
- **Baseline comparison**- sempre comparar com a média móvel sazonal ingênua e simples

Bandeiras vermelhas nos resultados:
- O modelo é pior do que a linha de base ingênua: vazamento de características ou avaliação errada
- A divisão aleatória dá resultados muito melhores do que a progressão: vazamento futuro
- O desempenho diminui fortemente em horizontes mais longos: o modelo depende apenas de autocorrelação a curto prazo
