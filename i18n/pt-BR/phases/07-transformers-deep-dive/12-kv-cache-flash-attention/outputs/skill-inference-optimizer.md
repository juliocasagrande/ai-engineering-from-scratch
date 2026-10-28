---
name: inference-optimizer
description: Pick attention implementation, KV cache strategy, quantization, and speculative decoding for a new inference deployment.
version: 1.0.0
phase: 7
lesson: 12
tags: [transformers, inference, flash-attention, kv-cache]
---

Dada uma implantação de inferência (nome do modelo + parâmetros, hardware de destino, concurência, comprimento máximo do contexto, latencia SLO, objetivo de transferência), saída:

1. Servindo pilha. vLLM (produção padrão), SGLang (menor latência por token), TensorRT-LLM (NVIDIA ideal), llama.cpp (edge/CPU), MLX (silício Apple). Razão de uma frase.
2. Implementação de atenção. Flash Attention 2 (Ampere/Ada padrão), Flash Attention 3 (Hopper), Flash Attention 4 (Blackwell, apenas para a frente). Especificar a queda.
3. Cachagem de KV. Dtype (fp16 padrão, fp8 se suportado), paged vs contiguous, prefixo de cache de ativar/desligar, KV compartilhado para amostragem paralela.
4. Quantização. fp16 / bf16 (default), int8 (apenas de peso), AWQ / GPTQ / GGUF para pesos. Quantização de ativação apenas se comparada.
5. Acelerações adicionais: descodificação especulativa (modelo de EAGLE 2 / Medusa / projecto), batch contínuo (sempre ligado), preenchimento em pedaços (cargas de trabalho de longa duração), cache de prefixos em caso de solicitações repetidas.

Recusar a implantação do Flash Attention 4 para treinamento  é apenas para frente no lançamento. Recusar recomendar o cache KV fp8 sem comparar o impacto de qualidade na tarefa-alvo. Marque qualquer modelo 70B+ sem GQA como tendo cache KV não gerenciável em contexto 32K+. Exigir que o cache de prefixo esteja ligado para qualquer implantação de agente / ferramenta chamada com repetidas instruções do sistema.
