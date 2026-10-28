---
name: runtime-picker
description: Escolha um agente de produção runtime (Agno, Mastra, LangGraph, SDK do provedor) para uma determinada pilha, orçamento de latência e forma operacional.
version: 1.0.0
phase: 14
lesson: 18
tags: [agno, mastra, langgraph, runtime, selection]
---

Dado um pacote, orçamento de latência, primitivas necessárias e forma operacional, escolha um tempo de execução.

Decisão:

1. Python + FastAPI + milhares de agentes de curta duração por segundo -> **Agno**- Não .
2. TypeScript + Next.js/Vercel + multi-provedor unificado -> **Mastra**- Não .
3. Estado duradouro, gráfico explícito, currículo-em-falha -> **LangGraph** (Lessão 13).
4. Claude-primeiro produto, quer o código Claude forma de arame -> **Claude Agent SDK** (Lessão 17).
5. O primeiro produto da OpenAI, quer entregas + barris + rastreamento -> **OpenAI Agents SDK** (Lessão 16).
6. Equipa multi-agente, simultaneidade de modelo de ator, isolamento de falhas -> **AutoGen v0.4** - Não . **Microsoft Agent Framework** (Lessão 14).
7. Os fluxos de trabalho deterministas baseados em funções ou em eventos -> **CrewAI** Tripulação ou Fluxo (Lessão 15).
8. Nenhum dos acima -> chamadas diretas da API + o loop stdlib da lição 01.

Produzir:

- Um documento de decisão curto: pilha, meta de latência, primitivos necessários, trade-offs observados.
- Um andaime mínimo no tempo de execução escolhido.
- Um plano de migração se outro tempo de execução estiver em uso hoje.

Rejeitos duros:

- A escolha de Agno ou Mastra puramente por "performance" quando a carga de trabalho é uma chamada lenta por pedido.
- Escolher um tempo de execução do TypeScript num monorepo Python sem uma razão.
- Escolhendo LangGraph para tarefas curtas sem estado. O checkpointer adiciona gastos gerais que um simples fluxo de trabalho (Lessão 12) evita.

Regras de recusa:

- Se o usuário quiser "todos os cinco tempos de execução, para comparar", recusar.
- Se o usuário quiser auto-host Mastra's `ee/` As características, recusa e aponta para os termos da licença.
- Se o produto precisar de trabalho de sincronia de longa duração (hora a dia), recuse-se a auto-hosting e encaminhe-se para Claude Managed Agents ou uma arquitetura baseada em fila (Lessão 29).

Resultado: doc de decisão + andaime + README. Concluir com "o que ler a seguir" apontando para a lição 24 (observabilidade) e lição 29 (tempo de execução da produção) para a camada operacional acima da estrutura.
