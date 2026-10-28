---
name: inference-server
description: Ship a speculative-decoding inference server with EAGLE-3 or P-EAGLE drafts, K8s autoscaling, and a full throughput/latency/cost report.
version: 1.0.0
phase: 19
lesson: 14
tags: [capstone, inference, vllm, sglang, eagle-3, p-eagle, speculative-decoding, quantization, hpa]
---

Dados dois modelos de alvo aberto (Llama 3.3 70B e Qwen3-Coder-30B MoE ou GPT-OSS-120B), enviar uma pilha de produção com descodificação especulativa, quantização e automática Kubernetes. Publicar velocidades medidas e números de latência de cauda.

Construir um plano:

1. Deploia modelos-alvo sob o vLLM 0,7 (ou SGLang 0,4) com quantização FP8 Marlin.
2. Carregar um rascunho alinhado da EAGLE-3 da Red Hat Speculators (ou treinar um através do SpecForge).
3. Números de linha de base: tokens/s e p50/p99 latência no lote 1/8/32 sem especulação.
4. Activa a EAGLE-3. Reinicie o mesmo índice de referência. Raporta aceleração, taxa de aceitação, delta de p99 de atraso de cauda.
5. Ativar a especulação paralela do P-Eagle; relatar a inflexão onde árvores mais profundas ajudam contra prejudicar.
6. Execute os índices de referência em distribuições: ShareGPT, HumanEval, dados de domínio. Publique a deriva da taxa de aceitação.
7. Repita o segundo modelo-alvo (MoE); identifique a sensibilidade ao ruído de roteamento na aceitação do projeto.
8. Deploição em Kubernetes com rastreamento de HPA `queue_wait_ms`Demonstrar escala quando a carga triplica-se.
9. Compare tokens de $ 1M vs. Antropic Claude Sonnet 4.7 e OpenAI GPT-5.4 em avaliações correspondentes.

Rubrico de avaliação:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | Measured speedup vs baseline | 2.5x+ throughput at matched quality on both models |
| 20 | Acceptance rate on realistic traffic | Per-distribution acceptance-rate report |
| 20 | P99 tail-latency discipline | p99 at batch 1/8/32 with and without speculation |
| 20 | Ops | K8s deploy, HPA on queue-wait, smooth rollout, drain-first upgrade |
| 15 | Write-up and methodology | Clear derivation of metrics, matched baselines |

Rejeitos duros:

- Relatório de velocidade de estado estável sem latência de cauda.
- O HPA na CPU em vez de espera na fila, vai bater sob saturação da GPU.
- Ignorar a alinhamento entre os projetos e as versões-alvo.
- Comparar custos que omitem os descontos de caching de prompt das APIs hospedadas.

Regras de recusa:

- Recusar-se a servir sem um esgoto de deslocamento.
- Recusar-se a comunicar a taxa de aceitação agregada entre distribuições.
- Recusar-se a reivindicar ganhos de descodificação especulativa em bs=32 sem um número não especulativo correspondente.

Resultado: um repo contendo as configurações vLLM / SGLang, o script de download de projeto EAGLE-3, manifestos de implantação de K8s, configuração HPA na espera de fila, o harness de referência para dados de domínio ShareGPT / HumanEval /, uma tabela de comparação de tokens de $/1M, e um texto nomeando as três regressões especulativas de latência de cauda introduzidas e a descodação (batch gating, ngram fallback, ajuste de quantização) que fixaram cada uma.
