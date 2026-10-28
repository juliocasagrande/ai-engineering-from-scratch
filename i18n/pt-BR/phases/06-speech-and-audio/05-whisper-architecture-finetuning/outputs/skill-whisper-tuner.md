---
name: whisper-tuner
description: Design a Whisper fine-tune or inference pipeline for a given language, domain, and latency budget.
version: 1.0.0
phase: 6
lesson: 05
tags: [audio, whisper, asr, fine-tuning, lora]
---

Dado um alvo (conjunto de linguagem, domínio, distribuição de comprimento de clip, orçamento de latência, hardware) e dados (horas disponíveis, qualidade), saída:

1. Variante: pequeno/base/ pequeno/médio/ grande v3/ turbo.
2. Tempo de execução. vanilla / mais rápido sussurro / sussurro / sussurro streaming. Razão.
3. Plano de sintonia: Full-FT vs LoRA (r, target_modules), política de congelamento de codificação, contagem de épocas.
4. Guarda de Inferência, VAD.`temperature=0`- Não .`condition_on_previous_text=False`- Não .`no_speech_threshold`- Não .
5. Avaliação, alvo do domínio WER, regras de normalização de texto, controlo de taxa de alucinação em clips de silêncio.

Recusar a implantação de Whisper em áudio arbitrário sem VAD. Recusar a configuração `condition_on_previous_text=True`Para empregos de vários pedaços sem um guarda fugitivo, marca qualquer sintonia que troque o tokenizer do Whisper ou o pipeline do Mel.
