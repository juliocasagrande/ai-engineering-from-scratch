---
name: token-gen-cost-analyzer
description: Compute contagens de tokens, latência de inferência e teto de qualidade para a próxima geração de tokens em estilo Emu3 e escolha entre a família Emu3 e difusão.
version: 1.0.0
phase: 12
lesson: 12
tags: [emu3, next-token-prediction, video-gen, diffusion, cfg]
---

Dada uma especificação de produto de geração (imagem ou vídeo, resolução-alvo, nível de qualidade, exigência de throughput), os tokens de cálculo contam para a próxima geração de tokens de estilo Emu3, estimam o custo de inferência e escolhem entre a família Emu3 e a difusão.

Produzir:

1. Contagem de tokens. Tokens por imagem na redução do tokenizer escolhido (normalmente 8x por dim para imagem). Tokens por vídeo com VQ 3D (normalmente 4 quadros x 8x8 pixels por token).
2. Latência de inferência. Tokens / throughput (tokens por segundo) para família Emu3; denoise-steps * step-time para difusão. Cite os intervalos de concreto A100 / H100.
3. O valor máximo de qualidade: reconstituição do tokenizer PSNR (30-32 dB para a classe IBQ), expectativas de FID para a MJHQ-30K, FVD para o vídeo.
4. Configuração CFG: peso de orientação recomendado (gamma) por tarefa; típico 3.0 para gen padrão, 5-7 para adesão rápida forte.
5. Selecionar. Família Emu3 se o produto precisar de compreensão unificada + geração ou flexibilidade de qualquer modalidade; difusão (SDXL / SD3 / Flux) se o produto é apenas de geração de imagem com latência rigorosa.

Rejeitos duros:
- A afirmação de Emu3 é mais rápida do que a difusão em inferência.
- Recomendo a família Emu3 sem especificar o peso do CFG.
- Propondo Emu3 para geração de imagens 4K rigorosa.

Regras de recusa:
- Se o orçamento de latência for < 5s por imagem, recuse o Emu3 e recomenda SDXL ou SD3.
- Se o produto deve emitir imagens E descrevê-las E raciocinar sobre imagens de terceiros, recomenda a família Emu3 (a perda unificada é o ponto); a difusão não pode fazer isso sem um VLM separado.
- Se o usuário quiser pesos abertos com licença permisiva para uso comercial, recuse-se a verificar a licença em primeiro lugar; algumas versões são apenas de pesquisa.

Resultado: análise de uma página com contagens de tokens, estimativas de latência, teto de qualidade, configuração CFG e uma escolha com justificação.
