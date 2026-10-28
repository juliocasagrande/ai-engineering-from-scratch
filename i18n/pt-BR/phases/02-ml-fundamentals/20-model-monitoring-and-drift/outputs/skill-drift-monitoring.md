---
name: skill-drift-monitoring
description: Planejar monitores de deriva para um modelo implantado e triagem de alerta de deriva
version: 1.0.0
phase: 2
lesson: 20
tags: [monitoring, drift, psi, kolmogorov-smirnov, chi-square, alerting]
---

# Monitoramento da deriva

Use esta habilidade em duas situações: Use a Parte A quando um modelo está prestes a ser lançado e precisa de monitores. Use a Parte B quando um alerta de deriva dispara.

## Parte A: Planejar os monitores

### Passo 1: Lista dos sinais por camada

| Layer | Minimum signals |
|---|---|
| System health | p99 latency, error rate, requests per minute |
| Inputs | One drift test per important feature, missing-value rate, new categories |
| Predictions | Score distribution (PSI on score deciles), positive-prediction rate |
| Outcomes | The offline metric from the design, computed on labeled events only |

### Passo 2: Escolha o teste para cada entrada

- Características numéricas: PSI em deciles de referência, mais estatística KS `D`
- Características categorias: teste de chi-quadrado numa tabela de duas fileiras, mais V de Cramér
- Características com cinco ou menos valores distintos: trate-as como categorias

### Passo 3: Configure as janelas

- Referência: os dados da formação ou um período de produção verificado por alguém
- Atual: uma janela grande o suficiente para que as janelas limpas permaneçam abaixo do nível de alerta.
- Recursa um ciclo semanal completo na referência quando o tráfego muda em relação ao dia da semana

### Passo 4: Configurar a política de alerta

Escreva estes números antes do lançamento:

```text
family alpha          = 0.01
per-test alpha        = family alpha / number of tests
PSI warn / drift      = 0.10 / 0.25
KS D for drift        = 0.10 together with p < per-test alpha
Cramér's V for drift  = 0.10 together with p < per-test alpha
persistence           = 2 consecutive drift windows before an alert
outcome alert         = metric below reference metric - tolerance, for 2 windows
```

Enviar alertas para um painel de instrumentos.

### Passo 5: Registrar o atraso da etiqueta

Indique quanto tempo demoram os rótulos para chegarem e o que a equipe observa até que eles o façam. Se o atraso for maior que uma semana, adicione uma estimativa de desempenho que use probabilidades calibradas.

## Parte B: Triagem de um alerta

### Passo 1: Excluir um defeito de oleoduto

Verifique estes primeiro, porque parecem deslocar-se:

- Uma mudança de esquema, uma coluna renomeada ou uma mudança de unidade
- Um aumento dos valores faltantes ou de um valor padrão
- Uma nova categoria que vem de uma mudança de código, não de usuários
- Uma junção quebrada que preenche características com nulos

### Passo 2: Nomear o tipo de deriva

| Evidence | Likely drift | Action |
|---|---|---|
| Inputs moved, outcome metric stable | Covariate drift | Keep watching. Retrain only if traffic moved into regions with little data. |
| Positive rate moved, inputs per class look the same | Prior drift | Recalibrate scores or move the decision threshold |
| Inputs stable, outcome metric dropped | Concept drift | Collect new labels, then retrain on recent labeled data |
| Inputs moved and outcome metric dropped | Covariate drift with damage, or both kinds | Retrain on recent labeled data and check the new model on the newest period |

### Passo 3: Verifique o tamanho do efeito

Um pequeno p-valor com uma janela grande diz pouco. `D`, ou V de Cramér, e a mudança na métrica de resultado.

### Passo 4: Escreva a nota de triagem

```text
Alert: <signal, window end, value, threshold>
Pipeline check: <defect found or none>
Drift kind: covariate | prior | concept | unclear
Impact: <outcome metric change, or "labels pending until <date>">
Action: wait | recalibrate | collect labels | retrain | roll back
Owner and review date: <name, date>
```

Após qualquer reestruturação, restabeleça a janela de referência para os novos dados de formação.
