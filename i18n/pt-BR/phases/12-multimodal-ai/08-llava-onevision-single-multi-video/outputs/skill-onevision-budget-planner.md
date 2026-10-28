---
name: onevision-budget-planner
description: Asigne orçamentos unificados de tokens visuais de estilo LLaVA-OneVision em cenários de imagem única, imagem múltipla e vídeo para uma mistura de produtos alvo.
version: 1.0.0
phase: 12
lesson: 08
tags: [llava-onevision, token-budget, curriculum, multi-image, video]
---

Dado a distribuição de tarefas esperada de um produto  percentagens de pedidos de imagem única, de imagem múltipla e de vídeo  e um orçamento de tokens visuais por amostra, emitir um plano de atribuição por cenário e um currículo de formação.

Produzir:

1. Configuração por cenário. Imagem única: Contagem de azulejos AnyRes + miniatura + fator de agregação; Multidimensional: imagens por amostra + agregação por imagem; vídeo: conteúdo de quadros + agregação por quadros.
2. Balanço do orçamento de tokens. Os tokens totais de cada cenário devem chegar a ± 30% do orçamento-alvo; marcar qualquer cenário que cai abaixo de 70% do objetivo (sub-tokenizado) ou acima de 130% (risco contextual).
3. Plano de currículo. Três fases (SI → OV → TT) com pesos de dados. Para a fase TT, use a mistura de produtos do usuário.
4. Competências emergentes esperadas. Dada a mistura de produtos do usuário, prever quais capacidades emergentes de estilo LLaVA-OneVision são susceptíveis de aparecer (multi-câmera, set-of-mark, agente de captura de tela ou variantes específicas do produto).
5. Formação-data balcão. Contagem aproximada de tokens / imagem / quadro necessários por estágio dado 7B base LLM, citando a escala de dados OneVision-1.5.

Rejeitos duros:
- Propondo ordens de etapa que colocam vídeo ou imagem múltipla antes de imagem única.
- A atribuição de todo o orçamento para o vídeo quando o produto é 80% de imagem única.
- Supondo que o AnyRes-16 (4x4 grid) encaixa num orçamento de tokens 4k sem agressão.

Regras de recusa:
- Se o orçamento de token por amostra for inferior a 1024, rejeitar casos de uso de imagens ou vídeos múltiplos  abaixo desse nível, os cenários desmoronam.
- Se o usuário quiser 5+ quadros de vídeo com resolução total de 729 tokens, recuse; recomenda a agregação de 3x ou menos quadros.
- Se a distribuição do produto omitir completamente a imagem única, recusar e recomendar M-RoPE de estilo Qwen2.5-VL em vez disso  O currículo da OneVision assume a imagem única como base de percepção.

O resultado: um plano de uma página com configuração de token por cenário, pesos de estágio do currículo, previsões de habilidades emergentes e uma estimativa de escala de dados.
