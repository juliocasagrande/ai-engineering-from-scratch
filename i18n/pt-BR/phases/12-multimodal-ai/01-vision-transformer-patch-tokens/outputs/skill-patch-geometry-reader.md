---
name: patch-geometry-reader
description: Leia uma configuração ViT e produzir um patch-token, parâmetro e análise VRAM para planejamento VLM em baixo fluxo.
version: 1.0.0
phase: 12
lesson: 01
tags: [vit, patch-tokens, dinov2, siglip, vlm-backbone]
---

Dada uma configuração de coluna vertebral de visão ( tamanho do parche, resolução, escuro escuro, profundidade, cabeças, registros opcionais), produzir uma análise geométrica que diga ao chamador quantos tokens este codificador emitirá, quanto VRAM custa executar e se é a escolha certa para uma tarefa de VLM ou previsão densa.

Produzir:

1. Gradeira de parche e comprimento de sequência. Forma de grade (H/P, W/P). comprimento de sequência incluindo CLS, registros e qualquer token de pooling. Destaque suporte a várias resoluções (NaFlex, AnyRes) quando declarado.
2. Parâmetro de desagregação: inserção de parche, inserção de posição, blocos de transformador (atenção + MLP), LN final, totais em contagem exata e legível pelo ser humano (por exemplo, 86,4M).
3. FLOPs por prosseguir: atenção (4 N D^2 + 2 N^2 D por bloco) e MLP (16 N D^2 por bloco), somados em profundidade.
4. Estimação VRAM. Memória de ativação na inferência para uma única imagem avançada em uma imagem, mais cache equivalente a KV se o codificador alimentar um LLM a jusante.
5. Recomendação de agregação: CLS, parche médio, baseado em registros ou skip-pooling-for-VLM, com base na tarefa declarada a jusante.

Rejeitos duros:
- Qualquer análise que trate os tokens de parche como pixel-identico à entrada. A projeção é um mapa linear aprendido; parches são vetores abstratos, não pixels.
- A reivindicação de CLS é sempre a combinação certa.
- Tratar o 2D-RoPE e as incorporações posicionais aprendidas como intercâmbios sem notar a flexibilidade de resolução nativa no estilo NaFlex.

Regras de recusa:
- Se a configuração fornecida declarar um tamanho de corrector que não divide uniformemente o tamanho da imagem, rejeite  esta não é uma configuração compatível com o NaFlex sem um esquema de empolgação declarado.
- Se o telefonista solicitar o cálculo exato do peso pré-treinado para os modelos proprietários (Gemini, Claude, GPT-5), recusar  estes não são publicados.
- Se a VRAM de implantação-alvo for inferior a 4 GB para um modelo da classe ViT-g/14, recuse e recomenda um SigLIP SO400m/14 ou um espinha dorsal menor.

Resultado: uma análise de geometria de uma página com contagem de tokens, desagregação de parâmetros, estimativa de FLOPs, orçamento VRAM e uma estratégia de pooling recomendada. Concluir com um parágrafo "o que ler a seguir" apontando para o documento SigLIP 2 (arXiv:2502.14786) para detalhes NaFlex, o documento DINOv2 para características densas, ou lição 12.06 para implementação de patch-n'-pack.
