---
name: var-tokenizer-designer
description: Design a multi-scale residual VQ tokenizer for next-scale visual autoregressive image generation.
version: 1.0.0
phase: 8
lesson: 19
tags: [var, next-scale-prediction, vq-vae, residual-vq, image-generation, tokenizer]
---

Dado o objetivo da imagem (resolução, canais, cor vs escala de cinza, tamanho do conjunto de dados, orçamento de computação LM a jusante, FID-alvo), saída:

1. Escala de escala. Lista os níveis de resolução K de 1x1 até (H/p) x (W/p). Escala de 10 por defeito para 256x256, 14 para 512x512. Justifique K contra o comprimento da sequência efetiva do LM (suma das áreas de escala) e o orçamento paralelo paralelo dentro da escala.
2. Código de código. Compartilhado único tamanho de código de código V em todas as escalas (típico 4096 / 8192 / 16384). escolha V do tamanho do conjunto de dados e capacidade de decodificador.
3. Compartilhamento residual. Confirme que as escalas 1..K juntas reconstruem o latente através de incorporados de amostragem somada (VQ residual). Indique o tamanho do parche p e a espinha dorsal de VAE (discriminador de tipo VQGAN, peso de perda perceptiva).
4. Decodificador. O decodificador VAE sumou o latente de volta para pixels. Escolha entre o decodificador VQGAN, o decodificador de papel VAR ou um decodificador de estilo MAGVIT mais leve. Justifique contra o alvo FID e o decodificador VRAM.
5. Embedamento de posição. Confirme (escala_index, linha, col) triplo com um embedamento aprendido por escala e um sin-cos 2D dentro da escala. Rejeita posições 1D planas; o LM precisa do rótulo da escala para aplicar o condicionado certo.

Recusar um tokenizer de várias escalas não residual para VAR. Sem resíduos somados, a condicional de próxima escala fica mal definida e o LM otimiza um objetivo diferente do que o documento prova. Recusar os codesbook separados por escala, a menos que o V seja calibrado para a contagem de pixels da escala menor e o colapso do codesbook seja mitigado. Rejeitar a previsão de próxima escala quando K x área média de escala exceder o comprimento máximo da sequência do LM menos espaço para condicionamento de texto.

Introdução de exemplo: "ImageNet 256x256 condicional para a classe, conjunto de dados 1.2M, parâmetros do orçamento LM 1.5B, FID alvo abaixo de 5.0."

Exemplo de saída:
- Escala de programação: K=10, tamanhos 1, 2, 3, 4, 5, 6, 8, 10, 13, 16.
- Código: compartilhado, V=4096.
- Partilha residual: confirmada; p=16, espinha dorsal VQGAN com perdas perceptivas + adversárias, reconstruções da soma residual f.
- Decodificador: Decodificador VQGAN, 4 blocos de amostragem, sem refinador extra.
- Embedamento de posição: (escala, linha, col) triplo, token de escala aprendido + sin-cos 2D dentro da escala.
