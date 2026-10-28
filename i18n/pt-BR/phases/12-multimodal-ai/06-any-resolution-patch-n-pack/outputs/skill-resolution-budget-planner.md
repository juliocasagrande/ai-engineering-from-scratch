---
name: resolution-budget-planner
description: Escolha entre quadrado-dimensional, AnyRes, M-RoPE e NaFlex para uma carga de trabalho VLM de relação de aspecto mista e emite um plano de orçamento de token por tarefa.
version: 1.0.0
phase: 12
lesson: 06
tags: [vlm, patch-n-pack, naflex, anyres, m-rope, token-budget]
---

Dada uma carga de trabalho  uma descrição das imagens que o VLM verá (documentos OCR, gráficos, captações de tela da UI, fotos naturais, quadros de vídeo) e um orçamento total de token por pedido  escolha uma estratégia de resolução por classe de imagem e produz uma configuração executável.

Produzir:

1. Para cada classe declarada (OCR, gráfico, UI, foto, vídeo-quadro), escolha uma das {quadrado-resis, AnyRes, M-RoPE, NaFlex}. Justifique em uma frase citando a sensibilidade de resolução da tarefa.
2. Orçamento de tokens por imagem. Incluir min_pixels, max_pixels (estilo Qwen2.5-VL) e o comprimento esperado da sequência na estratégia escolhida.
3. Plan de embalagem de lote. `cu_seqlens` (FlashAttn varlen), uma máscara de diagonal de bloco densa, ou inferência de imagem única não batchada.
4. Recomendação de codificador: SigLIP 2 NaFlex para cargas de trabalho mistas; Qwen2.5-VL nativo para UI de agente; CLIP-336 + AnyRes para implantações de codificadores congelados; ViT bruto em 224 para caminhos apenas para fotos.
5. Alarmes de modo de falha. Tokens por imagem na configuração escolhida; custo de latência em 30 tok/s pre-reempimento; porcentagem de conteúdo-reempimento; precisão esperada delta vs. tamanho quadrado em benchmarks típicos de OCR.

Rejeitos duros:
- Recomendar a quantificação quadrada para tarefas de OCR ou gráfico sem indicar qual número de referência o utilizador perderá.
- Proporcionar uma estratégia que produz mais tokens do que o contexto do LLM permite.
- Tratando AnyRes como a resposta universal  sua carga superior de azulejos multiplicativos pode exceder o contexto LLM antes de uma imagem terminar a codificação.

Regras de recusa:
- Se o orçamento declarado de token do usuário for inferior a 256 tokens por imagem, recusar para qualquer outra tarefa semântica que não seja apenas de foto  nenhuma quantidade de pooling recupera a precisão de OCR nesse orçamento.
- Se o utilizador quiser saídas de previsão densa (segmentação, profundidade) sem tokens de registro ViT no codificador, rejeite e aponte para DINOv2 / SigLIP 2 com registros habilitados.
- Se o contexto de LLM do utilizador for < 8k e a carga de trabalho incluir documentos ou captações de tela, recusar e recomendar um contexto maior ou um primeiro pipeline de OCR.

Resultado: um plano de orçamento de uma página com uma tabela de estratégia por classe, um plano de embalagem de lote, recomendação de codificador e uma lista de alarme.
