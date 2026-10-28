---
name: prompt-gpt-architecture-analyzer
description: Analyze architecture choices in any GPT-style transformer model
version: 1.0.0
phase: 10
lesson: 4
tags: [gpt, transformer, architecture, attention, kv-cache, scaling, pre-training]
---

# Analista de Arquitetura GPT

Ao avaliar um modelo de estilo GPT a partir de um relatório técnico, cartão de modelo ou registro de treinamento, use este quadro para desglosar a arquitetura e identificar as compensações de design.

## Protocolo de análise

### 1. Desagregação de atribuição de parâmetros

Calcule o número exato de parâmetros para cada componente:

- **Token embeddings**: vocab_size x embed_dim
- **Position embeddings**: max_seq_len x embed_dim
- **Per-block attention**: 4 x embed_dim x embed_dim (Q, K, V, projeções de saída)
- **Per-block FFN**: 2 x embed_dim x ff_dim + embed_dim + ff_dim (dois camadas lineares + preconceitos)
- **Per-block LayerNorm**: 4 x embed_dim (dois normas, cada uma com escala + viés)
- **Final LayerNorm**: 2 x embed_dim
- **Output head**: vocab_size x embed_dim (ou 0 se ligado por peso com embeddings de token)

A bandeira se qualquer componente exceder 40% dos parâmetros totais. A matriz de incorporação domina nos modelos pequenos.

### 2. Análise de Design de Atenção

Avaliação da configuração da atenção:

- **Head dimension**A norma é 64 (GPT-2) ou 128 (Llama 3). abaixo de 32 limites de expressão por cabeça. acima de 128 resíduos computação com pouco benefício.
- **Heads per layer**: Mais cabeças = padrões de atenção mais diversos mas mais memória para cache KV.
- **Grouped Query Attention (GQA)**O modelo compartilha cabeças K/V em várias cabeças Q? Llama 3 usa GQA com 8 cabeças KV para 32 cabeças Q. Isso reduz o cache KV em 4x.
- **Context length**A RoPE permite extrapolação além do tempo de treino.

### 3. Orçamento de memória

Para a inferência no comprimento máximo de contexto do modelo:

- **Weights (FP16)**: total_params x 2 bytes
- **KV Cache (FP16)**: 2 x num_layers x num_kv_heads x head_dim x max_seq_len x 2 bytes
- **Activations**: batch_size x seq_len x embed_dim x 2 bytes x num_layers (aproximado)

Flag se o cache KV excede a memória de peso. Isso acontece para modelos de contexto longo (128K +) e indica que o modelo está ligado à memória durante a decodificação.

### 4. Perfil de computação

- **Prefill FLOPS per token**: aproximadamente 2 x total_params (um matmul por parâmetro, passagem para a frente)
- **Decode FLOPS per token**: igual ao prefill mas com um único token
- **Prefill bottleneck**: computação ligada (GPU TFLOPS)
- **Decode bottleneck**: com memória limitada (GPU memória largura de banda)
- **Arithmetic intensity**FLOPS por byte de memória acessada. abaixo de 100 = memória limitada.

### 5. Decisoes de Escalada

Avaliação em relação às leis conhecidas de escalagem:

- **Chinchilla optimal**Para um determinado orçamento de computação C, o tamanho ideal do modelo N e a contagem de tokens D satisfazem N ~ D (escalação aproximadamente igual).
- **Llama 3 overtrained**Meta treinado Llama 3 8B em tokens 15T (100x Chinchilla ideal).
- **Width vs depth**: Os modelos mais profundos (mais camadas) são geralmente mais eficientes em relação às amostras do que os modelos mais largos (embed_dim maior) para a mesma contagem de parâmetros.

## Banderas vermelhas

- **FFN ratio not 4x**O Llama usa 8/3 x embed_dim com SwiGLU. Os desvios devem ser justificados.
- **No weight tying**: A cabeçalha de saída deve compartilhar pesos com embeddings de token, a menos que o vocab_size seja muito grande em relação ao embed_dim.
- **No GQA above 13B**: Os modelos acima de 13B sem atenção de consulta agrupada terão caches de KV excessivamente grandes.
- **No RoPE for long context**Os modelos que visam um contexto de 32K+ devem utilizar embutidos rotativos.
- **Learning rate too high for model size**Os modelos maiores precisam de taxas de aprendizagem mais baixas. GPT-2 Small usa 6e-4. Llama 3 405B usa 8e-5.

## Formatos de saída

1. **Parameter Table**: Parâmetro componente por componente contado com percentagens
2. **Memory Budget**: pesos, cache KV e memória de ativação no comprimento máximo do contexto
3. **Compute Profile**: estimativas de preenchimento e decodificação do volume de produção para A100/H100
4. **Design Assessment**O modelo é o que é certo e o que não é padrão
5. **Scaling Verdict**: se o modelo tem um tamanho adequado para os dados de formação
