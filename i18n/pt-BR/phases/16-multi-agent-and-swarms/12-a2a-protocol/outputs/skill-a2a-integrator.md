---
name: a2a-integrator
description: Design an A2A integration between two agents — Agent Card, task schemas, auth, streaming or polling.
version: 1.0.0
phase: 16
lesson: 12
tags: [multi-agent, a2a, protocol, interoperability, google]
---

Dados dois sistemas de agentes que precisam interoperar, produzir o plano de integração A2A: conteúdo do Cartão de Agente, esquemas de tarefas, auth, modo de transporte.

Produzir:

1. **Agent Card.**Nome, descrição, versão, competências (cada um com `id`- Não .`name`- Não .`description`- Não .`tags`), `supportedInterfaces`(cada um com `url`- Não .`protocolBinding`- Não .`protocolVersion`), `defaultInputModes`E ...`defaultOutputModes`como tipos de mídia (texto, JSON estruturado, imagem, áudio, vídeo), e a declaração de autor em `securitySchemes`- E mais .`securityRequirements`- Não .
2. **Task schemas per skill.**Introduza esquema JSON + esquema JSON de artefatos.
3. **Auth choice.**Tokens portadores (OAuth2 ou opaco), mTLS ou API, cada uma declarada como `securitySchemes`Introdução: Justificar dado o modelo de ameaça (internet público, VPC, mixto).
4. **Transport mode.**Pesquisas (`GetTask`) vs. streaming SSE (`SendStreamingMessage`- Não .`SubscribeToTask`) vs. notificações push (`CreateTaskPushNotificationConfig`O programa de pesquisa é um programa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa de pesquisa.
5. **Rate limits.**Limite por cliente e por tarefa.
6. **Idempotency.**Estratégia para duplicados `POST /message:send`pedidos (cliente estável `messageId`, deduplicação do lado do servidor).
7. **Failure handling.**Os estados de tarefa além `TASK_STATE_FAILED`(retraivel versus fatal), política de letra morta, esquema de artefacto de erro.
8. **MCP vs A2A split.**Se o agente remoto utilizar o MCP internamente, note quais as ferramentas são expostas versus mantidas internamente.

Rejeitos duros:

- O agente Cardes , cujo`supportedInterfaces`As entradas não declaram um `protocolVersion`- Não .
- Esquemas de tarefas que são texto em forma livre quando o caso de uso justifica a estrutura.
- Em vão .`securityRequirements`sobre as implementações da Internet pública.

Regras de recusa:

- Se ambos os agentes executarem no mesmo processo, recusar A2A e recomendar chamadas diretas Python/JS. A2A é para limites transversos do sistema.
- Se os requisitos de latência forem inferiores a 100 ms, recuse-se a A2A e recomenda RPC direta com um esquema compartilhado.
- Se o agente remoto não declarar um cartão de agente, recusar a integração e recomendar a publicação de um primeiro.

Resultado: um resumo de integração de uma página. Fechar com o cartão de agente JSON colados em linha para que a engenharia possa deixá-lo cair em `/.well-known/agent-card.json`- Não .
