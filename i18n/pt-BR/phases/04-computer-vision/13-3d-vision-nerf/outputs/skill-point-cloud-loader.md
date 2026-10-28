---
name: skill-point-cloud-loader
description: Write a PyTorch Dataset for .ply / .pcd / .xyz files with correct normalisation, centring, and point sampling
version: 1.0.0
phase: 4
lesson: 13
tags: [3d-vision, point-cloud, data-loading, pytorch]
---

# Loaders de nuvem de ponto

Transforme uma pasta de arquivos de digitalização 3D em um PyTorch pronto para treinamento `Dataset`- Não .

## Quando utilizar

- Iniciando um novo projeto de classificação/segmentação de nuvem de pontos.
- - A alternar entre os dois .`.ply`- Não .`.pcd`, e `.xyz`Formas.
- Desfazer um modelo que se exerce sem erro mas converge mal; muitas vezes a normalização do carregador de dados é errada.

## Input

- `data_root`: pasta de ficheiros de nuvem pontual e um CSV opcional com rótulos.
- `file_format`Não é o que eu quero.
- `num_points`: tamanho fixo da amostragem, tipicamente 1024 ou 2048.
- `augmentation`Não há nada que se torne.

## Política de normalização

Cada linha de condução de nuvem de ponto de produção é aplicada na ordem:

1. **Centre**A nuvem: subtrai a centróide.
2. **Scale**para a esfera unitária: dividir pela distância máxima do centro.
3. **Sample** `num_points`Se a nuvem tem mais, use **farthest point sampling**(FPS) para representação fiel da forma ou amostragem aleatória para velocidade.
4. **Shuffle**ordem de pontos (a ordem não deve importar para o modelo de qualquer forma, mas a mistura rompe dependências de ordem acidentais).

## Modelo de saída

```python
import numpy as np
import torch
from torch.utils.data import Dataset

try:
    import open3d as o3d
    HAS_O3D = True
except ImportError:
    HAS_O3D = False

def _read_ply(path):
    if HAS_O3D:
        pc = o3d.io.read_point_cloud(path)
        return np.asarray(pc.points, dtype=np.float32)
    # Fallback: minimal ascii-ply reader
    ...

def _fps(points, k):
    idx = np.zeros(k, dtype=np.int64)
    dist = np.full(len(points), np.inf)
    seed = np.random.randint(len(points))
    idx[0] = seed
    for i in range(1, k):
        dist = np.minimum(dist, ((points - points[idx[i-1]]) ** 2).sum(axis=1))
        idx[i] = int(np.argmax(dist))
    return idx

def normalise(points):
    centre = points.mean(axis=0)
    points = points - centre
    scale = np.max(np.linalg.norm(points, axis=1))
    return points / max(scale, 1e-8)

class PointCloudDataset(Dataset):
    def __init__(self, files, labels, num_points=1024, augment=False):
        self.files = files
        self.labels = labels
        self.num_points = num_points
        self.augment = augment

    def __len__(self):
        return len(self.files)

    def __getitem__(self, i):
        pts = _read_ply(self.files[i])
        pts = normalise(pts)
        if len(pts) >= self.num_points:
            idx = _fps(pts, self.num_points)
            pts = pts[idx]
        else:
            reps = int(np.ceil(self.num_points / len(pts)))
            pts = np.tile(pts, (reps, 1))[:self.num_points]
        # Shuffle point order to break any accidental dependencies (especially
        # important when tiling repeats points in deterministic order).
        np.random.shuffle(pts)
        if self.augment:
            theta = np.random.uniform(0, 2 * np.pi)
            R = np.array([[np.cos(theta), 0, np.sin(theta)],
                          [0, 1, 0],
                          [-np.sin(theta), 0, np.cos(theta)]], dtype=np.float32)
            pts = pts @ R
            pts = pts + np.random.normal(0, 0.02, pts.shape).astype(np.float32)
        pts = np.ascontiguousarray(pts, dtype=np.float32)
        return torch.from_numpy(pts).transpose(0, 1), int(self.labels[i])
```

## Relatório

```
[dataset]
  files:          <N>
  format:         <ply|pcd|xyz|npy>
  points_per_sample: <int>
  normalise:      centre + unit sphere
  sampling:       FPS | random
  augmentation:   <list>
```

## Regras

- Sempre centro antes de escalar; trocar a ordem muda o significado de "esfera unidade".
- Prefere FPS ao invés de amostragem aleatória para tarefas de forma; aleatório é bom para segmentação onde cada ponto importa de qualquer maneira.
- Nunca aumentem durante a avaliação; apenas durante o treinamento.
- Se os arquivos da nuvem de pontos incluir cores ou normais como canais extras, alargar o conjunto de dados para retornar um `(3 + C, num_points)`Tensor, não apenas XYZ.
