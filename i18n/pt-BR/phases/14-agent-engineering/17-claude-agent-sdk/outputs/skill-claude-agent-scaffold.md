---
name: claude-agent-scaffold
description: Scaffold a Claude Agent SDK app with subagents, lifecycle hooks, session store, MCP server attachment, and W3C trace propagation.
version: 1.0.0
phase: 14
lesson: 17
tags: [claude-agent-sdk, subagents, hooks, session-store, mcp]
---

Dado um domínio de produto e uma lista de servidores MCP, anda a construir um aplicativo Claude Agent SDK.

Produzir:

1. Uma definição de agente principal com instruções, acesso a ferramentas integradas (read_file, write_file, shell, grep, glob, web fetch) e ferramentas de funções personalizadas.
2. O gerador subagente para paralelação e isolamento de contexto.
3. Anéis de ciclo de vida registados: PreToolUse + PostToolUse para auditoria, SessionStart para configuração, SessionEnd para demolição, UserPromptSubmit para aplicação de regras (ver padrões de pro-workflow).
4. Armazenamento de sessão (SQLite padrão) com `list_subkeys`- A linha de ferro é a linha de ferro.
5. Anexo do servidor MCP para superfícies externas de ferramentas/recursos.
6. O W3C rastreia a propagação do contexto para que os intervalos de OTel do chamador continuem através do CLI.

Rejeitos duros:

- Desembaraçamento de um subagente para uma tarefa de ferramenta única. Subagentes são para paralelação ou isolamento de contexto; não para "uma chamada de arquivo read_file".
- Anéis com trabalho caro sincrónico. Anéis devem ser de microsecondas a milissegundos.
- Lojas de sessões sem política de eliminação de cascata.

Regras de recusa:

- Se o produto precisar de trabalho de sincronização de longa duração (hora a dia), recuse o SDK auto-host e encaminhe-se para Claude Managed Agents.
- Se o utilizador pedir `--session-mirror`As transcrições de sessão contêm PII; espelho para armazenamento criptografado por utilizador.
- Se o agente depender do streaming de LLM bruto para a UX sem o uso de ferramentas, recuse o SDK do agente e recomende o SDK do cliente diretamente.

Output: `agent.py`- Não .`tools.py`- Não .`hooks.py`- Não .`session.py`- Não .`README.md`Explicando a política de subagente, registro de gancho, backend de sessão, anexos MCP e cablagem OTel. Conclui com "o que ler a seguir" apontando para a lição 22 para transferências de voz, lição 23 para atribuição de tempo de OTel ou lição 18 se o produto precisa de forma de execução de produção.
