---
name: crew-or-flow
description: Pick CrewAI Crew or Flow for a given task, and scaffold the minimal implementation.
version: 1.0.0
phase: 14
lesson: 15
tags: [crewai, crews, flows, multi-agent, role-based]
---

Dada uma descrição de tarefa, escolha Crew (autônomo) ou Flow (determinista), em seguida, andaime.

Decisão:

1. A tarefa tem requisitos de SLA, conformidade ou reprodução determinista? -> Flow.
2. A tarefa é exploratória (investigação, primeiro esboço, tempestade de ideias)?
3. A tarefa tem mais de 4 especialistas com ordens de LLM escolhidas?
4. A tarefa tem <=3 especialistas em ordem fixa? -> A tripulação ou o fluxo sequencial  preferem o fluxo.

Para as tripulações, produzir:

1. Definições de agente: papel, meta, história de fundo (agreste, <= 200 palavras), ferramentas.
2. Definições de tarefa: descrição, expect_output, agente.
3. Equipamento com o processo certo.
4. Um arame de ensaio que dirige a tripulação sobre as entradas de amostra e verifica que as saídas esperadas são produzidas.

Para os fluxos, produzir:

1. `@start`função de entrada.
2. `@listen(topic)`Passo que forma um DAG.
3. Temas explícitos de eventos, sem transmissão mágica.
4. Um arnes de repetição: dada uma carga útil de arranque, reiniciar deterministicamente.

Rejeitos duros:

- Equipes sem histórias de fundo.
- Fluxos sem nomes explícitos de tópicos. "Cadenagem implícita" derrota o propósito da auditoria.
- Equipes hierárquicas com dois especialistas.

Regras de recusa:

- Se o utilizador pedir uma tripulação para uma tarefa de conformidade de apenas um produtor, recuse e migre para o Flow.
- Se o utilizador solicitar um Flow numa tarefa de investigação sem fim, recusar e migrar para Crew.
- Se a história de fundo exceder 200 palavras, recuse e precise um corte.

Output: `agents.py`- Não .`tasks.py`- Não .`crew.py`ou `flow.py`, mais `README.md`A conclusão é com "o que ler a seguir" apontando para a lição 24 (Langfuse/AgentOps) para observabilidade, ou lição 13 se o fluxo precisa de semântica de resumo duradoura.
