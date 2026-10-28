---
name: voice-pipeline
description: Scaffold a Pipecat-shaped voice pipeline (VAD + STT + LLM + TTS + transport) with barge-in, confidence gating, and latency budget enforcement.
version: 1.0.0
phase: 14
lesson: 22
tags: [voice, pipecat, livekit, webrtc, latency]
---

Dado um produto de voz (linguagem, transporte, fornecedores), estabeleça um esquadrão de canalização baseado em quadros.

Produzir:

1. `Frame`Tipo com `kind`- Não .`payload`- Não .`direction`(a jusante / a jusante).
2. Processadores: `VAD`- Não .`STT`- Não .`LLM`- Não .`TTS`- Não .`Transport`Cada um com .`process(frame)`- Não .
3. `link()`auxiliar de encadeamento dos processadores para frente e para trás.
4. Manutenção de quadros de cancelamento: caminho UPSTREAM do transporte para TTS para LLM para STT, deixando de lado o trabalho pendente em cada etapa.
5. Observadores: métricas de latência por fase; emitir um tempo de OTel por quadro atravessando um processador (Lessão 23).
6. Portais de confiança em STT: abaixo do limiar, emitir um quadro de texto "por favor repita" em vez de transcrição.

Rejeitos duros:

- O transporte de pipeline sem a manipulação UPSTREAM.
- As chamadas de LLM sem streaming.
- A transcrição errada para o LLM produz respostas erradas.

Regras de recusa:

- Se a latência de ponta a ponta exceder 1500ms em uma corrida fria, recuse-se a enviar. Optimize a cadeia ou use um MultimodalAgent (LiveKit direct-audio).
- Se o produto for de primeira linha e o tubo não tiver adaptador SIP, recuse-se.
- Se o produto transportar áudio de PII sem criptografia em trânsito, recusar.

Output: `frames.py`- Não .`processors.py`- Não .`pipeline.py`- Não .`observers.py`- Não .`README.md`A conclusão é com "o que ler a seguir" apontando para a lição 23 (OTel), lição 24 (backends de observabilidade) ou os documentos LiveKit para especificações WebRTC.
