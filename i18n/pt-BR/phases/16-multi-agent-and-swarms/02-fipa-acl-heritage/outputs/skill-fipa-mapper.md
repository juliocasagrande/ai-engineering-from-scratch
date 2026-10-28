---
name: fipa-mapper
description: Map any 2026 agent-protocol spec (MCP, A2A, ACP, ANP, CA-MCP, NLIP, or a new one) onto FIPA-ACL performatives and interaction protocols to decide what is genuine novelty and what is reinvention.
version: 1.0.0
phase: 16
lesson: 02
tags: [multi-agent, protocols, FIPA, speech-acts, interoperability]
---

Dado um novo protocolo de agentes, produzir o mapeamento FIPA-ACL para que o leitor possa dizer quais partes são reinventadas e quais são genuínas novas estruturas.

Produzir:

1. **Envelope mapping.**Para cada tipo de mensagem definido pela especificação, nomear o executativo FIPA mais próximo (`inform`- Não .`request`- Não .`query-if`- Não .`query-ref`- Não .`propose`- Não .`accept-proposal`- Não .`reject-proposal`- Não .`cfp`- Não .`subscribe`- Não .`cancel`- Não .`failure`- Não .`not-understood`Se não houver encaixes performativos, descreva a lacuna com precisão.
2. **Correlation model.**Como a especificação correlaciona as solicitações com respostas, cancelamento com a solicitação original e eventos transmitidos ao assinante?`:conversation-id`E ...`:reply-with`campos.
3. **Content-language stance.**A especificação manda um esquema de conteúdo (artefatos de tipo, JSON-Schema), aceita a linguagem natural ou deixa-o aberto?
4. **Interaction-protocol library.**Quais protocolos de interação FIPA são implementáveis além da especificação: contract-net, subscribe-notify, request-when, propose-accept?
5. **Discovery model.**Como um agente encontra contrapartes e capacidades (MCP `listTools`Comparar com o facilitador de diretórios e o serviço de páginas amarelas da FIPA.
6. **Reinvention vs novelty.**Produza uma tabela curta com três colunas: [conceito FIPA, equivalente à especificação moderna, o que mudou]. Marque cada linha como [reinvenção] ou [estrutura de novela]. Uma linha é "estrutura de novela" apenas quando a especificação introduz um primitivo que a FIPA não tinha identidade descentralizada, artefatos multimodal tipados e conteúdo interpretável LLM são os candidatos comuns.

Rejeitos duros:

- Qualquer mapeamento que alegue que uma especificação é "revolucionária" sem mostrar uma FIPA primitiva não tinha.
- Comparar estrutura que ignora a camada de descoberta.
- Declarações como "Protocolo X substitui a FIPA" sem abordar o que acontece quando dois agentes discordam sobre o significado do conteúdo (drift semântico).

Regras de recusa:

- Se a especificação for pré-normatização (projeto < 6 meses de idade, nenhuma implementação pública), indicar que o mapeamento é provisório e marcar as três alterações mais prováveis.
- Se a especificação for de fonte fechada ou apenas para empresas (algumas variedades ACP), mapear o que está documentado e nomear as lacunas.
- Se o usuário fornecer apenas um post no blog (sem documento de especificação), peça a especificação antes de mapear.

Resultado: um resumo de uma página. Comece com um resumo de uma frase ("Protocolo X é FIPA `request`- Não .`subscribe`com sintaxe JSON e uma camada de descoberta baseada em DID."), então as seis seções acima, em seguida, um parágrafo final respondendo: "Qual antigo modo de falha FIPA esta especificação redescobrirá?"
