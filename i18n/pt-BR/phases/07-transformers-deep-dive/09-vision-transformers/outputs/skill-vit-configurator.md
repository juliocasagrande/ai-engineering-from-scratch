---
name: vit-configurator
description: Escolha uma variante ViT, tamanho do parche e fonte de pré-treino para uma nova tarefa de visão.
version: 1.0.0
phase: 7
lesson: 9
tags: [transformers, vit, vision]
---

Dada uma tarefa de visão (classificação / segmentação / detecção / recuperação), resolução da imagem, tamanho do conjunto de dados (etiquetado + desetiquetado) e objetivo de implantação, saída:

1. Um dos seguintes: DINOv2 ViT-L/14 (default para recuperação/classificação), codificador SAM 3 (segmentação), SigLIP (língua de visão), ConvNeXt (latencia-crítica). Razão de uma frase.
2. Tamanho do parche. 16 para classificação padrão em 224, 14 para DINOv2, 8 para previsão de densidade em alta resolução. `(H/P)^2 + 1` e custo da atenção `O(N^2)`- Não .
3. Fonte de treinamento. Nome do ponto de verificação. Para pequenos conjuntos rotulados (<10k): DINOv2 apresenta sonda congelada + linear. Para >100k: ajuste fino dos últimos blocos.
4. Recepta de formação: Otimizador (AdamW), lr, aumentos (RandAug, MixUp, Erasing aleatório), suavizamento de rótulos (0,1 típico), EMA.
5. Nota de risco: risco do regime de dados (poucos dados para uma sintonia completa), desajuste de resolução (pre-tren 224 → deployment 1024 sem interpolação de posição), ausência de registros-tokens (poderá prejudicar as características DINOv2).

Recusar-se a recomendar o treinamento de um ViT a partir do zero em menos de 1M imagens  As linhas de base da CNN ganharão. Recusar-se a recomendar o tamanho do parche que produz comprimento de sequência > 4096 sem discussão explícita de Flash Attention + variantes hierárquicas (Swin). Marque qualquer implantação que mude a resolução de entrada sem interpolar embutidos posicionais.
