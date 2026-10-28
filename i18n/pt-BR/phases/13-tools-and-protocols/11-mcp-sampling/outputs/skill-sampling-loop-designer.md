---
name: sampling-loop-designer
description: Migração de ferramentas de MCP com modelo assistido para inferência direta ou MRTR sem estado 2026-07-28 com amostragem de compatibilidade limitada.
version: 2.0.0
phase: 13
lesson: 11
tags: [mcp, mrtr, sampling, stateless, migration]
---

Desenho de comportamento assistido por modelo para um servidor MCP que visa revisão de protocolo `2026-07-28`- Não .

A primeira é a de que o servidor pode integrar-se diretamente com um fornecedor de modelos.

Produzir:

1. Decidir sobre a arquitetura. Escolha inferência direta ou compatibilidade Amostra e diga o porquê.
2. Contrato de descoberta. `server/discover` com exato `supportedVersions`, capacidades anunciadas, `ttlMs`, e `cacheScope`- se as ferramentas forem publicitadas, incluir deterministas obrigatórios `tools/list` Descrição de um objeto válido `inputSchema`- Não . `resultType: "complete"`Metadados de identidade do servidor e sugestões de cache.
3. Incluir versão de protocolo e recursos do cliente em `_meta` - Em cada pedido. `-32602` para uma versão que não tenha ou não tenha cordas, `-32022` com exato `supported` e `requested` Os dados relativos a uma versão não suportada, e `-32021` com um `requiredCapabilities` Objeto quando a amostragem está ausente. Trate os metadados de identidade do cliente apenas como informativos. Nunca emite uma resposta JSON-RPC para uma notificação sem id; uma notificação HTTP aceita recebe `202` Sem corpo.
4. Para cada ronda MRTR, nomee o `inputRequests` O sistema de verificação deve ser executado em conformidade com o artigo 10.o, n.o 1, do Regulamento (UE) n.o 1095/2010.
5. Requer o método e argumentos originais, um novo ID JSON-RPC, rodada corrente `inputResponses`, e byte-exact `requestState`- Não .
6. Proteção do Estado: ligar o HMAC ou a criptografia autenticada ao principal, método, digestão de argumento, fase e curto prazo autenticado.
7. Política de segurança: define aprovação, rodadas máximas, limites de tokens e bytes, validação de resposta, registro e comportamento de recusa.
8. Se a amostragem permanecer, indicar a condição e a data para a sua substituição por integração direta.

Rejeitos duros:

- Um novo projeto que adopte a amostragem obsoleta sem um requisito documentado.
- Um servidor 2026-07-28 que envia `sampling/createMessage` como um pedido ao vivo de servidor a cliente.
- Qualquer utilização de `initialize`- Não . `notifications/initialized`- Não . `Mcp-Session-Id`, ou estado oculto de sessão de protocolo.
- Não assinado `requestState` que afeta a autorização, o acesso a recursos ou a lógica empresarial.
- Uma retentação que reutiliza o ID original JSON-RPC ou altera os argumentos originais.
- Um modelo de cliente sem verificações de capacidade, política de aprovação, validação e limite de rodada dura.
- `includeContext: "allServers"` ou contexto implícito entre servidores.

Regras de recusa:

- Recusar chamadas secretas ou qualquer projeto que oculte a intenção do servidor do usuário.
- Recusar a saída do modelo como prova de identidade, autorização ou consentimento do usuário.
- Recusar um projeto de várias rodadas quando uma chamada determinista de ferramenta for suficiente.
- Recusar chamar os metadados do cliente e do servidor de identidade autenticada.

Faça uma arquitetura de uma página com a decisão, o fluxo de fios, a mesa redonda, o conteúdo assinado do estado, o orçamento de segurança, os casos de falhas e o plano de migração. `direct inference`- Não . `temporary MRTR compatibility`, ou `no model required`- Não .
