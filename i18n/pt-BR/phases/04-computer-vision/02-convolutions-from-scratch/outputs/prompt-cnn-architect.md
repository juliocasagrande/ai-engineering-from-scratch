---
name: prompt-cnn-architect
description: Desenhar uma pilha de camadas Conv2d a partir do tamanho da entrada, orçamento de parâmetros e campo receptor alvo
phase: 4
lesson: 2
---

Dadas as três entradas abaixo, produzir um projeto camada por camada que atinja o orçamento e o campo receptivo sem desperdiçar computação.

## Input

- `input_shape`: (C, H, W) dos dados que chegam ao primeiro conv.
- `param_budget`: limite de duração dos parâmetros de aprendizagem total.
- `target_rf`: campo mínimo de recepção que a camada final deve ver, em pixels da entrada original.
- Opcional `downsample_factor`A classificação é feita por padrão, 8 para a classificação, 4 para a detecção das espinhas.

## Método

1. **Fix the spine.** Cada quarteirão é um dos seguintes: `Conv3x3(s=1,p=1)` (refinamento), `Conv3x3(s=2,p=1)` (programa inferior + refinamento), `Conv1x1` (mistura de canais), `DepthwiseConv3x3 + Conv1x1` (Bloqueamento da rede móvel).

2. **Compute receptive field as you add layers.** Utilização `RF = 1 + sum_i (k_i - 1) * prod(stride_j for j < i)`Pára de adicionar uma vez . `RF >= target_rf`- Não .

3. **Double channels on every downsample** 32 -> 64 -> 128 -> 256 é um padrão seguro, a menos que o orçamento o proíba.

4. **Compute parameters per layer** como `C_out * C_in * K * K + C_out`- Acumular e rejeitar o bloco se ele exceder o orçamento.

5. **Emit a table** com colunas: `idx | block | C_in | C_out | K | S | P | H_out | W_out | RF | params | cumulative_params`- Não .

6. **Final layer**: uma média global seguida por `Linear(C_final, num_classes)` para classificação ou um ponto de acesso de pirâmide de características para detecção.

## Formatos de saída

```
[spec]
  input: (C, H, W)
  budget: N params
  target RF: R px

[stack]
  idx  block              Cin  Cout  K  S  P  Hout  Wout  RF   params   cum
  1    Conv3x3 s=1 p=1    3    32    3  1  1  H     W     3    896      896
  2    Conv3x3 s=2 p=1    32   64    3  2  1  H/2   W/2   7    18,496   19,392
  ...

[summary]
  total params: X
  final spatial: H_out x W_out
  final RF:      F px
  headroom:      budget - X params unused
```

## Regras

- Se a RF-alvo não for atingível dentro do orçamento, informe a lacuna e propor um dos seguintes: a) utilizar um passo mais cedo para tornar a RF mais barata, b) mudar para blocos de profundidade, c) reduzir a largura da base.
- Se a RF-alvo for igual ou superior ao tamanho da entrada, marque-a e recomenda um pool global no final, em vez de mais camadas.
- Não invente tamanhos de núcleo incomuns (1x3, 5x5 com passo 3, etc.) a menos que o orçamento seja tão apertado que a coluna vertebral 3x3 padrão não se encaixe.
- Um bloco por fila de mesa, sem células combinadas, sem comentários entre filas.
