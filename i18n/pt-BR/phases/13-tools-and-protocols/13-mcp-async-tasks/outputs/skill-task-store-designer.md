---
name: task-store-designer
description: Design durable MCP work with the current Tasks extension, stateless requests, explicit ownership, polling, input updates, and cancellation.
version: 2.0.0
phase: 13
lesson: 13
tags: [mcp, tasks, extension, durable-state, stateless]
---

Projeto de trabalho de longo prazo de MCP contra o `io.modelcontextprotocol/tasks`- A extensão.

Produzir:

1. Decidir sobre a elegibilidade. Explicar por que a operação necessita de uma tarefa em vez de uma sincronização `tools/call`- Não .
2. Contrato de capacidade.`supportedVersions`, capacidades,`ttlMs`, e `cacheScope`em `server/discover`, mais a extensão tarefas nas capacidades do cliente por pedido.`tools/list`Descrição com um objeto válido `inputSchema`, metadados de identidade do servidor e sugestões de cache.`-32021`com um `requiredCapabilities`objecto quando a extensão estiver ausente, e `-32022`com exato`supported`E ...`requested`dados para uma versão não suportada.
3. A transacção de criação.`tasks/get`Pode resolvê-lo, e depois voltar dirigido ao servidor `resultType: "task"`- Não .
4. Forma do estado. Incluir `taskId`- Não .`status`- Não .`statusMessage`, marcas de tempo ISO, `ttlMs`- Não .`pollIntervalMs`, proprietário autorizado, referência de operação original, resultado ou erro, solicitações de entrada pendentes e todas as chaves de entrada emitidas.`CallToolResult`- O que é que é ?`resultType: "complete"`e DEVE incluir os seus próprios`io.modelcontextprotocol/serverInfo`Metadados.
5. Métodos atuais.`tasks/get`- Não .`tasks/update`, e `tasks/cancel`. Para Streamable HTTP, cada pedido é definido `Mcp-Name`- Não .`params.taskId`Não introduzir .`tasks/status`- Não .`tasks/result`, ou `tasks/list`- Não .
6. Continuidade da entrada.`tasks/get`- E mais .`tasks/update`Requer chaves de entrada únicas durante toda a vida e manuseio de resposta parcial.
7. Plano de durabilidade. Escolha armazenamento do sistema de arquivos atômico, um banco de dados transacional ou uma fila compartilhada e armazenamento. Incluir o arrendamento de trabalhadores e reiniciar o comportamento.
8. Política de propriedade. Autorize cada método de tarefa e assinatura por inquilino e principal. Nunca trate o conhecimento da identificação de tarefa como permissão.
9. O contrato de cancelamento indica que o reconhecimento é cooperativo e não pode levar a`cancelled`- Não .
10. Opção de notificação.`subscriptions/listen`em um fluxo de resposta POST SSE e `notifications/tasks`O relatório de avaliação da Comissão sobre a política de informação e de informação`io.modelcontextprotocol/subscriptionId`, igual ao id da solicitação de escuta, no reconhecimento e em cada notificação de tarefa. Uma notificação sem id não recebe resposta JSON-RPC; uma notificação HTTP aceita recebe `202`Sem corpo.
11. Política de expiração.`ttlMs`de criação, definir o comportamento de purga, e evitar vazamentos se a tarefa de outro inquilino existe.
12. Mapa de migração. Substitua as bandeiras de tarefas solicitadas pelo cliente e os métodos experimentais removidos com o fluxo de extensão atual.

Rejeitos duros:

- Retorno de um maná de tarefa antes de uma visão duradoura de leitura.
- Voltar .`resultType: "task"`a um pedido que não anunciou a prorrogação.
- Usando`params._meta.task.required`- Não .`tasks/status`- Não .`tasks/result`, ou `tasks/list`como a API atual.
- Usando`initialize`- Não .`Mcp-Session-Id`, rotas pegajosas, ou estado oculto de sessão de transporte como o armazém de tarefas.
- Tratamento`tasks/cancel`O reconhecimento como prova de que o trabalhador parou.
- Reutilização de um `inputRequests`chave durante a vida de uma tarefa.
- Returnar uma tarefa a um telefonista que não seja o seu titular autorizado.
- Implementação da notificação através de GET autónomo, sessão SSE ou `Last-Event-ID`Repete.

Regras de recusa:

- Recusar uma tarefa para uma busca determinista rápida, a menos que o chamador indique um requisito concreto de durabilidade.
- Recusar uma loja de produção apenas em memória quando o trabalho deve sobreviver ao reinicio do processo.
- Recusar uma carga útil de resultados ilimitados; armazenar artefatos grandes externamente e devolver um manuseio de recursos autorizado.
- Recusar um ponto final de histórico sem a propriedade explícita do inquilino, filtragem, paginamento e política de retenção.

Faça um desenho de uma página com uma tabela de ciclo de vida, métodos de transferência, transação de persistência, regras de propriedade, fluxo de entrada, cadência de votação, semântica de cancelamento, opção de assinatura, limpeza de expiração, modelo de falha e mapa de migração legado.
