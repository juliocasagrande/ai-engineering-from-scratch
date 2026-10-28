---
name: speaker-verifier
description: Design a speaker verification or diarization pipeline with model choice, enrollment protocol, and threshold tuning.
version: 1.0.0
phase: 6
lesson: 06
tags: [audio, speaker, verification, diarization]
---

Dado um alvo (verificação vs identificação vs diarização, domínio, canal, modelo de ameaça) e dados (horas para ajuste de limiar, número de alto-falantes, orçamento de inscrição), saída:

1. Embedder. ECAPA-TDNN / WavLM-SV / ReDimNet / x-vector. Razão.
2. Número de clips, duração mínima, porta de ruído, correspondência de canal.
3. Cossina/PLDA; com ou sem norma AS; tamanho da coorte.
4. Limite de risco: FAR (risco de fraude) ou EER; tamanho do conjunto de ajustes.
5. Defesa de fraude. Modelo anti- fraude (AASIST, RawNet2), desafio de vida, ou detecção de repetição.

Recusar qualquer implantação de nível de fraude sem uma frente anti-fausse. Recusar-se a publicar o EER sem relatar o conjunto de avaliação, seu canal e a distribuição de comprimento do clip.
