---
name: classifier-designer
description: Escolha arquitetura, aumento, estratégia de equilíbrio de classe e avaliação métrica para uma tarefa de classificação de áudio.
version: 1.0.0
phase: 6
lesson: 03
tags: [audio, classification, beats, ast]
---

Dada uma tarefa de classificação de áudio (domínio, contagem de rótulos, densidade de rótulos por clip, volume de dados, objetivo de implantação), saída:

1. Arquitetura. k-NN-MFCC / 2D CNN / AST / BEATs / Whisper-encoder. Razão de uma frase.
2. Aumentos: Parâmetros de especificações (mascaras de tempo, contagem de mascaras de freqüência), mistura α, nível de mistura de ruído de fundo.
3. Balanço de classe, amostra equilibrada contra perda focal contra peso de classe, fixação na relação cauda-cabeça.
4. Perda + métrica. CE / BCE / focal; métrica primária (top-1 / mAP / macro-F1) e secundária.
5. Plano de divisão + avaliação. Stratificado k-fold, alto-falantes-disjunto se fala, divisão temporal se fluir dados.

Rejeitar qualquer tarefa de vários rótulos marcada apenas com precisão superior a 1; exigir mAP. Rejeitar avaliar uma tarefa condicionada por alto-falantes sem divisões disjunto de alto-falantes. Marcar qualquer arquitetura a partir do zero em clips com rótulos <10k  começar com uma espinha dorsal pre-treinada SSL.
