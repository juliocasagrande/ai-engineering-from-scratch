---
name: codec-picker
description: Escolha um codec de áudio neural (EnCodec / DAC / SNAC / Mimi) para uma determinada tarefa de geração ou compressão.
version: 1.0.0
phase: 6
lesson: 13
tags: [codec, encodec, dac, snac, mimi, rvq, semantic-tokens]
---

Dado o trabalho (LM gerador, compressão, diálogo duplex completo, edição de música, objetivo de fidelidade), saída:

1. Código: EnCodec-24k · EnCodec-48k · DAC-44.1k · SNAC-24k · Mimi · (falta: Opus para compressão não neural). Razão de uma frase.
2. Taxa de quadros + codes. Orçamento de bitrate, contagem de codes (geralmente 4-12), comprimento de sequência para a duração do clipe alvo.
3. Esquema de tokenization. plano versus hierárquico (SNAC) versus semântico + acústico (Mimi). Como o LM consome tokens.
4. Decodificador. Decodificador de codec interno · Vocoder externo (HiFi-GAN) · LM-só (sem vocoder, previsão de tokens de codec diretamente).
5. Implicações do treinamento. Precisa de treinar codificador/decodificador? sintonização no áudio do domínio (somente fala → música específica do domínio)? congelado fora da prateleira?

Rejeitar DAC para cargas de trabalho AR-LM em orçamentos de latência apertados  86 Hz taxa de quadros × 8 codebooks = 5.504 tokens por 10 segundos, muito tempo para geração rápida. Rejeitar Mimi para música  é sintonizado com fala. Rejeitar EnCodec para geração semântica-condicional  nenhum codebook semântico, fala borrosa do texto.

Exemplo de entrada: "Construir um LM AR para TTS de texto a fala.

Exemplo de saída:
- Códek: Mimi. Divisão semântica + acústica permite a fatorização de texto → livro de códigos 0 → livro de códigos 1-7, que é rápida e suporta a clonagem de voz.
- Frequência de quadros + codes: 12,5 Hz · 8 codes · 4,4 kbps. 10 s = 1.000 tokens.
- Tokenization: prever o livro de código 0 primeiro a partir de texto + referência de alto-falantes; então prever os livros de código 1-7 dado livro de código 0 + referência de alto-falantes (patrão de profundidade-transformador).
- O decodificador da Mimi, sem vocoder externo.
- Treinamento: treinar o LM de texto a codec; congelar Mimi.
