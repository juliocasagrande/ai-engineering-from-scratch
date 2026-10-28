---
name: inference-platform-picker
description: Pick an inference platform (Fireworks, Together, Baseten, Modal, Replicate, Anyscale, or custom silicon) given workload, SLA, budget, and operational constraints. Normalize per-token, per-minute, and per-prediction pricing.
version: 1.0.0
phase: 17
lesson: 02
tags: [inference, fireworks, together, baseten, modal, replicate, anyscale, economics]
---

Dado um perfil de carga de trabalho (modelo, tokens/dia, utilização sustentada, TTFT SLA, fator de explosão, conformidade, Python vs stack mix), produzir uma recomendação de plataforma.

Produzir:

1. Plataforma primária. Nomear a plataforma e o nível de preços específico (serverless vs. dedicado vs. lote). Justificar com as características de carga de trabalho que correspondem  por exemplo, "Fireworks serverless porque TTFT < 500 ms é o SLA e o tráfego é estragado".
2. Custo eficaz. Normalize o modelo de preços escolhido para tokens de saída de $ / M. Compare com pelo menos duas alternativas. Chame quando por minuto bate por token (acima de ~ 30% de utilização sustentada) ou vice-versa.
3. Plano de início frio. Para as escolhas sem servidor (Fireworks, Modal, Replicate), estenda a latência esperada de início frio e uma mitigação (pre-aquecimento, min_workers=1, migração ao vivo). Para as escolhas dedicadas (Baseten, Anyscale), evite esta seção, mas note o trade-off.
4. O segundo vice-campeão. Nomear a segunda plataforma e a condição explícita sob a qual você mudaria (por exemplo, "mover para Baseten se fecharmos um negócio empresarial que requer GPUs dedicadas HIPAA +").
5. Layer Gateway. Recomenda se a plataforma deve ser encaminhada com um gateway de IA (LiteLLM, Portkey, Kong AI Gateway) para isolar o produto do fornecedor.

Rejeitos duros:
- Comparar tokens por minuto contra tokens por minuto sem normalizar.
- Escolher Fireworks porque é "mais rápido" sem validar o TTFT SLA contra os índices publicados.
- Recomenda-se o silício personalizado (Groq, Cerebras, SambaNova) para qualquer carga de trabalho não limitada à latência.

Regras de recusa:
- Se a carga de trabalho requer um quadro regulamentado (SOC 2 Tipo II, HIPAA) e o cliente escolheu Modal ou Replicate, rejeitar  nem tem a mesma pegada empresarial que Baseten ou Anyscale.
- Se o tráfego esperado for inferior a 100 mil tokens/dia, recuse-se a recomendar por minuto (Baseten, Modal, Anyscale).
- Se o cliente quiser "o mais barato", rejeite  nome a função de custo multidimensional (taxa de tokens + início a frio + atribuição + gateway + DX).

Output: uma recomendação de uma página nomeando a plataforma primária, custo eficaz, plano de início a frio, sub-campeão, postura do gateway. Terceira com a métrica única que revelará uma escolha errada (pico de início a frio P99, taxa por token ou deriva de utilização).
