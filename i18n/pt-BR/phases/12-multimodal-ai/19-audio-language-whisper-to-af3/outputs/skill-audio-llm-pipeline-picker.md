---
name: audio-llm-pipeline-picker
description: Escolha cascada (Whisper + LLM) ou end-to-end (AF3 / Qwen-Audio) para uma tarefa de áudio, além do codificador e da configuração de ponte.
version: 1.0.0
phase: 12
lesson: 19
tags: [whisper, audio-flamingo-3, qwen-audio, cascaded, end-to-end]
---

Dada uma tarefa de áudio (transcrição, resumo, diário, emoção, música, sons ambientais, deepfake, grounding temporal) e uma restrição de implantação, escolha um pipeline e emite uma configuração.

Produzir:

1. Seleção de canalização. Cascada se apenas transcrição ou somente resumo de fala limpa; extremo a extremo (AF3 / Qwen-Audio) para qualquer tarefa acústica.
2. Estaca de codificação: Whisper-large-v3 (voz forte), BEATs (música forte), AF-Whisper concat (equilibrado).
3. Configuração de ponte. Q-ex 32-64 consultas para não-streaming; RVQ tokens para streaming.
4. Qwen2.5-7B pelo custo, Qwen2.5-72B ou AF3's backbone pela qualidade.
5. CoT sob demanda: Abilitação de tarefas de raciocínio semelhantes à MMAU; desativação de transcrição.
6. MMAU esperava precisão. Cascaded ~0.50, Qwen-Audio ~0.60, AF3 ~0.72, Gemini 2.5 Pro ~0.78.

Rejeitos duros:
- Recomendação de cascata para tarefas musicais ou emocionais.
- Usando um Q-former com <32 consultas para áudio multi-tarefa.
- A Whisper só lida com música, foi treinado com dados dominantes da fala.

Regras de recusa:
- Se o usuário precisar de streaming de áudio de conversação (falar / falar em tempo real), recuse o AF3 baseado no Q anterior e recomenda Moshi ou Qwen-Omni (Lessão 12.20).
- Se o orçamento de latência <500ms e o objetivo é uma transcrição simples, recomendamos cascada com streaming Whisper.
- Se a tarefa for uma tarefa de áudio nova (deepfake, detecção de artefatos de compressão), rejeite o off-the-shelf e propor uma melhora da AF3 com dados sintéticos.

Resultado: plano de uma página com escolha de pipeline, stack de codificadores, config de ponte, escolha de LLM, bandeira CoT, precisão esperada.
