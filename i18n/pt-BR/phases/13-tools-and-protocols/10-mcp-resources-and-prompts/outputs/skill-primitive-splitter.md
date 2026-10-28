---
name: primitive-splitter
description: Review an MCP server design and separate tools, resources, prompts, caching, and subscriptions using the 2026-07-28 contract.
version: 2.0.0
phase: 13
lesson: 10
tags: [mcp, resources, prompts, subscriptions, caching]
---

Revisar um servidor MCP proposto do ponto de vista do consumidor.

Produzir:

1. A.`server/discover`Revisão da publicidade de resultados `2026-07-28`e a capacidade exacta de recursos e de urgência.
2. Uma mesa com `name`- Não .`chooser`- Não .`primitive`, e `reason`- Não .
3. Esquemas de URI de recursos estáveis e quaisquer modelos de recursos limitados.
4. Nomes rápidos, descrições e argumentos necessários ou opcionais.
5. Uma regra de ordem determinista para cada método de lista.
6. Uma política de cache com `ttlMs`E ...`cacheScope`para cada resultado cacheável.
7. A.`subscriptions/listen`Filtrar recursos ou alterações de lista que necessitem de atualizações.
8. Um exemplo de recurso inválido que retorna JSON-RPC `-32602`, mais um exemplo de revisão não suportada que retorna `-32022`com`supported`E ...`requested`- Não .

Usar estas regras de decisão:

- Uma operação selecionada pelo modelo é uma ferramenta.
- O conteúdo endereçado por URI legível pelo host é um recurso.
- Um fluxo de trabalho de mensagem selecionado pelo usuário é um prompt.
- Um fluxo de atualização é aberto pelo cliente através de `subscriptions/listen`- Não .
- A identificação de solicitação de escuta torna-se `io.modelcontextprotocol/subscriptionId`- Não .
- O reconhecimento deve preceder todos os eventos da assinatura.
- Uma notificação nunca evita a autorização para leitura posterior.
- `server/discover`é obrigatório mesmo quando um cliente escolhe chamar primeiro outro método.

Rejeitar um projeto quando:

- Uma lista varia por causa do histórico de conexão.
- Um resultado privado é colocado num cache público.
- Um URI de recurso é aceito sem análise, autorização e verificação de limites.
- O projeto utiliza `resources/subscribe`ou trata uma assinatura como uma sessão de protocolo.
- Um prompt é permitido anular instruções confiáveis do host.

Retorna uma revisão de contrato de uma página. Termine com o erro primitivo, cache ou assinatura de maior risco e a menor correção.
