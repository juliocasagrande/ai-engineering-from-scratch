---
name: actor-runtime
description: Build an AutoGen v0.4-shaped actor runtime with private state, inbox-per-actor, message-only IPC, fault isolation, and a dead-letter queue.
version: 1.0.0
phase: 14
lesson: 14
tags: [autogen, actor-model, messaging, fault-isolation, dead-letter]
---

Dado uma tarefa multi-agente, produzir um ator runtime e os agentes de atores necessários.

Produzir:

1. A.`Message`Tipo com `sender`- Não .`recipient`- Não .`topic`- Não .`body`- Não .`mid`- Não .
2. Um `Actor`classe base com `receive(message, runtime)`O Estado do ator é privado.
3. A.`Runtime`com uma fila compartilhada, `send()`- Não .`run_until_idle()`As exceções nos manipuladores vão para DLQ; não se propaguem.
4. Um auxiliar de topologia: RoundRobin (rotação fixa), Selector (LLM escolhe em seguida) ou transmissão personalizada.
5. Anéis de observabilidade por mensagem: emitir intervalos de OTel com `gen_ai.agent.name`E ...`gen_ai.operation.name`Por lição 23.

Rejeitos duros:

- Mensagem sincrônica que bloqueia o remetente até o receptor retornar.
- Os atores lêem o estado através de mensagens ou não.
- Um tempo de execução que propaga exceções do operador.

Regras de recusa:

- Se a tarefa tiver apenas dois atores com um retorno e uma saída fixas, recuse a enquadramento do ator e sugira uma cadeia de resposta rápida (Lessão 12).
- Se o usuário quiser "modo sincrônico" para "debug mais fácil", rejeite. Sugira registro + rastreamento (Lessão 23) em vez disso.
- Se o domínio for estritamente pedido/resposta com um único especialista, sugere encaminhamento (Lessão 12) em vez de uma equipa de atores.

Output: `message.py`- Não .`actor.py`- Não .`runtime.py`- Não .`teams.py`- Não .`README.md`A descrição da política de DLQ, a escolha de topologia e como os intervalos OTel são cablados.
