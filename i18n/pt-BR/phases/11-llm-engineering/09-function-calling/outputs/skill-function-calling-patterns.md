---
name: skill-function-calling-patterns
description: Quadro de decisão para a implementação de funções de chamada na produção - design de ferramentas, gestão de erros, segurança e padrões de fornecedores
version: 1.0.0
phase: 11
lesson: 09
tags: [function-calling, tool-use, agents, mcp, security, openai, anthropic]
---

# Função chamando padrões

Ao criar uma aplicação de Mestrado em Direito Jurídico que use ferramentas, aplique este quadro de decisão.

## Quando usar chamadas de função

**Use function calling when:**
- O modelo necessita de dados em tempo real (tempos, preços das ações, consultas de banco de dados)
- A tarefa requer efeitos colaterais (envio de e-mails, criação de registros, implantação de código)
- O modelo deve escolher entre várias ações com base na intenção do usuário
- Está a construir um agente que interage com sistemas externos.

**Use structured outputs instead when:**
- Você precisa extrair dados do texto (sem chamadas externas necessárias)
- A produção é o produto final, não um passo intermediário
- Você tem um único esquema, não várias ferramentas para escolher

**Use both when:**
- O modelo chama uma ferramenta, então estrutura o resultado da ferramenta em um formato de saída específico

## Orientações para a concepção de ferramentas

1. **One tool, one action.** Uma ferramenta chamada `manage_database` O sistema de gestão de dados é muito amplo. `query_records`- Não . `insert_record`- Não . `update_record`O modelo seleciona melhor com ferramentas específicas.

2. **Descriptions are prompts.** O modelo lê descrições de ferramentas para decidir a seleção. Escreva-as como se você escrevesse instruções para um desenvolvedor menor. Incluir o que a ferramenta retorna, não apenas o que faz.

3. **Constrain with enums.** Se um parâmetro tem 3 a 10 valores válidos, use um enum. O modelo vai inventar cordas -- "Celsius", "Celsius", "C", "metric" -- a menos que você o restrinja.

4. **Fewer tools is better.** GPT-4o lida bem com 5-10 ferramentas. Com mais de 20 ferramentas, a precisão de seleção diminui. Com mais de 50 ferramentas, espere 10-15% de seleção errada de ferramentas.

5. **Required means required.** Marque apenas um parâmetro conforme necessário se a ferramenta não puder literalmente funcionar sem ela.

## Padrões específicos do fornecedor

### OpenAI (GPT-4o, o3, GPT-4o-mini)

```python
tools=[{"type": "function", "function": {"name": ..., "parameters": ...}}]
tool_choice="auto"       # model decides
tool_choice="required"   # must call at least one tool
tool_choice={"type": "function", "function": {"name": "specific_tool"}}
```

- Suporta chamadas paralelas de ferramentas (múltiplas) `tool_calls` em uma resposta)
- As identidades de chamada de ferramenta devem ser transmitidas com os resultados
- `gpt-4o-mini` É 10 vezes mais barato e lida bem com o roteamento de ferramentas simples
- Modo de saída estruturada funciona com parâmetros de ferramenta para conformidade garantida com o esquema

### Antropico (Claude 3.5 Sonnet, Claude 4 Opus)

```python
tools=[{"name": ..., "description": ..., "input_schema": ...}]
tool_choice={"type": "auto"}     # model decides
tool_choice={"type": "any"}      # must call at least one tool
tool_choice={"type": "tool", "name": "specific_tool"}
```

- As chamadas de ferramentas aparecem como blocos de conteúdo com `type: "tool_use"`
- Os resultados vão para as mensagens do usuário com `type: "tool_result"`
- Nome de campo é `input_schema`Não , não . `parameters` (bug comum de migração)
- Suporta várias chamadas de ferramentas por resposta

### Google (Gemini 2.0 Flash, Gemini 2.0 Pro)

```python
function_declarations=[{"name": ..., "description": ..., "parameters": ...}]
function_calling_config={"mode": "AUTO"}   # or "ANY" or "NONE"
```

- Utilizações `function_declarations` no nível superior
- Resultados devolvidos através de `function_response` Partes
- Suporta chamadas paralelas de funções

### Modelos de código aberto (Llama 3, Hermes, Qwen)

- Não há formato padronizado - varia por modelo e estrutura de serviço
- O formato Hermes (NousResearch) é a convenção mais comum
- VLLM suporta ferramenta compatível com o OpenAI que exige modelos suportados
- Ollama suporta ferramentas básicas de chamada com modelos compatíveis
- Precision de seleção de ferramentas de teste antes da produção - modelos abertos são 15-30% menos precisos do que o GPT-4o no Berkeley Function Calling Leaderboard

## Padrões de manipulação de erros

### Retorno de erros estruturados

```json
{"error": true, "message": "City 'Toky' not found. Did you mean 'Tokyo'?", "code": "NOT_FOUND", "suggestions": ["Tokyo"]}
```

Incluir informações acessíveis. "Não encontrada" é ruim. "Não encontrada, quis dizer X?" é bom. O modelo usa mensagens de erro para autocorrigir.

### Estratégia de retomada

1. A chamada de ferramenta falha com um erro corrigível (typo, valor enum errado)
2. Enviar o erro de volta para o modelo como resultado de ferramenta
3. O modelo ajusta e retrata
4. Máximo de 3 retemps por chamada de ferramenta
5. Após 3 falhas, devolver o erro ao usuário

### Manutenção de tempo de ausência

Defina o tempo de execução de todas as execuções da ferramenta. 30 segundos é um padrão razoável. Se uma ferramenta termina, retorne um erro de tempo estruturado para que o modelo possa informar o usuário em vez de pendurar.

## Lista de verificação de segurança

| Check | Why | How |
|-------|-----|-----|
| Allowlist functions | Prevent arbitrary code execution | Only register tools the user needs |
| Validate argument types | Prevent type confusion attacks | Check types before execution |
| Sanitize string arguments | Prevent injection | Reject or escape special characters |
| Parameterize database queries | Prevent SQL injection | Never pass model-generated SQL directly |
| Filter tool results | Prevent data leakage | Remove API keys, PII, internal errors |
| Rate limit tool calls | Prevent runaway loops | Max 10-20 calls per conversation |
| Log all tool calls | Audit trail | Store tool name, arguments, result, timestamp |
| Block path traversal | Prevent file system access | Reject `..` and absolute paths in file tools |
| Sandbox code execution | Prevent system access | Use containers or restricted builtins |
| Validate return size | Prevent context stuffing | Truncate results over 10KB |

## Optimização de desempenho

- **Parallel calls:** Quando o modelo solicitar várias ferramentas independentes, execute-as simultaneamente com `asyncio.gather()` ou `concurrent.futures`
- **Caching:** Resultados de armazenamento em cache para argumentos idênticos na mesma sessão (o tempo não muda em 60 segundos)
- **Streaming:** Transmitir a resposta final do modelo enquanto os resultados da ferramenta estão sendo obtidos
- **Tool pruning:** Se o contexto for apertado, apenas inclua definições de ferramentas relevantes para a consulta atual (utilize um classificador para filtrar)
- **Smaller models for routing:** Utilização `gpt-4o-mini` ou `claude-haiku-4-5` para a seleção de ferramentas, então passar os resultados para um modelo mais forte para síntese

## Padrões comuns de falhas

| Failure | Cause | Fix |
|---------|-------|-----|
| Wrong tool selected | Ambiguous descriptions | Rewrite descriptions with specific trigger words |
| Missing required args | Model forgot a parameter | Add clear examples in parameter descriptions |
| Infinite tool loop | Model keeps calling same tool | Set max iterations (5-10) and detect repeated calls |
| Hallucinated arguments | Model invents plausible but wrong values | Use enums, validate against known values |
| Tool result too large | API returned 100KB of data | Truncate or summarize before feeding back |
| Model ignores tool result | Result format confusing | Return clean JSON with clear field names |
