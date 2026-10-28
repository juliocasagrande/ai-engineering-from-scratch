---
name: skill-segmentation-mask-inspector
description: Distribuição das classes de relatório, estatísticas de mascaras previstas e as classes mais propensas a ser sub-previsíveis ou confusas
version: 1.0.0
phase: 4
lesson: 7
tags: [computer-vision, segmentation, debugging, evaluation]
---

# Inspector de Máscara de Segmentação

Um diagnóstico para a diferença entre "a perda diminuiu" e "as máscaras realmente parecem certas".

## Quando utilizar

- Logo após uma corrida de treinamento, quando o MIoU parece bem, mas a inspecção visual diz o contrário.
- Antes da implantação: verificar o equilíbrio de classe das previsões contra a verdade de base.
- Quando a UIO por classe é alta para objetos grandes, mas baixa para pequenos.
- Descargar artefatos de fronteira que não aparecem na UIO porque são pequenos em número de pixels.

## Input

- `preds`: (N, H, W) tensor de identificação de classe prevista.
- `targets`: (N, H, W) tensor de identificação de classe de verdade de base.
- `num_classes`: número inteiro.
- Opcional `class_names`: lista de cordas C.

## Passo

1. **Class pixel histograms.** Calcule a percentagem de pixels por classe para `preds` e `targets`- Flag qualquer classe onde `|pred% - gt%| / max(gt%, 1e-6) > 0.30` (desviação relativa superior a 30%).`gt% == 0`), sinalize qualquer participação prevista acima `0.3` - Direto.

2. **IoU per class** e **boundary F1 per class**. O limite F1 é calculado dilatando cada máscara por 3 pixels, intersectando-se e marcando.

3. **Small-object recall.** Separar todos os componentes conectados à verdade de base em baldes de tamanho (minus < 100 px, pequeno < 1000 px, médio < 10000 px, grande > = 10000 px). Relatório de recall por balde por classe. Recall de objeto pequeno abaixo de 0,3 enquanto recall de objeto grande acima de 0,9 indica um problema de resolução / campo receptivo.

4. **Confusion pairs.** Para cada classe, encontre a classe com que mais frequentemente confunde (a classe mais comum de previsão errada dentro de sua máscara de verdade de base).

5. **Saturation check (requires `probs` or `logits`, not just `preds`).** Se o chamador passar a distribuição de probabilidade bruto por pixel `probs: (N, C, H, W)`, calcular a fracção de pixels onde `probs.max(dim=1) > 0.99` A saturação elevada (> 0,9 de pixels de uma classe) sugere uma confiança excessiva  candidato para o suavização ou calibração de rótulos. `preds` Se estiverem disponíveis, pular este passo e anotá-lo no relatório.

## Formatos de relatório

```
[mask-inspector]
  classes: C

[class distribution]
  name       gt %    pred %   delta
  ...

[metrics]
  class       IoU     bF1    recall_tiny  recall_small  recall_medium  recall_large
  ...

[confusion pairs]
  class A confused with class B: <N> pixels (most common)
  class B confused with class A: <N> pixels
  ...

[verdict]
  most impactful issue: <one sentence>
```

## Regras

- Ordenar as linhas de classes por parte de piksel gt descendente para que as classes mais frequentes sejam as primeiras.
- Classificações de bandeiras com IOU < 0,4 ou limite F1 < 0,3 como `critical`- Não .
- Quando o recall de pequenos objetos é o fracasso dominante, recomendamos: treinamento de maior resolução, passo menor na última fase do codificador, ou um decodificador de pirâmide de características.
- Quando o limite F1 é o falha dominante, recomendamos: perda consciente de limites (Lovasz ou BoundaryLoss), TTA com virada horizontal e decodificador sem passos.
- Nunca emitir índices de classes como único identificador, se: `class_names` Se for fornecido, use-o em todas as linhas.
