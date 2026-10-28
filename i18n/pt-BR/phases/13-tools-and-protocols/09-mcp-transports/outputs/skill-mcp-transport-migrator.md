---
name: mcp-transport-migrator
description: Migrá-lo para o contrato sem estatuto, apenas POST 2026-07-28.
version: 2.0.0
phase: 13
lesson: 09
tags: [mcp, streamable-http, stateless, migration, headers]
---

Dado um servidor HTTP ou HTTP+SSE Streamable baseado em sessão, produzir um livro de execução de migração para MCP `2026-07-28`- Não .

Produzir:

1. Mapa de endpoint. Defina um endpoint MCP moderno que aceita POST. Cada solicitação ou notificação JSON-RPC recebe um novo POST.
2. Mapa de resposta. `application/json` para uma resposta ou uma escala de pedido `text/event-stream` Para as notificações relacionadas seguidas da resposta final.
3. - Descontrolar o comportamento. `405` Para o GET e o DELETE modernos. `Mcp-Session-Id` e `Last-Event-ID`Não as coordenem, não as ecoem, não as revogam nem as reanimas.
4. Requer metadados. Requer versão de protocolo e recursos do cliente em cada corpo `_meta`, com a identidade recomendada do cliente.
5. - Requerendo validação de cabeçalho. `MCP-Protocol-Version`- Não . `Mcp-Method`, e condicional `Mcp-Name`Decodificar a sentinela Base64 e comparar os cabeçalhos com o corpo. `-32020` - Não coincide. `-32022` em uma versão de correspondência não suportada com chaves de dados exatas `supported` e `requested`- Não .
6. Migração de assinatura. Substitui GET independente, `resources/subscribe`, e `resources/unsubscribe` com POST `subscriptions/listen`Marcar o reconhecimento, cada notificação e o resultado final com `io.modelcontextprotocol/subscriptionId` igual ao ID da solicitação de escuta.
7. Migração de estado: substituir a afinidade da conexão por manuais de aplicação explícitos e opacos ligados ao principal autenticado.
8. Janela de compatibilidade. Mantenha os endpoints mais antigos separados e claramente rotulados. erros modernos POST devem ser inspecionados antes de qualquer retrocesso legado. Não redirecione POST com `301` ou `302` Porque o método e a preservação do corpo não são seguros.
9. Verificação. Teste de rejeição de origem, negociação de mídia POST, metadados do corpo, cabeçalhos espelhados, resposta JSON, notificação aceita `202` sem corpo, metadados de assinatura SSE abrangidos, GET e DELETE `405`, ignorou cabeçalhos removidos, e re-tentar com uma nova identificação.

Rejeitos duros:

- Presentar IDs de sessão, GET, DELETE ou replay como comportamento moderno.
- Compartilhamento de recursos por pedido através da memória de processo ou de conexão.
- Envio de solicitações JSON-RPC iniciadas pelo servidor.
- Reinicialização de um fluxo de SSE moderno com `Last-Event-ID`- Não .
- Voltar ao legado depois de um erro moderno reconhecido.
- Usando um redirecionamento para mover um POST JSON-RPC durante a migração.

Regras de recusa:

- Recusar a exposição pública sem autenticação, autorização e política exacta de origem.
- Recusar roteamento pegajoso oculto como substituição para o estado explícito de fluxo de trabalho.
- Recusar uma retestada automática de uma operação não idempotente sem um controlo da idempotência da aplicação.

Faça uma tabela de endpoint antes e depois, implementação em fases, limite de repassagem e lista de verificação de conformidade executável.
