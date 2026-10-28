---
name: skill-quantization
description: Escolha a estratégia de quantização certa para a implantação de LLM com base em restrições de hardware, qualidade e latência
version: 1.0.0
phase: 10
lesson: 11
tags: [quantization, inference, deployment, optimization, fp8, int4, int8, gptq, awq, gguf]
---

# Quadro de decisão de quantização

Ao implementar um modelo de linguagem, use esta estrutura para selecionar o formato de número certo, método de quantização e estratégia de validação de qualidade.

## Requisitos de entrada

Fornecer:
- **Model** (nome, número de parâmetros, precisão original)
- **Target hardware** (modelo GPU/VRAM, CPU, Apple Silicon, dispositivo de borda)
- **Latency target** (tokens/segundo, tempo para o primeiro token)
- **Quality floor** (aumento máximo de perplexidade aceitável, delta do índice de referência)
- **Serving pattern** ( tamanho do lote, comprimento máximo do contexto, usuários simultâneos)

## Seleção rápida

| Your Situation | Format | Method | Expected Quality Loss |
|---------------|--------|--------|----------------------|
| H100 GPU, maximum throughput | FP8 E4M3 | Native H100 casting | < 0.1% |
| A100/A10, need 2x throughput | INT8 | LLM.int8() or SmoothQuant | < 0.5% |
| Single 24GB GPU, 70B model | INT4 | AWQ or GPTQ | 1-3% |
| MacBook / Apple Silicon | INT4 GGUF | Q4_K_M via llama.cpp | 1-2% |
| Mobile / edge device | INT4 or INT3 | QAT + device-specific | 2-5% |
| Maximum compression, some loss OK | INT2 | QuIP# or AQLM | 5-15% |
| Training (mixed precision) | BF16 + FP32 accum | Native framework support | 0% |

## Seleção de precisão por componente

Nem todos os tensores devem receber o mesmo tratamento.

| Component | Safe Minimum | Recommended | Avoid |
|-----------|-------------|-------------|-------|
| FFN weights | INT4 | INT4 (AWQ/GPTQ) | INT2 without QAT |
| Attention weights | INT4 | INT8 or FP8 | INT2 |
| Embedding layer | INT8 | FP16 (keep original) | INT4 |
| Output head | INT8 | FP16 (keep original) | INT4 |
| KV cache | FP8 | FP8 or INT8 | INT4 at long context |
| Attention logits | FP16 | FP16 or BF16 | INT8 |
| Activations (inference) | INT8 | FP8 or INT8 | INT4 |

## Comparação de Métodos

### GPTQ
- **When:** Inferência da GPU, queres um modelo compatível com o Face Hugging
- **Calibration data:** 128 exemplos, 2048 tokens cada
- **Time:** 30 a 60 minutos para 70B na A100
- **Tooling:** `gptqmodel`- Não . `exllama`- Não . `exllamav2`
- **Strength:** Um zoológico modelo enorme bem testado em Hugging Face
- **Weakness:** Aplicação mais lenta do que a AWQ, de qualidade ligeiramente inferior à AWQ em alguns modelos

### AQ
- **When:** Inferência de GPU, você quer a melhor qualidade por bit
- **Calibration data:** 128 exemplos
- **Time:** 15-30 minutos para 70B na A100
- **Tooling:** `llmcompressor`- Não . `vLLM` (apoio nativo)
- **Strength:** Melhor qualidade INT4, rápida aplicação, integração vLLM
- **Weakness:** Zoológico modelo menor do que o GPTQ

### GGUF
- **When:** Inferência de CPU, Apple Silicon, ecossistema llama.cpp
- **Variants:** A posição de referência do ponto 1 do artigo 5.o do Regulamento (UE) n.o 1095/2013 é a seguinte:
- **Recommended default:** Q4_K_M (melhor equilíbrio entre qualidade e tamanho)
- **Tooling:** `llama.cpp`- Não . `ollama`- Não . `LM Studio`
- **Strength:** Arquivos independentes, precisão mista, ecossistema maciço
- **Weakness:** Não óptimo para GPU (projetado para CPU/Metal)

### SmoothQuant
- **When:** INT8 na GPU, precisa de quantização de peso e ativação
- **Key idea:** Migração de dificuldade de quantização das ativações para pesos através de escalação por canal
- **Tooling:** `smoothquant`- Não . `TensorRT-LLM`
- **Strength:** Abilita o W8A8 (peso e ativação no INT8) para aceleração de 2x
- **Weakness:** Apenas INT8, não se estende ao INT4

## Protocolo de validação da qualidade

Após quantização, valida antes de implantar:

1. **Perplexity test.** Compute no WikiText-2 ou no seu corpus de domínio. Delta < 0,5 é excelente, 0,5-1,0 é bom, > 2,0 é um problema.

2. **Benchmark sweep.** Execute MMLU (general), GSM8K (matemática), HumanEval (código).

3. **Output comparison.** Gerar 100 respostas a partir de modelos originais e quantizados. Usar LLM-as-judge para calcular a taxa de vitória.

4. **Latency measurement.** Messa-se os tokens/segundo no tamanho do lote 1 e no tamanho do lote-alvo. Verifique se a aceleração justifica o custo da qualidade.

5. **Long-context test.** Se servir contextos longos (> tokens 4K), teste no seu comprimento máximo de contexto.

## Calculador de orçamento de memória

```
Weight memory (GB) = parameters (B) * bits / 8 / 1.073741824
KV cache per token (MB) = 2 * num_layers * d_model * bits / 8 / 1048576
KV cache for context (GB) = kv_per_token * max_context_length / 1024
Activation memory (GB) ~ 1-4 GB (relatively constant, depends on batch size)
Total = weight_memory + kv_cache + activation_memory + overhead (10-20%)
```

Exemplo para Llama 3 70B no contexto INT4, 32K:
- Peso: 70B * 4 / 8 / 1,07 = 32,6 GB
- KV cache (FP16): 2 * 80 * 8192 * 16 / 8 / 1e9 * 32768 = ~ 40 GB
- Caches de KV (FP8): ~20 GB
- Total com FP8 KV: ~55 GB (corrige um A100 de 80 GB)

## Erros comuns

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| Quantizing the embedding layer to INT4 | First layer amplifies errors through entire model | Keep embeddings at FP16 or INT8 |
| Using per-tensor scales for INT4 | One outlier row destroys precision for all rows | Use per-channel or per-group scales |
| Not calibrating GPTQ/AWQ | Scale factors are wrong without representative data | Use 128 examples from your domain |
| Same bit-width for all layers | First/last layers are more sensitive | Mixed precision: higher bits for first/last |
| Quantizing KV cache at very long context | Errors compound quadratically with sequence length | Use FP8 for KV cache, not INT4 |
| Skipping quality validation | Some models quantize poorly (especially at boundaries) | Always run perplexity + task evals |

## Recetas de implantação

### Recepta 1: VLLM com AWQ (servidor de GPU)
```
pip install vllm
vllm serve model-awq --quantization awq --dtype half --max-model-len 8192
```

### Recepta 2: llama.cpp com GGUF (MacBook)
```
./llama-server -m model.Q4_K_M.gguf -c 4096 -ngl 99
```

### Recepta 3: TensorRT-LLM com FP8 (H100)
```
trtllm-build --model_dir model --output_dir engine --dtype float16 --use_fp8
```
