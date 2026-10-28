---
name: video-vlm-frame-planner
description: Planejar a amostragem de quadros, a agregação por quadros, o formato de saída e os objetivos de referência para a implantação de um modelo de vídeo-linguagem.
version: 1.0.0
phase: 12
lesson: 17
tags: [video-vlm, temporal-grounding, tmrope, dynamic-fps, benchmarks]
---

Dado uma tarefa de vídeo (reconhecimento de ação, fixação temporal, resumo, monitoramento, repetição do fluxo de trabalho do agente) e uma restrição de implantação (contexto do modelo, orçamento de latência, capacidade de produção), emitir um plano de amostragem e saída de quadros.

Produzir:

1. Seleção de amostras de quadros. Uniforme para conteúdo estável, FPS dinâmico para movimento místico, orientado a eventos para ação pesada, tela de teclado + contexto para cinematográfico.
2. A concentração por quadro: 2x2 para grandes detalhes, 3x3 por defeito, 4x4 ou 6x6 para fluxos de trabalho de agentes onde a densidade de conteúdo é menos importante do que a cobertura.
3. Encodificação temporal: M-RoPE alinhado com o tempo para a família Qwen2.5-VL (TMRoPE em Qwen2.5-Omni); incorporação temporal aprendida para modelos menores; nenhuma codificação para tarefas de um único clipe.
4. Formatos de saída. JSON com `{event, start, end, confidence}` para o grounding; texto livre para resumo; token-delimited para fluxos mistos.
5. O plano de referência: vídeo para PME em geral, TempCompass para terra, EgoSchema para longo horizonte. Especifique o nível de precisão esperado.
6. Contexto / orçamento de latência. Tokens totais = duração * fps * tokens_per_frame. Avisa se exceder 40% do contexto.

Rejeitos duros:
- Propõe uma amostragem uniforme para vídeos de ação pesada.
- A reivindicação de saída de token-delimitado corresponde à precisão JSON para análise de fluxo descendente.
- Recomendação de Video-LLaMA para qualquer projeto a partir de 2026. Arquiteturas mais antigas já não são competitivas.

Regras de recusa:
- Se a duração > 10 minutos e o contexto < 32k, recusar e recomendar resumo hierárquico ou recuperação agencial (Lessão 12.18).
- Se a precisão de destino for limitada (dentro de 2 pontos do Gemini 2.5 Pro no VideoMME), recuse-se a abrir modelos 7B e requerer 32B+ ou proprietários.
- Se a meta de FPS dinâmico > 8 em um clip > 30s em 7B, rejeitar em termos de latência e recomendar um limite inferior.

Resultado: plano de quadro de uma página com amostra, pooling, codificação temporal, formato de saída, metas de referência, estimativa de contexto.
