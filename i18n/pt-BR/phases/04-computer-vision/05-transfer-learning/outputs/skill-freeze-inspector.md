---
name: skill-freeze-inspector
description: Report which parameters are trainable, which BatchNorm layers are in eval mode, and whether the optimizer is actually consuming the trainable parameters
version: 1.0.0
phase: 4
lesson: 5
tags: [computer-vision, transfer-learning, debugging, pytorch]
---

# Inspector de congelação

Os bugs de transferência de aprendizagem ocultas em três lugares: parâmetros que deveriam ser congelados, mas não são, parâmetros que deveriam ser treináveis, mas não são, e os optimizadores que foram construídos antes do estado de congelamento mudar.

## Quando utilizar

- Logo após a configuração .`requires_grad`sobre um subconjunto de parâmetros.
- Antes do primeiro passo de treinamento de uma corrida de sintonia.
- Depois de ligar .`freeze_bn_stats`Ou qualquer auxiliar que volte o modo BN.
- Quando a precisão da val está presa ao acaso e suspeitas que nada está a treinar.

## Input

- `model`: uma PyTorch `nn.Module`- Não .
- `optimizer`Otimizador que está prestes a ser utilizado para formação.
- Facultativo`expected_frozen_prefixes`: lista de prefixos de nome de parâmetro que devem ser congelados (por exemplo `["conv1", "bn1", "layer1"]`)).

## Passo

1. **Walk parameters.**Para cada um .`(name, param)`- Não .
   - registro `requires_grad`
   - registro `shape`E ...`numel`

2. **Walk modules.**Para cada módulo:
   - Se for BatchNorm, registar se está em modo de avaliação e se os seus parâmetros afins são treináveis.

3. **Inspect the optimizer.**Para cada grupo de parâmetros:
   - Aplanar o seu`params`em um conjunto de `id(p)`- Não .
   - Comparar com o conjunto de todos `id(p)`para params onde `requires_grad == True`- Não .

4. **Detect the four failure modes:**
   - `leaked_train`: um param tem `requires_grad=True`Mas não aparece no optimizador (o gradiente é calculado mas nunca aplicado).
   - `ghost_train`: um param aparece no optimizador mas tem `requires_grad=False`(o estado do optimizer é desperdiçado; também pode causar bugs se você mais tarde re-habilitar requisit_grad).
   - `bn_mismatch`A primeira é a de que a camada BN está em modo de trens (acumula estatísticas de corrida) enquanto os seus parâmetros afins (`weight`- Não .`bias`Os dois estados são inconsistentes e quase sempre um bug.
   - `expected_vs_actual`: qualquer prefixo listado em `expected_frozen_prefixes`Ainda tem um parâmetro treinável.

## Relatório

```
[freeze-inspector]
  model trainable params: <N>
  model frozen params:    <N>
  batchnorm layers in eval mode: <count>
  batchnorm layers in train mode: <count>

[optimizer coverage]
  trainable params fed to optimizer: <M> of <N>
  leaked_train: <list of names> (trainable but not in optimizer)
  ghost_train:  <list of names> (in optimizer but frozen)

[bn audit]
  mismatched layers: <list of names>

[expectations]
  expected_frozen_prefixes: <...>
  violating params:         <list>

[verdict]
  ok | <one-line summary of the most severe issue>
```

## Regras

- Apenas notifique os nomes dos parâmetros; nunca imprima os pesos em si.
- Ordenar cada lista por nome de parâmetro.
- Se a cobertura do optimizador for de 100% e não houver desajustes, retorne `ok`E pára.
- Para o`leaked_train`Recomenda-se sempre reconstruir o optimizador depois do estado de congelamento mudar.
- Para o`ghost_train`Recomenda- se a remoção do grupo de parâmetros ou a configuração `requires_grad=True`Se a intenção era treinar.
