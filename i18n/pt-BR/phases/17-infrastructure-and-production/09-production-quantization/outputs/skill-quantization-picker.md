---
name: quantization-picker
description: Escolha um formato de quantização 2026 dado hardware, motor, carga de trabalho e tolerância de qualidade, e produz um plano de calibração + validação.
version: 1.0.0
phase: 17
lesson: 09
tags: [quantization, awq, gptq, gguf, fp8, nvfp4, calibration]
---

Dado o hardware (CPU / H100 / H200 / B200 / GB200, com contagem), motor (llama.cpp / vLLM / TRT-LLM / SGLang), modelo ( tamanho + tipo de tarefa  chat rotineiro / raciocínio / código / multi-LoRA), e tolerância de qualidade (pode absorver queda de N-points em HumanEval / MATH / MMLU), escolha um formato de quantização e produz um plano de validação.

Produzir:

1. Uma das recomendações é: GGUF Q4_K_M, GGUF Q5_K_M, GPTQ-Int4 + Marlin, AWQ-Int4 + Marlin, FP8, NVFP4 + FP8 KV, ou uma combinação empilhada. Justifique pela árvore de decisão: CPU → GGUF; raciocínio → FP8; multi-LoRA em vLLM → GPTQ; chat de rotina de GPU → AWQ; Blackwell validado → NVFP4.
2. Prestação de memória. Relata pesos + cache KV (em simultânea relatada × contexto) + ativações. Confirme que se encaixa na GPU alvo ou invoque o requisito de multi-GPU.
3. Plano de calibração. Fonte do conjunto de dados (domínio-compatível para AWQ/GPTQ; C4/WikiText genérico como último recurso). Contagem de amostras (500-2000 para domínio). Conjunto de validação (10% retirado do pool de calibração).
4. Plano de validação. conjunto de Eval combinado com a tarefa: HumanEval para código, MATH/MMLU para raciocínio, MT-Bench para chat. linha de base BF16 vs quantizada. Envio se cair ≤ tolerância de qualidade.
5. A decisão de cache de KV. Separar da quantização de peso. Recomendar FP8 KV para raciocínio; BF16 KV se a precisão da atenção for marginal; INT8 KV apenas após validação.
6. Mantenha os pesos BF16/FP8 no disco; bandeira para voltar se a qualidade da produção se degradar.

Rejeitos duros:
- Recomendação de pesos NVFP4 em cargas de trabalho pesadas sem validação do conjunto de avaliação.
- Calibração em dados web genéricos para modelos de domínio.
- Esquecer o cache do KV no orçamento da HBM.
- Reclamar números de transmissão sem nomear os kernels (Marlin-AWQ vs AWQ simples é 10x).

Regras de recusa:
- Se a carga de trabalho for inerentemente marginais de qualidade (geração criativa aberta, raciocínio de extremo), rejeite a INT4 agressiva.
- Se o motor for llama.cpp, recuse qualquer formato que não seja o GGUF. O formato correspondente ao motor é a mesa de apostas.
- Se o usuário não conseguir executar uma avaliação de 1.000 amostras, recuse.

Resultado: uma lista de escolha de quantização de uma página, que indica o formato escolhido, o orçamento HBM, o plano de calibração, o plano de validação, a decisão do cache KV e o caminho de regresso.
