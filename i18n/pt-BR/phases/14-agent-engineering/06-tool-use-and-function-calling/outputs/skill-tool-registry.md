---
name: tool-registry
description: Construa um catálogo de ferramentas de produção e registro com validação de JSON Schema, envio paralelo e observabilidade.
version: 1.0.0
phase: 14
lesson: 06
tags: [function-calling, tools, schema, validation, bfcl, parallel-tools]
---

Dado um domínio de tarefa, produzir um catálogo de ferramentas que um agente pode usar de forma confiável através dos eixos BFCL V4 (agente, multi-turn, vivo, não-vivo, alucinação).

Produzir:

1. Definições de ferramentas. `name` (serpente_causa), `description` (indica ao modelo quando usá-lo e quando não usá-lo), entrada de esquema JSON com propriedades digitalizadas, campos exigidos, enums, se for caso disso, mínimo/máximo para números, tempo de espera por ferramenta, política de caixa de areia por ferramenta (f surface, rede, limite de memória).
2. Verifique a qualidade da descrição. Exerça cada descrição através de "Isso diz ao modelo quando escolher esta ferramenta sobre as outras?" Se duas ferramentas tiverem descrições sobrepostas, rejeite e reescreva.
3. Plano de despacho paralelo: para cada tarefa realista, identifique quais as chamadas de ferramentas são independentes (podem ser paralelos) e quais devem ser sequenciais.
4. Política de validação. verificações de enum, regras de coerção de tipo (por exemplo, "aceitar int-as-string, rejeitar float-as-string"), aplicação de campo exigido.
5. Observabilidade. Cada ferramenta emite um OpenTelemetry GenAI `tool_call` span com atributos `gen_ai.tool.name`- Não . `gen_ai.tool.call.id`- Não . `gen_ai.tool.call.arguments`- Não . `gen_ai.tool.call.result` (referência, não em linha, quando exigido pela política de conteúdo).

Rejeitos duros:

- Ferramenta de execução de comandos/shell genérica.`git_status`- Não . `fs_read`- Não . `npm_test`)).
- Enum faltando quando o parâmetro tem um conjunto fechado de valores.
- A mesma descrição para duas ferramentas diferentes.
- `description` A lista de dados é composta por um conjunto de dados que só nomeia a ferramenta ("Agrega dois números").
- Não há tempo para qualquer chamada de ferramenta.

Regras de recusa:

- Se a lista de ferramentas exceder 30 ferramentas para um único agente, recusar e recomendar a delegação de subagentes (Lessão 17).
- Se qualquer ferramenta executar uma ação destrutiva sem um portal de confirmação, rejeite e aponte para a lição 09 (permissões, sandboxing).
- Se a tarefa for o uso de computador (clique, digite, captura de tela), rejeite e aponte para a lição 21  que é uma forma de ferramenta separada com ações baseadas na visão.

Saída: um catálogo de ferramentas JSON pronto para ser colado em chamadas SDK Anthropic / OpenAI / Gemini, um diagrama de despacho-grafo, um documento de política de validação e um mini-evento de estilo BFCL que o registro deve passar.

Conclui com um indicador de "o que ler a seguir": Lição 09 (sandboxing), Lição 23 (OTel GenAI) ou Lição 30 (driven-ev).
