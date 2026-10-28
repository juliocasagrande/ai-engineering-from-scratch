---
name: web-desktop-harness
description: Construir um arame de estilo WebArena/OSWorld com métricas de avaliação baseadas em execução e eficiência de trajetória.
version: 1.0.0
phase: 14
lesson: 20
tags: [webarena, osworld, harness, trajectory-efficiency]
---

Dado um aplicativo-alvo (web ou desktop) e uma lista de tarefas com trajetórias de ouro, construa um arnes de avaliação.

Produzir:

1. Definições de tarefas: `(tid, description, gold_steps, success_predicate, state_reset)`- Não .
2. Corredor: executa o agente, capta todas as ações, registra a contagem de passos + tempo passado + estado de sucesso.
3. Metrica de eficiência de trajetória: `agent_steps / gold_steps`- Relatório por tarefa e agregado.
4. Reset de estado entre tarefas  nunca execute uma tarefa em estado contaminado por outra.
5. Classificador de modo de falha: para cada falha, etiquete se é uma falha de aterragem (elemento errado) ou uma falha de planejamento (ação errada).

Rejeitos duros:

- Não há reset de estado entre tarefas.
- A eficiência da trajetória é a norma de 2026.
- Aplicação de imagens de tela apenas sem paridade DOM. Alguns agentes usam DOM + vision; dar ambos, a menos que especificamente restringir a superfície.

Regras de recusa:

- Se as tarefas não têm trajetórias de ouro, rejeite.
- Se o aplicativo não estiver fixado a uma versão específica, recuse.
- Se o agente tiver ferramentas destrutivas (eliminar, publicar), exija uma cópia sandbox do aplicativo.

Output: `tasks.py`- Não . `runner.py`- Não . `failure_classifier.py`- Não . `report.py`- Não . `README.md` A primeira é a explicação da política de reset, da obtenção de recursos de trajetória de ouro e da divisão entre o terreno e o planejamento.
