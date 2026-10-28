---
name: mcp-request-tracer
description: O MCP de auditoria transcreve mensagem por mensagem em épocas modernas de protocolo legado sem estado e explícito.
version: 2.0.0
phase: 13
lesson: 06
tags: [mcp, json-rpc, stateless, metadata, compatibility]
---

Dado uma sequência de envelopes JSON-RPC de MCP, auditem cada mensagem de forma independente contra o MCP `2026-07-28`Detectar tráfego antigo, mas nunca assumir que exista um aperto de mão ou sessão de protocolo.

Produzir:

1. Anotado de mensagem: direção de estado, tipo JSON-RPC, método, primitivo, ID de solicitação e era detectada.
2. Verificação de metadados modernos. `params._meta.io.modelcontextprotocol/protocolVersion` e `params._meta.io.modelcontextprotocol/clientCapabilities`Registrar se é recomendado `clientInfo` Está presente.
3. Verificar todos os sucessos modernos `resultType: "complete"` ou outro tipo de resultado especificado, mais a identidade recomendada do servidor no resultado `_meta`- Não .
4. Verificação de descoberta e versão. Verificar servidores modernos implementar `server/discover`Interpreta . `-32022` como evidência e verificação modernas `data.requested` Mais `data.supported`- Não .
5. Verificação de cache. `server/discover`, métodos de listagem, e `resources/read`, exigir `ttlMs` e `cacheScope`- Ordem de lista não determinista.
6. Verificação de direção. Rejeitar solicitações JSON-RPC iniciadas pelo servidor no tráfego moderno. Permitir notificações relacionadas a solicitações e abertas pelo cliente `subscriptions/listen` - Os rios.
7. Verificação de compatibilidade. `initialize` e `notifications/initialized` Não é necessário em trânsito moderno.

Rejeitos duros:

- Tratar um processo de estúdio, conexão HTTP, ou `Mcp-Session-Id` como o protocolo moderno.
- Inferir as capacidades do cliente a partir de uma solicitação anterior.
- Regressando ao legado após um erro moderno reconhecido como `-32020`- Não . `-32021`, ou `-32022`- Não .
- Aceitar um sucesso moderno sem `resultType`- Não .

Regras de recusa:

- Se a transcrição não for JSON-RPC 2.0, pare e identifique o envelope incompatível.
- Se for pedido que reescreva silenciosamente as provas, recuse, preserve a transcrição original e produza um exemplo corrigido separado.

Exitamento de uma linha por mensagem na ordem de chegada:

```text
[request/modern/tools] id=7 tools/list metadata=valid
```

Terminar com o conteúdo de mensagens modernas, antigas, inválidas e ambíguas, seguidas pela primeira ação corretória.
