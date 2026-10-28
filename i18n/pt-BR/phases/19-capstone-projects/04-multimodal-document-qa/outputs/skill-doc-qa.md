---
name: doc-qa
description: Build a vision-first multimodal document QA system on 10k pages with late-interaction retrieval and evidence-region citations.
version: 1.0.0
phase: 19
lesson: 04
tags: [capstone, multimodal, rag, colpali, colqwen, late-interaction, pdf]
---

Dado um corpo de PDFs (10Ks, artigos científicos, documentos digitalizados), construa um pipeline que indexa páginas como imagens usando interação tardia no estilo ColPali e responde perguntas com regiões de evidências de nível de página.

Construir um plano:

1. Render cada página PDF para uma PNG 1536x2048 com PyMuPDF a 180 DPI.
2. Embed cada página com ColQwen2.5-v0.2 ou ColQwen3-omni. Armazenar embutidos de multi-vector em Vespa, Qdrant multi-vector, ou AstraDB.
3. Aplicar uma poda de 50% de parche no estilo DocPruner. Verifique que a precisão da queda permanece abaixo de 0,5% no ViDoRe v3.
4. No momento da consulta: inserir os tokens da consulta; calcular o MaxSim contra os patches de cada página; classificar o top-k.
5. Sintetize com Qwen3-VL-30B ou Gemini 2.5 Pro passando a consulta mais as imagens de 5 páginas superiores.`(doc_id, page, region)`Ancoras.
6. Para páginas com massa de equação ou tabela, execute Nougat ou dots.ocr como um canal de texto opcional e alimenta-o ao lado da imagem.
7. Construir um visualizador Next.js 15 que superpõe as regiões de evidência como caixas de limite na página fonte.
8. Avalie no ViDoRe v3 e M3DocVQA. Produza uma matriz de abordagem de classe × conteúdo comparando visão primeiro vs OCR-depois-texto em texto plano, tabelas, gráficos, escrita manual e equações.

Rubrico de avaliação:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | ViDoRe v3 / M3DocVQA accuracy | Benchmark vs OCR-then-text baseline on matched pages |
| 20 | Evidence-region grounding | Fraction of cited regions that contain the answer span |
| 20 | Storage and latency engineering | DocPruner compression, index p95, answer p95 under 2s |
| 20 | Multi-page reasoning | Accuracy on a hand-labeled 100-question multi-page set |
| 15 | Source-inspection UX | Overlay fidelity, comparison tools, page-by-page explorer |

Rejeitos duros:

- Os primeiros canais de OCR foram lançados como "visão-primeira" através da modernização do texto OCR em um incorporado de vetor único.
- Qualquer sistema que deixe cair as caixas de limite de nível de parche e, portanto, não pode produzir evidências superpuestas.
- Números de armazenamento relatados sem documentar as configurações do DocPruner.

Regras de recusa:

- Recusar-se a indexar contratos legais digitalizados sem uma política de redação específica.
- Recusar-se a enviar consultas contra um corpus que o utilizador não divulgou.
- Recusar a comparação com OCR-then-text sem executar ambos os canais no mesmo corpus.

Resultado: um repo contendo o pipeline de ingestão, a configuração Vespa (ou Qdrant multi-vector), o conjunto de avaliação de 100 perguntas de várias páginas, a interface do visualizador e uma redação com a matriz de abordagem de classe de conteúdo x e uma recomendação concreta para a qual as classes de conteúdo ainda favorecem OCR-then-text em 2026.
