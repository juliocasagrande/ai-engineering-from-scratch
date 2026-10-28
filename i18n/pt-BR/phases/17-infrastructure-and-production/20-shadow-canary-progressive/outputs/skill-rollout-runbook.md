---
name: rollout-runbook
description: Design a shadow → canary → A/B → 100% rollout plan for a new LLM model or prompt template, with five canary gates, noise-floor-aware thresholds, and a seconds-fast rollback path.
version: 1.0.0
phase: 17
lesson: 20
tags: [rollout, canary, shadow, progressive-delivery, feature-flags, argo-rollouts, flagger, kserve]
---

Dada uma mudança de candidato (novo modelo, novo modelo de resposta, nova política de roteador), métricas de produção de base e tolerância ao risco, produzem um runbook de implantação.

Produzir:

1. Plano de sombra. Duração (24-72 horas). Métricas registradas: saídas, contagem de tokens, latência, recusa, erro. Alerta sobre: >20% mudança de custo, >30% mudança de comprimento de saída, qualquer violação de esquema.
2. Progressão canária. Etapas (1% → 10% → 25% → 50% → 75% → 100%). Duração por etapa (30m-24h com base no volume de tráfego; certifique-se de que cada etapa tenha dados suficientes para a confiança estatística).
3. 5 portas. Especifique os limites exatos para a latência P99, custo/requisito, erro/recusão, comprimento de saída P99, taxa de ponta baixa.
4. Nomear o controlador de implantação (Argo Rollouts, Flagger, KServe) e o sistema de bandeira de recurso para o retrocesso instantâneo.
5. Percurso de volta. Documentar as três ações: desviar a bandeira → reverter digestado → verificar. Tempo de meta: menos de 60 segundos de ponta a ponta.
6. Salta A/B? Justificar. Mudanças de variantes melhoradas salta A/B; mudanças claramente diferentes (novo comportamento, nova curva de custo) exigem A/B.

Rejeitos duros:
- Salto do modo sombra. Rejeitar picos de custo e regressões de comprimento passar de avaliação offline.
- Os portões mais apertados do que 15% de variação.
- Rejeitar não é um rollback, é um relatório de danos.

Regras de recusa:
- Se a alteração for crítica à segurança (por exemplo, alteração no tratamento de PII), exigir uma porta adicional explícita: zero vazamento de PII na amostra de sombra antes do início do canário.
- Se o volume de tráfego for < 100 req/hora, é necessário alargar os estágios canários  caso contrário, o ruído da porta abrange o sinal.
- Se a equipa não puder fornecer métricas de base para os cinco portões canários, recusar a implantação  a linha de base é um pré-requisito.

Output: um livro de uma página com sombra, canário, portas, ferramentas, rollback, postura A/B. Terceiro com um requisito de perfuração rollback: ensaio de rollback uma vez antes da primeira implantação real.
