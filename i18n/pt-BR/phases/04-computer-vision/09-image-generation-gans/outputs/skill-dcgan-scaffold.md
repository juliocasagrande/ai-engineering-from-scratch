---
name: skill-dcgan-scaffold
description: Escreva um andaime completo DCGAN a partir de z_dim, image_size e num_channels, incluindo loop de treinamento e salvador de amostras
version: 1.0.0
phase: 4
lesson: 9
tags: [computer-vision, gan, dcgan, scaffolding]
---

# Estafa DCGAN

Dados três parâmetros, emitir um esqueleto de projeto DCGAN executável com a arquitetura dimensionada corretamente para a resolução da imagem-alvo.

## Quando utilizar

- Começando um novo experimento gerativo num pequeno conjunto de dados.
- Ensino de fundamentos da DCGAN com um exemplo mínimo de trabalho.
- Protótipo de GANs condicionais (a injecção de etiqueta ocorre no mesmo andaime).

## Input

- `image_size`: um de 32, 64, 128 (deve ser um poder de dois).
- `num_channels`: 1 (escala de cinza) ou 3 (RGB).
- `z_dim`: normalmente 64 ou 128.
- `with_spectral_norm`Sim, não, por padrão sim.

## Dimensão de arquitetura

O número de blocos de convos transpostos em G e de blocos de convos passados em D depende da `image_size`- Não .

| image_size | G blocks | D blocks |
|------------|----------|----------|
| 32         | 4        | 4        |
| 64         | 5        | 5        |
| 128        | 6        | 6        |

Cada bloco adicional duplica (G) ou divide (D) a dimensão espacial. `feat_base * 2^block_index`- Não .

## Arquivos de saída

- `model.py`  Classe de gerador + discriminador
- `train.py`  ciclo de formação, perda, configuração de optimizador
- `sample.py`  Salvador de rede de amostra
- `config.json`  hiperparâmetros
- `README.md`  10 linhas de arranque rápido

## Relatório

```
[scaffold]
  image_size:       <int>
  num_channels:     <int>
  z_dim:            <int>
  spectral_norm:    yes | no

[arch]
  G blocks:         <N>, channels: [list]
  D blocks:         <N>, channels: [list]
  G params (est):   <N>
  D params (est):   <N>

[training defaults]
  optimizer:   Adam(lr=2e-4, betas=(0.5, 0.999))
  batch_size:  64
  epochs:      50
  sample_every: 1 epoch

[files written]
  - model.py
  - train.py
  - sample.py
  - config.json
  - README.md
```

## Regras

- Sempre utilizar `nn.Tanh()` sobre os dados de saída e escala de G até [-1, 1] durante o treinamento.
- Sempre utilizar `LeakyReLU(0.2)` em D.
- Quando `with_spectral_norm == yes`, envolver cada conve em D com `spectral_norm()` e remover BatchNorm de D. Mantenha BatchNorm em G.
- Nunca emitir um andaime para imagem_size > 128  DCGAN se torna instável acima disso; apontar o usuário para StyleGAN ou um modelo de difusão.
