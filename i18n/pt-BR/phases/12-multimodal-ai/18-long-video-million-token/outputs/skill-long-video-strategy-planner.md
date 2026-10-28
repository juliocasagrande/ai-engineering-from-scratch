---
name: long-video-strategy-planner
description: Escolha conteúdo bruto, atenção de ring, compressão de tokens ou recuperação de agentes para uma tarefa de compreensão de vídeo longo e computa a latência + expectativas de recall.
version: 1.0.0
phase: 12
lesson: 18
tags: [long-video, gemini, ring-attention, videoagent, retrieval]
---

Dada a duração do vídeo, a complexidade da consulta (evento único vs resumo holístico) e as restrições abertas vs fechadas, escolha uma estratégia de vídeo longo e emite uma configuração.

Produzir:

1. Seleção de estratégia: contexto bruto, atenção ao anel (LongVILA), compressão de tokens (Video-XL) ou recuperação de agentes (VideoAgent).
2. Orçamento de tokens. Duração * FPS * por tokens-quadro. Aviso se > contexto LLM.
3. Recall esperado, recall de agulha em uma pilha de feno em percentil de comprimento de vídeo, cita os relatórios Gemini 1.5 quando relevante.
4. Latência, tempo de preenchimento para conteúdo bruto, recuperação + VLM para agente.
5. O esquartejo de snippet de código para a estratégia escolhida.
6. Plano de regresso. híbrido: resumo global de contexto bruto + detalhes locais.

Rejeitos duros:
- Propondo conteúdo bruto para um vídeo de 2 horas num modelo aberto 72B.
- A reivindicação de recuperação agencial sempre ganha, mas para questões holísticas, perde para o contexto bruto.
- Recomendar a compressão de tokens sem marcar o imposto de retirada.

Regras de recusa:
- Se o objetivo for um vídeo de 90 minutos no recall de fronteira (> 95%), recuse as opções de apenas aberta e recomende o Gemini 2.5 Pro.
- Se o utilizador não puder pagar os loops de chamada de ferramenta, recuse a recuperação de agentes e propor conteúdo bruto comprimido.
- Se o usuário precisar de tempo real (stream-as-it-plays), recuse a recuperação (demasiado lenta) e recomenda o streaming Qwen2.5-VL.

Resultado: plano de uma página com estratégia, orçamento, recall, latência, caminho de engenharia e retrocesso.
