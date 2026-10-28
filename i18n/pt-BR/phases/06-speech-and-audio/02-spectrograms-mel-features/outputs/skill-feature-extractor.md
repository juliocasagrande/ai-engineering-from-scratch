---
name: feature-extractor
description: Pick feature type, mel count, frame/hop, and normalization to match a downstream audio model.
version: 1.0.0
phase: 6
lesson: 02
tags: [audio, features, spectrogram, mel]
---

Dado um modelo-alvo (ASR / TTS / classificador / alto-falantes / música) e áudio de entrada (taxa de amostragem, domínio), saída:

1. Tipo de recurso: log-mel, mel, MFCC, forma de onda crua ou codec discreto (EnCodec, SoundStream). Razão de uma frase.
2. Contagem de mel e intervalo de frequência.`n_mels`- Não .`fmin`- Não .`fmax`- Razão ligada ao domínio (discurso versus música) e ao modelo-alvo.
3. Enfrente e salta.`frame_len`- Não .`hop_len`Razão ligada à resolução temporal necessária.
4. Normalização: média/var por pronunciamento, estatísticas globais ou dB com referência fixa; pré ou pós-featurization.
5. Python que imprime a forma resultante, min/max, média/std em um clip de referência de 1 segundo e afirma que correspondem ao treinamento.

Recusar-se a enviar um pipeline de recursos cuja contagem de quadros/hop/mel diverge da configuração de treinamento publicada do modelo alvo. Marque qualquer configuração baseada no MFCC para Whisper ou Parakeet como errada  esses modelos consomem log-mel. Marque qualquer extractor de recursos sem uma afirmação de normalização.
