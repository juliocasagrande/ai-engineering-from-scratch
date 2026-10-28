---
name: mcp-client-harness
description: Scaffold a multi-server MCP client with modern metadata, safe era negotiation, deterministic merge, and routing.
version: 2.1.0
phase: 13
lesson: 08
tags: [mcp, client, stateless, compatibility, routing]
---

Dada uma lista de MCP servidor transporte, produzir um cliente harness que prefere MCP `2026-07-28`e isola a compatibilidade do legado.

Produzir:

1. Configuração de pares. Mapear um nome de servidor estável para um comando ou endpoint afixado, argumentos, lista de permisos de ambiente, contexto de autorização, tipo de transporte e um explícito `allow_legacy`bandeira que é padrão para falsa.
2. Moderno construtor de solicitações. versão de protocolo de selo, capacidades atuais do cliente e identidade recomendada do cliente em cada `params._meta`imediatamente antes da serialização.
3. - A sonda da era do estúdio.`server/discover`Primeiro, aceita um DiscoverResult válido, tente novamente.`-32022`A Comissão propõe que os Estados-Membros adoptem medidas de protecção dos animais em condições de segurança.`-32020`- E mais .`-32021`como erros modernos corrigíveis.
4. Análise de compatibilidade de legado. Trata um erro não reconhecido, tempo de espera, fechamento de conexão ou resposta vazia como ambígua. Envie um limite limite.`initialize`Só quando esse igual exato tiver`allow_legacy: true`Selecione legado apenas após um sucesso correlacionado JSON-RPC contendo uma revisão configurada do legado, recursos de objeto e identidade de servidor não vazio. Caso contrário, falha fechado.
5. O cache da ferramenta.`ttlMs`E ...`cacheScope`Tratar o legado ausente `resultType`Como `"complete"`- Não .
6. Combinar espaço de nomes, classificar pares e ferramentas, prefixar ou rejeitar colisões, proibir a sobreescrita silenciosa.
7. Router. Mapear nomes canônicos de ferramentas para peer mais nome local, criar um novo ID de solicitação, enviar a solicitação correta de época e verificar o ID de resposta.
8. Recuperação: em caso de perda de transporte, falha de trabalho no voo, reinicialização ou reconnecção, repetição de descobertas e listas, reabertura de assinaturas e reaprovação de operações permitidas pela política de segurança.

Rejeitos duros:

- Enviar pedidos modernos sem corrente `_meta`- Não .
- Regressando à inicialização após um erro moderno reconhecido.
- Envio`initialize`para um grupo de pares que não tenha expressamente autorização para a compatibilidade com o legado.
- Tratar um timeout, fechamento de conexão, resposta vazia, erro não reconhecido, resultado mal formado ou revisão não suportada como prova de comportamento legado.
- Tratamento de um processo, conexão ou`Mcp-Session-Id`como o protocolo moderno.
- Compartilhar uma lista privada em cache em contextos de autorização.
- A sobreescrever silenciosamente um nome duplicado da ferramenta.
- Aceitar um sucesso moderno sem`resultType`- Não .

Regras de recusa:

- Recusar-se a gerar um comando fora de uma lista de permisos ficada.
- Recusar-se a encaminhar uma ferramenta quando o proprietário é ambíguo.
- Recusar-se a retomar uma chamada não idempotente automaticamente sem uma chave de idempotência de aplicação ou decisão do utilizador.

Faça um arnês completo do Python, pelo menos seis testes de conformidade e um relatório de inicialização listando pares, era selecionada, versão selecionada, escopo de cache e nomes de ferramentas canônicas.
