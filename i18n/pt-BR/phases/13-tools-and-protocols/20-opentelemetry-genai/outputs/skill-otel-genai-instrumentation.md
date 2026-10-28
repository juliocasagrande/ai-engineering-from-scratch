---
name: otel-genai-instrumentation
description: Produce an instrumentation plan for an agent codebase to emit OTel GenAI spans end-to-end.
version: 1.0.0
phase: 13
lesson: 19
tags: [otel, observability, gen-ai, tracing]
---

Dado um código base de agente (chamadas de LLM, despacho de ferramentas, cliente MCP, sub-agentes), produzir um plano de instrumentação OTel GenAI.

Produzir:

1. Espanha hierarquia.`agent.invoke_agent`(INTERNAL) e crianças: `llm.chat`(CLIENTE), `tool.execute`(INTERNAL), `mcp.call`(CLIENTE), `subagent.invoke`- Não, não.
2. Atribuir lista de verificação por período. `gen_ai.operation.name`- Não .`gen_ai.provider.name`- Não .`gen_ai.request.model`- Não .`gen_ai.response.model`- Não .`gen_ai.usage.*`- Não .`gen_ai.tool.name`- Não .`gen_ai.agent.name`- Não .
3. Regra de propagação. Injectar W3C traceparent em cada chamada remota; para uso de MCP estúdio `_meta.traceparent`como um campo provisório.
4. Política de captura de conteúdo: desligado por padrão; documento que permite o envvar; nomear riscos de PII.
5. A escolha do exportador: Jaeger / Tempo / Langfuse / Phoenix / Datadog / Honeycomb; OTLP como o fio.

Rejeitos duros:
- Qualquer plano que não tenha rastro de propagação através dos limites do MCP ou do sub-agente.
- Qualquer plano com captura de conteúdo por padrão, vazamentos de informações e PII.
- Qualquer plano que emita atributos custom arbitrários sem o `gen_ai.`ou pré-fixo explícito do fornecedor.

Regras de recusa:
- Se a base de código utilizar um framework com auto-instrumentamento OTel incorporado (AI Pydantic, LangGraph, AgentOps), recomendamos primeiro o framework hook.
- Se o exportador tiver um backend local e a equipe não tiver suporte SRE, recomendamos um backend gerenciado.
- Se o utilizador solicitar capturar conteúdo para o debugging prod, recusar sem uma política de consentimento digitado e pipeline de redação de PII.

Output: um plano de uma página com hierarquia de espaço, lista de verificação de atributos por espaço, regra de propagação, política de captura de conteúdo e escolha do exportador.`gen_ai.client.operation.duration`)).
