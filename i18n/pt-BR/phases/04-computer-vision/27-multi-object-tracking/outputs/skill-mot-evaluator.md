---
name: skill-mot-evaluator
description: Write a complete evaluation harness for MOTA / IDF1 / HOTA against ground-truth tracks
version: 1.0.0
phase: 4
lesson: 27
tags: [mot, evaluation, tracking, metrics]
---

# Avaliação do MOT

Envolva a saída do seu rastreador no gasoduto MOTA/IDF1/HOTA padrão para que possa comparar justamente com a literatura.

## Quando utilizar

- Benchmarking de um novo rastreador no MOT17 / MOT20 / DanceTrack / SportsMOT.
- Comparar ByteTrack com BoT-SORT com SAM 2 em sua própria gravação.
- Produção de um número reprodutivel para um artigo ou uma descrição de relações públicas.

## Input

- `predictions`: lista por quadro de `(track_id, x, y, w, h, confidence)`- Túples.
- `ground_truth`: lista por quadro de `(gt_id, x, y, w, h)`- Túples.
- `iou_threshold`: 0,5 típico para MOTA; HOTA utiliza um varredor.
- `evaluator`- Não .`py-motmetrics`(MOTA, IDF1) ou `TrackEval`- Não.

## Contrato de formato de saída

Ambos .`py-motmetrics`E ...`TrackEval`Expectar um formato específico no disco:

```
# predictions.txt
<frame>,<track_id>,<x>,<y>,<w>,<h>,<confidence>,-1,-1,-1

# ground_truth.txt
<frame>,<gt_id>,<x>,<y>,<w>,<h>,1,-1,-1,-1
```

Os quadros são indexados em 1, as caixas são (x, y, w, h), não (x1, y1, x2, y2). A conversão é onde a maioria dos bugs de integração vive.

## Passo

1. Converte a saída do seu rastreador para o formato de texto MOT Challenge.
2. Corra .`py-motmetrics.io.loadtxt`Em ambos os ficheiros.
3. Calcule MOTA + IDF1 com `mm.metrics.create().compute()`- Não .
4. Para a HOTA, invoque`TrackEval`com os mesmos ficheiros e `Metrics: HOTA`- Não .
5. Salvar resultados como JSON para painéis de controle.

## Esboço de execução

```python
import motmetrics as mm

def evaluate_mota_idf1(pred_path, gt_path):
    gt = mm.io.loadtxt(gt_path, fmt="mot15-2D")
    pred = mm.io.loadtxt(pred_path, fmt="mot15-2D")
    acc = mm.utils.compare_to_groundtruth(gt, pred, dist="iou", distth=0.5)
    metrics = mm.metrics.create().compute(
        acc, metrics=["num_frames", "mota", "motp", "idf1", "idp", "idr", "num_switches"]
    )
    return metrics


def write_mot_txt(predictions, path):
    with open(path, "w") as f:
        for frame_idx, detections in enumerate(predictions, start=1):
            for tid, x, y, w, h, conf in detections:
                f.write(f"{frame_idx},{tid},{x:.2f},{y:.2f},{w:.2f},{h:.2f},{conf:.3f},-1,-1,-1\n")
```

## Relatório

```
[mot evaluation]
  frames:     <int>
  gt tracks:  <int>
  pred tracks: <int>

[metrics]
  MOTA:       <float>
  MOTP:       <float>
  IDF1:       <float>
  IDP/IDR:    <float/float>
  ID switches: <int>
  HOTA:       <float>  (from TrackEval)
```

## Regras

- Sempre use quadros indexados em 1 no arquivo de texto de saída; ferramentas MOT espera isso.
- Converte (x1, y1, x2, y2) para (x, y, w, h) antes de escrever.
- Não informe o MOTA sozinho para comparações modernas; inclua IDF1 e HOTA.
- Observe as detecções privadas versus públicas no MOT17  são avaliadas separadamente e misturando-as aumenta as pontuações.
- Registo de pontuações por sequência; agregado esconde falhas em sequências difíceis individuais.
