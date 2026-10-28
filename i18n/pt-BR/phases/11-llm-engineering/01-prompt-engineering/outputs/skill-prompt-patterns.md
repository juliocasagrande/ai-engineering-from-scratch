---
name: skill-prompt-patterns
description: Quadro de decisão para a escolha do modelo de solicitação adequado com base no tipo de tarefa, nos requisitos de confiabilidade e no modelo-alvo
version: 1.0.0
phase: 11
lesson: 01
tags: [prompt-engineering, patterns, llm, temperature, cross-model, few-shot, chain-of-thought]
---

# Guia de seleção de padrões

Quando você constrói um recurso de LLM, escolha o seu padrão de prompt antes de escrever o prompt. O padrão determina a estrutura. O conteúdo enche-o.

## Matriz de decisão de padrão

| Task Type | Primary Pattern | Secondary Pattern | Temperature | Few-Shot Needed? |
|-----------|----------------|-------------------|-------------|-----------------|
| Data extraction | Template Fill | Few-Shot | 0.0 | Yes (2-3 examples) |
| Classification | Few-Shot | Guardrail | 0.0 | Yes (3-5 examples) |
| Summarization | Persona + Template | Audience Adapt | 0.3 | No |
| Code generation | Persona | Chain-of-Thought | 0.0 | Optional |
| Creative writing | Persona | Critique | 0.7-1.0 | No |
| Multi-step reasoning | Chain-of-Thought | Decomposition | 0.3 | Optional |
| Question answering | Persona + Guardrail | Boundary | 0.3 | No |
| Prompt generation | Meta-Prompt | Critique | 0.7 | Yes (1-2 examples) |
| Content moderation | Guardrail + Boundary | Few-Shot | 0.0 | Yes (5+ examples) |
| Translation/adaptation | Audience Adapt | Few-Shot | 0.3 | Yes (2-3 examples) |

## Quando usar cada padrão

**Persona Pattern**Para as tarefas genéricas, um papel amplo é suficiente. Para tarefas específicas de domínio, o papel deve nomear o domínio, nível de antiguidade e contexto.

**Few-Shot Pattern**O modelo precisa produzir uma forma específica de JSON, formato CSV ou etiqueta de classificação, os exemplos são mais eficazes do que as instruções. Regra geral: 2-3 exemplos para formatos simples, 5+ para formatos complexos ou ambíguos.

**Chain-of-Thought Pattern**A utilização de dados para análise matemática, lógica, análise em várias etapas e qualquer tarefa em que o modelo precisa "mostrar seu trabalho". Melhora a precisão em 10-40% nas tarefas de raciocínio (Wei et al., 2022).

**Template Fill Pattern**A melhor forma de funcionar é com temperatura=0,0 e manipulação explícita "N/A" para campos faltantes.

**Critique Pattern**O modelo gera, critica e melhora. Aumente o custo dos tokens, mas melhora significativamente a precisão e a integridade. É ideal para resultados de alto risco (relatórios, recomendações, conteúdo público).

**Guardrail Pattern**Sempre incluir: limites de alcance, comportamento de recusa para solicitações fora do alcance e manejo explícito de "não sei". Combine com validação de entrada no lado da aplicação.

**Meta-Prompt Pattern**Em vez de escrever um prompt a partir do zero, descreva a tarefa e deixe o modelo escrever o prompt.

**Decomposition Pattern**O modelo divide o problema em partes, resolve cada uma e combina. É mais eficaz para tarefas com 3-7 subproblemas.

**Audience Adaptation Pattern**Especifique o público explicitamente - não dependa do modelo adivinhando a partir do contexto.

**Boundary Pattern**A utilização de sistemas de produção que NUNCA devem responder a certos tipos de perguntas.

## Compatibilidade entre modelos

Padrões classificados por quão consistentemente eles funcionam em GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro e Llama 3:

| Pattern | Cross-Model Consistency | Notes |
|---------|------------------------|-------|
| Few-Shot | Very high | Examples transfer well across all models |
| Template Fill | Very high | Explicit structure leaves little room for divergence |
| Chain-of-Thought | High | All major models support "think step by step" |
| Persona | High | Works everywhere but different models respond to different role specificity levels |
| Guardrail | Moderate | Claude follows guardrails most strictly; GPT-4o sometimes drifts in long conversations |
| Critique | Moderate | Quality of self-critique varies significantly by model |
| Meta-Prompt | Moderate | GPT-4o and Claude produce different prompt styles |
| Boundary | Low-Moderate | Refusal behavior varies; test per model |

## Erros comuns

1. **Using Chain-of-Thought for everything**CoT adiciona tokens e latência.
2. **Too many constraints**O modelo começa a deixar cair algumas restrições.
3. **Contradictory persona + constraints**: "Você é um escritor criativo" + "Nunca use metáforas" confunde o modelo.
4. **No temperature specification**A temperatura é de acordo com o padrão (geralmente 1,0) quando é necessária uma saída determinista.
5. **Copy-pasting prompts across models**Uma resposta com sintonia para o GPT-4o pode ter um desempenho inferior no Claude e vice-versa.
6. **Ignoring system message**: colocar tudo na mensagem do utilizador em vez de usar a mensagem do sistema para regras persistentes.
7. **Over-relying on negative constraints**: "Não faça X, Y, Z, A, B, C" é menos eficaz do que "SÓ faça W".

## Objetivos de confiabilidade

| Use Case | Pattern Combination | Expected Accuracy | Token Cost |
|----------|-------------------|-------------------|------------|
| Production extraction | Template + Few-Shot | 95%+ | Low (500-1K) |
| User-facing Q&A | Persona + Guardrail + Boundary | 90%+ | Medium (1-2K) |
| Code generation | Persona + Chain-of-Thought | 85%+ | Medium (1-3K) |
| Content generation | Persona + Critique | 90%+ quality | High (2-4K, double pass) |
| Classification | Few-Shot + Guardrail | 95%+ | Low (300-800) |
| Complex analysis | Decomposition + Chain-of-Thought | 85%+ | High (3-5K) |
