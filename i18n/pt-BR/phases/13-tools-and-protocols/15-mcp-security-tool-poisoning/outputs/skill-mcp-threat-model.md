---
name: mcp-threat-model
description: Threat-model an MCP 2026-07-28 deployment across metadata, routing, authorization, MRTR, and compatibility boundaries.
version: 2.0.0
phase: 13
lesson: 15
tags: [mcp, security, stateless, tool-poisoning, mrtr]
---

Dada uma implantação de MCP, produzir um modelo de ameaça baseado em evidências. Suponha que qualquer servidor, pacote, cache, entrada de registro ou rota de gateway possa ser comprometida.

## Introduções necessárias

- Cliente, gateway, servidor, servidor de autorização e limites de confiança do registo.
- Descrição completa de ferramentas normalizadas e digestões aprovadas.
- Principais de autenticação, emissor, público, escopo e política de ferramentas.
- As revisões atuais e antigas do protocolo são aceitas.
- Operações de MRTR, esquemas de entrada, proteção do Estado e política de repetição.
- Escópios de cache, TTLs, rotas de assinatura e retenção de auditoria.

## Produção

1. Verificação por fio. Verifique versão e recursos por solicitação, em seguida, igualdade de cabeçalho de roteamento antes do suporte à versão. Requer HTTP 400 `-32020`para uma descoincidência, HTTP 400 `-32022`com dados exatos suportados e solicitados para uma versão não suportada, HTTP 404 `-32601`Para um método desconhecido, e 202 com um corpo vazio para uma notificação aceita.
2. Revisão do descriptor: relatar indicadores de intoxicação, alterações no digestor completo, ferramentas desconhecidas e alterações no esquema ou anotação.
3. Mapa de espaço de nomes. Dê um nome público qualificado para cada ferramenta de backend e rejeite a resolução silenciosa de colisão.
4. Matriz de autorização. Mapa autenticado principal e emissor para recurso, ferramenta, restrições de argumento e escopo. Não use `clientInfo`ou `serverInfo`como identidade.
5. Revisão do MRTR.`inputRequests`A entrada é uma solicitação integrada completa apoiada pela capacidade declarada do cliente.`elicitation: {}`como forma implícita de apoio e `elicitation: {form: {}}`rejeite a solicitação apenas para URL com HTTP 400 `-32021`E ...`data.requiredCapabilities.elicitation.form`- Proteção de ligação .`requestState`Para o método, ferramenta, argumentos exatos, principal, propósito, expiração e não.`inputResponses`entrada por chave antes de consumir atomicamente o nonce em uma loja de reprodução limitada, cortada com TTL compartilhada por cada instância de processador.
6. Revisão do eixo de risco. Marque qualquer passo automático que combina entradas não confiáveis, dados sensíveis e ação consequente.
7. A análise de cache e de assinaturas.`subscriptions/listen`- Não .
8. Limite de compatibilidade. Isole qualquer aperto de mão, sessão, fluxo GET, chamada de volta do servidor ou comportamento de tarefa experimental por trás do gating de versão explícita.
9. Limite de transporte. Identifique se a implementação é um adaptador HTTP completo ou um modelo de protocolo em processo. Conecte um modelo à lição 09 para JSON Content-Type e JSON mais SSE Accept validation.
10. Dê os três maiores investimentos com os proprietários e provas de aceitação.

## Rejeitos duros

- O instrumento silencioso de sobreescritura ou a selecção de rota por ordem de descoberta.
- Atualização de um digestor descritivo sem a reaprobação humana ou política.
- Tratar as informações auto-relatadas de clientes ou servidores como autenticação.
- Tratar uma capacidade declarada como permissão.
- Confiança em texto claro ou sem assinatura `requestState`para uma acção consequente.
- Manter o único livro de reprodução dentro de um gateway ou instância do servidor.
- Limite de taxa de chave ou estado de aprovação apenas por `Mcp-Session-Id`- Não .
- Presentar o padrão de implementação de padrões de amostragem, raízes, registos ou HTTP mais SSE antigo.

## Formatos de saída

Seções de retorno com nomes como limites de confiança, resultados de fio, resultados de descriptores, mapa de rota, matriz de autorização, resultados de MRTR, resultados de compatibilidade e remediação. evidências confirmadas separadas de suposições.
