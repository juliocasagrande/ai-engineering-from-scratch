---
name: skill-classification-diagnostics
description: Dada uma matriz de confusão e nomes de classes, superficial por classe falhas e propor a única solução mais impactante
version: 1.0.0
phase: 4
lesson: 4
tags: [computer-vision, classification, evaluation, debugging]
---

# Classificação de diagnóstico

Uma lente de leitura para matrizes de confusão. A precisão agregada diz-lhe que um classificador funciona. A matriz de confusão diz-lhe *o que ainda não sabe*.

## Quando utilizar

- Primeiro, veja o desempenho de validação de um classificador treinado.
- Entre treinamentos para decidir o que mudar a seguir.
- Antes de enviar um modelo: verificar se nenhuma classe crítica está a falhar silenciosamente.
- Descargar uma regressão de produção onde a precisão geral caiu um ponto e você precisa saber porquê.

## Input

- `cm`: Matriz de confusão CxC (roas = verdade, cols = previsão).
- `labels`: lista de nomes da classe C, na mesma ordem.
- Opcional `class_priors`: frequência de formação por classe (defactos com as somas de linhas de `cm`)).

## Passo

1. **Compute per-class metrics.** Trate qualquer divisão por zero como a métrica sendo indefinida para essa classe, e relata-o como `n/a`; nunca substituir silenciosamente por 0.
   - precisão_i = cm[i,i] / soma(cm[:, i]) (indefinido quando a classe nunca foi prevista)
   - recall_i = cm[i,i] / sum(cm[i, :]) (indefinido quando a classe não possui amostras de verdade de base)
   - f1_i = 2 * p * r / (p + r) (indefinido quando qualquer componente não é definido)

2. **Rank up to three worst classes** Se a matriz de confusão tiver menos de três classes, classifique por mais que existam. Excluir classes com todas as métricas indefinidas.

3. **Find the top off-diagonal cell per row**  a classe que mais comumente rouba desta classe. `true -> predicted`- Não .

4. **Classify the failure mode** Para cada classe pior, use estes limites quantitativos para que o rótulo seja reprodutivo:
   - `ambiguity`  confusão bidireccional com outra classe: ambas `cm[i,j] / sum(cm[i, :]) >= 0.15` e `cm[j,i] / sum(cm[j, :]) >= 0.15`- Não .
   - `imbalance`  a classe tem `< 0.5x` O número de treinos do seu confusor superior.
   - `label_noise`  `|precision_i - recall_i| >= 0.2` e a classe não está nos caminhos de desequilíbrio / ambigüidade.
   - `systematic`  nenhum confusor excede 0,2 porção dos erros desta classe; os erros se espalham por três ou mais outras classes.

5. **Recommend the single most impactful next action**- Não .
   - `ambiguity` -> recolher ou sintetizar exemplos discriminatórios, adicionar um aumento direcionado que preserve a característica distintiva.
   - `imbalance` -> exagere a classe minoritária ou aplique a perda ponderada por classe.
   - `label_noise` -> auditoria de uma amostra estratificada da classe; correcção de rotulagens erradas antes de qualquer outra alteração.
   - `systematic` -> aumentar os dados para a classe ou ajustar com maior peso sobre a perda desta classe.

## Relatório

```
[diagnostics]
  aggregate accuracy: X.XX
  macro F1:           X.XX

[top-3 worst classes]
  1. class <name>  F1 = X.XX  prec = X.XX  rec = X.XX
     top confusion: <name> -> <other>  (N cases)
     failure mode:  ambiguity | imbalance | label_noise | systematic
     action:        <one sentence>

  2. ...
  3. ...

[recommendation]
  single biggest lever: <one sentence naming the class and the fix>
```

## Regras

- Voltem no máximo três classes, mas mais escondem o sinal.
- Nome o confuso dominante para cada classe pior; nunca resuma como "confundiu com muitos".
- Não há genérico "agrega mais dados" sem especificar qual classe.
- Quando a precisão e a retirada discordam em mais de 0,2 pontos, sempre sinalize o ruído como candidato  as classes reais geralmente alinham P e R após o treinamento.
