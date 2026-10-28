---
name: oauth-scope-planner
description: Projeto de autorização MCP 2026-07-28 com CIMD, isolamento do emissor, indicadores de recursos e escopo de intensificação.
version: 2.0.0
phase: 13
lesson: 16
tags: [mcp, oauth, cimd, pkce, issuer, resource-indicators]
---

Dado um servidor MCP HTTP remoto e sua lista de ferramentas, desenhe o limite completo de autorização.

## Introduções necessárias

- URI de recurso de MCP canônico e localização de metadados de recurso protegido.
- Emitentes de servidores de autorização autorizados.
- Tempo de execução do cliente: nativo ou web, com URIs de redirecção exatas.
- Mapeamento de ferramentas para o escopo e operações consequentes.
- Constrangimentos de tokens, atualizações e armazenamento de credenciais.
- Servidores de autorização legais que não possuam CIMD, se houver.

## Produção

1. Metadados de recursos. `resource`- Não . `authorization_servers`, e `scopes_supported`. Preservar o caminho de recursos após o segmento conhecido, como `https://notes.example.com/.well-known/oauth-protected-resource/mcp` para `https://notes.example.com/mcp`- Não .
2. Política do emissor: Estado exato dos emissores autorizados, validação de metadados, manipulação de alterações e RFC 9207 `iss` - Comparar.
3. Inscrição. Use pré-inscrição quando disponível, caso contrário, prefira um documento de metadados de ID do cliente. `client_id`; exigir um redirecionamento exacto dos URI e tratar os metadados de exibição como não confiáveis. `application_type` É opcional aqui.
4. Se necessário, etiquetar o seu prazo de prescrição, declarar `application_type`Não baixe a classificação após uma falha genérica da segurança CIMD.
5. Classificação de dados: `(issuer, resource)`. Proibir a reutilização entre emissores. Indicar que um URL CIMD auto-hospedado é portátil e não requer reinscrição de DCR quando um emissor de confiança muda.
6. Requer S256, redirecionamento exato URI, validação do emissor de resposta de autorização, e o mesmo recurso em solicitações de autorização e token.
7. Modelo de alcance: mapear cada ferramenta para o seu alcance mínimo. `WWW-Authenticate` O desafio de âmbito é autoritário.
8. Experiência de intensificação: identifique o escopo adicional, a explicação do usuário, o ponto de consentimento, a nova autorização e tente novamente com um novo ID de solicitação do MCP.
9. Verificação do servidor de recursos. `tools/list` com esquemas de raiz de objeto válidos, ordem determinista, tipo de resultado, identidade do servidor e indicações de cache. Validar o emissor, o público, a expiração, o escopo, os cabeçalhos atuais do MCP e solicitar metadados antes do envio da ferramenta.
10. Higiene de tokens, cabeçalho de portador só, sem token de consulta, sem token passthrough, armazenamento confidencial de atualizações e plano de rotação.
11. Contrato de erro. Preserva todas as solicitações id em um envelope de erro JSON-RPC, incluindo falhas OAuth. Requer HTTP 400 `-32020` para desajuste de cabeçalhos antes do HTTP 400 `-32022` Verificação de suporte de versão, dados exactos suportados e solicitados, HTTP 404 `-32601` Para métodos desconhecidos, e 202 com um corpo vazio para as notificações aceites.
12. Limite de transporte. Etiquete exemplos de corpos analisados como modelos de protocolo em processo e anexe-os ao adaptador HTTP Streamable completo da lição 09 para JSON Content-Type e JSON mais validação SSE Accept.

## Rejeitos duros

- O DCR foi apresentado como o novo mecanismo de inscrição preferido.
- DCR sem `application_type`- Não .
- Reutilizar credenciais de registro criadas pelo emissor, tokens de acesso ou tokens de atualização após as alterações do emissor.
- Normalização da resposta à autorização `iss` antes da comparação.
- Falta PKCE S256 ou desaparecida `resource` Em pedidos de autorização e de token.
- Aceitar um token para outro público ou encaminhar o token MCP para baixo.
- Utilização `clientInfo`- Não . `serverInfo`, capacidades, ou uma sessão de protocolo removido como autenticação.
- Adicionar OAuth ao estúdio local apenas para imitar o HTTP remoto.
- Deixar o caminho do recurso protegido ao construir o URL de metadados RFC 9728.
- Retorno de um objeto de texto simples ou ad hoc para um erro de solicitação de MCP em vez de um envelope JSON-RPC com a mesma identidade.

## Formatos de saída

Seções de retorno com nomes de recurso, emissores, inscrição, loja de credenciais, PKCE Flow, Matrix de alcance, Step-Up, validação do servidor, higiene de tokens e compatibilidade.
