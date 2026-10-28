---
name: mcp-server-designer
description: Projetar um servidor MCP 2026-07-28 sem estado com contratos explícitos de descoberta, estado, transporte e segurança.
version: 2.0.0
phase: 11
lesson: 14
tags: [llm-engineering, mcp, stateless, tool-use]
---

Dado um domínio (API interna, banco de dados, fonte de arquivo) e os hosts que montarão o servidor, saída:

1. Mapa primitivo. `tools` (acção), que se tornam `resources` (dados apenas para leitura), que se tornam `prompts` Uma linha por primitiva.
2. Contrato de descoberta. `server/discover` com as versões exatas que a implementação suporta, as capacidades, a identidade do servidor, as instruções, `ttlMs`, e `cacheScope`- Não .
3. Requer uma versão de protocolo de cadeia e recursos do cliente objeto em `params._meta` Recomendação de identidade do cliente.`-32602`) para os metadados necessários, que faltam ou não tenham um tipo adequado. `UnsupportedProtocolVersionError` (`-32022`) com `data.supported` e `data.requested` apenas para uma cadeia de versão fornecida que o servidor não implementa.
4. Contrato de resultado. `resultType`, metadados de identidade do servidor, ordem determinista de listas e política de cache para cada resultado aplicável.
5. Plano MRTR. `input_required` apenas para `tools/call`- Não . `resources/read`, ou `prompts/get`Incluir pelo menos um dos `inputRequests` ou opaco `requestState`; reter o método original com um novo ID JSON-RPC, respostas de entrada correspondentes quando solicitadas e o valor de estado exato quando presente.
6. Plano de estado. Para cada fluxo de trabalho de várias chamadas, defina um manilho opaco de servidor, passado como um argumento de ferramenta comum. Não esconda o estado por trás de uma sessão de conexão ou protocolo.
7. Transportes e planos de auth. Escolha estúdio ou o endpoint 2026-07-28 Streamable HTTP POST. Para HTTP, define validação de origem e autorização por solicitação. Requer `MCP-Protocol-Version` em pedidos de POST, `Mcp-Method` sobre os pedidos JSON-RPC, e `Mcp-Name` apenas para `tools/call`- Não . `resources/read`, e `prompts/get`. Uma notificação POST aceita retorna HTTP 202 sem corpo.
8. Esboço de esquema. Escreva JSON Schema para cada parâmetro da ferramenta, com descrições sintonizadas para seleção de modelo e limites explícitos para entrada não confiável.
9. Lista de ações destrutivas. `destructiveHint: true` E exigem aprovação humana.
10. Plano de verificação. Cobrir notificações que não produzem resposta JSON-RPC, envelopes malformados e IDs de solicitação, rejeição de metadados, descoberta, listas deterministas, não correspondência de versões, campos de cache, não correspondência de cabeçalho a corpo, autorização, aprovação e um caso de injeção de prompt.

Rejeitar um projeto que usa `initialize`- Não . `notifications/initialized`- Não . `Mcp-Session-Id`, GET HTTP autônomo, DELETE HTTP, ou `Last-Event-ID` Permitir esses mecanismos apenas dentro de um adaptador claramente isolado para versões de protocolo até 2025-11-25. Não adicione Roots, Sampling ou Logging depreciados a uma nova implementação; o suporte de compatibilidade deve ser rotulado e Roots ou Sampling input deve usar MRTR. Recusar um servidor que escreve para disco ou chama uma API externa sem autorização, validação e um caminho de aprovação.
