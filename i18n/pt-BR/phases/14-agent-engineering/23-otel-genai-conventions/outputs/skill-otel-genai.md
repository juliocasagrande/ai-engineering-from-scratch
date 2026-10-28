---
name: otel-genai
description: Instrument an agent with OpenTelemetry GenAI semantic conventions — invoke_agent, chat, tool_call spans with correct attributes and opt-in content capture.
version: 1.0.0
phase: 14
lesson: 23
tags: [opentelemetry, genai, observability, tracing, semantic-conventions]
---

Dado o tempo de execução de um agente, o OTel GenAI convida convenções semânticas.

Produzir:

1. `invoke_agent`Tipo de cliente para serviços de agente remoto, interno para processo. Nome: `invoke_agent {gen_ai.agent.name}`- Não .
2. `chat`Espéndulo por chamada de LLM com `gen_ai.operation.name=chat`- Não .`gen_ai.provider.name`- Não .`gen_ai.request.model`- Não .`gen_ai.response.model`- Não .
3. `tool_call`span por invocação de ferramenta com `gen_ai.tool.name`e, se aplicável, `gen_ai.data_source.id`(registro de memória do corpus RAG).
4. Captura de conteúdo de opção: desligado por padrão; quando ligado, armazenar entradas/salidas externamente e registar `*.reference_id`- Em espansões.
5. Propagação de contexto: utilizar cabeçalhos de contexto de rastreamento W3C para que executos de múltiplos processos (subprocesso de SDK CLI de Claude Agent) se juntem em uma única rastreamento.

Rejeitos duros:

- Captura de todas as instruções/sais em linha por padrão. PII e risco de vazamento secreto; também viola a especificação.
- Desaparecido .`gen_ai.provider.name`Os painéis de multi-provedor quebraram-se.
- Sempre definir a relação pai-filho através de contexto ativo.

Regras de recusa:

- Se o tempo de execução não puder propagar o contexto através dos limites do processo, recuse.
- Se o produto tiver restrições regulamentares (HIPAA, GDPR), recuse a captura de conteúdo em linha.
- Se o backend não for configurado `OTEL_SEMCONV_STABILITY_OPT_IN=gen_ai_latest_experimental`, aviso: os nomes dos atributos podem mudar no upgrade do colector.

Output: `tracer.py`- Não .`attributes.py`- Não .`content_store.py`- Não .`README.md`Explicando a estrutura de espaço, a opção de estabilidade e a política de captura de conteúdo.
