---
name: agent-loop
description: Write a correct, minimal ReAct agent loop in any target language/runtime with tools, stop condition, and turn budget.
version: 1.0.0
phase: 14
lesson: 01
tags: [react, agent-loop, tools, observability, stop-condition]
---

Dado um tempo de execução de destino (Python async, Python sync, Node, Rust async, Go) e uma lista de ferramentas (nome, esquema de entrada, chamada), produzir um loop de agente ReAct que é correto na primeira tentativa.

Produzir:

1. Um tipo de buffer de mensagens com papéis {usuário, assistente, ferramenta, final} e o esquema que o provedor-alvo espera (Antropic `tool_use`- Não .`tool_result`Não trocem nunca em silêncio esquemas entre provedores.
2. Um registro de ferramentas com nome -> despacho de chamada, validação de entrada e resultado digitado. Os erros devem ser capturados e transformados em cadeiras de observação, nunca levantados para o loop.
3. Um ciclo que corre até um de: explícito `finish`Ação, sem chamadas de ferramentas na virada assistente, viradas máximas, tokens máximos totais, ou uma viagem de guarda.
4. Um orçamento de turno escalado para a classe de tarefas  tarefa curta 10, uso de computador 200, pesquisa profunda 400.
5. Um registro de rastreamento que registra cada pensamento, ação, observação e paragem da razão.`invoke_agent`- Não .`tool_call`) quando o tempo de execução tiver um SDK OTel presente.

Rejeitos duros:

- Isto é uma questão de fiabilidade, não de otimização.
- Engolindo erros de ferramenta em uma observação vazia. O modelo deve ver o texto de falha para que possa corrigir.
- Tratar o conteúdo recuperado como instruções confiáveis. Todas as saídas da ferramenta são entradas não confiáveis  somente a mensagem do usuário tem permissão (ver documentos do OpenAI CUA).
- Provisores de mistura sem uma camada de tradução de esquema.

Regras de recusa:

- Se o alvo for "sem framework, apenas bash", rejeite e recomende pelo menos um esquema de mensagem digitado; os loops de agente são propensos a erros demais para cola de shell não digitada.
- Se o utilizador solicitar "retrover automaticamente uma chamada de ferramenta falhada sem feedback ao modelo", recusar.
- Se a lista de ferramentas tiver uma ferramenta destrutiva sem uma confirmação humana no loop, rejeite e aponte para a lição 09 (permissões + sandboxing).

Resultado: um arquivo por idioma-alvo mais um `README.md`Explicando a escolha de parada, a justificação do orçamento e um rastro de trabalho mostrando observação de pensamento-ação por passo. Conclui com "o que ler a seguir" apontando para a lição 02 (ReWOO planejamento) se a tarefa é de longo horizonte, lição 03 (reflexão) se a tarefa é repetição de anteriores, ou lição 27 (injeção rápida) se as ferramentas tocarem conteúdo não confiável.
