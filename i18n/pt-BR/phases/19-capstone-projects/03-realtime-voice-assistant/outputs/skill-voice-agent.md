---
name: voice-agent
description: Construa um agente de voz em tempo real com o primeiro som de sub-800ms, o manejo de barge-in e o uso de ferramentas de conversação no meio.
version: 1.0.0
phase: 19
lesson: 03
tags: [capstone, voice, webrtc, livekit, pipecat, asr, tts, streaming]
---

Dado um domínio (suporte ao cliente, agendamento, assistente de varejo), implantar um agente de voz WebRTC que mantém o primeiro áudio de ponta a ponta abaixo de 800ms enquanto lida com barge-in, chamadas de ferramentas e perda de pacotes.

Construir um plano:

1. Instale uma sala LiveKit Agents 1.0 com um cliente web que transmite áudio do microfone. Adicione um gateway Twilio PSTN para cobertura telefônica.
2. Execute o streaming ASR (Deepgram Nova-3 hospedado ou mais rápido-murmurmurando Whisper-v3-turbo em um g5.xlarge).
3. Execute Silero VAD v5 em quadros de 20 ms. No final da fala, marque a última parcela com o detector de viradas LiveKit; comprometa-se a completar a virada somente quando o silêncio VAD >= 500 ms e a pontuação de conclusão >= 0,6.
4. Transmitir o LLM (GPT-4o em tempo real, Gemini 2.5 Flash Live, ou Claude Haiku 4.5).
5. Stream TTS (Cartesia Sonic-2 ou ElevenLabs Flash v3).
6. Barge-in: quando o VAD detecta uma nova fala do usuário durante a fala ou pensamento, cancelar o TTS, eliminar o resultado restante do LLM, re-armar o ASR. Publicar um `tts_canceled` - Espanha.
7. Canal lateral da ferramenta: função de execução liga simultaneamente; se a latência > 300ms, emitir um preenchimento de reconhecimento para que o fluxo de áudio nunca parem.
8. Gravar 100 chamadas. Medir WER contra transcrições mantidas, taxa de corte falso no Hamming VAD benchmark, primeira saída de áudio p50, NISQA MOS, e comportamento abaixo de 3% de queda de pacotes.
9. Teste de carga 50 chamadas simultâneas em um único g5.xlarge com um chamador sintético; relatório de primeira saída de áudio sustentada p95.

Rubrico de avaliação:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | End-to-end latency | p50 first-audio-out under 800ms across 100 recorded calls |
| 20 | Turn-taking quality | False-cutoff rate under 3% on the Hamming VAD benchmark |
| 20 | Tool-use correctness | Mid-conversation tool calls return correct data without stalling audio |
| 20 | Reliability under packet loss | WER and turn-taking stability with 3% packet drop injected |
| 15 | Eval harness completeness | Reproducible measurements with public config |

Rejeitos duros:

- As linhas de condução não fluidizadas (batch ASR, batch TTS) não podem atingir o objetivo de latência.
- Qualquer política de barge-in que não cancele o buffer TTS imediatamente.
- As chamadas de ferramentas que bloqueiam sincronicamente o fluxo LLM devem ser executadas num canal lateral.

Regras de recusa:

- Recusar-se a implantar sem um VAD ou um detector de viradas.
- Recusar-se a comunicar o MOS sem documentar se é avaliado pelo ser humano ou por NISQA.
- Recusar-se a relatar "p50 latencia abaixo de X" sem pelo menos 100 chamadas gravadas e publicar os rastros de chamadas.

Resultado: um repo contendo o agente LiveKit, a configuração do gateway PSTN, o harness de avaliação de 100 chamadas, um painel de voz público Langfuse, uma comparação lado a lado com um concorrente hospedado (Retell, Vapi ou OpenAI Realtime API diretamente), e uma descrição das três maiores falhas de tomada de turno que você observou e o sintonização do detector que corrigia cada uma.
