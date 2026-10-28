---
name: role-designer
description: Produção de uma lista de funções para um sistema multi-agente, nomeando o planejador/executor/crítica/verificador para uma determinada tarefa com esquemas de I/O explícitos.
version: 1.0.0
phase: 16
lesson: 08
tags: [multi-agent, role-specialization, metagpt, chatdev, verification]
---

Dado uma tarefa, produzir uma lista de papéis especializada com esquemas de I / O e um verificador determinista. Pronto para mapear em CrewAI, LangGraph, AutoGen ou loops personalizados.

Produzir:

1. **Role roster.** Nome de cada um, como mínimo: planeador, executor, verificador, crítico opcional.
2. **I/O schema per role.** Para cada papel: o que ele consome (a partir do papel upstream) e o que produz (esquema, não prosa).
3. **Verifier specification.** Nomear o controlo determinista: conjunto de testes, verificador de tipo, validador de esquema, linter. Descrever critérios de aprovação/falha.
4. **Critic specification (optional).** Se for incluído, diga qual é a qualidade subjetiva que julga.
5. **Communicative dehallucination rules.** Nomear as perguntas que cada papel de baixo está autorizado a enviar para cima quando um detalhe está faltando, para que eles não inventem.
6. **Revision loop budget.** Max rounds antes da escalada para humano.
7. **Framework mapping.** Cada linha: como expressar esta lista em CrewAI, LangGraph, AutoGen.

Rejeitos duros:

- Qualquer lista sem um verificador determinístico.
- Fuzzy I/O ("o executor retorna a saída"). Sempre indicar o esquema.
- O crítico e o verificador confluem. Eles capturam bugs diferentes; ambos devem existir se ambos são justificados.

Regras de recusa:

- Se a tarefa não tiver verificação determinista de corretão (trabalho generativo puro, escrita criativa), recuse e recomenda um ciclo de revisor humano ou um debate multi-agente (Lessão 07) em vez disso.
- Se a tarefa for pequena demais para 3 ou mais funções (menos de 10 minutos de trabalho humano), recuse e recomenda um único agente.

Resultado: um resumo de um papel de uma página. Fechar com a verificação de falha MAST: confirmar a existência de pelo menos um verificador determinístico.
