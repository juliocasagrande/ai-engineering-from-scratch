---
name: prompt-distributed-training-planner
description: Plan a distributed training run given model size and available hardware
version: 1.0.0
phase: 10
lesson: 5
tags: [distributed-training, fsdp, deepspeed, tensor-parallelism, pipeline-parallelism, scaling]
---

# Planeador de Formação Distribuído

Ao planejar uma formação distribuída para um modelo de linguagem grande, use esta estrutura para determinar a estratégia de paralelismo, o orçamento de memória, a despesa geral de comunicação e o rendimento esperado.

## Requisitos de entrada

Fornecer:
- **Model size**(parâmetros em bilhões)
- **Target training tokens**(em trilhões)
- **Available GPUs**(tipo: A100/H100/H200, contagem, interconexão: NVLink/InfiniBand)
- **GPU memory**(80 GB para A100/H100, 141 GB para H200)
- **Nodes**(GPUs por nó, número de nós)
- **Budget constraints**(Costo máximo em dólares, tempo máximo de relógio de parede)

## Passo 1: Orçamento de memória

Calcular a memória por GPU para cada componente:

| Component | Formula | FP16 | FP32 |
|-----------|---------|------|------|
| Weights | params x bytes_per_param | params x 2 | params x 4 |
| Adam optimizer (m + v) | params x 4 x 2 | 8 bytes/param always | 8 bytes/param |
| Gradients | params x bytes_per_param | params x 2 | params x 4 |
| Activations (estimate) | seq_len x batch x hidden x layers x 2 | varies | varies |

Se o total exceder a memória da GPU, é necessário fazer um sharding.
1. ZeRO-1 (apenas otimizador de fragmentos) - comunicação mais barata
2. ZeRO-2 (+ gradientes) -- comunicação moderada
3. FSDP/ZeRO-3 (+ pesos) - maior comunicação mas poupança máxima de memória
4. Adicionar o ponto de verificação de ativação se as ativações ainda forem grandes demais
5. Adicionar paralelismo tensor se uma única camada não se encaixa em uma GPU

## Passo 2: Estratégia paralela

### Árvore de decisão

1. **Does one layer fit on one GPU?**
   - Não: Você precisa de paralelismo tensor.
   - Sim, pular o paralelismo tensorial.

2. **Does the full model (with sharding) fit on GPUs within one node?**
   - Não: Você precisa de paralelismo de pipeline.
   - Sim: Salta o paralelismo do oleoduto.

3. **How many remaining GPUs for data parallelism?**
   - DP = total_gpus / (TP x PP)

4. **What sharding level within the data parallel group?**
   - Comece com o FSDP (ZeRO-3). Reduzir para ZeRO-2 ou ZeRO-1 se a comunicação for um gargalo de engarrafamento.

### Configurações típicas

| Model Size | Total GPUs | TP | PP | DP | Sharding |
|-----------|-----------|----|----|-----|----------|
| 7B | 8 | 1 | 1 | 8 | FSDP |
| 13B | 16 | 2 | 1 | 8 | FSDP |
| 70B | 64 | 8 | 1 | 8 | FSDP |
| 70B | 128 | 8 | 2 | 8 | FSDP |
| 405B | 16,384 | 8 | 16 | 128 | FSDP |

## Passo 3: Análise da comunicação

Estimar o volume de comunicação por etapa de formação:

- **Data parallel (all-reduce)**: 2 x gradiente_ tamanho x (N-1)/N por etapa
- **FSDP (all-gather + reduce-scatter)**: ~3 x peso_ tamanho x (N-1) / N por etapa (mais alta que DP)
- **Tensor parallel (all-reduce per layer)**: 2 x tamanho de ativação x número de camadas por etapa (necessidade NVLink)
- **Pipeline parallel (point-to-point)**: activation_size por limite de estágio (minimal)

Se o tempo de comunicação exceder 20% do tempo de computação, a estratégia é vinculada à comunicação.
- Acumulação gradual (redução de frequência total)
- Comunicação sobreposição com computação (FSDP faz isso por padrão)
- Aumentar o tamanho do micro-batch (melhor relação entre computação e comunicação)
- Passe para uma fase de fragmentação menos pesada para comunicação

## Passo 4: Estimar o volume e o custo

**FLOPS per training step:**
- Para frente: ~ 2 x params x tokens_per_batch
- Para trás: ~ 4 x params x tokens_per_batch (2x para frente)
- Total: ~ 6 x params x tokens_per_batch

**Training time:**
- total_flops = 6 x params x total_tokens
- tempo_segundos = total_flops / (número_gpus x gpu_tflops x 1e12 x utilização)
- Utilização típica: 35-45% (contabilidade de comunicações, bolhas de pipeline, despesas gerais de memória)

**Cost:**
- total_gpu_hours = num_gpus x tempo_segundos / 3600
- custo = total_gpu_hora x custo_por_gpu_hora

## Passo 5: Lista de verificação de validação

Antes do lançamento:

1. Memória por GPU cabe dentro do limite de hardware (com 10% de espaço de cabeça)
2. Dimensões de lote efetivas correspondem ao objetivo (por lote x DP x gradiente_acumulação_pasos)
3. A relação comunicação-computação é inferior a 20%
4. A fração de bolhas de oleodutos é inferior a 15% (micro-partidas suficientes)
5. A taxa de aprendizagem é dimensionada para o tamanho do lote efetivo
6. A frequência de checkpointing contabiliza a probabilidade de falha (salvo a cada 1-2 horas para grandes corridas)
7. O corte de gradiente é definido (normalmente 1,0 para modelos grandes)
8. Os passos de aquecimento são proporcionais ao total dos passos (normalmente 0,1-1% do total)

## Banderas vermelhas

- **TP > 8**: O paralelismo tensor entre nós (em InfiniBand) é quase sempre mais lento do que o paralelismo de pipeline
- **Pipeline stages > 32**: A carga de burbujas torna-se significativa mesmo com muitos micro-batches
- **Effective batch size > 10M tokens**: Redução dos rendimentos; pode prejudicar a convergência
- **Utilization below 30%**: Comunicação vinculada - reavaliação da estratégia de paralelismo
- **No activation checkpointing above 13B**Você vai ficar sem memória durante o passe para trás
- **No gradient accumulation with small per-GPU batch**: Aumento do ruído gradual; acumulação de 256+ amostras em lote efetivo
