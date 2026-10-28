---
name: structured-output-picker
description: Choose a structured output approach, schema design, and validation plan.
version: 1.0.0
phase: 5
lesson: 20
tags: [nlp, llm, structured-output]
---

Dado um caso de utilização (provedor, orçamento de latência, complexidade do esquema, tolerância à falha), saída:

1. Mecanismo. saída estruturada de fornecedor nativo, instructor retries, Outlines FSM, ou XGrammar CFG. Razão de uma frase.
2. Desenho de esquema: ordem de campo (razão em primeiro lugar, resposta em último lugar), campos nulaveis para "desconhecido", enum vs regex, campos necessários.
3. Estratégia de falha, Max retrocede, modelo de retorno, gracioso.`null`Tratamento, recusa de saída de distribuição.
4. Plano de validação: taxa de conformidade com o esquema (alvo 100%), validade semântica (Juge LLM), taxa de cobertura de campo, latência p50/p99.

Recusar qualquer projeto que coloque`answer`ou `decision`Rejeitar a utilização de modo JSON nu sem um esquema. Flag esquemas recorrentes por trás de uma biblioteca apenas FSM.
