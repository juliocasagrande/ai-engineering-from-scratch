---
name: vae-trainer
description: Especificar a arquitetura do VAE, o tamanho latente, o cronograma beta e o plano de avaliação para um determinado conjunto de dados e uso a jusante.
version: 1.0.0
phase: 8
lesson: 02
tags: [vae, latent, generative]
---

Dado um perfil de conjunto de dados (modalidade, resolução, tamanho do conjunto de dados) e a utilização posterior (apenas reconstrução, amostragem ou codificação de entrada para um modelo de difusão latente ou token-AR), a saída:

1. Variante: VAE simples, beta-VAE, VQ-VAE, RVQ (residual) ou NVAE. Razão de uma frase ligada à modalidade e ao uso a jusante.
2. Arquitetura. Topologia de codificação/decodificação (conv downsample factor, largura do canal, dim oculto, blocos de atenção).`sd-vae-ft-ema`, Encodec, DAC, WAN-VAE) quando aplicável.
3. Dim latente, dim espacial e de canal, bits totais por amostra, relação de compressão contra os dados brutos.
4. Programação beta, rampas de aquecimento, valor final e limiar de bits livres se usados.
5. Planos de Eval. Reconstrução MSE/SSIM/PSNR, KL por dim, contagem de dim ativo, limiar de alarme de colapso posterior, distância Frechet entre `q(z|x)` E antes.

Recusar-se a enviar um VAE com beta > 0,5 no início do treinamento (desintegração posterior). Recusar-se a usar um VAE Gaussian simples como gerador final para imagens - ele será borroso; usá-lo como um codificador latente para um modelo de difusão ou de correspondência de fluxo em vez disso. Marque qualquer VQ-VAE com uso de código de menos de 20% como uma política de reset de código de código de configuração errada.
