---
name: gateway-bootstrap
description: Design a stateless MCP 2026-07-28 gateway with registry admission, policy, routing, and compatibility boundaries.
version: 2.0.0
phase: 13
lesson: 17
tags: [mcp, gateway, stateless, registry, rbac, subscriptions, tasks]
---

Dados clientes, backends, requisitos de autorização e restrições de conformidade, produzem um design de gateway.

## Introduções necessárias

- Recursos URI de gateway público, revisões de protocolo aceitas e transporte.
- Principal e modelo de referência autenticado.
- Os pontos finais de fundo, os emissores, os recursos, os registos de registro, a evidência do editor e os descritores aprovados.
- Visívelidade das ferramentas, política de argumentos, classes de custos e sensibilidade aos dados.
- Requisitos de transmissão, notificação de alterações, MRTR e tarefas.
- Requisitos de auditoria, retenção, rastreamento e redação.

## Produção

1. Entrada sem estado. Um ponto final POST, versão e recursos por solicitação, método de correspondência e cabeçalhos de nome, JSON ou SSE escopo de solicitação, e 405 para GET e DELETE modernos. Validar a igualdade de cabeçalhos antes do suporte de versão. Especificar HTTP 400 `-32020`, HTTP 400 `-32022`com dados exactos suportados e solicitados, HTTP 404 `-32601`, serialização opcional de dados de erro e 202 manipulação de notificações de corpo vazio.
2. Plano de descoberta.`server/discover`, descobrir cada backend, expor apenas interseções de segurança de capacidade de ponta a ponta, e incluir atuais `resultType`- Não .`ttlMs`- Não .`cacheScope`, e metadados de identidade do servidor.
3. Tabela de admissão. Valida o Registo Oficial `server.json`forma de publicação e `com.example/*`Nome de estilo separadamente da admissão de segurança. Para cada backend, junte o registro ao espaço de nomes de editor verificado externo, fonte de proveniência, ponto final, política de versão, digest descriptor, emissor, recurso, aprovação e estado de expiração.
4. Mapa do espaço de nomes. Dê a cada ferramenta backend um nome público estável e mantenha uma raiz-objeto válida `inputSchema`em cada`tools/list`Descrição, rejeita a colisão por ordem.
5. Matriz de autorização. Mapear principal e papel para ferramenta pública, recurso, argumentos e escopo. Mantenha credenciais externas e backend separadas e vinculadas ao emissor.
6. Contrato de encaminhamento: criar uma nova solicitação de backend independente, anunciar apenas as capacidades do cliente mediado, validar o resultado do backend e preservar a correlação de rastreamento.
7. Plano de cache, fazer descobertas dependentes do principal e listas privadas, definir TTLs limitados e comportamento de invalidação.
8. Política de taxas e auditoria. Limitações-chave por principal, emissor, recurso, ferramenta, classe de custos e tempo. Redigir credenciais e argumentos sensíveis desnecessários.
9. Descrever a SSE a escala de solicitação,`subscriptions/listen`reconhecimento e comportamento de reconexão, encaminhamento de estado de MRTR de byte-exact, e roteamento de tarefas por id de tarefa em `Mcp-Name`- Não .
10. Adaptador de transporte. Se o gateway receber solicitações e cabeçalhos analisados, etiquete-o como um modelo de protocolo em processo e conecte-o à lição 09 para JSON Content-Type e JSON mais SSE Accept enforcement.
11. Adaptador de compatibilidade. Cence inicialização mais antiga, IDs de sessão, fluxos GET, assinaturas de recursos e métodos de tarefas experimentais longe do núcleo moderno do gateway.

## Rejeitos duros

- A afinidade de sessão, as lojas de sessão ou a reescritura da identificação de sessão apresentada conforme exigido para 2026-07-28.
- Presença de registos de confiança ou um nome de exibição sem provas de admissão.
- Colições silenciosas de ferramentas ou atualizações de pines de descrição sem reaprovação.
- Reutilização do token do portador externo em um backend ou de um token backend em outro emissor ou recurso.
- Cachagem pública de uma lista filtrada por diretores.
- Um fluxo de eventos GET moderno independente, repetição de Last-Event-ID ou método de assinatura de recursos.
- Novos .`tasks/list`ou `tasks/result`- Comportamento.
- Limites de taxa especificados apenas por uma sessão de protocolo removida.
- Verificação de segurança inventada dentro de casa .`server.json`Em vez de um estado de admissão e proveniência verificados separados.
- Descrição de ferramentas com espaços de nome que omitem `inputSchema`- Não .

## Formatos de saída

Seções de retorno com nomes como Ingress, Discovery, Admission, Namespace Map, Authorization, Forwarding, Cache, Rate Limits, Audit, Interactions e Legacy Adapter.
