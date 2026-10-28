---
name: prompt-backbone-selector
description: Escolha a espinha dorsal de visão certa (LeNet, VGG, ResNet, MobileNet, EfficientNet-Lite, ConvNeXt, ViT) para uma determinada tarefa, tamanho do conjunto de dados e orçamento de computação
phase: 4
lesson: 3
---

Considerando as quatro entradas abaixo, recomenda uma coluna vertebral, explique o porquê e lista os dois primeiros-candidatos com suas compensações.

## Input

- `task`Classificação , detecção , segmentação , inserção , imagem médica , inspeção industrial.
- `input_resolution`: HxW típico das imagens que o modelo verá na produção.
- `dataset_size`: exemplos marcados disponíveis para formação ou ajuste fino.
- `compute_budget`Uma das seguintes: `edge` (telefone, microcontrolador), `serverless` (Inferência apenas para CPU, sensível ao arranque a frio), `server_gpu` (T4/A10), `batch` (offline, qualquer GPU).

## Método

1. Mapa do orçamento de cálculo para um limite máximo de parâmetros:
   - margem: <= 5M parâmetros
   - Servidor sem servidor: <= 25M params
   - servidor_gpu: <= 100M parâmetros
   - Batch: sem teto

2. Tamanho do conjunto de dados de mapa para o requisito de transferência de aprendizagem:
   - < 1k etiquetas: devem ajustar de forma fina uma coluna vertebral pré-treinada
   - 1k-100k: pré-treinado + curto ajuste fino, considere congelar as camadas iniciais
   - > 100k: o comboio do zero é uma opção se a computação permitir

3. Eliminar famílias que não se encaixem:
   - LeNet apenas para tarefas do tamanho do MNIST em entradas pequenas.
   - VGG apenas se o índice de referência exigir características VGG; quase sempre dominado pela ResNet em igual cálculo.
   - ResNet-18/34 simples se o cálculo for apertado e os requisitos de campo receptivo forem modestos.
   - ResNet-50 se precisar de recursos fortes de imagem-Net em escala de servidor.
   - MobileNet / EfficientNet-Lite se `compute_budget == edge`- Não .
   - ConvNeXt se `batch` O orçamento e a precisão são mais importantes do que a simplicidade do modelo.
   - Transformador de visão (ViT) se o conjunto de dados for grande o suficiente (>= ImageNet-1k) e a resolução é >= 224; caso contrário, preferir uma CNN.

4. Para tarefas não classificativas, ajustar a cabeçalha:
   - Detecção: alimentação da coluna vertebral FPN -> RetinaNet / FCOS / DETR cabeça.
   - Segmentação: alimenta a cabeça de U-Net / DeepLab; mantenha as conexões de saltos em múltiplas resoluções.
   - Embed: alimenta a projecção linear normalizada L2; treino com triplet ou perda contrastante.
   - OCR: espinha dorsal alimenta uma cabeça de sequência CTC ou encoder-decoder; use uma espinha dorsal CNN + BiLSTM (estilo CRNN) quando as linhas são longas, ou uma variante baseada em ViT para OCR de página inteira.
   - Imagem médica: espinha dorsal mais cabeça adequada à tarefa (classificação, U-Net para segmentação); preferem fortemente variantes baseadas no GroupNorm ou pré-treinadas em domínio (RETFound, RadImageNet) quando disponíveis.
   - Inspecção industrial: espinha-preta mais anomalia ou cabeça de segmentação; na borda, uma espinha-preta EfficientNet-Lite ou MobileNetV3 com cabeça de classificação superficial é a receita comum para o transporte.

## Formatos de saída

```
[recommendation]
  pick:     <family + size>
  params:   <approx>
  pretrain: <ImageNet-1k | ImageNet-21k | CLIP | domain-specific | none>
  reason:   <one sentence, grounded in dataset size and compute>

[runner-up 1]
  pick:    <family + size>
  tradeoff: <why we did not pick it>

[runner-up 2]
  pick:    <family + size>
  tradeoff: <why we did not pick it>

[plan]
  - stage: <freeze layers / train head / joint fine-tune>
  - input: <resize and crop policy>
  - aug:   <mixup/cutmix/randaug level>
  - eval:  <metric and threshold>
```

## Regras

- Sempre indicar um tamanho específico do modelo (ResNet-18, não "ResNet").
- Nunca recomendo uma coluna vertebral que exceda o teto param.
- Se o orçamento de cálculo proíbe a precisão necessária à tarefa, diga-o e propor destilação ou resolução de entrada menor em vez de violar silenciosamente o orçamento.
- Para `edge`, exigem um plano de quantificação concreto (INT8 pós-treinamento ou QAT).
- Quando o tamanho do conjunto de dados < 1k, proíba o treinamento a partir do zero, independentemente da computação.
