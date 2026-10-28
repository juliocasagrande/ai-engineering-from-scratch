---
name: document-ai-stack-picker
description: Escolha entre o pipeline de OCR, especialista livre de OCR e nativo de VLM para um projeto de IA de documento com base em domínio, escala e necessidades regulatórias.
version: 1.0.0
phase: 12
lesson: 22
tags: [document-ai, ocr, donut, nougat, paligemma, vlm-native]
---

Dado um projecto de IA-documento (domínio: faturas / artigos científicos / formulários / misturados; escala: páginas por dia; barra de qualidade; necessidades regulatórias), escolha uma pilha e produz uma configuração de referência.

Produzir:

1. Escolha de pilha. Era 1 (OCR pipeline + LayoutLMv3), Era 2 (Donut / Nougat OCR livre), Era 3 (VLM-nativo), ou híbrido.
2. Estimação de custo por página, contagem de tokens e latencia na pilha escolhida.
3. Precisão de referência DocVQA + ChartQA + referências específicas de domínio.
4. Estratégia de escrita manual. VLM-nativa para custo-insensível; TrOCR + roteamento dedicado para escala.
5. Resultados matemáticos / LaTeX. Nougat para artigos científicos; VLM para outros.
6. Regras regulatórias, híbrido com registro de auditoria.

Rejeitos duros:
- Proporcionar VLM-nativo para > 1M páginas / dia sem análise de custos.
- Recomendar soluções de modelo único para fluxos de trabalho regulamentados sem vias de auditoria.
- A Claiming Nougat trata de contas digitalizadas.

Regras de recusa:
- Se a escala for > 10 milhões de páginas/dia, rejeite a Era 3 e recomenda a Era 1 com a Era 3 como validador de amostragem.
- Se o domínio for pesado em escrita manual, recuse o pipeline de OCR e recomenda especialista em escrita manual (TrOCR) nativo do VLM.
- Se a fidelidade LaTeX for necessária para equações, exija Nougat no loop.

Resultado: plano de uma página com pilha, custo, precisão, escrita, matemática, regulatório.
