---
name: multi-region-router
description: Design a multi-region LLM routing plan with KV-cache locality, residency boundaries, DR manifest, and a quarterly failover drill.
version: 1.0.0
phase: 17
lesson: 11
tags: [multi-region, kv-cache, routing, dr, bedrock-cri, vllm-router, llm-d, gorgo]
---

Dadas as regiões em âmbito, os limites de residência, a diversidade esperada de prefixos e o TTFT SLA, produzem um roteamento multi-regional e um plano de DR.

Produzir:

1. Seleção do roteador. Escolha o roteador consciente do cache (roteador vLLM, roteador llm-d) e descreva o canal de evento KV. Indique o algoritmo de prefixo-hash (por exemplo, 512-token rolling) e tie-breaker (menos profundidade de fila).
2. Política de roteamento. Minimizar o pre-fill + RTT em primeiro lugar regional ou global (estilo GORGO)? Justificar com a distribuição de comprimento de tempo rápido  pedidos longos (> 8K tokens) beneficiam do roteamento transregional; pedidos curtos não.
3. Residência particionamento. Antes de qualquer otimização: quais solicitações estão vinculadas a quais regiões por razões legais (GDPR, HIPAA). Proibir roteamento transversal de residência mesmo quando a TTFT melhora.
4. Comércio CRI camada. Recomenda se habilitar Bedrock Cross-Region Inference ou GKE Multi-Cluster Gateway como a camada de disponibilidade. Esta camada não é uma otimização TTFT.
5. Manifesto DR. Minimo de três arquivos (HF repo + configuração do motor + manifesto de implantação). Verifique o tokenizer, configurações de quantização, RoPE, modelos de bate-papo, adaptadores LoRA estão incluídos. Indique o armazenamento (replicação interregional S3, GCS multi-região).
6. Perseguição de falha. Cadência trimestral. Quem a executa, o que é medido (RTO, RPO, tempo de aquecimento no cache).

Rejeitos duros:
- Ignorar a residência para otimizar o roteamento.
- Reclamar que o CRI do Bedrock "resolve" o roteamento trans-regional.
- Recusar  nomear a estatística de falha de 32% DR e exigir o manifesto de três arquivos.

Regras de recusa:
- Se apenas uma região estiver a ser abrangida, o plano de recusa  a região única tem diferentes modos de falha (a fase 17 · 03 abrange).
- Se a residência e o SLA TTFT forem incompatíveis (por exemplo, a residência da UE forçando preenchimento em prefixo frio por pedido com P99 TTFT < 100 ms em 8K), recusar a promessa do SLA e aumentar o requisito do produto.

Resultado: um plano de uma página nomeando roteador, política de roteamento, partições de residência, postura de camada CRI, manifesto DR, proprietário de perfuradores trimestrais.
