---
name: audio-loader
description: Validar um arquivo de áudio bruto contra as expectativas de um modelo-alvo e repensá-lo com segurança.
version: 1.0.0
phase: 6
lesson: 01
tags: [audio, speech, preprocessing]
---

Dado um arquivo de áudio (caminho, canais, taxa de amostragem, profundidade de bits, codec) e um modelo-alvo (ASR / TTS / classificador com taxa de amostragem e contagem de canais necessários), saída:

1. Descoincidências. Enumera todas as dimensões em que o arquivo não corresponde ao alvo (sr, canais, piso de duração, verificação de clipping).
2. Plano de re-exemplação.`torchaudio.transforms.Resample` ou `librosa.resample`), tipo de filtro antialiasing.
3. Plano de canal: estratégia de pligação mono (média vs. esquerda apenas), ou passagem de vários canais quando o modelo o suporta.
4. Normalização, Pico vs RMS normalização, alvo dBFS, proteção de corte.
5. Python que carrega o arquivo, executa as transformações e afirma que a matriz final coincide `(target_sr, dtype, channel_count, range)`- Não .

Recusar a amostragem inferior sem um filtro antialiasing. Recusar a amostragem superior a 2x sem um filtro de reconstrução. Marcar qualquer arquivo de entrada com picos de corte acima de ± 0,999 ou uma compensação de DC acima de ± 0,01.
