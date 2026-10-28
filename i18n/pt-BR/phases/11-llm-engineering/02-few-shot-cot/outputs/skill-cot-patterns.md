---
name: skill-cot-patterns
description: Quadro de decisão para a escolha da técnica de raciocínio correta com base na complexidade da tarefa, nos requisitos de precisão e nas restrições de custos
version: 1.0.0
phase: 11
lesson: 02
tags: [chain-of-thought, few-shot, self-consistency, tree-of-thought, react, reasoning, prompting]
---

# Guia de seleção de técnicas de raciocínio

Quando você precisa de um Mestrado em Direito para raciocinar um problema, escolha a técnica antes de escrever o pedido.

## Árvore de decisão rápida

1. A tarefa é uma simples pesquisa factual ou uma classificação em um único passo?
   - Sim: utilização **zero-shot**O CoT acrescenta custos sem ganho de precisão.
   - Não, continua.

2. A tarefa requer raciocínio em vários passos (matemática, lógica, planejamento)?
   - Sim: utilização **Chain-of-Thought**Continuem com o passo 3.
   - Não: utilização **few-shot** Se o formato importa, zero-shot se não.

3. É aceitável um único erro de raciocínio?
   - Sim: utilização **few-shot CoT** (uma única amostra, temperatura 0,0).
   - Não: utilização **self-consistency** (N=5, temperatura 0,7). Continuar para o passo 4.

4. O problema é um problema de busca/planejamento com muitos caminhos possíveis?
   - Sim: utilização **Tree-of-Thought**- Não .
   - Não: a autoconsistência é suficiente.

5. A tarefa requer informações externas ou cálculos?
   - Sim: utilização **ReAct** (razão + apelos a ferramentas).
   - Não: as técnicas de raciocínio puro são suficientes.

## Matriz Técnica

| Technique | Accuracy Lift | Cost Multiplier | Latency | Best For |
|-----------|--------------|-----------------|---------|----------|
| Zero-shot | Baseline | 1x | ~1s | Simple tasks, factual Q&A |
| Few-shot | +5-15% | 1.2x | ~1s | Format matching, classification |
| Zero-shot CoT | +10-20% | 1.3x | ~1.5s | Quick reasoning boost |
| Few-shot CoT | +15-25% | 1.5x | ~2s | Math, logic, multi-step |
| Self-Consistency (N=5) | +2-5% over CoT | 5x | ~5s | High-stakes reasoning |
| Self-Consistency (N=10) | +1-2% over N=5 | 10x | ~10s | Critical decisions only |
| Tree-of-Thought | Task-dependent | 10-40x | ~30s+ | Search, planning, puzzles |
| ReAct | Task-dependent | 3-10x | ~5-15s | Knowledge-grounded tasks |
| Prompt Chaining | +5-10% over single | 2-5x | ~5-10s | Complex multi-part tasks |

## Orientação específica para o modelo

### GPT-4o / GPT-4.1
- Raciocínio de base forte.
- CoT de pouca tiragem com 3 exemplos atinge 95% no GSM8K.
- A autoconsistência dá ganhos marginais (95% a 97%) - vale a pena apenas para tarefas críticas.
- Suporta saídas estruturadas nativas para extracção de respostas.

### Claude 3.5 Sonnet / Claude 3.7 Sonnet
- Excelente em seguir formatos de prompt estruturados (tags XML).
- CoT de poucas fotos com exemplos delimitados XML funciona melhor.
- O pensamento alargado (Cláusula 3.7) é a TCC nativa - não é necessário pedir-lhe.
- A autoconsistência é eficaz porque o raciocínio de Claude varia bem em temperatura de 0,7.

### Llama 3.1/3.3 70B
- Beneficia-se principalmente da CoT com poucas injeções (maior diferença de precisão versus zero injeções).
- Autoconsistência com N=5 recomendada para tarefas de raciocínio.
- Precisa de instruções de formato mais explícitas do que os modelos comerciais.
- A TTO é cara em inferência local - considera apenas para processamento em lote.

### Gemini 2.5 Pro
- Forte em raciocínio de vários passos fora da caixa.
- O modo de pensar fornece a CoT embutida sem engenharia rápida.
- Poucos exemplos ajudam a manter a consistência do formato mais do que a precisão.
- A janela de contexto grande (1M) torna prático o exemplo pesado de poucas fotos.

## Antipatrões

**CoT for simple tasks**O modelo obtém um direito aritmético simples sem raciocínio. CoT ajuda quando há 3 passos.

**Self-consistency at temperature 0.0**Para diferentes vias de raciocínio, deve-se utilizar a temperatura > 0 (0,5-0,8 recomendado).

**ToT for everything**A TOT requer chamadas de O (b^d) LLM onde b=factor de ramificação e d=profundidade. Uma árvore com b=3, d=3 requer até 39 chamadas. Reserva para problemas onde técnicas mais baratas falham.

**Few-shot with bad examples**A análise de dados de dados e de dados de dados é uma das principais funções da análise de dados.

**Extracting answers without a consistent format**A autoconsistência exige a comparação de respostas entre amostras. Se o formato da resposta varia ("$ 18, "$ 18, "$ 18, "$ 18"), a votação falha.

## Optimização dos custos

Para um sistema de produção que lida com 10 000 consultas/dia a preços GPT-4o ($2.50/1M input, $10/1M de produção):

| Technique | Avg Tokens/Query | Daily Cost | Accuracy |
|-----------|-----------------|------------|----------|
| Zero-shot | ~200 | ~$5 | 78% |
| Few-shot CoT | ~600 | ~$15 | 95% |
| Self-Consistency (N=5) | ~3,000 | ~$75 | 97% |
| ToT (b=3, d=2) | ~6,000 | ~$150 | Task-dependent |

A estratégia de custo-optimalidade para a maioria das aplicações: começar com CoT de poucas injeções. Adicionar autoconsistência apenas para consultas em que a confiança é baixa (o padrão de escalada da seção "Construir".

## Integração com a Encadeação Prometida

As técnicas de raciocínio compõem-se de uma cadeia rápida:

**Chain Step 1** (Extracto): zero-choque, temperatura 0,0
**Chain Step 2** (Reason): CoT de poucas injecções, temperatura 0,0
**Chain Step 3** (Verificar): autoconsistência com N=3, temperatura 0,7

Esta cadeia de três etapas custa ~ 3x uma única chamada de CoT, mas detecta erros de extração, erros de raciocínio e fornece uma pontuação de confiança a partir da etapa de verificação.

## Quando ir além da pressa

Se você está gastando mais tempo em instruções de engenharia do que na redacção de código de aplicação, considere:

1. **Fine-tuning**: se você tem 500 + exemplos rotulados e a tarefa é estreita
2. **DSPy compilation**: se você quiser otimização automática de prompt
3. **Agent frameworks**: se a tarefa requer utilização de ferramentas de várias voltas (fase 14)
4. **RAG**: se o modelo necessita de acesso a conhecimentos privados/currentes (Lessões 06-07)

As técnicas de promoção são a base. Eles trabalham com qualquer modelo, qualquer fornecedor, e não exigem dados de treinamento. Mas eles têm limites. Saber quando se formar para o próximo nível é tão importante quanto dominar as próprias técnicas.
