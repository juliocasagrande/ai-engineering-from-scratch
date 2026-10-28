---
name: observability-stack
description: Pick an LLM observability stack (development platform + gateway + optional scale layer) given stack, scale, budget, and license posture, and define the OpenTelemetry GenAI attribute set.
version: 1.0.0
phase: 17
lesson: 13
tags: [observability, langfuse, langsmith, phoenix, arize, helicone, opik, opentelemetry, genai-conventions]
---

Dada a pilha (LangChain / DSPy / SDK bruto), escala (traços / dia), orçamento, posição da licença (apenas MIT vs comercial OK), e auto-host requisito, produzir um plano de observabilidade.

Produzir:

1. A escolha de plataforma de desenvolvimento. Langfuse (OSS), LangSmith (LangChain-first commercial), Opik (Comet OSS), ou nenhum. Justificar com pilha e licença.
2. Opção de gateway/telemetria. Helicone (proxy + gateway), SigNoz (full APM), OpenLLMetry (puro OTel).
3. Scala/lago de camada: opcional: Arize AX ou Iceberg bruto para análise a longo prazo, Phoenix para deriva RAG.
4. Convenções OTel GenAI. Especifique o conjunto mínimo de atributos: `gen_ai.system`- Não .`gen_ai.request.model`- Não .`gen_ai.usage.input_tokens`- Não .`gen_ai.usage.output_tokens`- Não .`gen_ai.request.temperature`- Não .`gen_ai.response.finish_reasons`, mais org-específico (tenant_id, user_id, tarefa).
5. Política de amostragem. 100% de erros, 100% de alto custo (> 0,10$/ chamada), taxa de sucesso de amostragem N%.
6. Alerta. Cinco métricas que devem ter alertas: taxa de erro, P99 TTFT, custo/requisito, taxa de acidente de caché de pedido, taxa de recusa.

Rejeitos duros:
- Instrumentar dentro do SDK específico de framework sem um OTel fallback. Recusar o bloqueio de framework.
- Manter 100% dos vestígios a preços da classe Datadog > 500$/m por mês para uma carga de trabalho não regulamentada.
- Ignorar as convenções da OpenTelemetry GenAI.

Regras de recusa:
- Se os dados/dia forem > 5M e a equipa insistir na retenção completa do Datadog, recusar sem previsão de custos.
- Se a equipe é apenas MIT e escolhe LangSmith, rejeite  Langfuse é o equivalente MIT.
- Se a equipe não tiver gateway de IA e escolher Helicone como gateway E observabilidade, aceitar  o duplo proxy como gateway até ~ 500 RPS (Fase 17 · 19 cobre escala de gateway).

Resultado: um plano de uma página que nomeia plataforma de desenvolvimento, gateway, camada de escala (se houver), conjunto de atributos OTel, regra de amostragem, cinco alertas.
