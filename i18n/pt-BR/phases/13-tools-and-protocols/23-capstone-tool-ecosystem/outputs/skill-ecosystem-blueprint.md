---
name: ecosystem-blueprint
description: Produce a full Phase 13 ecosystem architecture given a product need; name primitives, security posture, telemetry, and packaging.
version: "1.0.0"
phase: "13"
lesson: "23"
tags: [mcp, capstone, ecosystem, architecture, a2a, otel]
---

Dado o necessário produto (pesquisa, resumo, automação, qualquer fluxo de trabalho orientado por agentes), produzir a arquitetura completa.

Produzir:

1. Superfície de MCP.`server/discover`, os metadados do protocolo por pedido, ferramentas, recursos, instruções e política de cache.`ui://`Aplicações.
2. Extenções. Se o trabalho for assíncrono, declare `io.modelcontextprotocol/tasks`e design `tasks/get`- Não .`tasks/update`, e `tasks/cancel`Mantenha a manobra inicial em`resultType: task`, fazer resultados das pesquisas `resultType: complete`, e não utilizar `tasks/result`ou `tasks/list`- Não .
3. O set de alcance OAuth 2.1, gateway RBAC matriz, hash fichado, regra de dois auditoria.
4. Identificar as chamadas dos agentes, definir os cartões dos agentes.
5. Telemetria, gerenciamento de escala, exportação e opção de backend.
6. Embalagem: AGENTS.md, SKILL.md e superfície de implantação (Docker Compose, K8s).
7. Mapeando para as lições da Fase 13, a que cada escolha de design remonta.

Rejeitos duros:
- Qualquer arquitetura que combina entradas não confiáveis, dados sensíveis e ação consequente em um único turno (Relação de dois).
- Qualquer arquitetura sem traços de propagação entre os hops MCP e A2A.
- Qualquer arquitetura sem pelo menos um fornecedor de fallback na camada LLM.
- Qualquer conceito actual de MCP que dependa de `initialize`- Não .`Mcp-Session-Id`- Não .`tasks/result`, ou `tasks/list`- Não .

Regras de recusa:
- Se a necessidade de produto for melhor atendida por uma chamada direta de LLM, recuse-se a construir todo o ecossistema.
- Se a equipa não tiver capacidade operacional para um portal, recomendar um portal gerenciado e documentar a transferência de confiança.
- Se a arquitetura envolver pagamentos, exigir um protocolo de autorização de pagamento revisto separadamente e assinatura explícita.

Resultado: um plano de uma página com os primitivos, a postura de segurança, os saltos A2A, o plano de telemetria, a embalagem e o mapa das lições.
