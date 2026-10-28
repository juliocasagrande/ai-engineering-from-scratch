---
name: permission-mode-picker
description: Match a Claude Code task to the correct permission mode, budget caps, and required isolation before starting a run.
version: 1.0.0
phase: 15
lesson: 10
tags: [claude-code, permission-modes, auto-mode, budgets, isolation]
---

Dada uma tarefa proposta pelo código Claude, escolha o modo de permissão, defina orçamentos e especifique o isolamento mínimo necessário antes que o agente seja autorizado a iniciar.

Produzir:

1. **Task profile.**Uma frase sobre o que a tarefa faz, uma frase sobre o raio da explosão se correr mal.
2. **Mode recommendation.**Um dos seguintes: `plan`- Não .`default`- Não .`acceptEdits`- Não .`auto`- Não .`dontAsk`- Não .`bypassPermissions`Justificar com uma única frase referente ao raio da explosão.
3. **Budget numbers.**Valores concretos para `max_turns`- Não .`max_budget_usd`Para corridas desatendidas de mais de uma hora, especifique um limite de dólar igual ou inferior ao que pagaria por um erro humano que não pode reverter.
4. **Isolation requirements.**O âmbito do sistema de arquivos (só diretório de projeto, diretório de arranque, recipiente efêmero). Política de rede (sem saída, apenas lista de permisos, completa).`bypassPermissions`ou `dontAsk`O processo de execução deve estar dentro de um recipiente efêmero sem credenciais de produção montadas.
5. **Trajectory audit plan.**Como um humano revisará a trajetória após a corrida?`auto`- Não .`dontAsk`, e qualquer coisa acima de um horizonte de 30 minutos.

Rejeitos duros:
- `bypassPermissions`contra um repositório com alterações não comprometidas.
- `auto`sem limite orçamental.
- Qualquer modo acima .`acceptEdits`com amplas credenciais no ambiente (AWS, GCP, GitHub PAT com alcance de repo).
- Os períodos de execução sem supervisão são superiores a uma hora sem previsão de auditoria de trayectoria.
- A declaração de que o classificador de modo automático é suficiente para uma nova distribuição de tarefas.

Regras de recusa:
- Se o utilizador não puder indicar o raio de explosão de uma falha, recusar e exigir uma sentença explícita no pior dos casos antes de iniciar.
- Se o utilizador solicitar `auto`num espaço de trabalho com credenciais de base de dados de produção acessíveis, recusar e exigir credenciais de alcance ou um recipiente efêmero primeiro.
- Se o limite orçamental proposto exceder o que o utilizador está disposto a perder numa situação de mau funcionamento, recusar e exigir um limite mais baixo.

Formatos de saída:

Retorna um cartão de execução de uma página com:
- **Task summary**(uma frase)
- **Blast radius**(uma frase, pior caso)
- **Mode**- Não .
- **Budgets**(`max_turns`- Não .`max_budget_usd`, tampas por ferramenta)
- **Isolation**(de âmbito, política de rede, superfície de credenciais)
- **Audit plan**(que revisar a trajetória, quando e contra que rubrica)
