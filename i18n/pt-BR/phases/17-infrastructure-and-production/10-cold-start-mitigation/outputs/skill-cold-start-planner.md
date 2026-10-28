---
name: cold-start-planner
description: Pick and stack cold-start mitigations for serverless LLM deployments. Budget phases (node, image, weights, engine, first forward) and match mitigations to SLA.
version: 1.0.0
phase: 17
lesson: 10
tags: [cold-start, serverless, bottlerocket, model-streamer, gpu-snapshot, warm-pool, serverlessllm]
---

Dado o tamanho do modelo, o SLA (TTFT P99), a forma do tráfego (estabilizado versus explodido) e a postura orçamental produzem um plano de mitigação de arranque a frio.

Produzir:

1. Orçamento de arranque a frio. Descompõe o caminho de arranque a frio bruto (provisão de nós, puxão de imagem, pesos para HBM, motor init, primeiro para frente). Use 2026 segundos nominais para o tamanho do modelo indicado.
2. Seleção de camadas. Escolha o número mínimo de camadas que traz o total abaixo do SLA: imagem pré-sementeada (L1), streamer modelo (L2), snapshot da GPU (L3), piscina quente (L4), carga em camadas (L5). Justifique cada camada contra a fase específica que ataca.
3. Dimensão de piscina quente.`min_workers`Se o SLA for TTFT P99 < 60s num modelo 70B+, faça obrigatório a piscina quente, independentemente do custo.
4. Estimativa de custos: custo mensal da GPU para a piscina de calor escolhida e o número esperado de arranques de frio por dia.
5. Política de cauda. O que acontece com o primeiro usuário em uma réplica fresca?  eles ficam na fila para uma réplica quente, ou pagam o imposto de início frio? Nomear uma política específica (por exemplo, "route primeiro pedido para qualquer réplica quente dentro de 10 anos; cair para frio").
6. Modo de falha. O que acontece se uma réplica quente morrer no meio da sessão. A recuperação é automática (migração ao vivo), ou é um começo frio no próximo pedido?

Rejeitos duros:
- Propondo "apontar apenas uma piscina quente" sem calcular o custo mensal.
- A reivindicação de uma mitigação sem uma fase específica que ataca (por exemplo, "utilizar Bottlerocket" sem dizer que elimina a atração de imagem de 180s).
- Ignorando a restrição de topologia por GPU em instantâneos de GPU  se a plataforma migrar para SKU, instantâneos são inválidos.

Regras de recusa:
- Se o SLA for TTFT P99 < 5s em um início frio de 70B fresco sem piscina quente, rejeitar  matematicamente impossível em velocidades de infraestrutura de 2026.
- Se o orçamento proíbe a piscina quente, mas o SLA requer um início a frio de sub-30s, nomee a correção específica da plataforma (impressões de GPU Modal, pré-aquecimento Baseten) e recuse-se a prometer o SLA em uma plataforma diferente sem ele.
- Se o operador pedir uma escala de zero com tráfego em erupção e um modelo 70B, recusar-se a prometer SLA  a matemática não funciona sem instantâneos ou piscinas quentes.

Resultado: um plano de uma página que enumera fases, camadas,`min_workers`, custo mensal, política de cauda, modo de falha.
