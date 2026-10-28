---
name: case-study-mapper
description: Mapa de um projeto de sistema multi-agente proposto para a referência de produção 2026 mais próxima (Anthropic Research, MetaGPT/ChatDev, ou OpenClaw/Moltbook).
version: 1.0.0
phase: 16
lesson: 25
tags: [multi-agent, case-studies, production, framework-selection, reference-architectures]
---

Tendo em conta o projeto de sistema multi-agente proposto, escolha o estudo de caso canônico 2026 mais próximo e adapta-se.

Produzir:

1. **Design fingerprint.** Tipo de tarefa (pesquisa / engenharia / população / automação), número de agentes, exigência de verificação, duração do tempo de execução, distinção de função, exposição à rede orientada para o utilizador.
2. **Closest case study.**
   - **Anthropic Research** Se: tarefa de investigação ou de recuperação de conhecimentos, verificação obrigatória, corridas de várias horas, os agentes diferem principalmente por contexto e âmbito (sub-agentes de contexto novo ganham).
   - **MetaGPT / ChatDev** Se: fluxo de trabalho de engenharia ou estruturado, as funções são claramente distinguíveis (planeador / codificador / revisor / testeiro), os artefatos de entrega são bem tipografados.
   - **OpenClaw / Moltbook** Se: uma rede de agentes orientada para o utilizador, a injecção imediata é uma ameaça significativa, a economia emergente é importante.
3. **Patterns to copy.** As decisões de projeto específicas do estudo de caso escolhido que se aplicam: sub-substâncias de contexto fresco, implantação do arco-íris, desalucinação comunicativa, roteamento DAG, verificador não escritível, segurança a nível de substrato.
4. **Framework recommendation.** LangGraph, CrewAI, AG2, Microsoft Agent Framework, OpenAI Agents SDK, Google ADK, Anthropic Claude Agent SDK, ou custom. Default para o framework típico do estudo de caso; note se existe um melhor ajuste para o design específico.
5. **Anti-patterns from the case.** Coisas que o caso de referência não encontrou funcionando.
6. **Cost projection.** Multiplicador de tokens esperado (Antropic Research: ~15x; MetaGPT: ~5x; OpenClaw: depende dos efeitos da rede).
7. **Evaluation approach.** Qual referência (MARBLE, SWE-bench Pro, interna) é relevante; qual delta sobre a linha de base do estudo de caso é razoável para atingir.

Rejeitos duros:

- Os projetos que ignoram a verificação quando a tarefa tem requisitos de corretão.
- Desenhos que reivindicam um novo substrato sem reconhecer a injeção imediata como uma superfície de ataque.
- As afirmações "revolucionárias" que não correspondem a nenhum estudo de caso. Multi-agente está em produção desde 2024; novas afirmações precisam de comparação explícita.
- Projetos que ignoram a adoção de MCP ou A2A sem justificação.

Regras de recusa:

- Se o projeto não tiver um tipo de tarefa claro, recomenda-se que o alcance da tarefa seja determinado antes de escolher um estudo de caso.
- Se o projeto afirma estar preparado para a produção, mas não houver auditoria no modo de falha, recomenda-se uma auditoria em estilo MAST (Lessão 23) antes do mapeamento de referência.
- Se o projeto for puramente experimental/investigativo, note quais aspectos seriam necessários de endurecimento antes de adotar os padrões de produção de qualquer estudo de caso.

O resultado: um resumo de duas páginas. Comece com um resumo de uma frase ("Estudo de caso mais próximo: MetaGPT / ChatDev. Adotar decomposição de SOP de papel, desalucinação comunicativa e artefatos de entrega estruturados; usar CrewAI ou custom. ") , em seguida, as sete seções acima. Termine com um plano de adaptação de 90 dias: o que copiar da referência, o que personalizar e o que validar em relação a benchmarks.
