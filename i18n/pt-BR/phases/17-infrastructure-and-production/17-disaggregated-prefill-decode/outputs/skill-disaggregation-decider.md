---
name: disaggregation-decider
description: Decide whether to adopt disaggregated prefill/decode (Dynamo or llm-d) for a given workload and cluster. Quantify prefill:decode ratios, KV transfer cost, and the expected savings.
version: 1.0.0
phase: 17
lesson: 17
tags: [disaggregated-serving, dynamo, llm-d, nixl, kv-transfer, prefill-decode]
---

Dado o perfil da carga de trabalho (distribuição de comprimento de saída/pronto, modelo, concurência), topologia do cluster (GPUs, tecido, disponibilidade de RDMA) e custo de serviço atual, resulta uma decisão de desagregação.

Produzir:

1. Desagregar? Sim / Não com justificação numerada. Linha de base: pedidos > 512 E saídas > 200. Fábrico: RDMA disponível ajuda; somente TCP empurra o break-even mais tempo.
2. Opção de pilha. NVIDIA Dynamo (orquestrador gerenciado acima de vLLM/SGLang/TRT-LLM) ou llm-d (Serviços nativos Kubernetes).
3. Prefill:decode ratio. Use leituras do Dynamo Planner Profiler, ou compute a partir da forma da carga de trabalho (prefill TFLOPS vs decode bytes/sec). Exemplo: 2 prefill: 1 decode para RAG-heavy; 1:2 para output-heavy.
4. Plano de transferência de KV. Transporte nomeado (NIXL sobre InfiniBand / RDMA / TCP fallback). Calcule o imposto de transferência por pedido para o seu pedido de P99.
5. Integração do roteador. Roteador consciente de cache (Fase 17 · 11) deve estar na frente  desagregação sem prefixo de correspondência perde o cache ganha.
6. A economia esperada: cálculo versus linha de base colocada; cita o caso publicado (30-40% na mesma SLA).

Rejeitos duros:
- Desagregação de cargas de trabalho de breve prazo (< 512 tokens).
- Deploying sem um roteador consciente de cache. Refuse  blind routing nega a localização KV.
- Ignorar a topologia (pacotamento de rack): Recusar  Transferência de KV sobre saltos de rack múltiplos custa mais do que RDMA no mesmo rack.

Regras de recusa:
- Se o cluster tiver < 4 GPUs, rejeite  não a diversidade suficiente para que a desagregação se repeta.
- Se não houver RDMA/InfiniBand e nenhum plano, note que o TCP aumenta o equilíbrio para pedidos > 2K; reavalia.
- Se a equipe não puder operar dois pools de GPU com escalação por papel, recusar llm-d e exigir Dynamo como a alternativa gerenciada.

Output: uma decisão de uma página com desagregação Y/N, escolha de pilha, proporção, transporte, roteador, economias esperadas.
