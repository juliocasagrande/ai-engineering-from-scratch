---
name: stylegan-inversion
description: Escolha um canal de inversão e edição para um StyleGAN pré-treinado em vez de uma foto real.
version: 1.0.0
phase: 8
lesson: 05
tags: [stylegan, inversion, editing]
---

Dado uma foto real + um checkpoint StyleGAN pré-treinado (FFHQ-1024, StyleGAN-XL, um ajuste fino personalizado) e edição de alvo (idade, sorriso, postura, cabelo, preservação da identidade), saída:

1. Método de inversão. e4e (rápido, baixa fidelidade), ReStyle (encoder iterativo), HyperStyle (hipernet), PTI (ajuste pivotal), ou direita W-optimização. Razão de uma frase ligada à fidelidade vs velocidade.
2. Espaço alvo. W, W+, ou StyleSpace. Trade-offs: W = mais desentralado mas menor fidelidade, W+ = por camada w, StyleSpace = nível de canal.
3. Direção de edição. Fonte de direção nomeada: InterFaceGAN (baseado em SVM), canais StyleSpace, GANSpace PCA ou um classificador aprendido.
4. Orçamento de fidelidade: limiar de LPIPS antes da deriva de identidade; heurística de retrocesso.
5. Eval. Identificação de semelhança (ArcFace cosine), LPIPS para original, força de edição (escore de classificador de atributo-alvo).

Rejeitar qualquer pipeline que edite diretamente em Z (enredado). Rejeitar grandes edições (&gt;1.5 sigma em W) sem verificações de identidade. Flag requisites que precisam de edição de domínio aberto (por exemplo, "fazê-lo um desenho animado") - aqueles exigem difusão + IP-Adapter, não StyleGAN.
