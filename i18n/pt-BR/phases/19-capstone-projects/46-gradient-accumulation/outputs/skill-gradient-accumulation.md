---
name: gradient-accumulation
description: Treinar em um lote eficaz maior que a memória do dispositivo, aumentando as perdas de micro-batch e acelerando o optimizador uma vez por janela.
version: 1.0.0
phase: 19
lesson: 46
tags: [training, batch-size, distributed, scaling]
---

## Quando utilizar

O lote eficaz é a alavanca que suaviza o gradiente e corresponde ao cronograma de taxa de aprendizagem.

## Receita

1. Escolha `micro_batch` O acelerador é o maior que se encaixa na memória e satura o acelerador.
2. Escolha `effective_batch` do calendário de taxa de aprendizagem.
3. Set `accum_steps = effective_batch // (micro_batch * world_size)` e afirmar que divide igualmente.
4. Por micro lote: `loss = criterion(model(x), y) / accum_steps; loss.backward()`- Não .
5. Em micros não finais, inserir `model.no_sync()` para saltar o gradiente total-redução no DDP.
6. Após o último micro lote, corre `optimizer.step()` Gradientes zero antes da próxima janela.
7. O estado de otimização avança uma vez por lote efetivo; o cronograma de taxa de aprendizagem passa uma vez por lote efetivo.

## Escavação

Emite um pequeno registro JSON por passo efetivo com `samples_per_sec`- Não . `median_step_ms`- Não . `sync_calls`- Não . `accum_steps`- Não . `effective_batch`Sem isto, o comércio de custos é invisível.

## Modos de falha

- Esquecendo-se do `/ accum_steps` Escalada: os gradientes explodem em N.
- Passo no meio da janela: parâmetros a deslocar-se.
- Sincronização em cada micro lote: rede limitada sem ganho estatístico.
- Misturar isto com precisionamento misto de descalculação: escalar apenas a perda não escalada.
