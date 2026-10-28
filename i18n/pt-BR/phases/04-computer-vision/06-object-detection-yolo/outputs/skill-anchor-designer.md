---
name: skill-anchor-designer
description: Given a dataset of ground-truth boxes, run k-means on (w, h) and return anchor sets per FPN level plus coverage statistics
version: 1.0.0
phase: 4
lesson: 6
tags: [computer-vision, detection, anchors, kmeans]
---

# Ancorador

Ancoras são o único hiperparâmetro mais específico de conjunto de dados em um detector baseado em âncora. Ancoras COCO por defeito têm um desempenho inferior em imagens de cultura celular, azulejos de satélite ou vigilância de pequenos objetos. Esta habilidade deriva âncoras que realmente correspondem aos dados alvo.

## Quando utilizar

- Antes de uma primeira formação em um novo conjunto de dados.
- Quando a lembrança de objetos muito pequenos ou muito grandes é fraca em um modelo saudável.
- Após uma grande expansão do conjunto de dados onde a distribuição do tamanho da caixa pode ter mudado.

## Input

- `boxes`: matriz de forma numpy (N, 4) em qualquer `(cx, cy, w, h)`ou `(x1, y1, x2, y2)`formato; recomendam-se pelo menos 1000 caixas positivas.
- `num_anchors_per_level`: geralmente 3.
- `num_fpn_levels`: geralmente 3 (P3, P4, P5) ou 4.
- `input_size`: formação-resolução HxW.
- Facultativo`strides`: passos por nível; quando omitidos, tome o primeiro `num_fpn_levels`Inscrições de `[8, 16, 32, 64]`Passar uma matriz mais ou menos expressa se o FPN do detector tiver diferentes passos.

## Passo

1. **Normalise boxes**- Não .`(w, h)`pares em unidades de píxeles em `input_size`- Deixe cair qualquer um com w ou h < 2 pixels.

2. **Run k-means**- Não .`(w, h)`em pares, com `k = num_anchors_per_level * num_fpn_levels`- Usar .`1 - IoU(box, cluster)`como a função de distância, não distância euclidiana  euclidiana em `(w, h)`Se você tem um conjunto de dados desequilibrado de classes e deseja retomar caixas maiores, repita caixas de classes raras na matriz de entrada em vez de passar um vetor de peso.

3. **Sort clusters by area**A ascensão.`num_fpn_levels`Grupos de`num_anchors_per_level`As zonas mais pequenas atingem o nível de resolução mais elevado (máxima fase).

4. **Compute coverage statistics**por nível:
   - `median IoU`de cada caixa de verdade de terra para a sua melhor âncora nesse nível.
   - `recall@IoU=0.5` percentagem de caixas cuja melhor âncora tenha uma IU >= 0,5.
   - `area coverage` fracção das caixas cuja área corresponde a `[anchor_min_area / 4, anchor_max_area * 4]`do nível.

5. **Report per-level anchors**e níveis de bandeira, onde `recall@IoU=0.5 < 0.9`As âncoras desse nível não correspondem bem aos dados e devem ser retornadas ou o número de âncoras por nível aumentado.

## Formatos de relatório

```
[anchor-designer]
  total boxes:         <N>
  clusters:            <k>
  distance metric:     1 - IoU

[level P3  stride=8]
  anchors (w, h):      [(A, B), (C, D), (E, F)]
  median IoU:          <X>
  recall@IoU=0.5:      <X>
  coverage:            <X>
  flag:                ok | retune

[level P4  stride=16]
  ...

[summary]
  overall recall@IoU=0.5: <X>
  smallest anchor:        <w x h>
  largest anchor:         <w x h>
  recommendation:         <one sentence if any level flagged>
```

## Regras

- Sempre use distância baseada em IoU; as meias k de Euclides produzem âncoras visualmente razoáveis, mas empiricamente piores.
- Ordenar os aglomerados por área, depois atribuir aos níveis em ordem ascendente.
- Quando ?`num_anchors_per_level = 1`, saltar k-means inteiramente: dividir as caixas em `num_fpn_levels`Os dados de cada nível são definidos em termos de quantilo de área (por exemplo, tercílios para 3 níveis) e definidos na mediana por bin (w, h).`k = num_fpn_levels`em pequenos conjuntos de dados.
- Nunca produzir dimensões negativas de âncora; sujeitar a 1.
- Se o conjunto de dados tiver < 200 caixas, avise o utilizador de que a busca de âncora não é confiável e recomenda o uso de âncoras COCO padrão, além de mais dados de treinamento.
