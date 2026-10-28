---
name: parallel-call-safety-check
description: Verifique um registro de ferramentas para obter uma parallelização segura. Marque cada ferramenta paralelo_seguro, note dependências de ordem e marque o risco de limite de taxa para baixo.
version: 1.0.0
phase: 13
lesson: 03
tags: [parallel-tool-calls, streaming, correlation, rate-limits]
---

Dado um registo de ferramentas (lista de ferramentas com nomes, descrições e executores), devolva uma cópia com anotações com `parallel_safe: bool`- Não . `ordering_deps: [tool_name]`, e `rate_limit_group: name` campos adicionados.

Produzir:

1. Classificação por ferramenta: para cada ferramenta, decida: seguro para executar em paralelo na mesma curva (lecturas puras, recursos diferentes); inseguro (mutações, recursos compartilhados, limites de taxa externa).
2. Grafico de dependência. Identifique pares onde a saída de uma ferramenta deve alimentar a entrada de outra. Não pode paralelalizar dentro de uma curva. Marque com `ordering_deps`- Não .
3. Grupo de limite de taxa. Ferramentas que atingem a mesma API a jusante compartilham um grupo.
4. Recomendações de segurança: Para cada ferramenta insegura, indique se desativar o paralelo para essa curva, fila ou fragmento por recurso.
5. Banderas específicas do fornecedor. `parallel_tool_calls=false` sobre o OpenAI ou `disable_parallel_tool_use=true` No Anthropic quando há ferramentas inseguras no set.

Rejeitos duros:
- Qualquer registo sem classificação após a auditoria.
- Qualquer ferramenta de escrita de um recurso compartilhado marcada `parallel_safe: true`Condições de corrida.
- Qualquer ferramenta que acesse uma API externa limitada de taxa sem um `rate_limit_group`- Não .

Regras de recusa:
- Se for pedido que todas as ferramentas sejam marcadas de forma paralela sem inspecção, recuse.
- Se o registo incluir ferramentas consequentes no mesmo recurso (`delete_file` e `write_file` A fase 14 · 09 para a serialização a nível de caixa de areia.
- Se o usuário argumenta que suas ferramentas nunca competem, recusa e pede a prova (tests, registros ou um argumento formal).

Resultado: um registo revisto como um bloco JSON com os três novos campos por ferramenta, seguido por um breve resumo nomeando a escolha de paralelalização de maior risco e a mitigação recomendada. `tool_choice` - Não. - Não.
