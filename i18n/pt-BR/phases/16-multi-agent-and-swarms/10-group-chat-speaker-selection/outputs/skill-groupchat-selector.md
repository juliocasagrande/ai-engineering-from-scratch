---
name: groupchat-selector
description: Configure um selector de GroupChat de estilo AutoGen / AG2 para uma tarefa, nomeando a variante do selector, terminação e regras anti-falantes quentes.
version: 1.0.0
phase: 16
lesson: 10
tags: [multi-agent, groupchat, autogen, ag2, speaker-selection]
---

Dadas uma tarefa e uma lista de agentes, produzir uma configuração do GroupChat: escolha do selector, entradas do selector, regras de terminação e barris de segurança.

Produzir:

1. **Selector variant.** Round-robin (barato, justo, cego ao contexto), LLM selecionado (contextualmente consciente, caro) ou personalizado (LLM + fallback baseado em regras).
2. **Selector inputs.** Se for selecionado LLM: N recentes mensagens, especialidades de agente, conta de turno.
3. **Termination rules.** Max rounds, token TERMINATE, verificador de meta atingida, ou combinação.
4. **Hot-speaker mitigation.** Captura de rotação por agente, pontuação de balanço do alto-falantes na entrada do selector, rotação forçada após viradas consecutivas de K.
5. **Context bloat mitigation.** Plano de projecção (visões escaladas por função), pontos de controlo de resumo, limite de contexto por agente.
6. **Observability.** A entrada do selector de registro, a escolha do selector, a latência do agente por turno.

Rejeitos duros:

- Qualquer configuração selecionada pela LLM sem registro da entrada/saída do selector.
- Configurações sem limite máximo.
- Os conversos simétricos (sem especialização) sobre tarefas de raciocínio  usam o debate (Lessão 07) em vez disso.

Regras de recusa:

- Se a tarefa tiver uma estrutura DAG conhecida, recuse o GroupChat e recomenda o gráfico estático LangGraph para determinismo.
- Se a tarefa requer estrita auditoria, recuse o GroupChat; recomenda LangGraph com checkpointer.
- Se os agentes forem mais numerosos do que 5-6, recusar o GroupChat plano e recomendar grupos aninhados ou padrão hierárquico.

Resultado: um brief de configuração de um grupo de chat de uma página. Fechar com a estimativa de custo (LLM selecionado incumbe uma chamada selector por turno).
