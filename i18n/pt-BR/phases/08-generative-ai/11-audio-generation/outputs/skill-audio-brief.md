---
name: audio-brief
description: Traduza um resumo de áudio em um modelo + prompt + plano de avaliação em TTS, música e SFX.
version: 1.0.0
phase: 8
lesson: 11
tags: [audio, tts, music, sfx, codec]
---

Dado um resumo de áudio (tarefa: TTS / música / SFX / clone de voz, duração, estilo, voz ou gênero, restrições de licença, em tempo real ou offline, barra de qualidade), saída:

1. Modelo + hospedagem. ElevenLabs V3, OpenAI TTS, XTTS v2, Suno v4, Udio, Stable Audio 2.5, MusicGen 3.3B, AudioCraft 2, ou GPT-4o em tempo real. Razão de uma frase.
2. Formatos de vídeo. TTS: texto + vídeo de voz (3-10 s sample ou ID de voz) + emoção / ritmo tags. Música: gênero + instrumentação + humor + BPM + marcadores estruturais. SFX: onomatopéia + fonte + indicação de duração.
3. Nomear o codec específico (Encodec 32 kHz, DAC 44 kHz, personalizado) e a escolha do gerador (token-AR vs flow-matching).
4. Semente + reproducibilidade. Pin de semente, pin de versão, hash de ponta.
5. Eval. MOS (score médio de opinião) ou A/B para TTS, CLAP score para música, CER para transcrição TTS, teste de audição do usuário para SFX.
6. Guardrails: consentimento de clone de voz + marca de água (PerTh / SynthID-audio), digitalização de direitos autorais na saída de música, verificação de políticas de dados de treinamento.

Recusar-se a clonar qualquer voz sem o consentimento verificado do proprietário (a "pronto de 3 segundos" da era da cassete não é consentimento). Recusar-se a enviar música com material de referência não licenciado. Marque qualquer alvo em tempo real &lt; 200 ms que não use um modelo de token-AR de streaming - áudio baseado em difusão não pode atender a sub-300 ms TTFB em 2026.
