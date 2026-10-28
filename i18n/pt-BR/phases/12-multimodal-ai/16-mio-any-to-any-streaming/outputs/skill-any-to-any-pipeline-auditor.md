---
name: any-to-any-pipeline-auditor
description: Auditar um design de conversação qualquer-a-qualquer e calcular o orçamento de latência para uma pilha de família MIO / AnyGPT / Moshi.
version: 1.0.0
phase: 12
lesson: 16
tags: [mio, anygpt, moshi, any-to-any, streaming, ttfab]
---

Dado um produto de conversação (discurso / fala fora, visão opcional, música opcional), um tamanho do modelo e uma latência de destino, auditem o design de qualquer um e produzam uma configuração viável.

Produzir:

1. MIX de modalidades. Que modalidades, que fora. Família de escolha: MIO / AnyGPT (tokens discretos, 4 modalidades), Moshi (discurso + texto focado, monólogo interno), Unified-IO 2 (rico de visão).
2. Plano de vocabulário compartilhado. Áreas de identificação para texto + imagem + fala + música + separadores. Tamanho total tipicamente 40-50k.
3. Estaca de tokenizer. BPE + SEED + SpeechTokenizer-RVQ + Encodec. Destaque que ainda são gargalos de engarrafamento (qualidade de fala tipicamente).
4. Currículo de treinamento. Receita de quatro etapas MIO, ou duas etapas para Moshi focado na fala.
5. TTFAB orçamento de latência. Mic encoder + prefill + primeiro token + decodificação residual + decodificador de voz. Compare com ~ 500ms bar de conversação.
6. Pareto qualidade versus latência: modelo menor para baixa latência, maior para qualidade superior; números aproximados por A100/H100.

Rejeitos duros:
- Proporcionar modelos separados por modalidade quando o requisito é fluidez conversacional.
- Usando um tokenizer de voz com apenas uma camada de código.
- A afirmação de que o TTFAB do MIO corresponde ao GPT-4o. Ainda não; Moshi 160ms é o número aberto mais próximo.

Regras de recusa:
- Se atingir TTFAB < 200ms, recuse-se a escala MIO (8B+) e recomenda a classe Moshi (7B, sintonizada para fala) ou um modelo especializado em fala menor.
- Se o usuário quiser uma saída de voz de qualidade de estúdio, recuse-se a abertura residual-VQ e recomenda ElevenLabs / chained-TTS até que a qualidade aberta se recupere (Qwen3-Omni / Moshi2).
- Se o usuário quiser geração de imagem durante uma chamada de voz, recuse-se ao streaming-speech-first e propor um pipeline dividido com comutação de modo.

Resultado: auditoria de uma página com mix de modalidade, plano de vocabulário, stack de tokenizer, currículo, latência TTFAB, pareto de latência de qualidade.
