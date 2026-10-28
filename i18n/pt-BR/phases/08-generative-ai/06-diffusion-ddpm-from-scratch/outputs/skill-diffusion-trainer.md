---
name: diffusion-trainer
description: Configurar uma execução de treinamento de difusão: cronograma, meta de previsão, amostragem e plano de avaliação.
version: 1.0.0
phase: 8
lesson: 06
tags: [diffusion, ddpm, training]
---

Dado um perfil do conjunto de dados (modalidade, resolução, tamanho do conjunto de dados), orçamento de cálculo (horas de GPU, piso VRAM) e barra de qualidade (alvo de utilização do FID ou uso a jusante), saída:

1. Lista: Linear, cosino (Nichol) ou sigmoide. Número de etapas T (1000 para linha de base do DDPM; 256 para variantes mais rápidas).
2. Objetivo de previsão. epsilon, v-predicção, ou x_0. Razão ligada à resolução e sinal-ruído em todo o cronograma.
3. Arquitetura. Profundeza de rede U + largura de canal para difusão de pixels, DiT para difusão latente ou 3D U-Net / DiT para vídeo. Incluir esquema de inserção de tempo (sinusoidal + MLP, FiLM ou AdaLN).
4. Próprio: DDIM (20-50 passos), DPM-Solver++ (10-20), Euler-A (criativo) ou destilado 1-4 passos. Inclua a recomendação de escala de orientação (CFG w).
5. Plano de avaliação: FID/KID/CLIP-score/human-preferência, com conteúdo de amostras (>=10k para FID), protocolo de varredura para CFG w.

Recusar-se a recomendar o treinamento de difusão de pixels-espaço em &gt;=256x256 quando a difusão latente atinge a mesma qualidade em 1/16 das FLOPs. Recusar-se a enviar um modelo sem CFG para geração condicional - amostras incondicionais de um modelo condicional são geralmente degeneradas. Marque qualquer cronograma com beta_T &gt; 0,1 como provável de produzir treinamento saturado ou instável.
