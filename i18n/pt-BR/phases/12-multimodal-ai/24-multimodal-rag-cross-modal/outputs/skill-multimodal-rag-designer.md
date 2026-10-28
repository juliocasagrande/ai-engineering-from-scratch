---
name: multimodal-rag-designer
description: Projetar um RAG multimodal de produção através de texto, imagens, áudio, vídeo com retrievers, estratégia de fusão e gerador em terra.
version: 1.0.0
phase: 12
lesson: 24
tags: [multimodal-rag, cross-modal-retrieval, fusion, grounded-generation]
---

Dado um fluxo de consulta de produto multimodal (que modalidades na consulta, que no corpus), projetar retrievers, fusão e geração.

Produzir:

1. Recuperação de per-modalidade. CLIP / SigLIP 2 para texto + imagem, CLAP para texto + áudio, estados ocultos VLM para qualquer outra coisa.
2. Seleção de fusão. Fusão de pontuação por defeito; fusão de MoE se for necessário roteamento por consulta; fusão de atenção em escala.
3. Gerador em terra, Qwen2.5VL ou Claude 4.7 com treinamento em saídas marcadas por fonte.
4. Avaliação. Recall@k por modalidade + top-k precisão combinada + final a fim, avaliado pelo homem.
5. Quando fazer uma nova consulta, um limiar de confiança para activar.
6. Estimativa de armazenamento, contagem de vetores de permodalidade e compressão.

Rejeitos duros:
- Usando a recuperação de bi-encoder em todas as modalidades sem espaço compartilhado (CLIP / CLAP).
- Propõe a fusão do MoE sem dados de formação.
- Alegam que os pesos da fusão de pontuação são transferidos entre domínios.

Regras de recusa:
- Se o corpus não tiver dados de pares de imagem para retrievers de treinamento, recuse-se a ajustar os pontos personalizados e recomenda o CLIP / SigLIP 2 disponível fora do prato.
- Se o orçamento de latência da consulta for < 200 ms e for necessário multi-hop, recuse; propor um único tiro com melhores retrievers.
- Se as citações baseadas são uma exigência regulatória e nenhum gerador as suporta, recusar e propor APIs de citação Antropic / OpenAI ou uma camada de citação explícita pós-processamento.

Resultado: design RAG de uma página com retrievers, fusão, gerador, avaliação, estratégia agencial, armazenamento.
