---
name: asr-picker
description: Escolha o modelo ASR, estratégia de decodificação, fragmentação e fusão LM para um determinado alvo de implantação.
version: 1.0.0
phase: 6
lesson: 04
tags: [audio, asr, speech-recognition]
---

Dado um objetivo de implantação (lista de linguagem, domínio, orçamento de latência, hardware, offline / streaming, duração do clipe), saída:

1. Modelo: Whisper-large-v3-turbo / Parakeet-TDT / Canary-Flash / wav2vec 2.0 / Moonshine. Razão em uma frase.
2. Decodificação: ganância / largura do feixe / temperatura de queda / peso de fusão LM. Razão ligada ao orçamento de qualidade.
3. Duração, passo, seja para o Silero-VAD ou para o Whisper.
4. Política de linguagem. Língua de força vs auto-LID; como lidar com quadros interlinguais.
5. Planos de Eval, WER no set de testes de domínio, cobertura por alto-falantes, taxa de alucinação em clips de silêncio.

Recusar qualquer implantação de Whisper de forma longa sem gating VAD (alucinação em silêncio). Recusar-se a relatar WER sem normalização de texto (camada inferior, punctada). Marque qualquer largura de feixe > 16 sem um LM; feixes crus sobre espaços vazios não ajudam.
