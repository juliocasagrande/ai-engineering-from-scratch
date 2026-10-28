---
name: skill-structured-outputs
description: Decision framework for choosing the right structured output strategy based on provider, reliability, and complexity
version: 1.0.0
phase: 11
lesson: 03
tags: [structured-output, json, schema, constrained-decoding, pydantic, function-calling]
---

# Estratégia estruturada de produção

Ao criar uma aplicação de Mestrado em Direito Jurídico que requer dados estruturados, aplique este quadro de decisão.

## Quando utilizar cada abordagem

**Prompt-based ("Return JSON"):**Apenas prototipagem. Aceitável para ferramentas internas onde falhas ocasionais de análise são toleráveis. Adicione uma tentativa/exceto com retest. Nunca use em canais de produção.

**JSON mode (API flag):**Você precisa de JSON válido garantido, mas o esquema é simples ou flexível. Funciona quando você valida a forma no lado da aplicação. Disponível: OpenAI, Anthropic (através do uso de ferramentas), Google.

**Schema mode (constrained decoding):**Sistemas de produção em que cada saída deve corresponder a um esquema específico. Falhas de análise zero. Violações de esquema zero. Use isso por padrão para qualquer tarefa de extração ou classificação de produção. Disponível: saídas estruturadas OpenAI, Outlines, Guidance.

**Function calling / tool use:**O modelo precisa escolher qual função chamar, não apenas preencher parâmetros. Você tem vários esquemas e o modelo seleciona o adequado. Também use ao se integrar com a infraestrutura de ferramentas / funções existentes.

**Instructor library:**Quer validação Pydantic com retry automático em qualquer provedor. Melhor DX para projetos Python. Enrola OpenAI, Anthropic, Google e modelos de código aberto.

## Orientações específicas para o prestador

**OpenAI:**Utilização`response_format`com`json_schema`Tipo. Descodagem restrita está incorporada. Modelos Pydantic funcionam diretamente.

**Anthropic:**Use ferramenta para saída estruturada. Defina uma única ferramenta com o esquema desejado. O modelo retorna argumentos de chamada de ferramenta correspondentes ao esquema. Confiável, mas requer que a ferramenta use padrão API.

**Open-source models (vLLM, Ollama):**Use Outlines ou Guidance para decodificação restrita. Essas bibliotecas compilam esquemas JSON em máquinas de estado finito que mascaram tokens inválidos durante a geração. Requer executar inferência localmente.

## Orientações para o projeto de esquemas

1. Mantém os esquemas planos quando possível. Os objetos aninhados além dos 2 níveis aumentam os erros de extracção.
2. Use enums para campos categóricos. Não confie no modelo que invente a cadeia certa.
3. Fazer campos ambíguos exigidos com suporte explícito de nulo em vez de opcionais. Força o modelo a tomar uma decisão.
4. Adicionar descrições às propriedades do esquema. O modelo lê-as como instruções.
5. Evite os tipos unificados (oneOf/anyOf) a menos que seja necessário.
6. Defina o mínimo/máximo nos números.
7. Use minItems/maxItems em matrizes para evitar saídas vazias ou sem limites.

## Padrões e correções comuns de falhas

- **Model wraps JSON in markdown fences**: mudar de modo baseado em prompt para modo JSON ou schema
- **Schema-valid but factually wrong**: adicionar uma fase de validação de LLM-as-judge após a extracção
- **Inconsistent enum values**: mudar para decodificação restrita ou adicionar normalização pós-processamento
- **Missing optional fields**: fazer-os necessários ou adicionar valores padrão no código de aplicação
- **Very slow extraction**: decodificação limitada adiciona 5-15% de latência, reduz a complexidade do esquema se a latência é sensível
- **Large arrays with varied items**: despejar a entrada e extrair por pedaço, e depois fundir os resultados

## Escala de confiabilidade

| Approach | Parse Success | Schema Match | Setup Effort |
|----------|-------------|-------------|-------------|
| Prompt-based | ~90% | ~80% | 1 minute |
| JSON mode | 100% | ~90% | 5 minutes |
| Schema mode | 100% | ~99% | 15 minutes |
| Constrained decoding | 100% | 100% | 30 minutes |
| Instructor + retry | 100% | ~99.5% | 10 minutes |
