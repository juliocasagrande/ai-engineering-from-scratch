---
name: mcp-server-platform
description: Design a stateless MCP 2026-07-28 server with registry metadata, live discovery, authorization, policy, audit, and scale evidence.
version: 2.0.0
phase: 19
lesson: 13
tags: [capstone, mcp, stateless, streamable-http, oauth, registry, governance]
---

Tendo em conta a necessidade de uma plataforma interna, conceba um servidor MCP sem estado e limites de governança com foco na revisão do protocolo `2026-07-28`- Não .

Construir um plano:

1. Um esquema-válido `server.json`cujo nome de DNS inverso corresponda ao espaço de nomes autenticado do editor.
2. Obrigação`server/discover`para versões ao vivo, capacidades, extensões e identidade do servidor.
3. Versão e recursos do cliente em cada pedido `_meta`- O que é ?`resultType`e identidade do servidor em cada resultado.
4. Determinista .`tools/list`com`ttlMs`E ...`cacheScope`- Não .
5. POST-only Streamable HTTP com versão, método e cabeçalhos de nome necessários; sem sessões de protocolo, GET stream, sessão DELETE, ou cabeçalho de repetição.
6. Autorização que valida emissor, público, expiração e escopo em cada chamada.
7. Política sobre ator, ferramenta, alvo e argumentos normalizados. Ligue as aprovações de alto risco à ação exata e expiração, e depois prove que mudar um argumento rejeita repetição.
8. Reedição de auditoria e rastreamento de evidências fora do contexto visível do modelo.
9. Um adaptador de registo que valida `server.json`, sondas .`server/discover`, e relatórios de metadados/drift no tempo de execução.
10. Duas réplicas interchangeáveis e uma sonda de carga simultânea sem afinidade de sessão.

Rubrico de avaliação:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | Protocol correctness | Stateless envelopes, discovery, results, headers, and negative cases |
| 20 | Authorization | Issuer, audience, expiry, scope, and exact-action approval cases |
| 15 | Registry integrity | Valid `server.json`, live probe, and drift report |
| 15 | Policy and safety | Allow, deny, malformed, stale approval, and sensitive-data cases |
| 15 | Scale | Two replicas with no affinity dependency plus cancellation and recovery |
| 10 | Auditability | Redacted receiver-side audit and trace evidence |

Rejeitos duros:

- Um projeto de MCP atual que utiliza `initialize`- Não .`notifications/initialized`, ou `Mcp-Session-Id`- Não .
- Tratamento`server.json`como descoberta ou invenção de capacidade viva `.well-known/mcp-capabilities`como requisito de MCP.
- Publicar um nome de servidor fora do espaço de nomes autenticado para esse editor.
- Aceitação de um token sem validação do emitente e do público ou do recurso.
- Tratar as anotações da ferramenta ou uma aprovação de chat como autorização.
- Registros de auditoria que persistem segredos ou dados sensíveis.

Regras de recusa:

- Recusar-se a reivindicar a prontidão de produção apenas a partir das simulações locais.
- Recusar-se a expor uma ferramenta de mudança de estado sem provas de aprovação vinculada a políticas e ações.
- Recusar-se a publicar metadados que apontem para um ponto final cuja descoberta ao vivo não possa ser verificada.

Output: um plano de construção e uma matriz de evidências que cobre a publicação de metadados, descoberta ao vivo, transporte sem estado, esquemas de ferramentas, autorização, política, aprovação, auditoria e escala.
