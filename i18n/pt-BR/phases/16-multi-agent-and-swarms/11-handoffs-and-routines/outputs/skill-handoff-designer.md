---
name: handoff-designer
description: Desenhar uma topologia de transferência para um sistema de estilo Swarm/Agents-SDK: quais agentes existem, quais transferências podem chamar, quais transferiam contexto.
version: 1.0.0
phase: 16
lesson: 11
tags: [multi-agent, swarm, handoff, openai-agents-sdk]
---

Dada uma tarefa orientada para o usuário (frequentemente triagem ou roteamento baseado em habilidades), produzir uma topologia de transferência pronta para ser mapeada no OpenAI Swarm ou no OpenAI Agents SDK.

Produzir:

1. **Agent roster.** Cada agente: nome, propósito de uma frase, ferramentas e a que outros agentes pode entregar.
2. **Handoff functions.** As assinaturas de ferramentas por agente, cada função de entrega devolve um agente alvo.
3. **Context transfer policy.** Em cada ponta da entrega: histórico completo, últimas mensagens N, ou snapshot resumido.
4. **Guardrails.** A validação de entrada por agente (o que é permitido para desencadear entregas a especialistas sensíveis), a autenticação na entrega, quando necessário.
5. **Loop detection.** Regra para detectar ping-pong (por exemplo, "A entregue a B; B entregue de volta a A" ocorrendo mais de uma vez seguida).
6. **Fallback behavior.** Se um alvo de transferência estiver faltando (agente removido, falha do autor), qual agente trata a sessão.
7. **Session / memory plan.** Se usar sessões do Agents SDK, memória gerenciada por chamadores ou nenhuma memória.

Rejeitos duros:

- Qualquer projeto de transferência sem detecção de circuito.
- Funções de transferência que transmitem o histórico completo a especialistas com diferentes permissões de ferramentas (risco de segurança).
- Os desenhos que assumem o comportamento sem estado do Swarm, mas depois exigem memória de várias voltas usam sessões do Agents SDK em vez disso.

Regras de recusa:

- Se a tarefa precisar de execução paralela, recuse o Swarm e recomenda o supervisor (Lessão 05) em vez disso.
- Se a tarefa precisar de auditoria/replay determinista, recuse e recomenda o gráfico estático de LangGraph.
- Se a tarefa for um simples DAG de etapas (investigação → código → revisão), recomendamos o CrewAI Sequential em vez disso.

Resultado: um brief de uma página de entrega. Fechar com uma nota de segurança sobre como a injecção rápida pode desencadear entregas indesejadas e quais cortinas bloqueiam-na.
