---
name: llm-observability
description: Build a self-hosted LLM observability dashboard that ingests OpenTelemetry GenAI spans, runs evals, and catches injected regressions in under five minutes.
version: 1.0.0
phase: 19
lesson: 11
tags: [capstone, observability, otel, langfuse, phoenix, evals, drift, clickhouse]
---

Dado o tráfego de produção LLM em pelo menos seis famílias de SDK (OpenAI, Anthropic, Google GenAI, LangChain, LlamaIndex, vLLM), implantar um plano de observabilidade auto-hostado que ingere os espaços OTLP GenAI-semconv, executa avaliações, detecta deriva e alertas.

Construir um plano:

1. OpenTelemetry Collector com receptor HTTP OTLP, processador de amostragem de cauda (manter 100% de erros, 10% de sucesso, 100% de alta toxicidade/PII), exportadores para ClickHouse + S3.
2. ClickHouse span schema que reflete o genAI semconv: gen_ai.system, gen_ai.request.model, usage.input/output_tokens, latency_ms, user_id, app_id, mais JSON bag para instruções/completações.
3. Armazenar metadados de pós-gres para aplicativos, usuários, sessões, fila de anotações.
4. OpenLLMetry auto-instrumentamento em um aplicativo cliente por família de SDK; verificar o alcance canônico de terra.
5. DeepEval + RAGAS + Phoenix pacotes de avaliação programados sobre os vestígios de amostras; jurado LLM personalizado para PII e fora da política.
6. Detetor de deriva semanal PSI/KL em embutidos conjuntos de imediato; limiar de alerta 0,2.
7. Exportador Prometheus para agregados de pontuação de eval e percentil de latência; Alertmanager para Slack (alerta) + PagerDuty (crítico).
8. Next.js 15 App Router painel de controle: visão geral, rastreamento + cascata, tendências de avaliação, gráfico de deriva, alertas.
9. Probe de regressão: injetar um padrão de resposta que divulgue SSNs falsos 1% das vezes; medir MTTD (tempo desde a implantação até o alarme de incêndio).

Rubrico de avaliação:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | Trace-schema coverage | Number of SDK families producing canonical GenAI spans (target 6+) |
| 20 | Eval correctness | DeepEval / RAGAS scores vs hand-labeled set |
| 20 | Dashboard UX | MTTD on injected regression (target under 5 minutes) |
| 20 | Cost / scale | Sustained 1k spans/sec ingest without backlog |
| 15 | Alerting + drift detection | Prometheus/Alertmanager chain exercised end to end |

Rejeitos duros:

- Esquemas de span que inventam nomes de atributos não no OpenTelemetry GenAI semconv.
- Políticas de amostragem de cauda que deixam cair erros (um antipatrão bem conhecido).
- Evalos que funcionam a taxa de ingestão sem amostragem (costo inaceitável).
- Painéis de controlo que mostram "latencia" sem separação p50/p95/p99.

Regras de recusa:

- Recusar a persistência de pedidos ou conclusões sem uma política de redação de PII.
- Recusar-se a reivindicar "suporte multi-SDK" sem um teste de regressão de espaço canônico por SDK.
- Recusar a detecção de deriva de navio sem uma janela de linha de base; a deriva de tiro zero é inútil.

Saída: um repo contendo a configuração do coletor, o esquema ClickHouse, o painel Next.js 15, os trabalhos de eval, o detector de deriva, a cadeia de alerta, o conjunto de dados demo de 10k-trace com regressões anotadas e uma documentação de MTTD para a regressão de PII injetada, além das três melhorias de UX do painel que deixaram cair o MTTD sobre iteração.
