---
name: sd-prompter
description: Configure Stable Diffusion / Flux inference for a given prompt, style, and quality bar.
version: 1.0.0
phase: 8
lesson: 07
tags: [stable-diffusion, flux, latent-diffusion]
---

Dado um prompt, estilo de destino e barra de qualidade (previsão rápida / qualidade do portfólio / pronto para impressão), saída:

1. Modelo + ponto de verificação. SD 1.5 (ferramentas legadas), SDXL-base + refinador, SDXL-Turbo (rápido), SD3.5-Large, Flux.1-dev (melhor aberto), Flux.1-schnell (rápido aberto), ou uma API hospedada (DALL-E 3, Imagen 4, Midjourney v7). Razão de uma frase.
2. Amostra. Euler A (criativo), DPM-Solver++ 2M Karras (estavel), LCM (rápido) ou amostra de correspondência de fluxo (SD3/Flux).
3. Escala CFG. 0 para turbo / LCM, 3-4 para Flux, 5-7 para SDXL, 7-10 para SD1.5. Documente a compensação.
4. ControleNet (posição, profundidade, canny, seg), IP-Adapter (imagem de referência), LoRA (estilo ou assunto), T5 toggle para SD3+.
5. Indicações de ordem negativa. Explicitação de uma cadeia vazia versus conteúdo preenchido (artefactos, baixa qualidade, anatomia errada); especifique ambas.

Rejeitar CFG &gt; 10 para SDXL + (output saturado). Rejeitar &gt; 50 passos de amostragem em pontos de verificação não legados (plateaus de qualidade por 30). Rejeitar misturar LoRAs treinados em diferentes modelos base (SD 1.5 LoRA em SDXL é silenciosamente quebrado). Marque qualquer solicitação para humanos fotorrealistas sem um lembrete sobre NSFW, deepfake e política de direitos autorais.
