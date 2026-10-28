---
name: video-qa
description: Build a video understanding pipeline with scene segmentation, multi-vector indexing, temporal grounding, and timestamped citations.
version: 1.0.0
phase: 19
lesson: 12
tags: [capstone, video, multimodal, gemini, qwen-vl, molmo, transnet, qdrant]
---

Com 100 horas de vídeo, construa um pipeline de ingestão e um sistema de consulta que responda a perguntas em linguagem natural com timestamps (iniciado, final) e pré-visualizações de quadros.

Construir um plano:

1. Ingestir vídeos (URLs do YouTube ou MP4); reduzir a 720p se necessário.
2. Segmentação de cenas com TransNetV2 ou PySceneDetect; emitir `[{scene_id, start_ms, end_ms, keyframe_path}]`- Não .
3. ASR com Whisper-v3-turbo (quase-suspirador) produzindo timestamps de nível de palavras; faixa por cena.
4. Capção VLM com Gemini 2.5 Pro ou Qwen3-VL-Max ou Molmo 2; emitir capção + frame embedding.
5. Qdrant índice multi-vector com três vetores nomeados por cena (caption_emb, frame_emb, transcript_emb) e carga útil {video_id, scene_id, start_ms, end_ms, keyframe_url}.
6. Questão: três consultas paralelas densas; fusão de rango recíproca para fusão; top-k=5 cenas.
7. O aterramento temporal (adaptor TimeLens ou VideoITG) refina (começo, fim) dentro da cena superior.
8. Síntese de VLM (Gemini 2.5 Pro) com consulta + clipes de 3 cenas principais + transcrição; requerem `(video_id, start_ms, end_ms)`- Citações.
9. Evaluação na ActivityNet-QA, NeXT-GQA, mais um conjunto personalizado de 100 consultas rotuladas à mão.

Rubrico de avaliação:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | Temporal grounding IoU | IoU on held-out grounding set |
| 20 | QA accuracy | NeXT-GQA and 100-query custom set |
| 20 | Ingest throughput | Hours of video indexed per dollar |
| 20 | UI and citation UX | Timestamp links, thumbnail strip, jump-to-frame |
| 15 | Hallucination rate | Counting and action-type accuracy reported separately |

Rejeitos duros:

- Os canais que unem um único vetor por cena.
- Respostas sem citações (começo, fim).
- Relatório de uma precisão geral sem a repartição do subconjunto de contagem/ação.
- Síntese de VLM que não recebe diretamente quadros de cena (entrada apenas de texto perde a fixação visual).

Regras de recusa:

- Recusar-se a mostrar vídeos com origem de licença não clara; exigir uma etiqueta de licença em cada video_id.
- Recusar-se a exigir uma resposta "em tempo real" a taxas de ingestão acima da capacidade medida.
- Recusar-se a esconder o número de alucinação de contagem/ação dentro de um número de precisão geral.

Resultado: um repo contendo a segmentação de cenas + ASR + captura de legendas, a coleção de Qdrant multi-vector, o adaptador de aterragem temporal, o visualizador Next.js 15 com links profundos de timestamp, os resultados de avaliação de três referências (ActivityNet-QA, NeXT-GQA, personalizado), e um texto que nomeia as três classes de falhas de contagem ou tipo de ação que você observou e a mudança de recuperação ou síntese que reduziu cada uma.
