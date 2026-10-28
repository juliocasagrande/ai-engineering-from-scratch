---
name: skill-ml-design-review
description: Revisar um documento de projeto do sistema ML antes do início da formação, bloqueando primeiro as lacunas
version: 1.0.0
phase: 2
lesson: 19
tags: [ml-system-design, design-review, baselines, serving, rollout]
---

# Revisione do projeto ML

Use essa habilidade quando alguém compartilhar um documento de projeto, uma proposta ou um plano para um modelo que tomará decisões reais. Reveja o documento na ordem abaixo.

## Passo 1: Verifique os seis itens de bloqueio

Pare a revisão e peça uma correcção quando algum destes itens estiver faltando:

1. **Decision.** O documento nomeia a ação que usa cada previsão e quem ou o que a leva.
2. **Business metric.** O documento indica o resultado da empresa que a decisão deve mudar e como um experimento a mede.
3. **Strong baseline.** O documento compara o modelo com uma regra heurística ou com o sistema atual.
4. **No leakage.** O documento confirma que cada característica existe no momento da previsão.
5. **Rollout and rollback.** O plano tem um estágio de sombra ou canário e um retorno que leva minutos.
6. **Failure defaults.** Cada modo de falha tem uma ação padrão, como a regra heurística ou a última boa pontuação.

## Passo 2: Verifique o enquadramento do problema

- A previsão nomeia uma entidade, um alvo e um horizonte, como "o usuário cancela nos próximos 30 dias".
- O documento diz por que uma regra ou uma tabela de busca não são suficientes.
- O tipo de tarefa ML corresponde à decisão: classificação, regressão, classificação, previsão ou detecção de anomalias.

## Passo 3: Verifique as métricas

| Layer | Ask |
|---|---|
| Offline | Does the metric match the decision threshold? Use precision in the top 5 percent if the job acts on the top 5 percent. |
| Online | Which live signals show that the model works: acceptance rate, share of requests scored, score distribution? |
| Business | Which experiment measures the outcome, and how long until the result? |
| Guardrails | Which metrics must not get worse: cost, latency, complaints, unsubscribes? |

## Passo 4: Verificar os dados e as etiquetas

- De onde vêm os rótulos e quem é o dono daquela mesa
- O retardo da etiqueta em dias, e o que a equipa monitora até que as etiquetas cheguem
- Número de exemplos positivos
- Um conjunto de retenções baseado no tempo, com o período mais recente

## Passo 5: Verifique a escolha de porção com aritmética

Peça cinco números: entidades, solicitações por dia, pico QPS, máxima estabilidade em horas e orçamento de latência p99.

```text
batch runs per day   = 24 / (max_staleness_hours - batch_job_hours)
batch cost per day   = entities * runs per day * price per prediction + lookups * price per lookup
online replicas      = max(2, ceil(peak_qps / qps per replica))
online cost per day  = replicas * price per replica hour * 24
```

- O lote não pode funcionar quando o limite de atraso é menor do que um lote de trabalho.
- A Internet não pode funcionar quando a latência do modelo é acima do orçamento p99.
- Quando ambos funcionam, prefira o mais barato e verifique quantas partidas ninguém lê.
- Novas entidades sem história precisam de um caminho online ou uma regra.

## Passo 6: Verifique os circuitos de feedback

Pergunte como as decisões do modelo alteram os dados de formação futuros:

- Uma intervenção, como uma oferta ou um bloqueio, oculta o verdadeiro resultado?
- Só os itens que o modelo mostra recolhem feedback?
- Há um grupo aleatório ou uma partilha de exploração que mantém os dados limpos?
- O sistema registra a pontuação e a decisão em cada exemplo?

## Passo 7: Escreva a revisão

Use este formato:

```text
Verdict: ready for review | revise
Blocking: <list, or "none">
Missing: <list of non-blocking gaps>
Serving check: <batch $/day, online $/day, chosen mode, pass or fail>
Questions: <at most five questions for the author>
```

Para marcar uma versão JSON do documento, execute `python3 code/main.py path/to/design_doc.json` da pasta das lições.
