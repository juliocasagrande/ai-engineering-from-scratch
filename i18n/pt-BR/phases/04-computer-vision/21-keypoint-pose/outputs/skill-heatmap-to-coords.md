---
name: skill-heatmap-to-coords
description: Escreva a rotina de sub-pixel heatmap-to-coordinate usada por cada modelo de pose de produção
version: 1.0.0
phase: 4
lesson: 21
tags: [keypoint, pose, subpixel, inference]
---

# Mapa de calor para cordas

Transforma mapas de calor de pontos-chave em coordenadas precisas sub-pixels.

## Quando utilizar

- Implementação de um modelo de pontos-chave baseado em mapas de calor.
- Metricas de posições de benchmarking  O OKS é extremamente sensível à precisão de sub-pixels.
- Portando código de pose de uma estrutura para outra.

## Input

- `heatmaps`- Não . `(N, K, H, W)` Tensor, mapas de calor por ponto chave do modelo.
- `confidence_threshold`: descartar pontos-chave cujo pico seja inferior a este valor.

## Passo

1. **Argmax** cada mapa de calor para encontrar o pico de localização do número inteiro.
2. **First-difference offset**  estimar o deslocamento de subpixels dos pixels vizinhos. `0.25` O coeficiente é um coeficiente heurístico calibrado para mapas de calor gaussianos com `sigma >= 1`; para a recuperação de subpixels de princípio, utilizar um ajuste quadrático completo (DARK) ou um ajuste gaussiano.

```
dx = 0.25 * sign(heatmap[y, x+1] - heatmap[y, x-1])
dy = 0.25 * sign(heatmap[y+1, x] - heatmap[y-1, x])
```

Para a variante escura / quadrática, aproximar usando um quadrático local:

```
dx = -0.5 * (heatmap[y, x+1] - heatmap[y, x-1])
        / (heatmap[y, x+1] - 2 * heatmap[y, x] + heatmap[y, x-1] + eps)
```

O ajuste quadrático é mais preciso em mapas de calor de pico; o offset baseado em sinal é o padrão mais seguro quando os mapas de calor são barulhentos.

3. **Add offset** para o pico de números inteiros.
4. **Confidence**  retornar o valor máximo por ponto chave; os clientes usam-no para mascarar as previsões de baixa confiança.
5. **Boundary case**  quando o pico atinge o primeiro ou último pixel ao longo de um eixo, um dos vizinhos é apertado; o deslocamento desabate para zero, que é o retorno mais seguro.

## Modelo de saída

```python
import torch

def heatmap_to_coords_subpixel(heatmaps, threshold=0.2):
    N, K, H, W = heatmaps.shape
    flat = heatmaps.reshape(N, K, -1)
    conf, idx = flat.max(dim=-1)
    ys = (idx // W).float()
    xs = (idx % W).float()

    ys_int = ys.long()
    xs_int = xs.long()

    x_minus = (xs_int - 1).clamp(min=0)
    x_plus = (xs_int + 1).clamp(max=W - 1)
    y_minus = (ys_int - 1).clamp(min=0)
    y_plus = (ys_int + 1).clamp(max=H - 1)

    batch_idx = torch.arange(N).view(-1, 1).expand(-1, K)
    kp_idx = torch.arange(K).view(1, -1).expand(N, -1)

    dx_raw = (heatmaps[batch_idx, kp_idx, ys_int, x_plus]
              - heatmaps[batch_idx, kp_idx, ys_int, x_minus])
    dy_raw = (heatmaps[batch_idx, kp_idx, y_plus, xs_int]
              - heatmaps[batch_idx, kp_idx, y_minus, xs_int])
    dx = 0.25 * torch.sign(dx_raw)
    dy = 0.25 * torch.sign(dy_raw)

    at_left = xs_int == 0
    at_right = xs_int == (W - 1)
    at_top = ys_int == 0
    at_bottom = ys_int == (H - 1)
    dx = torch.where(at_left | at_right, torch.zeros_like(dx), dx)
    dy = torch.where(at_top | at_bottom, torch.zeros_like(dy), dy)

    refined_x = xs + dx
    refined_y = ys + dy
    coords = torch.stack([refined_x, refined_y], dim=-1)
    mask = conf >= threshold
    return coords, conf, mask
```

## Relatório

```
[subpixel decode]
  keypoints:   K
  threshold:   <float>
  valid_rate:  fraction of keypoints above threshold
```

## Regras

- Sempre apertar os índices vizinhos para o intervalo válido; os pontos-chave fora da borda têm compensação de diferença zero, mas não há colisão.
- Retorna a confiança ao lado das coordenadas para que os clientes possam mascarar pontos de baixa confiança.
- O refinamento de sub-pixels só ajuda quando o heatmap é suave em torno do pico verifique se o treinamento usou um alvo gaussiano com sigma >= 1.
- Para resoluções muito pequenas de heatmap (< 48x48), considere aumentar a amostra do heatmap para o tamanho completo da imagem antes de extrair as coordenadas; as escalas sub-pixels compensam com o passo.
