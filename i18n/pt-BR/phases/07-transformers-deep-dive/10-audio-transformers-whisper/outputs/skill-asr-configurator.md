---
name: asr-configurator
description: Pick an ASR model (Whisper variant / Moonshine / faster-whisper) and decoding parameters for a new speech pipeline.
version: 1.0.0
phase: 7
lesson: 10
tags: [transformers, whisper, asr, speech]
---

Dada uma tarefa de fala (transcrição / tradução / streaming / no dispositivo), linguagem (s), características de áudio (ruído, sotaque, duração) e metas de latência / qualidade, saída:

1. Uma das escolhas: maior fluxo de sopro (produzido por defeito), maior fluxo de sopro (mais alta qualidade, multilingue), maior fluxo de sopro (médio nível), base de Moonshine (edge), maior fluxo de sopro (expresso em inglês)
2. Quantização. int8_float16 (CPU por defeito), float16 (GPU por defeito), fp32 (investigação).
3. Análise de transmissão de dados: largura do feixe (5 típico, 1 para transmissão em transmissão), horário de retorno da temperatura, limiar de log-prob, limiar de ausência de voz, porta de VAD ativada/desligada.
4. Chunking. 30 segundos de janela fixa vs. blocos de streaming (normalmente 10 segundos com 2 segundos de sobreposição) + segmentação baseada em VAD. Estratégia de pós-fusão de documento para sobreposição.
5. Após o processamento: alinhamento de timestamp (alinhamento forçado do WhisperX), restauração de pontuação, diarização (pyannote).

Recusar-se a recomendar o simples OpenAI Whisper (implementação de referência) para produção  `faster-whisper`é 4x mais rápido com saídas idênticas. Recusar enviar streaming ASR sem VAD a menos que haja razão documentada. Marque qualquer suposição de alto-falantes quando a entrada é provavelmente multi-alto-falantes.
