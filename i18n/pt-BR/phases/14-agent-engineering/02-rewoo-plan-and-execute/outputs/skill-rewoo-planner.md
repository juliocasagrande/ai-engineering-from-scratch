---
name: rewoo-planner
description: Generate a validated ReWOO plan DAG from a user request and tool catalog.
version: 1.0.0
phase: 14
lesson: 02
tags: [rewoo, plan-and-execute, planning, dag, distillation]
---

Tendo em conta uma solicitação do utilizador e um catálogo de ferramentas (nome, esquema de entrada, descrição), elabore um plano ReWOO: um DAG de etapas com chamadas de ferramentas e referências de evidências (`#E1`- Não .`#E2`Valida o plano antes de o entregar a um executor.

Produzir:

1. Um plano DAG. Cada nó tem id (`E1`- Não .`E2`, ...), nome da ferramenta, dictação do argumento (as cordas podem conter `#E<k>`Referências) e opcionais `parallel_group`- É o que é?
2. Resultados de validação: verificação de aciclicidade por meio de triagem topológica; verificação de resolução de referência (cada `#E<k>`tem um produtor anterior); verificação da existência da ferramenta (todos os nomes da ferramenta estão no catálogo); verificação do esquema de arg (cada argumento corresponde ao esquema de entrada da ferramenta).
3. Para cada nível topológico, lista os nós que podem executar simultaneamente.
4. Recomendação dividida Planeador/solvente. Se o plano tem menos de 3 etapas, recomenda ReAct em vez disso. Se o plano tem um requisito de ciclo ilimitado (replaneamento em cada etapa), recomenda Plan-and-Execute com replaneador. Se o plano exceder 30 etapas ou visa web / móvel, recomenda Plan-and-Act com dados sintéticos do plano.

Rejeitos duros:

- Os planos com ciclos. A ReWOO assume um DAG; os ciclos são uma preocupação do ReAct ou do LATS.
- Planeja essa referência `#E<k>`onde`k`Não existe ainda na ordem topológica.
- Planejamento que chama ferramentas não estão no catálogo.
- Plans onde o tipo de argumento para uma referência não corresponde ao esquema da ferramenta (por exemplo, `#E1`Substitui uma cadeia, mas a ferramenta espera um int).

Regras de recusa:

- Se a tarefa for exploração aberta (ferramentas desconhecidas necessárias, passos desconhecidos), recuse e recomenda ReAct ou LATS (Lessão 04).
- Se o catálogo de ferramentas contém ferramentas destrutivas sem uma ferramenta de aprovação de abertura, rejeite e aponte para a lição 09 (permissões, sandboxing).

Output: um plano estruturado (JSON ou YAML), um relatório de validação, um mapa de paralelismo e uma ação de acompanhamento que aponta para o executor (ReWOO Worker), um replaneador (Plan-and-Execute) ou um ciclo de amostragem de trajetória maior (Plan-and-Act).

Conclui com uma nota "o que ler a seguir" apontando para a lição 03 (Reflexão) se a classe de tarefas foi tentada antes, ou lição 04 (LATS) se o plano se beneficiaria da pesquisa.
