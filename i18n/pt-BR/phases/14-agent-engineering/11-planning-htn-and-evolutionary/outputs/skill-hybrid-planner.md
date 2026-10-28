---
name: hybrid-planner
description: Build a hybrid planner — ChatHTN for provably-sound plans, AlphaEvolve for code search with a machine-checkable evaluator — and pick the right one for the problem.
version: 1.0.0
phase: 14
lesson: 11
tags: [planning, htn, chathtn, alphaevolve, evolutionary-search]
---

Dada uma classe de problemas (fluxo de trabalho vinculado a políticas versus otimização de código versus tarefa aberta), escolha um planejador e produz um andaime correto.

Decisão:

1. O problema tem condições prévias duras / políticas / restrições de programação? -> HTN (ChatHTN).
2. O problema tem uma função determinista de condicionamento físico verificável por máquina? -> Evolucional (AlphaEvolve).
3. Não? -> Reach para ReAct (Lessão 01) ou ReWOO (Lessão 02).

Para HTN, produzir:

1. `Operator`Tipo com `preconditions`- Não .`effects_add`- Não .`effects_remove`- Não .
2. `Method`Tipo com `task`- Não .`preconditions`- Não .`subtasks`- Não .
3. Um planejador que experimenta métodos primeiro, volta à decomposição do LLM e guarda em cache decomposições bem sucedidas do LLM.
4. Uma etapa de validação que rejeita a decomposição do MLL referindo operadores ou métodos desconhecidos.

Para a Evolutionary, produzir:

1. Uma população de programas candidatos.
2. Um avaliador determinista que retorna uma aptidão escalar.
3. Um operador de mutação (driven by LLM ou baseado em regras).
4. Um ciclo de seleção (manter o top-k, mutar, repetir) com paragem precoce.

Rejeitos duros:

- ChatHTN em que a saída de LLM é aplicada diretamente sem validação do esquema do operador.
- AlphaEvolve onde o avaliador chama um juiz de LLM. A aptidão deve ser determinista; os juízes de LLM introduzem ruído estoquístico do qual o ciclo não pode se recuperar.
- Nenhum padrão para tarefas abertas ("escrever uma postagem de blog").

Regras de recusa:

- Se o domínio não tiver um esquema de operador claro, recuse o ChatHTN. Sugira ReWOO ou simples ReAct.
- Se o domínio não tiver aptidão verificável por máquina, recuse o AlphaEvolve. Sugira Auto-Refine (Lessão 05).
- Se o utilizador quiser que "planner + LLM faz a chamada final", recuse.

Output: `operators.py`- Não .`methods.py`- Não .`planner.py`(HTN) ou `evaluator.py`- Não .`mutator.py`- Não .`loop.py`(evolução), mais `README.md`A conclusão é "o que ler a seguir" apontando para a lição 25 se a verificação de debate se encaixa no problema, ou a lição 02 se a tarefa é realmente ReWOO-formada afinal.
