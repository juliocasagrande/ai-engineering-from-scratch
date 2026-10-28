---
name: mcp-server-scaffolder
description: Design a stateless MCP 2026-07-28 server with discovery, request validation, and deterministic primitives.
version: 2.0.0
phase: 13
lesson: 07
tags: [mcp, server, stateless, discovery, scaffold]
---

Dado um domínio, produzir um plano moderno do servidor MCP. Mantém o estado da aplicação explícito e mantém o comportamento do protocolo estatal.

Produzir:

1. Divisão primitiva: define ferramentas atômicas, recursos com endereço URI e instruções úteis. omita uma primitiva quando o domínio não tem uso honesto para ela.
2. Resultado da descoberta.`supportedVersions`, capacidades do servidor, instruções opcionais, `resultType: "complete"`, dicas de cache e identidade do servidor em resultado `_meta`- Não .
3. Requer validador de protocolo versão e recursos do cliente em cada `params._meta`- Validar a identidade recomendada do cliente quando presente.`-32022`com versões solicitadas e suportadas em caso de desajuste.
4. Envase de resultado.`resultType: "complete"`E a identidade do servidor para cada sucesso.`ttlMs`E ...`cacheScope`para a descoberta, listas, modelos e leituras de recursos.
5. Defina uma chave de classificação estável para cada resposta da lista.
6. Política de estado. Coloque estado durável em uma base de dados ou retorne um manilho explícito e opaco como um argumento de ferramenta normal. Nunca esconda estado em uma sessão de protocolo.
7. Limite de compatibilidade. Se for necessário o suporte legado, isolar um `2025-11-25`Selecione-o apenas para tráfego antigo e teste as duas eras de forma independente.

Rejeitos duros:

- Um servidor moderno cujo primeiro método válido deve ser`initialize`- Não .
- Reutilização de recursos, identidade ou versão de um pedido anterior.
- Voltar .`Mcp-Session-Id`no tráfego HTTP moderno.
- Retorno de lista ou resultados de leitura de recursos sem sugestões de cache.
- Tratar as anotações como controles de autorização.
- Envio de um pedido independente de JSON-RPC do servidor.

Regras de recusa:

- Se um recurso solicitado revelar segredos sem autorização, parar e exigir uma política de acesso.
- Se um domínio não tiver dados de somente leitura, omita recursos em vez de inventarem.
- Se um domínio não tiver um modelo reutilizável, omita as instruções em vez de enviar o preenchimento.

Exporte uma arquitetura de uma página, tabela de métodos, pseudcódigo de validação, exemplos de resultados, regras de ordem determinista e pelo menos seis testes de conformidade.
