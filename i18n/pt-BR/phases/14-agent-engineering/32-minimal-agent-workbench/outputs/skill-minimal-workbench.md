---
name: minimal-workbench
description: Defina o banco de trabalho de três arquivos mínimo viável para qualquer roteador de repo  short AGENTS.md, agent_state.json durável e um task_board.json JSON teclado para o backlog atual do projeto.
version: 1.0.0
phase: 14
lesson: 32
tags: [workbench, agents-md, state, task-board, scaffold]
---

Dado um caminho de repo e um atraso curto, estabeleça o banco de trabalho mínimo de agente viável.

Produzir:

1. `AGENTS.md` Não mais de 80 linhas. Deve encaminhar para: o arquivo de estado, o painel de tarefas, o documento de regras mais profundas (mesmo se vazio), e o comando de verificação.
2. `agent_state.json` com estas chaves: `active_task_id`- Não . `touched_files`- Não . `assumptions`- Não . `blockers`- Não . `next_action`Todos os campos opcionais são padrão para matriz vazia ou cadeia vazia, nunca `null` para matrizes.
3. `task_board.json` Como uma matriz de tarefas JSON. Cada tarefa tem `id`- Não . `goal`- Não . `owner` (`builder` - Não. `reviewer` - Não. `human`), `acceptance` (lista de cordas), e `status` (`todo` - Não. `in_progress` - Não. `done` - Não. `blocked`)).
4. `docs/agent-rules.md` O reservatório de espaço com um único H2 por superfície para que lições posteriores possam preenchê-lo.

Rejeitos duros:

- `AGENTS.md` Mais de 80 linhas ou menos de 10 linhas.
- Um arquivo de estado que faz referência ao histórico de bate-papo em vez do repo.
- Um quadro de tarefas sem `acceptance`As tarefas sem critérios de aceitação tornam-se selos de borracha "parecem bons".
- As tarefas de `owner` é `agent` ou `model`Os proprietários são papéis, não entidades.

Regras de recusa:

- Se o repo não tiver comando de verificação, recuse-se a escrever `AGENTS.md` Um roteador que aponta para um portão faltante é pior do que nenhum roteador.
- Se o backlog tiver mais de 12 tarefas abertas, recuse e peça ao usuário que o divida.
- Se o projeto enviar segredos em arquivos rastreados, recuse-se a escrever o arquivo do estado e surja a fuga secreta como uma descoberta bloqueadora primeiro.

Estrutura de saída:

```
<repo>/
├── AGENTS.md
├── agent_state.json
├── task_board.json
└── docs/
    └── agent-rules.md
```

Conclui com "o que ler a seguir" apontando para:

- Lição 33 para transformar o lugar de regra em restrições executáveis.
- Lição 34 para o esquema de estado duradouro.
- Lição 36 para o contrato de âmbito por tarefa.
