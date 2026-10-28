---
name: terminal-coding-agent
description: Construir e avaliar um agente de codificação nativo do terminal contra o banco SWE Pro com custo limitado, ferramentas em caixa de areia e superfície de gancho completa para 2026.
version: 1.0.0
phase: 19
lesson: 01
tags: [capstone, coding-agent, claude-code, swe-bench, mcp, hooks, sandbox]
---

Com um repositório-alvo e uma tarefa de linguagem natural, construa um arnes que planeja, executa em uma caixa de areia e abre uma solicitação de puxão.

Construir um plano:

1. Ergue um arnes de TUI Bun + Ink com um painel de planos, um fluxo de chamadas de ferramentas e um orçamento de tokens/dólares ao vivo.
2. Defina seis ferramentas (read_file, edit_file, ripgrep, tree_sitter_symbols, run_shell, git) através do Modelo Context Protocol StreamableHTTP. Cada chamada retorna no máximo 4k tokens.
3. Execute cada chamada de ferramenta dentro de uma caixa de areia E2B ou Daytona em um novo `git worktree add` Nunca toques no sistema de arquivos do host.
4. Enviar todos os oito eventos de gancho 2026: SessionStart, SessionEnd, PreToolUse, PostToolUse, UserPromptSubmit, Notificação, Stop, PreCompact. Enviar pelo menos quatro ganchos autorizados pelo usuário (guarda de comando destrutivo, contabilidade de tokens, emissor OTel span, escritor de traços de pacotes).
5. Faça três orçamentos: 50 voltas, 200 mil tokens, 5 dólares.
6. Emite OpenTelemetry abrange com convenções semânticas da GenAI a um Langfuse auto-anfitrião.
7. Se tiver sucesso, empurra o ramo e abra um PR com o plano e o rastro no corpo.
8. Avalie contra mini-swe-agent em um subconjunto Pro Python SWE-bench de 30 edições e registre pass@1, viradas, tokens e dólares por tarefa.

Rubrico de avaliação:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | SWE-bench Pro pass@1 | Matched 30-task subset vs mini-swe-agent baseline |
| 20 | Architecture clarity | Plan/act/observe separation, hook surface, tool schema readability |
| 20 | Safety | Sandbox escape red-team + destructive-command guard audit |
| 20 | Observability | 100% of tool calls spanned, token accounting per turn |
| 15 | Developer UX | Cold-start under 2s, crash recovery, Ctrl-C cancel semantics |

Rejeitos duros:

- Arnes que explode para o sistema de arquivos do host em vez de dentro da caixa de areia.
- Qualquer agente que possa escrever fora da árvore de trabalho ou curl URLs externas sem um gancho de autorizador explícito.
- Números equivalentes relatados sem uma linha de base correspondente nas mesmas 30 questões.
- As reivindicações de "taxa de passagem" que dependem de `git reset --hard` entre as retemptadas; SWE-bench Pro é pass@1.

Regras de recusa:

- Recusar-se a empurrar diretamente para o principal sob qualquer configuração.
- Recusa-te a desativar o comando destrutivo.
- Recusa-se a correr sem um limite orçamental.

Resultado: um repo contendo o arnes, um arnes SWE-bench Pro eval fixo de 30 tarefas com execução de linha de base de mini-swe-agent correspondente, um arquivo de rastreamento OpenTelemetry por pelo menos 5 rodadas completas e uma denominação de escrita que as tarefas do arnes resolvem que a linha de base não e vice-versa.
