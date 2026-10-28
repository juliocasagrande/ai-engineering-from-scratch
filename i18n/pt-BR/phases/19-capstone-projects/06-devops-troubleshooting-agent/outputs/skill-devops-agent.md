---
name: devops-agent
description: Construir um agente de solução de problemas Kubernetes que percorra um gráfico de conhecimento de cluster, classifica as causas raizes e detecta todas as remédios através do Slack.
version: 1.0.0
phase: 19
lesson: 06
tags: [capstone, devops, sre, kubernetes, langgraph, fastmcp, aiops]
---

Dado um cluster K8s e uma fonte de alerta (PagerDuty ou Alertmanager), construa um agente que produz hipóteses de causa raiz classificadas em menos de cinco minutos e cancelou todas as remédios através de um cartão de aprovação Slack.

Construir um plano:

1. Ingerir dados de estado em Neo4j ou kuzu a cada 30 anos. Construir um gráfico de Pods, Deployments, Services, Nodes, PVCs, HPAs e bordas de sobreposição de telemetria para fontes Prometheus, Loki e Tempo.
2. Instale um receptor de webhook FastAPI para PagerDuty e Alertmanager.
3. Expor ferramentas de somente leitura através do FastMCP com transporte StreamableHTTP: kubectl get/describe, promql, logql, traceql.
4. Construir um agente de causa raiz de LangGraph com três nós: `sample` (Tiragem de 15m telemetria), `walk` (vizinhos de gráficos transversais), `hypothesize` (classificação dos candidatos por recência × especificidade × número de citações).
5. Postar as três hipóteses classificadas com visualização de gráfico-caminho para Slack com botões de aprovação.
6. Coloque ferramentas destrutivas (escalada, retrocesso, exclusão) em um servidor FastMCP separado atrás de um token de aprovação que o agente obtém apenas após a assinatura Slack.
7. Manter um registro de auditoria apenas apêndice: cada comando *considerado*, seja aprovado ou executado, quem aprovou.
8. Construir 20 cenários de incidentes sintéticos (OOMKill, flap DNS, HPA thrash, PVC preenchimento, vizinho barulhento, carro de lado defeituoso, ConfigMap mal implantação, rotação de cert, retorno de imagem-pulsão, falha da sonda, e 10 mais).

Rubrico de avaliação:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | RCA accuracy on scenario suite | At least 80% correct root cause across 20 synthetic incidents |
| 20 | Safety | Destructive-action guard never fires without Slack approval in the audit log |
| 20 | Time-to-hypothesis | p50 under 5 minutes from alert to Slack brief |
| 20 | Explainability | Every hypothesis has graph paths and telemetry citations |
| 15 | Integration completeness | PagerDuty, Slack, ArgoCD, Prometheus end-to-end working |

Rejeitos duros:

- Agentes com um único servidor MCP que mistura ferramentas destrutivas e somente letas.
- Qualquer RCA produzida sem citações telemétricas.
- Registros de auditoria que registam apenas execuções.
- As reivindicações de precisão sem executar o agente contra a suite de 20 cenários com sementes.

Regras de recusa:

- Recusar a reparação sem a aprovação do Slack de um humano em contacto, mesmo que a hipótese seja óbvia.
- Recusar-se a expor `kubectl exec`- Não . `kubectl port-forward`O sistema de controlo de dados é um sistema de controlo de dados, ou qualquer ferramenta interactiva através do MCP de leitura.
- Recusar-se a aplicar remédios em lote em várias implantações sem cartões de aprovação por implantação.

Resultado: um repo contendo o receptor FastAPI, o agente LangGraph, os servidores MCP só-leitor e destrutivos, a integração Slack, o conjunto de testes de 20 cenários, uma comparação lado a lado com o Agente AWS DevOps em três incidentes compartilhados e uma redação de comandos quase perdidos (o que o agente *considerou* mas não executou) durante uma janela de observação de uma semana.
