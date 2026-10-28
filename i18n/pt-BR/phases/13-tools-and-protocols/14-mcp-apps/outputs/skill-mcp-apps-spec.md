---
name: mcp-apps-spec
description: Projeto e revisão de um contrato de aplicação do MCP sobre o protocolo sem Estado 2026-07-28.
version: 2.0.0
phase: 13
lesson: 14
tags: [mcp, apps, stateless, ui-resources, csp, sandbox]
---

Dado uma ferramenta de MCP que possa necessitar de uma visão interativa, produzir um contrato de âmbito neutro.

## Introduções necessárias

- Nome da ferramenta, argumentos, resultado de texto ordinário e resultado estruturado.
- Interações de utilizadores que a visão deve suportar.
- Sensibilidade dos dados e se as respostas variam de acordo com o contexto da autorização.
- Permissões de navegador e origens externas que a visão precisa.
- Comportamento de apenas texto para hosts sem suporte de Apps.

## Produção

1. Envelope do núcleo atual. `2026-07-28`, por pedido `protocolVersion`- Não . `clientCapabilities`, recomendado `clientInfo`, correspondente `Mcp-Method` e `Mcp-Name` cabeçalhos, e `resultType` - Respostas.
2. Entrada de descoberta. `io.modelcontextprotocol/ui` em `server/discover`, com conservador `ttlMs` e `cacheScope`- Não .
3. Declaração de ferramenta. `_meta.ui.resourceUri` sobre a ferramenta devolvida por `tools/list`Não espere . `tools/call` Para revelar a interface.
4. Contrato de recursos. Incluir determinista `resources/list` Metadados anteriores `resources/read`Dá-me um canónico . `ui://` URI, nome e descrição estáveis, `text/html;profile=mcp-app`, dicas de cache, listas de domínios CSP (`connectDomains`- Não . `resourceDomains`- Não . `frameDomains`- Não . `baseUriDomains`), e os objectos mínimos de permissão.
5. Resultado de contrato. Retorna texto útil e dados estruturados, quer o host seja ou não o aplicativo.
6. Contrato de ponte. `ui/*` ou método proxied, origem exata da mensagem, esquema de argumento, esquema de resultado e verificação de consentimento do lado host.
7. Descreva a ferramenta e o resultado quando o cliente omite a capacidade de extensão de aplicativos.
8. Tabela de verificação. `-32020` Descoincidência de cabeçalho antes do roteamento, HTTP 400 `-32022` com dados de versão exatos suportados e solicitados, HTTP 400 `-32021` com `data.requiredCapabilities`, HTTP 404 `-32601`, 202 notificações de corpo vazio, violação do CSP, conteúdo não confiável, ligações não autorizadas e texto de retorno.
9. Limite de transporte. Se a implementação receber solicitações e cabeçalhos analisados, marque-o como um modelo de protocolo em processo e conecte-o ao adaptador HTTP Streamable completo da Lesson 09 . Um adaptador real deve exigir o JSON Content-Type e um valor de Aceitação contendo JSON mais SSE.

## Rejeitos duros

- Um núcleo `initialize`- Não . `notifications/initialized`, ou `Mcp-Session-Id` caminho apresentado como MCP atual.
- Um cartão selvagem `postMessage` origem-alvo ou receptor que salta `event.origin` Avalidação.
- Uma ligação de interface de interface revelada apenas após a ferramenta ser executada.
- Lista de domínio CSP Wildcard, origem de rede ilimitada ou permissões sem recurso visível.
- HTML controlado pelo usuário inserido sem um limite de desinfecção definido.
- Uma ação de interface consequente que trata um clique de iframe como autorização de hospedagem.
- Um servidor que anuncia recursos mas omite `resources/list`- Não .
- Qualquer organismo de resposta JSON-RPC para uma notificação sem um `id`- Não .

## Limite de compatibilidade

Os metadados de interface de interface plana herdados podem ser lidos como um retrocesso, mas novas saídas usam nested `_meta.ui.resourceUri`- Não . `ui/initialize` é permitido apenas quando identificado como o Aplicativos pós-Message aperto de mão. Nunca interfere para a inicialização do núcleo MCP removido.

## Formatos de saída

Retorna um design compacto com as seguintes cabeçalhos: Core Wire, Discovery, Tool, Resource, Resultado, Bridge, Security, Fallback, Verificação. Termine com a única suposta origem, permissão ou consentimento.
