---
name: hierarchy-fitness
description: Decida se uma tarefa multi-agente se encaixa em hierarquia, supervisor plano ou sequencial.
version: 1.0.0
phase: 16
lesson: 06
tags: [multi-agent, hierarchy, crewai, langgraph, decomposition-drift]
---

Tendo em conta uma descrição de tarefa e uma estrutura de órgãos opcionais, recomenda-se o padrão de coordenação (supervisor plano, hierárquico, sequencial) e lista os modos de falha específicos a evitar.

Produzir:

1. **Task shape analysis.** A tarefa é um fluxo linear, de expansão com ramos independentes, ou equipes aninhadas com suas próprias sub-equipas?
2. **Pattern verdict.** Se hierárquico, especifique a profundidade (2 níveis fortemente preferidos; 3 apenas com forte necessidade de auditoria).
3. **Decomposition plan.** A divisão exata que o gerente superior deve fazer, para cada ramo, nomear o subgerente e o escopo limitado.
4. **Reconciliation budget.** Número de tiros permitidos antes que o gerente superior se comprometa.
5. **Guardrails.** Três barris mínimos: operário canário por nível, cadeia de proveniência em cada síntese, alerta sobre a deriva de decomposição.
6. **Failure-mode checklist.** Qual dos {erro de atribuição de tarefa, interpretação errada de saída, ciclo de consenso} é mais provável que tenha a forma da tarefa? Descreva um sintoma concreto e uma mitigação por modo.

Rejeitos duros:

- Qualquer recomendação que proponha profundidade > 2 sem indicar um requisito concreto de auditoria ou órgão que o exija.
- Hierárquica para tarefas de fluxo único linear.
- Projetos sem um orçamento de reconciliação explícito.

Regras de recusa:

- Se a tarefa for simples o suficiente para caber a um agente (em menos de 10 chamadas de ferramentas), rejeite a hierarquia e recomenda um agente único.
- Se a tarefa não tiver limites naturais da equipe (cada sub-passo depende de cada outro), recuse e recomenda um padrão de bate-papo em grupo.
- Se o usuário quer hierarquial para "realismo" (porque o órgão humano é profundo), sinalize que a hierarquia humana não mapeia para a hierarquia LLM e recomenda mais plana.

Abre com o veredicto de padrão, feche com os três maiores riscos e os seus guardrails.
