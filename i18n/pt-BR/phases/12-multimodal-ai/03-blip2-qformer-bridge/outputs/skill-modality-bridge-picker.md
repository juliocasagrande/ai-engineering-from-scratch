---
name: modality-bridge-picker
description: Recommend Q-Former vs MLP projector vs Perceiver resampler for a VLM configuration given token budget, quality target, and training compute.
version: 1.0.0
phase: 12
lesson: 03
tags: [blip2, qformer, vlm, modality-bridge, architecture]
---

Dado o número de tokens por imagem de um codificador de visão, o orçamento contextual do LLM, o número de imagens alvo por prompt e o orçamento de computação de treinamento, recomendam qual ponte de modalidade usar e justificar com o número de parâmetros e a economia de tokens.

Produzir:

1. Auditoria do orçamento de tokens. Relate tokens brutos por imagem a partir do codificador de visão, tokens por imagem após cada opção de ponte e a fração do contexto de LLM consumido em contas de imagem por prompt declaradas.
2. Para cada um dos Q-Former (32 tokens, ~188M params), projeto MLP (todos os patches, ~20M params), e perceptor resampler (K learnable queries via N-layer cross-attention, variável), dar parâmetros, proxies de qualidade e treinamento custo de campo.
3. Recomendação. Única melhor escolha para as restrições declaradas, com uma justificação de linha única.
4. Traçação de treinamento em duas etapas. Se for escolhido o Q-Former, descreva as perdas de ITC + ITM + ITG para a fase 1 e a perda de LM para a fase 2. Nomeie um conjunto de dados representativo para cada uma (COCO, LAION, Visual Genome).
5. Lista de verificação de ablação: cinco experimentos que o chamador deve executar antes de bloquear a ponte (contação de perguntas, duas etapas versus uma etapa, profundidade do projetor, cronograma de congelamento, subconjunto de tunes finetos).

Rejeitos duros:
- Qualquer recomendação que ignore o orçamento de tokens. "Use MLP" com 576 tokens por imagem falha em 10 imagens em um contexto 4k.
- A afirmação de que o Q-Former domina estritamente o MLP. Em tarefas de alta qualidade de imagem única com contexto ilimitado, o MLP ganha.
- Tratando o resampler do Perceptor como equivalente ao Q-Former. Flamingo aplica-o em cada camada LLM; BLIP-2 aplica-o uma vez.

Regras de recusa:
- Se o chamador pedir uma ponte que possa lidar com vídeo sem especificar quantas quadros e a que taxa de quadros, rejeite pontes de vídeo diferem de pontes de imagem única por especificação, não apenas escala.
- Se o Mestrado em Direito Executivo de âmbito é treinado a partir do zero com a torre de visão (fuso precoce, estilo camaleão), recusar  Lição 12.11 abrange esse caso separadamente.
- Se não for indicado o cálculo do treinamento, recuse e pergunte se o chamador pode pagar a fase 2 do BLIP-2 (cerca de algumas centenas de horas de treinamento) ou apenas o treinamento com projetor.

Resultado: uma recomendação de ponte de uma página com matemática de tokens, contagens de parâmetros, arquitetura recomendada, esquema de treinamento e lista de verificação de ablação.
