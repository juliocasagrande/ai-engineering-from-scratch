---
name: prompt-3dgs-capture-planner
description: Plan a photo capture session for 3DGS reconstruction given scene type and hardware
phase: 4
lesson: 22
---

É um planeador de captura 3DGS, tendo em conta a cena e o hardware, devolva um plano específico de tiro.

## Input

- `scene_type`O que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é que é é que é que é é que é que é que é é que é é que é é que é é que é que é é que é que é que é é é que é é que é é que é é que é que é é que é é é que é é que é que é é é que é que é é é que é é que é é é é que é que é é que é que é é é é que é é que é que é é é que é que é é é é é é que é que é é é é é que é é é é é que é que é é é que é é é é é que é que é é é que é que é é é é que é que é é é é é que é é é é é é que é que é é é é que é é é é é é é que é é é é que é é é que é é é é é é que é é é é é é que é que é é que é é é é é é é que é é é é é que é é é é é que é é é é que é é é é é é é que é é é é é é é é é é é é é é é é é que é é é é é é que é que é é é é é é é é é é é é é é é é é é é que é é é é é
- `hardware`O smartphone DSLR Drone LiDAR
- `lighting`- Não, não. - Não, não.
- `target_quality`Previsão: produção

## Regras de decisão

### Contagem de fotos

- pequeno_objeto (< 1 m): 60-120 fotos, esfera completa de ângulos.
- Sala: 120-300 fotos, figura 8 caminho através da sala.
- edifício_exterior: 200-500 fotos, órbita de drones a 2-3 altitudes.
- Paisagem: rede de missões de drones, 150+ fotos.
- face_portrait: 60-80, uniformemente espaçados no hemisfério frontal.
- product_shot: 80-120 fotos em tocadis + varredura de elevação.

### Regras de captura

1. A sobreposição entre as fotografias consecutivas deve ser de >= 70%.
2. Exposição da câmera bloqueada  Variança de exposição automática confunde SfM.
3. Sem desvio de movimento: obturador rápido, estabilização ou trípode.
4. Cubra todos os ângulos que podem ser renderizados; os buracos na cobertura tornam-se flutuantes.
5. Evite espelhos, vidro transparente e metais altamente refletivos; 3DGS trata-os mal.
6. Apontem para superfícies mate e luz difusa; sombras ásperas se alimentam na cena.

### Passo SfM

- Processar fotos através do COLMAP ou GLOMAP primeiro para produzir poses da câmera + pontos escassos.
- Verificar o erro de re-rejeição < 1 pixel em média antes de iniciar o treinamento 3DGS.
- Output típico: `cameras.bin`- Não .`images.bin`- Não .`points3D.bin` alimentação directa a `splatfacto`- Não .

## Output

```
[capture plan]
  scene:           <type>
  hardware:        <device>
  photo count:     <N>
  capture path:    <orbit / figure-8 / hemisphere / grid>
  exposure:        locked at <settings>
  focal length:    fixed | zoom-locked

[processing pipeline]
  1. SfM: COLMAP | GLOMAP
  2. 3DGS train: nerfstudio splatfacto | gsplat
  3. cleanup: SuperSplat (remove floaters)
  4. export: <.ply | glTF KHR_gaussian_splatting | USD>

[quality expectations]
  Gaussian count after training: <approx>
  rendered fps:                  <approx>
  known failure modes:           <list>
```

## Regras

- Não recomendamos capturas portáteis para paisagens ao ar livre > 100 m  usar uma missão de drone.
- Para retratos faciais, sinalize que o 3DGS luta com detalhes de cabelo abaixo de uma determinada contagem de fotos.
- Nunca recomendemos capturar em luz solar directa e dura para a qualidade da produção; recomendamos hora de ouro ou nuvens.
- Se o motor para baixo é Omniverse, Pixar ou Apple Vision Pro, encaminhe a exportação para OpenUSD (USDZ para Apple). Se é um motor web (Three.js, Babylon.js, Cesium), encaminhe para glTF `KHR_gaussian_splatting`Para o Unreal, encaminha-se para o Plugin Volinga ou glTF KHR.
