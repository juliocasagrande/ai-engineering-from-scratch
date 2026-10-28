---
name: skill-lora-training-setup
description: Write a full LoRA training config for a custom dataset, including captions, rank, batch size, and learning rate
version: 1.0.0
phase: 4
lesson: 11
tags: [computer-vision, stable-diffusion, lora, fine-tuning]
---

# Configuração de treinamento do LoRA

Transformar uma descrição da intenção de ajuste fino em uma configuração de treinamento concreto que está pronto para passar para `diffusers`ou `kohya_ss`- Não .

## Quando utilizar

- Formação de um LoRA para um assunto (pessoas, objetos, personagens), um estilo (artista, marca) ou um conceito (posição, iluminação).
- Extensão de um LORA existente com mais dados.
- Desfazer uma execução de LoRA cuja saída seja inferior ou superior às imagens de treinamento.

## Input

- `purpose`Conceptos de estilo de assunto.
- `num_images`: quantas imagens de formação estão disponíveis
- `base_model`SD 1.5  SDXL  SD3  FLUX
- `gpu_vram_gb`O que é que eu faço?
- `caption_source`Manual: gerado pelo BLIP2

## Selector de classificação

| Purpose | Rank | Alpha |
|---------|------|-------|
| Subject | 8-16 | rank |
| Style | 16-32 | rank * 2 |
| Concept | 32-64 | rank |

Uma posição mais elevada = mais capacidade, mais risco de sobreajuste em pequenos conjuntos de dados.`alpha == rank`É o padrão seguro.`alpha == rank * 2`dá um impulso mais forte ao estilo ao custo de mais risco de cozinhar o estilo muito duro  usar apenas quando a fidelidade do assunto não é o objetivo.

## Objectivo da fase de formação

- `subject`com 5-20 imagens: 500-1500 passos.
- `style`com 30 a 100 imagens: 1500 a 4000 passos.
- `concept`com mais de 100 imagens: 4000-10000 passos.

Superar a seu risco  uma LoRA que tenha memorizado as suas imagens de treinamento não pode generalizar.

## Taxa de aprendizagem

- Encoder de texto LoRA: `1e-4`para SD 1.5, `5e-5`para a SDXL.
- U-Net LoRA: `1e-4`para SD 1.5, `1e-4`para a SDXL.
- FLUX / SD3: `5e-5`Para o transformador, os codificadores de texto geralmente congelados.
- Reduzir a LR para metade quando `num_images < 15`(título) ou quando se realiza um treino de mais de 3000 passos; pequenos conjuntos de dados e longas corridas beneficiam de uma atualização mais suave.

## Programação

- `cosine_with_warmup`(default): aquecimento durante os primeiros 5 a 10% dos passos, depois decaimento cosínico.`steps >= 1000`A cauda de decomposição dá amostras finais mais nítidas.
- `constant`: só para corridas muito curtas (`steps < 500`) ou ao retomar um LoRA anterior, onde se deseja preservar as características aprendidas atuais sem anulação.

## Formatos de legendas

- Subject: prepare um token de gatilho único ("myperson") para cada legenda. Mantenha o token de gatilho raro para que não sobreescreva conceitos existentes. Evite palavras reais e nomes comuns.
- Estilo: aplique uma etiqueta de estilo única no final de cada legenda ("...em estilo mystyle"). Trate a própria etiqueta como um símbolo de gatilho raro  `mystyle`Não , não .`impressionism`, que já se encaixa num conceito real.
- Concept: descreva o conceito em cada legenda; sem token de gatilho. O próprio conceito (por exemplo, "choque de baixo ângulo") é a âncora.

## Configuração de saída

```yaml
model:
  base: <base_model HF id>
  precision: fp16 | bf16

lora:
  rank: <int>
  alpha: <int>
  targets: unet.cross_attention  # and/or unet.to_q, to_k, to_v, to_out

training:
  steps:          <int>
  batch_size:     <int, tuned to gpu_vram_gb>
  grad_accum:     <int, usually 1 on >=16 GB, 4 on <=12 GB>
  learning_rate:  <float>
  optimizer:      AdamW8bit | AdamW
  scheduler:      cosine_with_warmup | constant
  warmup_steps:   <int>
  save_every:     <int>

data:
  images_dir:     <path>
  caption_source: <manual | BLIP2 | native>
  trigger_token:   <string if purpose==subject>
  resolution:      <512 for SD 1.5, 1024 for SDXL>
  aspect_ratio_bucketing: true
  augmentation:
    flip:          true
    color_jitter:  false

validation:
  prompts:
    - "<trigger> ...test prompt..."
    - "<trigger> in a different scene"
  every_steps: 250
```

## Relatório

```
[lora setup]
  purpose:   <subject|style|concept>
  base:      <model>
  rank:      <int>
  steps:     <int>
  batch:     <int>   grad_accum: <int>
  lr:        <float>
  vram est.: <float> GB
```

## Regras

- Nunca recomendo .`rank > 64`O LoRA torna-se um mini-finado e perde a sua natureza "adaptória".
- Para o`num_images < 5`, alertar fortemente  LoRAs de identidade em 1-3 imagens sobre-equipadas cada vez.
- Para o`gpu_vram_gb < 12`, exigem AdamW8bit e controle de gradiente.
- Se`base_model == FLUX`E ...`gpu_vram_gb < 24`, rota para o`schnell`A variante e observe que o treinamento é mais lento.
- Nunca omita as instruções de validação; é impossível avaliar um LoRA sem redes de amostragem.
