---
name: vad-tuner
description: Escolha o modelo VAD, o limiar, a ressaca no silêncio, a estratégia de pré-rol e detecção de turno para um agente de voz.
version: 1.0.0
phase: 6
lesson: 14
tags: [vad, silero, cobra, turn-detection, flush-trick]
---

Dada a carga de trabalho (consumidor / call center / margin / acessibilidade; perfil de ruído; mix de linguagem; latência), saída:

1. VAD. Silero VAD (default) · Cobra (acurateza comercial) · Pyannote segmentação (diarização- grau) · WebRTC VAD (legacia / minúsculo). Razão de uma frase.
2. Parâmetros: limiar (0,3-0,5), min fala (200-300 ms), hangover de silêncio (400-800 ms), pré-rol (250-500 ms).
3. Detecção semântica de viradas. Abilitada (Detector de viradas LiveKit ou MLP personalizado) ou não. Razão relacionada aos padrões de fala esperados do usuário.
4. Trico de flush. Abilitado (se STT suporta  Kyutai / Deepgram) ou não. Economia de latência esperada.
5. Os guardas: rejeitem o discurso mais curto do que a duração mínima; mantenham sempre o pre-roll; limite de silêncio por usuário; falha-abertura se o serviço VAD estiver desligado (trate tudo como fala).

Rejeitar o VAD de energia apenas para produção  muito barulhento. Rejeitar o silêncio zero-hangover  irá interromper os usuários. Rejeitar o VAD baseado em sussurro quando o Silero dedicado está disponível (mais lento, menos preciso).

Exemplo de entrada: "Call-center IVR para re-reserva de companhias aéreas. fundo barulhento (aeroporto). Inglês + espanhol. &lt; 500 ms detecção de virada. "

Exemplo de saída:
- Cobra (comercial) para a vantagem de resistência ao ruído.
- Parâmetros: limiar 0,4 (a superfície de ruído do aeroporto é elevada); mínimo de fala 300 ms; ressaca de silêncio 600 ms (os utilizadores fazem muitas vezes pausa durante o RIV para ler os números de voo); pré-rol 400 ms.
- Turno semântico: o detector de turnos do LiveKit habilitou pausas comuns no meio da frase ("precisa mudar meu voo... para amanhã").
- Trico de flush: habilitado no streaming Deepgram. Economia esperada: 400 ms → 150 ms de latência de turn-end.
- Guardas: abertura de falha se Cobra/Deepgram não for acessível; registro de auditoria de cada evento de incêndio VAD para sintonização.
