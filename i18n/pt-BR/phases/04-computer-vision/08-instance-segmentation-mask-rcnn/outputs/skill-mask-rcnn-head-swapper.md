---
name: skill-mask-rcnn-head-swapper
description: Generate the exact code for swapping box and mask heads on a torchvision Mask R-CNN for a custom num_classes
version: 1.0.0
phase: 4
lesson: 8
tags: [computer-vision, mask-rcnn, fine-tuning, torchvision]
---

# Mascarete de cabeça R-CNN

Produz a placa de aquecimento de câmbio de cabeça especificamente para Mask R-CNN. O modelo abaixo assume `model.roi_heads.box_predictor`E ...`model.roi_heads.mask_predictor`, que existem em`maskrcnn_resnet50_fpn`E ...`maskrcnn_resnet50_fpn_v2`A R-CNN mais rápida tem um preditor de caixa mas não há preditor de máscara.`RetinaNetHead`E não tem .`roi_heads`Os dois requerem competências diferentes.

## Quando utilizar

- - Melhores ajustes .`maskrcnn_resnet50_fpn`ou `maskrcnn_resnet50_fpn_v2`num conjunto de classes personalizados.
- Portando um posto de controlo R-CNN mascarado em COCO para uma classe não COCO.
- Desfazer um treinamento da R-CNN que se desabar em`cls_score.out_features`ou `mask_predictor`Não coincide.

## Não é aplicável

- `fasterrcnn_*`Não há mascarador, só trocar.`box_predictor`; utilizar uma receita separada de trocas de cabeças da Faster R-CNN.
- `retinanet_*`Não .`roi_heads`; cabeças de classificação + regressão vivem sob `model.head.classification_head`E ...`model.head.regression_head`Usa uma habilidade específica da RetinaNet.
- `keypointrcnn_*` utilizações `keypoint_predictor`Em vez de`mask_predictor`- Não .

## Input

- `model_name`: constructor de modelos de detecção de torcas, por exemplo `maskrcnn_resnet50_fpn_v2`- Não .
- `num_classes`Um conjunto de dados de 4 classes de objetos significa `num_classes=5`- Não .
- `freeze`: um dos `backbone`- Não .`backbone_fpn`- Não .`none`- Não .

## Passo

1. Importar o constructor do modelo e as duas classes de predictor (`FastRCNNPredictor`- Não .`MaskRCNNPredictor`)).
2. Carregar o modelo pré-treinado de peso padrão.
3. Substitui`model.roi_heads.box_predictor`com um novo`FastRCNNPredictor(in_features, num_classes)`- Não .
4. Substitui`model.roi_heads.mask_predictor`com um novo`MaskRCNNPredictor(in_features_mask, hidden_layer=256, num_classes)`- Não .
5. Aplicar a política de congelamento solicitada.
6. Imprimir um bloco de confirmação que enumere os parâmetros treinaveis por módulo.

## Modelo de código de saída

```python
from torchvision.models.detection import {MODEL_NAME}, {MODEL_WEIGHTS}
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.models.detection.mask_rcnn import MaskRCNNPredictor

def build_model(num_classes={NUM_CLASSES}):
    model = {MODEL_NAME}(weights={MODEL_WEIGHTS}.DEFAULT)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)
    in_features_mask = model.roi_heads.mask_predictor.conv5_mask.in_channels
    model.roi_heads.mask_predictor = MaskRCNNPredictor(in_features_mask, 256, num_classes)

    {FREEZE_BLOCK}

    return model
```

Onde ?`{FREEZE_BLOCK}`é:

- `none`-> vazio
- `backbone`- Não.
  ```python
  for p in model.backbone.parameters():
      p.requires_grad = False
  ```
- `backbone_fpn`- Não.
  ```python
  for p in model.backbone.parameters():
      p.requires_grad = False
  # FPN parameters live inside backbone.fpn
  ```

## Relatório

```
[head-swap]
  model:         <MODEL_NAME>
  num_classes:   <N>  (includes background)
  freeze policy: <choice>
  trainable:     <N>
  total:         <N>
```

## Regras

- Nunca recomendo .`num_classes`sem o fundo incluído; sempre lembre o utilizador.
- Sempre use o `_v2`variantes de modelos de detecção de torchvision, quando disponíveis; têm pesos pré-treinados melhores do que os antigos.
- Não instantanear o modelo dentro desta habilidade  produzir o bloco de código e deixar o usuário executá-lo.
- Se o utilizador solicitar `freeze backbone`num conjunto de dados maior que 10.000 imagens, sugerem que considerem ajustar a espinha dorsal também.
