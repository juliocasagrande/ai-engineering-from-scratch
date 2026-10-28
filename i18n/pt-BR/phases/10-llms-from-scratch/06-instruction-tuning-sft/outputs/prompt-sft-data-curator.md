---
name: prompt-sft-data-curator
description: Concepção e instrução de curadoria de conjuntos de dados para ajustes finos supervisionados
version: 1.0.0
phase: 10
lesson: 6
tags: [sft, instruction-tuning, fine-tuning, data-curation, alignment]
---

# Curator de dados SFT

Ao projetar um conjunto de dados de ajuste de instruções para uma capacidade específica (geração de código, matemática, conversação, segurança), use esta estrutura para planejar a coleta de dados, definir critérios de qualidade e estruturar o pipeline de treinamento.

## Requisitos de entrada

Fornecer:
- **Target capability** (por exemplo, "Generação de código Python", "Q&A médica", "conversa de várias voltas")
- **Base model** (por exemplo, Llama 3 8B, Mistral 7B, Qwen 2.5 72B)
- **Budget** (horas de anotação, custos de API para a geração sintética)
- **Format preference** (Alpaca, ShareGPT, ChatML)

## Passo 1: Design de conjunto de dados

### Orientações de tamanho

| Quality Level | Examples Needed | Expected Outcome |
|--------------|----------------|------------------|
| Research prototype | 1,000-5,000 | LIMA-quality: comparable to larger datasets if examples are expert-written |
| Production v1 | 10,000-50,000 | Stanford Alpaca level: solid instruction following across common tasks |
| Production v2 | 50,000-200,000 | Vicuna/Llama 2 Chat level: robust multi-turn, domain coverage |

A qualidade sempre supera a quantidade. 1.000 exemplos escritos por especialistas (LIMA, maio 2023) combinaram modelos treinados em mais de 50.000 exemplos. Priorizar:

1. **Diversity** -- abranger toda a gama de capacidades-alvo
2. **Accuracy** - cada resposta deve ser factualmente correta
3. **Clarity** - as respostas devem ser concisas e bem estruturadas
4. **Difficulty gradient** - incluir exemplos fáceis, médios e difíceis

### Lista de verificação da diversidade

Para um assistente de finalidade geral:
- Perguntas abertas (20%)
- Perguntas e respostas factuais (20%)
- Escrita criativa (10%)
- Geração de código (15%)
- Raciocínio e matemática (15%)
- Resumo (10%)
- Instrução com restrições (10%)

Ajustar as percentagens para modelos específicos de domínio. Um assistente de codificação pode atribuir 60% à geração de código e 20% à explicação de código.

## Passo 2: Formatos de dados

### Formatos de Alpaca (turnado único)

```json
{
  "instruction": "Write a function that reverses a string in Python.",
  "input": "",
  "output": "def reverse_string(s):\n    return s[::-1]"
}
```

Utilização quando: tarefas de turno único, pares simples de instrução-resposta, prototipagem rápida.

### Formatos ShareGPT (múlti-turn)

```json
{
  "conversations": [
    {"from": "system", "value": "You are a Python expert."},
    {"from": "human", "value": "How do I reverse a string?"},
    {"from": "gpt", "value": "Use slicing: s[::-1]"},
    {"from": "human", "value": "What about for a list?"},
    {"from": "gpt", "value": "Same syntax works: my_list[::-1]"}
  ]
}
```

Utilize quando: aplicações de conversação, contexto de várias rotas é importante.

### Formatos de chatML (com tokens especiais)

```
<|im_start|>system
You are a Python expert.<|im_end|>
<|im_start|>user
How do I reverse a string?<|im_end|>
<|im_start|>assistant
Use slicing: s[::-1]<|im_end|>
```

Utilize quando: direcionar modelos que usam ChatML nativamente (Qwen, Yi).

## Passo 3: Critérios de qualidade

### Verificações por exemplo

1. **Response relevance**A resposta responde realmente à instrução?
2. **Factual accuracy**Todas as alegações são verificáveis e corretas?
3. **Completeness**A resposta responde plenamente à instrução?
4. **Conciseness**O mesmo poderão ser transmitidos com menos palavras?
5. **Format consistency**A resposta segue o estilo esperado?

### Banderas vermelhas (rejeitar o exemplo)

- A resposta contradiz-se a si mesma .
- A resposta inclui conteúdo prejudicial sem recusa
- Resposta alucina fatos ou citações
- As instruções são ambíguas e a resposta não esclarece
- Resposta é uma cópia da instrução reformulada

### Verificações de nível de conjunto de dados

- Não mais de 5% de exemplos de qualquer fonte/template
- Pelo menos 80% dos tokens de resposta são significativos (não preenchimento)
- A duração média da resposta é de 50 a 200 tokens (evite muito curto ou muito longo)
- Diversidade de instruções de sistema: representam-se pelo menos 10 instruções de sistema diferentes

## Passo 4: Configuração de treinamento

| Parameter | Recommended Range | Notes |
|-----------|------------------|-------|
| Learning rate | 1e-5 to 5e-5 | Lower for larger models (1e-5 for 70B, 5e-5 for 7B) |
| Epochs | 1-3 | Monitor validation loss, stop at first sign of increase |
| Batch size | 32-128 | Scale with gradient accumulation if GPU-limited |
| Warmup | 0-5% of steps | Less critical than pre-training |
| Weight decay | 0.0-0.1 | Optional for short fine-tuning runs |
| Loss masking | Response tokens only | Mask instruction and system prompt tokens |
| Pre-training data mixing | 2-5% | Mix raw text to prevent catastrophic forgetting |

## Passo 5: Protocolo de Avaliação

Após a formação, avaliar:

1. **Instruction following rate**: Percentagem de instruções de ensaio em que o modelo produz uma resposta relevante e completa
2. **Forgetting score**: Perplexidade sobre um corpus de texto geral prolongado em comparação com o modelo base
3. **Format compliance**: Percentagem de respostas que seguem o formato de chat esperado
4. **MT-Bench or AlpacaEval**: Referências padrão para modelos ajustados para instruções
5. **Domain-specific eval**: Avaliação personalizada para a sua capacidade de alvo

### Sinais de alerta

- A perda de validação aumenta após a primeira época: você está sobre-ajustado, reduzir as épocas ou aumentar os dados
- Aumento da pontuação de esquecimento > 15%: taxa de aprendizagem muito alta ou muitas épocas
- O modelo reproduz exemplos de formação literalmente: sobreajuste grave, necessidades de dados mais diversos
- Modelo recusa instruções benignas: sobre-treinamento em dados de segurança, reequilíbrio do conjunto de dados
