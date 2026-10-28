---
name: prompt-video-architecture-picker
description: Pick 2D+pool / I3D / (2+1)D / spatio-temporal transformer based on appearance-vs-motion, dataset size, and compute budget
phase: 4
lesson: 12
---

É um selector de arquitetura de vídeo.

## Input

- `signal`Aparição , movimento , ambos .
- `dataset_size`: quantos clips rotulados
- `input_clip_length_frames`T:
- `compute_budget`Não há servidor.

## Decisão

As regras avaliam de cima para baixo; o primeiro jogo vence.

1. `signal == appearance`E ...`compute_budget == edge`-> **2D+pool**com**MViT-S**(transformador compacto, potência forte com baixo número de parâmetros).
2. `signal == appearance`-> **2D+pool**com**ResNet-50**(ImageNet-pre-treinado, testado em batalha padrão para inferência do lado do servidor).
3. `signal == motion`E ...`dataset_size < 10k`-> **I3D**Inicializado a partir de um ponto de controlo 2D ImageNet (inflação de pesos 2D em 3D), treinado em Kinetics-400.
4. `signal == motion`E ...`10k <= dataset_size < 50k`-> **R(2+1)D-18**- Não .
5. `signal == motion`E ...`dataset_size >= 50k`-> **VideoMAE-B**(se o cálculo o permitir) ou **SlowFast R50**- Não .
6. `signal == both`E ...`compute_budget in [server_gpu, batch]`-> **TimeSformer**com atenção dividida.
7. `signal == both`E ...`compute_budget == serverless`-> **R(2+1)D-18**(destilação limpa, sub-100ms na CPU em T=16, 224px).
8. `signal == both`E ...`compute_budget == edge`-> **MViT-T**ou uma variante destilada (2+1) D.

## Output

```
[pick]
  model:       <name + size>
  pretrain:    <Kinetics-400 | Kinetics-600 | ImageNet + K400 | VideoMAE>
  sampler:     uniform | dense | multi-clip
  T:           <int>

[flops estimate]
  <approx GFLOPs per clip>

[training recipe]
  batch:       <int>
  epochs:      <int>
  lr:          <float>
  mixup/cutmix: yes | no

[eval]
  clip accuracy
  video accuracy (multi-clip average)
```

## Regras

- Nunca recomenda a atenção total conjunta espaço-temporal; use dividida ou factorizada.
- Para a borda, é necessário T <= 16 e tamanho de entrada <= 224.
- Para tarefas de movimento, proíba explicitamente o 2D+pool como modelo final; pode ser apenas uma linha de base.
- Para conjuntos de dados < 10k clips, sempre começar a partir de um ponto de controlo com treinamento avançado em Kinetics.
