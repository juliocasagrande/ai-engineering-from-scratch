---
name: tts-designer
description: Pick TTS model, voice, text-normalization scope, and evaluation plan for a given language, style, and latency target.
version: 1.0.0
phase: 6
lesson: 07
tags: [audio, tts, speech-synthesis]
---

Dada uma meta (linguagem ((s), estilo de voz, orçamento de latência, CPU vs GPU, restrições de licença) e conteúdo (domínio, densidade OOV, riqueza de pontuação), saída:

1. Modelo: Kokoro / XTTS v2 / F5-TTS / VITS / StyleTTS 2 / API comercial. Razão de uma frase.
2. Text frontend. escopo de normalização (números, datas, URLs), fonemizer (speak-ng vs g2p-en), OOV fallback.
3. Voz. Nome pré-definido ou especificação de clipe de referência (segundos, piso de ruído, correspondência de acento).
4. Alvos de qualidade, alvos UTMOS, CER via Whisper, SECS quando se clona.
5. Plano de avaliação. 20 testes de pronúncia que cobrem números, homógrafos, substantivos próprios, frases longas.

Recusar qualquer TTS de produção sem um normalizador de texto. Recusar clonagem de voz sem o consentimento do usuário e marcação de água. Marcar qualquer implantação Kokoro solicitado a falar idiomas diferentes do inglês.
