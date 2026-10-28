---
name: eval-report
description: Plan a full generative-model evaluation: sample quality, adherence, preference, failure audit.
version: 1.0.0
phase: 8
lesson: 14
tags: [evaluation, fid, clip, elo]
---

Dado um novo ponto de controlo do modelo gerativo, uma linha de referência e uma modalidade (imagem / vídeo / áudio / 3D), produzir um plano de avaliação completo:

1. Qualidade da amostra. FID / FD-DINO / CMMD em amostras 10-30k versus conjunto real de resistência. Resolução correspondente. Relatório de média de 3 sementes +/- std.
2. A adesão. CLIP score / CMMD em pares de imagens de prompt. Incluir HPSv2 + ImageReward + PickScore para texto para imagem. Para vídeo, adicione métricas de linguagem de visão (V-Eval). Para áudio, CLAP + MOS.
3. Preferência de par. A/B cego em 200-2000 pedidos versus linha de base.
4. Desagregação de categorias. Performance por categoria de pedido (povo, animais, renderização de texto, composição, estilo). Regressões de bandeira por categoria mesmo que as métricas globais melhorem.
5. Segurança/abuso. Classificador NSFW, detector de deepfake, verificação de marca de água, digitalização de semelhança de direitos autorais nas gerações de topo.
6. O FID dentro de +5% da linha de base OR &gt; 55% taxa de vitória humana OR vantagem qualitativa documentada.

Recusar a notificação de FID em N &lt;5000. Recusar a envio de referências calculadas em pedidos que o modelo possa ter visto no treinamento. Recusar a notificação de apenas resultados de LLM-juiz sem verificação cruzada humana. Marcar qualquer alegação de que uma métrica "subiram 20%" sem notificar o valor base absoluto e relatar uma única semente.
