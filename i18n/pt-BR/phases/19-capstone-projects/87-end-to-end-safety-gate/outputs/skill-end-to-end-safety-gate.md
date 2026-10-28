---
name: skill-end-to-end-safety-gate
description: Three-checkpoint safety gate composing the input detector, streaming token filter, output classifier, and rules engine with a deterministic aggregation table and per-request trace
version: 1.0.0
phase: 19
lesson: 87
tags: [safety, harness, composition]
---

# Porta de segurança de ponta a ponta

## Ciclo de vida

1. Pre-gen - executar a lição 83 detector no prompt
   - Se a confiança >= limite de bloqueio: recusa de devolução, emissão de rastro, parada
2. durante a geração - fluxo do modelo, buffer de dois pedaços, rastreio de continuidades nocivas conhecidas
   - Se for combinado: encerrar o iterador, marcar o rastro, tratar como gravidade média
3. post-gen - se não houver rescisão antecipada, executar o roteador classificador lição 85 e o motor regra lição 86 sobre a saída concluída
4. agregado - tomar a gravidade máxima em relação a pre, durante, post.classificador, post.regras
5. aplicar - mapa para bloquear, redigir, alertar ou permitir

## Tabela de agregação

| Signal state | Action |
|---|---|
| any high severity | block |
| any medium severity | redact |
| any low severity | warn |
| nothing | allow |

## Estrutura de rastreamento

```text
RequestTrace
  request_id: str
  prompt: str
  pre_gen: { category, confidence, fired[] }
  during_gen: { terminated_early, matched_pattern, partial_chunks }
  post_gen: { classifier_action, classifier_severity, rules_max_severity, rules_violations[] } | null
  final_action: block | redact | warn | allow
  final_output: str
  latency_ms: float
```

## Artifacto

`outputs/gate_trace.json`Conta o resumo e uma traça por pedido, incluindo 50 fixos de taxonomia e 10 indicações benignas.
