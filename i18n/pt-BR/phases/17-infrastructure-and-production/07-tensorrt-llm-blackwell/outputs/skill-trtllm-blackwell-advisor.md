---
name: trtllm-blackwell-advisor
description: Decide whether Blackwell + TensorRT-LLM + Dynamo is worth the NVIDIA-lock for a given workload and budget.
version: 1.0.0
phase: 17
lesson: 07
tags: [tensorrt-llm, blackwell, b200, gb200, nvfp4, fp8, dynamo]
---

Dada a carga de trabalho ( tamanho do modelo, parâmetros ativos, volume anual de tokens, sensibilidade à qualidade  raciocínio-pesado ou rotina), infra-estrutura atual (GPU H100/H200/B200, motor de servidão), e orçamento, produz um Blackwell + TRT-LLM de migração de aconselhamento.

Produzir:

1. Base de dados atual. Calcule tokens atuais de US $/M e gastos anuais a partir do volume relatado e do preço por hora de GPU.
2. Meta stack. Recomenda mistura de precisão exata (pesos: NVFP4 ou FP8; cache KV: FP8; ativações: NVFP4; acumulador: FP32). Para cargas de trabalho pesadas, recomenda pesos FP8 primeiro, NVFP4 apenas após calibração por bloco validada no conjunto de avaliação.
3. A partir da forma de custo de 2026: H100 + VLLM ~$0.09/M → B200 + TRT-LLM ~$0,02/M → GB200 NVL72 + Dynamo ~ $0,012/M. Projeto de poupança anual para o volume de tokens da carga de trabalho.
4. Custo de migração. Tempo de engenharia (10-30 semanas de engenharia para a primeira migração).
5. O período de produção necessário para amortizar a migração.
6. Riscão de bloqueio. TRT-LLM é apenas para NVIDIA. Nomear duas estratégias de saída (pilha dupla com vLLM no H100 para nível de iteração; manter pesos exportáveis para GGUF / HF para portabilidade para não-NVIDIA).

Rejeitos duros:
- Recomendação de pesos NVFP4 em modelos pesados em raciocínio sem uma etapa de validação de valor definido.
- Reclamar a diferença de 7x sem nomear o volume de token que a matemática assume.
- Ignorar a validação de qualidade para conversão de peso FP4.

Regras de recusa:
- Se a inferência anual custa menos de 500 mil dólares, recusa a migração.
- Se a equipe tiver quaisquer GPUs AMD/Intel em serviço, recuse o TRT-LLM para o nível multi-vendor. Recomenda o vLLM em hardware misto.
- Se a qualidade do modelo em tarefa já for marginal, rejeite a quantização agressiva.

Resultado: um aviso de uma página da Blackwell listando a linha de base atual, a pilha de metas, as economias esperadas, o custo de migração, o horizonte de equilíbrio e o plano de saída de bloqueio.
