---
name: skill-depth-to-pointcloud
description: Construa nuvens de pontos a partir de mapas de profundidade com manejo intrínseco correto e exportação para .ply
version: 1.0.0
phase: 4
lesson: 26
tags: [depth, point-cloud, 3d, intrinsics]
---

# Profundidade a nuvem

Transformar um mapa de profundidade e uma imagem a cores numa nuvem de pontos texturizada, exportável para visualização ou trabalho em 3D.

## Quando utilizar

- Visualizar previsões de profundidade como uma cena 3D real.
- Bootstrapping uma reconstrução 3D rara a partir de uma única imagem.
- Produção de entrada para o treinamento 3DGS quando o SfM falhar.
- Comparar profundidade prevista com a verdade do LiDAR.

## Input

- `depth`- Não . `(H, W)` Numpy array de profundidades nas mesmas unidades que deseja na saída (metros recomendados).
- `rgb`- Não . `(H, W, 3)` Array de cores numpy (uint8 ou float32 [0, 1]).
- `intrinsics`- Não . `(fx, fy, cx, cy)` em unidades de pixels.
- Opcional `depth_scale`: multiplicador para converter unidades de profundidade previstas em metros.

## Pipeline

1. **Validate** A profundidade deve ser positiva e finita em todos os lugares que pretende incluir.
2. **Lift**  `X = (u - cx) * d / fx`- Não . `Y = (v - cy) * d / fy`- Não . `Z = d` por pixel.
3. **Pair** com RGB  cada ponto 3D obtém um `(r, g, b)` Triplo do pixel correspondente.
4. **Export**  PLY (portátil), `.xyz` (luz), `.pcd` (Open3D-native), `.las`- Não .`.laz` (geospatial).

## Modelo de execução

```python
import numpy as np

def depth_to_point_cloud(depth, intrinsics, depth_scale=1.0, min_depth=0.1, max_depth=100.0):
    H, W = depth.shape
    fx, fy, cx, cy = intrinsics
    v, u = np.meshgrid(np.arange(H), np.arange(W), indexing="ij")
    z = depth.astype(np.float32) * depth_scale
    valid = (z > min_depth) & (z < max_depth) & np.isfinite(z)
    x = (u - cx) * z / fx
    y = (v - cy) * z / fy
    points = np.stack([x, y, z], axis=-1)
    return points, valid


def write_ply(path, points, colors=None, valid_mask=None):
    p = points.reshape(-1, 3)
    if valid_mask is not None:
        p = p[valid_mask.flatten()]
    lines = [
        "ply",
        "format ascii 1.0",
        f"element vertex {p.shape[0]}",
        "property float x", "property float y", "property float z",
    ]
    if colors is not None:
        c = colors.reshape(-1, 3).astype(np.uint8)
        if valid_mask is not None:
            c = c[valid_mask.flatten()]
        lines += ["property uchar red", "property uchar green", "property uchar blue"]
    lines.append("end_header")
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
        if colors is not None:
            for pt, col in zip(p, c):
                f.write(f"{pt[0]:.4f} {pt[1]:.4f} {pt[2]:.4f} {col[0]} {col[1]} {col[2]}\n")
        else:
            for pt in p:
                f.write(f"{pt[0]:.4f} {pt[1]:.4f} {pt[2]:.4f}\n")
```

## Relatório

```
[export]
  input depth shape:  (H, W)
  valid points:       <N> of <H*W>
  output format:      ply | xyz | pcd | las
  coordinate system:  camera (+X right, +Y down, +Z forward)
  scale:              metres | millimetres | normalised
```

## Regras

- Mascarar sempre profundidade inválida (zero, NaN, inf, saturada); incluindo-as produz uma nuvem de pontos de lixo na origem.
- Para previsão a partir de um modelo de profundidade relativa, NÃO exportar como métrica; prefixo nome de arquivo de saída com `relative_` Para sinalizar a convenção.
- Mantenha a convenção de coordenadas da câmera consistente (OpenCV: +X à direita, +Y para baixo, +Z para frente).
- Para cenas densas (> 1M pontos), ofereça um parâmetro de sub-programa; os ficheiros PLY > 500 MB são difíceis de carregar em todos os lugares.
- Nunca clipe em silêncio profundidade para produzir saída "razão"; clipe explicitamente com limites avisados para que os usuários saibam o que foi descartado.
