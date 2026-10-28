---
name: engine-picker
description: Pick a self-hosted LLM engine (llama.cpp, Ollama, TGI, vLLM, SGLang) given hardware, scale, and workload. Name 2026 TGI maintenance mode as a migration trigger.
version: 1.0.0
phase: 17
lesson: 28
tags: [self-hosted, vllm, sglang, llama-cpp, ollama, tgi, trt-llm, engine-selection]
---

Dado o hardware (CPU / Apple Silicon / AMD / NVIDIA Hopper / NVIDIA Blackwell), escala (um único usuário / pequena equipe / produção / empresa), e carga de trabalho (chat geral / agentec / RAG / longo contexto / código), produz uma recomendação do motor.

Produzir:

1. Nomear o motor específico, citar a árvore hardware primeiro, escala segundo, carga de trabalho terceiro.
2. Para cada motor alternativo, diga por que não é a escolha (modo de manutenção TGI, AMD exclui TRT-LLM, Ollama é apenas dev).
3. Em caso de produção, nomear o padrão de oleoduto (dev Ollama → estacionamento llama.cpp → prod vLLM/SGLang) e confirmar o formato de peso (GGUF ou HF) passa.
4. Em escala de produção, aponte para a fase 17 · 18 (stack de produção), · 17 (desagregado), · 11 (router consciente de cache) para a composição.
5. Migração TGI: se o titular é TGI, especifique o plano de migração e o cronograma  não urgente, mas deve começar dentro de 6 meses.
6. O hardware tem o que fazer. Exigir as duas restrições duras: apenas CPU → llama.cpp; AMD → nenhum TRT-LLM.

Rejeitos duros:
- Defaulting de novos projetos para TGI em 2026. Rejeitar o modo de manutenção.
- Ollama para produção compartilhada a > 1 utilizador simultâneo.
- Sugerir TRT-LLM sem confirmar apenas NVIDIA.

Regras de recusa:
- Se o hardware for misturado (alguns AMD, alguns NVIDIA), exigir decisões de motor por cluster; não forçar um único motor.
- Se a carga de trabalho for "desconhecida/gênera" na escala de produção, por defeito, para o vLLM e planejar uma reavaliação após 3 meses de dados de tráfego.
- Se a equipe quiser "mais rápido por GPU sem disponibilidade Blackwell" e insistir em Hopper-somente, confirme  TRT-LLM ou vLLM são ambos aceitáveis.

Output: uma recomendação de uma página com motor, alternativas descartadas, pipeline, produção empilhada, postura de migração TGI.
