---
name: realtime-voice-pipeline
description: Pick transport, VAD, streaming STT, LLM, streaming TTS, and orchestration for a target end-to-end latency.
version: 1.0.0
phase: 6
lesson: 11
tags: [voice-agent, livekit, pipecat, silero, streaming, latency]
---

Dado o objetivo (latencia P50/P95, linguagem, canal, offline vs nuvem, volume de chamada), saída:

1. Transportes. WebRTC (LiveKit / Daily) · WebSocket · SIP trunking (Twilio / Telnyx). Razão ligada à tolerância ao jitter + caso de uso.
2. VAD + tomada de viradas. Silero VAD (aberto, 99,5% TPR) · Cobra (comercial) · LiveKit detector de viradas. limiar, duração mínima de fala, silêncio de morte.
3. Transmissão STT. Parakeet TDT (aberto mais rápido) · Kyutai STT (com truque de flush) · Deepgram Nova-3 (API, ~ 150 ms) · Whisper-streaming. Razão.
4. LLM + streaming. Pin os primeiros 20 tokens antes de TTS entrar em vigor. Modelo + streaming config + guardrails para injeção rápida.
5. Transmissão de TTS. Kokoro-82M (~ 100 ms TTFA) · Orpheus · Cartesia Sonic · ElevenLabs Turbo.
6. Orquestração. Agentes LiveKit · Pipecat · Vapi · Retell · personalizado Rust. Razão ligada às habilidades da equipe + escala.
7. Observabilidade: histogramas P50/P95/P99 por fase; taxa de interrupção falsa positiva; taxa de chamadas descartáveis; WER em amostras de chamadas.

Rejeitar implementa que buffer declarações inteiras antes de STT. Rejeitar TTS que não fluem. Rejeitar avaliação por latência média  requer P95. Rejeitar plataformas gerenciadas (Vapi / Retell) por &gt; 100k minutos / mês sem uma comparação de custos para construir-o seu próprio.

Exemplo de entrada: "Agente de voz para a citação de seguro de carro. &lt; 500 ms P95. Inglês, EUA. 50k minutos / semana. Conformidade: HIPAA-adjacente (sem PII em registros). "

Exemplo de saída:
- Transporte: Agentes LiveKit + Twilio SIP. Proveído em escala de call center, modo HIPAA opt-in.
- Silero VAD @ limiar 0,45, min fala 220 ms, silêncio pendurado 400 ms. Superposição do detetor de viradas LiveKit.
- STT: Deepgram Nova-3 Inglês (~ 150 ms P95); retorno para Parakeet-TDT se for necessária uma auditoria no local.
- LLM: GPT-4o streaming através da API em tempo real OpenAI; proteção contra injeção rápida com um pós-filtro; pin primeiro 20 tokens para TTS.
- TTS: Cartesia Sonic 2 (~ 150 ms TTFA, clonagem de voz não utilizada  voz predefinida).
- Orquestração: Agentes LiveKit. Observabilidade através de Hamming AI para produção.
- Registros: desprenda CVV / SSN / DOB com um regex + NER antes da persistência.
