---
name: skill-inference-optimization
description: Diagnóstico e otimização da inferência LLM servindo o rendimento, a latência e o custo
version: 1.0.0
phase: 10
lesson: 12
tags: [inference, kv-cache, batching, speculative-decoding, vllm, optimization]
---

# Mestrado em Optimização da Inferência LLM

Duas fases: preenchimento (computado, paralelo) e decodificação (memória, sequencial).
Cada otimização visa uma ou ambas.

```
Request -> Prefill (process prompt) -> Decode (generate tokens) -> Response
              |                            |
         Compute-bound               Memory-bound
         Optimize: fusion,           Optimize: batching,
         prefix caching              quantization, speculation
```

## Quadro de decisão

### Passo 1: Identifique o seu gargalo de garrafa

Messa a relação ops:byte para a sua carga de trabalho:

| ops:byte | Bound | What to optimize |
|----------|-------|-----------------|
| < 50 | Memory | Quantize KV cache, increase batch size |
| 50-200 | Transitional | Both matter, start with batching |
| > 200 | Compute | Kernel fusion, tensor parallelism, FP8 |

### Passo 2: Escolha o motor

- **Default**: vLLM (suporte de modelo mais amplo, PagedAttention, API compatível com OpenAI)
- **Multi-turn / structured output**: SGLang (Cachagem de préfixos RadicAttention, decodificação restrita)
- **Max NVIDIA throughput**: TensorRT-LLM (fusão do núcleo, FP8 em H100)

### Passo 3: Aplique as otimizações em ordem

1. **KV cache** - Sempre a favor, sem desvantagens.
2. **Continuous batching** - sempre ligado, sem desvantagem (vLLM/SGLang fazer isso por padrão)
3. **Prefix caching** -- ativar se você tem compartilhado system prompts (a maioria dos chatbots fazem)
4. **Quantization** -- KV cache INT8/FP8 reduz a memória 2-4x com perda de qualidade mínima
5. **Speculative decoding** -- adicionar quando a latência importa mais do que o rendimento
6. **Tensor parallelism** -- dividido em GPUs quando o modelo não cabe em um

## Fórmula de memória cache KV

```
per_token = 2 * num_layers * num_kv_heads * head_dim * bytes_per_param
total = per_token * sequence_length * num_concurrent_users
```

Referência rápida para os modelos comuns (BF16):

| Model | Per token | 100 users @ 4K |
|-------|-----------|----------------|
| Llama 3 8B | 32 KB | 12.5 GB |
| Llama 3 70B | 320 KB | 125 GB |
| Llama 3 405B | 504 KB | 197 GB |

## Lista de verificação de descodificação especulativa

- O modelo de projeto deve ser de 5 a 10 vezes menor do que o objetivo (por exemplo, os projeto 8B para 70B)
- Taxa de aceitação > 70% para acelerar significativamente
- Melhor em texto previsível (código, saída estruturada, linguagem natural)
- Pior em tarefas criativas/sampulantes pesadas (a baixa temperatura ajuda)
- AEGLE > projecto-alvo > n-gram para a maioria das cargas de trabalho

## Erros comuns

- Descódigo em execução em batch=1 (memória limitada, GPU 95% ociosa em computação)
- Alocação de blocos de cache KV contíguos (utilizar PagedAttention, obter resíduos quase zero)
- Ignorar o caching de prefixos quando 80% das solicitações compartilham o mesmo pedido do sistema
- Super-provisionamento de memória GPU para pesos do modelo, deixando nada para cache KV
- Medir o rendimento sem medir a latência (altos rendimentos em 10s TTFT é inútil)
- Utilização de descodificação especulativa com alta temperatura (taxa de aceitação cai abaixo de 50%)

## Lista de controlo de controlo

- Tempo para primeiro token (TTFT): latência de preenchimento, meta < 500ms para uso interativo
- Latência entre tokens (ITL): velocidade de decodificação, meta < 50ms para streaming
- Transmissão (tokens/segundo): total de todos os utilizadores simultâneos
- Utilização do cache KV: percentagem do cache atribuído em uso
- Utilização de lote: percentagem de espaços de lote preenchidos por iteração
- Profundidade da fila: pedidos à espera de um espaço de lote
