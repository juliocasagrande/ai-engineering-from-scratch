---
name: supervisor-designer
description: Desenhar um sistema de supervisores/orquestração-trabalhador para uma determinada consulta de estilo de pesquisa, especificando o prompt de liderança, as funções dos trabalhadores, as regras de decomposição e o modelo de síntese.
version: 1.0.0
phase: 16
lesson: 05
tags: [multi-agent, supervisor, orchestrator, anthropic-research, langgraph]
---

Dada uma consulta do usuário que se beneficia de pesquisas paralelas sobre subagentes, produzir um design de padrão de supervisor pronto para ser incorporado em qualquer framework (LangGraph, OpenAI Agents SDK, CrewAI Hierarchical).

Produzir:

1. **Complexity estimate.** Esta consulta é simples (1 agente, 3-10 chamadas de ferramentas), média (2-4 trabalhadores) ou complexa (5+ trabalhadores)?
2. **Lead system prompt.** Deve incluir: a) instruções de decomposição, b) instruções de síntese, c) regra explícita de que o lead nunca lê conteúdo de origem bruto, apenas resumos de trabalhadores.
3. **Worker system prompts.** Um por papel, cada um nomeando o seu escopo estreito e o formato de saída que o lead espera.
4. **Sub-question decomposition rules.** Como o lead divide a consulta? Largo primeiro, depois estreito, ou decomposição direta? O que desqualifica uma sub-question (superposição com outra, muito ampla)?
5. **Synthesis template.** Regra explícita de gestão de conflitos: se dois trabalhadores retornarem fatos contraditórios, a síntese deve expor o desacordo em vez de escolher silenciosamente um.
6. **Model pairing.** Qual modelo para o nível de liderança (nível de raciocínio), qual para os trabalhadores (nível mais rápido/mais barato).
7. **Observability requirements.** Pontos mínimos de rastreamento: plano, início/final de cada trabalhador, entrada de síntese, saída de síntese.

Rejeitos duros:

- Qualquer projeto onde o lead usa ferramentas por si mesmo.
- As instruções de trabalho que permitem a deriva de alcance (por exemplo, "investigar qualquer coisa relacionada a X" sem limite).
- Templates de síntese que escondem conflitos.

Regras de recusa:

- Se a consulta for simples (estimada abaixo de 10 chamadas de ferramentas no total), recuse o projeto e recomenda um único agente em vez disso. Cite a constatação do custo de token Anthropic 15x.
- Se a consulta for sequencial (a etapa 2 precisa de saída da etapa 1), recuse e recomenda um padrão de pipeline/cadeia em vez disso.
- Se o usuário está a optimizar para determinismo e auditoria, recuse o supervisor e recomenda um gráfico estático LangGraph.

Resultado: resumo de design de uma página. Comece com a estimativa de complexidade e um veredicto de padrão-ajuste ("supervisor fits"). Feche com um lembrete de implantação do arco-íris se o sistema estiver em execução continuamente.
