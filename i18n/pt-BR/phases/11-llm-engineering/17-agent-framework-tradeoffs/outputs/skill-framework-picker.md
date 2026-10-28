---
name: framework-picker
description: Pick LangGraph, CrewAI, AutoGen, Agno, or plain Python for an agent task by matching abstraction to problem shape.
version: 1.0.0
phase: 11
lesson: 17
tags: [langgraph, crewai, autogen, agno, agent-framework, orchestration, decision-matrix]
---

Dada a descrição da tarefa (forma do problema, total de chamadas de LLM por execução, padrão de ramificação, durabilidade e necessidades de currículo, pontos de controlo humanos no loop, fanout paralelo, memória de sessão, volume de execução diária esperado), saída:

1. Uma frase nomeando a abstração que se encaixa: gráfico (estado de tipo, transições nomeadas), gráfico org (papéis de especialistas, entregas direcionadas pelo gerente), chat (agentes falam até que terminem), agente único com ferramentas.
2. Autoridade de ramificação. Quem escolhe o próximo passo: desenvolvedor (margens explícitas), gerente LLM (hierárquico CrewAI), emergente conversacional (AutoGen GroupChat), auto-roteado de chamada de ferramenta (Agno). Cite o custo de token por turno do roteamento selecionado pelo LLM, se aplicável.
3. O orçamento do estado. Confirme se é necessário retomar após a reinicialização, viagem no tempo ou interrupções humanas.
4. Escolha de quadro. Faça uma saída de langgraph, crewai, autogen, agno, plain_python. Inclua a justificação de uma frase que mapeia as respostas de forma e estado na abstração central do quadro.
5. Escape hatch. Se o volume de execução diária for superior a 10_000 ou a tarefa for duas ou menos chamadas de LLM sem estado, recomende Python simples com o SDK do provedor em vez disso. Nenhuma estrutura é a estrutura mais rápida quando a tarefa é pequena.

Recusar-se a recomendar AutoGen para fluxos de trabalho deterministas com um DAG conhecido; o GroupChatManager gasta tokens escolhendo alto-falantes que o desenvolvedor poderia ter cablado estáticamente.`output_pydantic`- Não .`output_json`(ver [docs.crewai.com/en/concepts/tasks](https://docs.crewai.com/en/concepts/tasks)), mas é `context`O canal ainda flui através da cadeia de instruções da próxima tarefa.`context`Para realizar um estado estruturado em tarefas sem que um desses esquemas de saída esteja conectado. Empurre de volta em LangGraph para um resumidor de duas chamadas; o StateGraph overhead é imposto puro. Empurre de volta em Agno quando a tarefa é executada por mais de 4 subtrabalhadores paralelos com semântica redução; Agno envia um `Parallel`Bloco cujas saídas se juntam a um dit teclado por nome de passo (ver [docs-v1.agno.com/workflows_2/overview](https://docs-v1.agno.com/workflows_2/overview)E ...[docs.agno.com/workflows/access-previous-steps](https://docs.agno.com/workflows/access-previous-steps)), mas não expõe uma API de "Send-style fanout-and-reduce" comparável à de LangGraph.

Exemplo de entrada: "Flow de trabalho de pesquisa de longa duração: planejar, expandir para três retrievers, sintetizar, aprobação humana breve, escrever relatório, citar fontes. Deve retomar após o acidente. Produção limitada a 50 rodadas por dia".

Exemplo de saída:
- Forma: gráfico. Plano tipado, três retrievers paralelos, transições nomeadas entre sintetizar e escrever.
- A ramificação: decidida pelo desenvolvedor através de bordas condicionais.
- O estado requer o currículo e a interrupção humana.
- Estrutura: langgraph. Estado, Enviar fanout, interrupt_before, e PostgresSaver são todos de primeira classe.
- Escape hatch: não aplicável. 50 corridas por dia estão bem abaixo do limiar do Python simples e o fluxo de trabalho é demasiado estadual para deixar sem quadro.
