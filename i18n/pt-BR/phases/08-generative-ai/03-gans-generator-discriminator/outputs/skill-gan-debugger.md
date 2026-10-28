---
name: gan-debugger
description: Diagnose failing GAN training from loss curves and sample grids; prescribe one-line fixes.
version: 1.0.0
phase: 8
lesson: 03
tags: [gan, adversarial, debugging]
---

Dado um GAN de execução falha (curvas de perda D e G, rede de amostra, tamanho do conjunto de dados, configuração do optimizador), saída:

1. Uma causa fundamental: colapso do modo, D muito forte, D muito fraco, gradiente desaparecendo, vazamento da norma de lote, overfit D, desajuste da taxa de aprendizagem, mau início.
2. Evidência: indicação do indicador nas curvas de perda ou amostras (por exemplo, "D(falsa) &lt;0,05 por passo 500 = D muito forte").
3. Correcção, uma alteração concreta.`lr_D = lr_G / 2`, substituir BN por IN, adicionar a norma espectral para D, mudar para WGAN-GP com lambda=10, cortar o tamanho do lote em 2, adicionar 0,1 ruído gaussiano para as entradas de D.
4. Protocolo de reavaliação: sementes a tentar, número de etapas antes da reavaliação, critério de aceitação (por exemplo, "FID cai abaixo da linha de base em 20k").
5. Fallback. Se a correção não aterrar em uma repetição, o que tentar a seguir. Geralmente: alterar arquitetura (StyleGAN, R3GAN) ou mudar paradigma (difusão, correspondência de fluxo) se o conjunto de dados é muito diversificado.

Recusar recomendar aumentar a taxa de aprendizagem de G quando D já está saturado. Recusar adicionar regularização a G quando a falha real é D - corrigir D primeiro. Marcar qualquer corrida que mostre o colapso do treinamento dentro de 100 passos como provável que inicie ou explode mal, não um problema algorítmico profundo.
