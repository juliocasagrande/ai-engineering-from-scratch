---
name: skill-pipeline-budget-planner
description: Dada a latência e o rendimento-alvo, atribuir um orçamento de tempo a cada fase do gasoduto e indicar qual estágio perderá o seu orçamento primeiro
version: 1.0.0
phase: 4
lesson: 16
tags: [vision, pipeline, performance, deployment]
---

# Planeador de Orçamento de Pipeline

Transforme um alvo de latencia/transmissão em um orçamento estágio a estágio para que cada membro da equipe saiba para que número eles estão projetando.

## Quando utilizar

- Antes de construir um novo serviço de visão, definir expectativas para cada etapa.
- Após um primeiro índice de referência, para ver qual estágio está mais longe do seu orçamento.
- Quando um SLA muda e os orçamentos precisam ser renegociados.

## Input

- `p95_latency_target_ms`: orçamento por pedido.
- `target_qps`: rendimento por réplica.
- `stages`Lista de: `{ name: str, current_ms: float }`- Não .

## Regras de atribuição

A atribuição por defeito nas sete etapas padrão, caso não sejam fornecidas medições de corrente:

| Stage | Share |
|-------|-------|
| decode + preprocess | 15% |
| detector forward | 55% |
| postprocess detections (NMS, clamp) | 5% |
| crop + resize for classifier | 5% |
| classifier forward | 15% |
| schema validation | <1% |
| response serialisation | 4% |

Em tubulações ligadas a GPU (nuvem), a participação do detector muitas vezes aumenta para 70%. Na CPU, o pré-processamento e a classificação de lotes consomem mais.

## Relatório

```
[budget plan]
  p95 target:  <ms>
  throughput:  <qps per replica>

| stage               | target_ms | current_ms | headroom | gate |
|---------------------|-----------|------------|----------|------|
| decode+preprocess   | ...       | ...        | ...      | ok|X |
| detector            | ...       | ...        | ...      | ok|X |
| ...                 | ...       | ...        | ...      |      |

[bottleneck]
  stage:  <name>
  miss:   <ms over budget>
  lever:  <specific action>

[levers]
  decode+preprocess:   Pillow-SIMD, libjpeg-turbo, decode on GPU via NVJPEG
  detector:            smaller backbone, lower input resolution, INT8, TensorRT
  postprocess:         GPU-side NMS (torchvision.ops), fused masks
  crop+resize:         GPU crop with grid_sample, batched interpolate
  classifier:          smaller backbone, INT8, warm cache, batch
  schema:              skip validation in hot path, validate at boundaries only
  response:            orjson, stream protobuf
```

## Regras

- Nunca recomenda deixar de lado a validação do esquema do caminho de produção; propor que seja movida para o limite.
- Se o pré-processamento não tiver o seu orçamento, tente sempre o Pillow-SIMD ou o NVJPEG antes de alterar o modelo.
- Se a falha do detector for superior a 30% do alvo, mude os modelos em vez de otimizar o atual.
- Marque o portão como `X` quando current_ms > 1.1 * target_ms; marca `ok` se estiverem dentro de 10% do orçamento.
