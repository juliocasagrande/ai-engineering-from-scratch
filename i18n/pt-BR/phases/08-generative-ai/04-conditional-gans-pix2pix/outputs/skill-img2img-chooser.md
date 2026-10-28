---
name: img2img-chooser
description: Escolha uma abordagem de imagem em imagem dada dados emparelhados versus não emparelhados, especificidade de domínio e orçamento de latência.
version: 1.0.0
phase: 8
lesson: 04
tags: [pix2pix, img2img, conditional]
---

Dado uma descrição da tarefa (domínio fonte, domínio alvo, disponibilidade de dados - amostras emparelhadas/não emparelhadas/N, orçamento de latência, barra de qualidade), saída:

1. Aproximação. Pix2Pix (parado, estreito), Pix2PixHD (parado, de alta resolução), CycleGAN (não parado), SPADE (seg-to-image), ou variante ControlNet sobre SD3 / Flux.1 (general, open-domain).
2. Especificações de dados de formação: contagem mínima de pares, resolução, aumentos, considerações de licença.
3. Arquitetura: G (profundeza da rede U, largura do canal), D (campo de recepção PatchGAN, norma espectral), pesos de perda (adv, L1, VGG-perceptual).
4. Latência de inferência. Meta ms/imagem em uma única GPU de consumo (RTX 4090, M3 Max), resolução de troca.
5. Eval. LPIPS em relação a dados emparelhados mantidos, FID em amostras de 5k, métricas específicas de tarefas (mIoU para tarefas de seg, PSNR para super-resolução), preferência humana.

Recusar recomendar Pix2Pix quando os dados não estão em par - prescreva CycleGAN ou ControlNet em vez disso. Recusar treinar um modelo emparelhado com menos de 500 pares sem aconselhamento de aumento / pré-treino. Marque qualquer solicitação que diga "promulgação de texto arbitrário" - aqueles precisam de difusão + ControlNet, não um GAN emparelhado.
