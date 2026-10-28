---
name: skill-3dgs-export-router
description: Escolha o formato de exportação 3DGS certo (.ply / .splat / glTF KHR_gaussian_splatting / USD) dado o visualizador ou motor a jusante
version: 1.0.0
phase: 4
lesson: 22
tags: [3d-gaussian-splatting, export, glTF, OpenUSD, pipeline]
---

# Roteador de exportação 3DGS

Mapear um alvo a jusante para o formato de arquivo 3DGS certo.

## Quando utilizar

- Depois de treinar uma cena 3DGS, antes de compartilhá-la com um pipeline de conteúdo.
- Escolha entre formatos de nível de investigação (.ply) e de nível de produção (glTF / USD).
- Transferência de canais: equipe de captura -> engenheiro 3DGS -> designer de jogos / artista VFX / desenvolvedor web.

## Input

- `target_engine`Não é real, unidade, universo, misturador, visão, pro, três, babilônio, césio, tela de jogo, superespaço.
- `priority`Portabilidade , tamanho de arquivo , qualidade , preservação .
- `include_sh_degree`- Não, não.

## Decisão de formato

| Target | Recommended format | Why |
|--------|--------------------|-----|
| Unreal Engine (virtual production) | Volinga plugin or glTF KHR_gaussian_splatting | Native Unreal SDK path |
| Unity (XR / game) | .ply via Aras-P Unity-GaussianSplatting plugin | Community-standard Unity pipeline |
| NVIDIA Omniverse, Pixar tools | OpenUSD 26.03 (UsdVolParticleField3DGaussianSplat) | Native USD prim type |
| Apple Vision Pro | OpenUSD 26.03 | Native to visionOS 2.x |
| Blender | .ply + KIRI Engine add-on | Community add-on reads raw splats |
| Three.js web viewer | glTF KHR_gaussian_splatting or .splat | Browser-standard, works with `GaussianSplats3D` |
| Babylon.js V9+ | glTF KHR_gaussian_splatting | V9 added native support |
| Cesium (CesiumJS 1.139+, Cesium for Unreal 2.23+) | glTF KHR_gaussian_splatting | Shipped explicit support |
| PlayCanvas | .splat | PlayCanvas native quantised format |
| SuperSplat (editor) | .ply or .splat | Import + export |

## Comércio de quantificação

- `.ply` Precision total: maior arquivo, sem perda, qualquer visualizador.
- `.splat`: 4x-8x menor, ligeira perda de qualidade nos coeficientes SH3, padrão PlayCanvas-ecossistema.
- glTF KHR: configurável através da EXT_meshopt_compressão; menor com maior compatibilidade.
- USD: comprimido pela embalagem USDZ; menor para os oleodutos da Apple.

## Relatório de produção

```
[export plan]
  target:         <engine>
  format:         <name>
  sh degree:      <0|1|2|3>
  compression:    <none|meshopt|quantisation|usdz>
  expected size:  <MB>
  compatible with: <list of viewers>

[pipeline]
  1. source: <.ply from training>
  2. optional: SuperSplat cleanup pass
  3. convert: <tool + CLI or API call>
  4. package: <.gltf / .glb / .usd / .usdz / .splat / .ply>
  5. validate: <viewer sanity check>
```

## Regras

- Nunca desprenda os coeficientes SH3 silenciosamente.
- Se `priority == file_size`, recomendar `.splat` ou glTF com meshopt; adverte sobre perda de qualidade.
- Para plataformas da Apple, prefira USD / USDZ em relação ao glTF em 2026; USDZ tem suporte a visionOS de primeira classe.
- Se o suporte 3DGS do telespectador-alvo for pré-padrão (antes de Fevereiro 2026), recomendamos `.ply` e o carregador personalizado do espectador; ainda não será reconhecido o GLTF padrão de Khronos.
- Valide sempre o arquivo exportado em pelo menos um visualizador antes de entregar; a corrupção silenciosa ocorre durante a quantização.
