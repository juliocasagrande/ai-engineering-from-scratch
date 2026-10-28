---
name: skill-image-tensor-inspector
description: Inspect any image-shaped tensor or array and report dtype, layout, range, and whether it looks raw, normalized, or standardized
version: 1.0.0
phase: 4
lesson: 1
tags: [computer-vision, debugging, preprocessing, tensors]
---

# Inspetor de Tensão de Imagem

Uma habilidade de diagnóstico para qualquer ponto de um tubo de visão onde você está segurando uma matriz em forma de imagem e precisa saber exatamente em que estado está.

## Quando utilizar

- Um modelo pré-treinado retorna previsões de lixo e suspeitas do pré-processamento.
- Não está claro como é possível migrar um gasoduto entre o OpenCV e a torchvision e a ordem do canal.
- As camadas de empilhamento de várias estruturas e o eixo do lote continua a aparecer no lugar errado.
- Descargar um ciclo de treinamento onde a perda está presa.`log(num_classes)`- Não .

## Input

- `x`: qualquer matriz 2-D, 3-D ou 4-D (NumPy, PyTorch, JAX).
- Facultativo`expected`: um ditado de invariantes a verificar, por exemplo `{"layout": "CHW", "range": "standardized"}`- Não .

## Passo

1. **Resolve backend** detectar se `x`Converte-o para NumPy para inspeção sem alterar o original.

2. **Classify rank**- Não .
   - classificação 2 -> imagem de canal único (H, W).
   - 3o grau -> `HWC`Se o último eixo for 1, 3 ou 4 e for estritamente menor que os outros dois; caso contrário `CHW`- Não .
   - classificação 4 -> preferência `NCHW`Se o eixo 1 estiver em {1, 3, 4} **and**seja o eixo 2 ou o eixo 3 maior que 16; de outra forma, é preferível `NHWC`O controlo do eixo 1 puro classifica erroneamente os lotes NHWC de imagem pequena como`(3, 4, 224, 3)`- Não .
   - Sempre sinalize casos ambíguos (por exemplo `(1, 3, 3, 3)`) como `ambiguous`Em vez de adivinhar; exigir que o chamador forneça `expected`- Não .

3. **Classify dtype and range**- Não .
   - `uint8`em [0, 255] -> `raw`- Não .
   - `float*`com min >= 0 e max <= 1,01 -> `normalized`- Não .
   - `float*`Min < 0 e com média < 0,5 e 0,5 <= std <= 1,5 -> `standardized`- Não .
   - Qualquer outra coisa -> `unusual`- Imprimir o histograma.

4. **Per-channel stats**Comparar com a média/std da ImageNet se a matriz parecer padronizada e apresentar uma confiança de correspondência.

5. **Report**Neste bloco exato:

```
[inspector]
  backend:   numpy | torch | jax
  rank:      2 | 3 | 4
  layout:    HW | HWC | CHW | NHWC | NCHW
  dtype:     <dtype>
  shape:     <shape>
  range:     raw | normalized | standardized | unusual
  min/max:   <min> / <max>
  per-channel mean: [ ... ]
  per-channel std:  [ ... ]
  likely source:    camera | PIL | OpenCV | torchvision | random init
  likely target:    display | training | inference
```

6. **Recommend next action**baseada no `likely target`- Não .
   - Para o`display`: transponha para HWC, clip, converta para uint8.
   - Para o`training`A definição de um sistema de dados é:
   - Para o`inference`: correspondem às invariantes exatas do modelo de cartão.

## Regras

- Nunca mude a entrada, apenas imprime diagnósticos.
- Se`expected`Se for fornecido, sinalize cada desajuste com `[expected X got Y]`- Não .
- Apela a riscos de falha silenciosa quando o layout ou a ordem do canal é ambígua.
- Recomendar uma ação por vez, não uma lista de opções.
