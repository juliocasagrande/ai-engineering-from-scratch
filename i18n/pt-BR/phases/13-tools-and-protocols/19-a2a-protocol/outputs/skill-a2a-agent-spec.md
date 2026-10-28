---
name: a2a-agent-spec
description: Produzi o cartão de agente e o esquema de habilidades para um agente que deve ser chamado através da A2A.
version: 1.0.0
phase: 13
lesson: 18
tags: [a2a, agent-card, task-lifecycle, delegation]
---

Dadas as capacidades de um agente e os colaboradores pretendidos, produzir o seu cartão de agente A2A e definições de habilidades.

Produzir:

1. Agente Card. `name`- Não . `description`- Não . `version`- Não . `supportedInterfaces[]` (cada um com `url`- Não . `protocolBinding`- Não . `protocolVersion`), `capabilities` (streaming, pushNotifications), `defaultInputModes`- Não . `defaultOutputModes`- Não . `securitySchemes` e `securityRequirements`- Não . `skills[]`- Servir-lhe no `/.well-known/agent-card.json`- Não .
2. Lista de habilidades. `id`- Não . `name`- Não . `description`- Não . `tags`, e opcionais `inputModes` - Não . `outputModes` Tipo de mídia. Use o padrão "Use when X. Do not use for Y". nas descrições.
3. Para cada habilidade, as transições esperadas para o estado e as `TASK_STATE_INPUT_REQUIRED` Os caminhos.
4. Se assinar o cartão com entradas JWS `signatures` (recomendado para agentes de ligação externa).
5. Protocolo vinculativo. `JSONRPC`- Não . `GRPC`, ou `HTTP+JSON`, cada um declarado como um `supportedInterfaces` entrada com `protocolVersion` `1.0`Os clientes enviam `A2A-Version: 1.0`Nota: compatível com a versão 1.0.

Rejeitos duros:
- Qualquer cartão de agente sem um estábulo `supportedInterfaces` URL, quebra a descoberta.
- Qualquer habilidade sem `tags` Os chamadores não podem raciocinar sobre a compatibilidade.
- Qualquer agente de ligação externa sem um plano de assinatura de cartão.

Regras de recusa:
- Se o caso de utilização do agente for uma única chamada de ferramenta, recusar a construção do andaime A2A; recomendar MCP.
- Se o agente expõe os elementos internos não deve (traços de chamada de ferramenta, cadeia de pensamento), rejeitar e exigir opacidade.
- Se o agente precisar de A2A para os pagamentos (caso de utilização de AP2), confirme a versão de extensão de AP2 e sinalize que o AP2 é separado do núcleo de A2A.

Resultado: um JSON de uma página do Cartão do Agente, um esquema de habilidades para cada operação, plano de transição de estado, opções de assinatura e transporte.
