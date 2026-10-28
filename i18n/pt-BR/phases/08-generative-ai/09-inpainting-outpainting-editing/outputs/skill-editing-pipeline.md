---
name: editing-pipeline
description: Planeje um pipeline de edição de imagem da fonte + edição da descrição para uma saída pronta para o navio.
version: 1.0.0
phase: 8
lesson: 09
tags: [inpaint, outpaint, edit, sam]
---

Dada a imagem fonte, edição de destino (remover X, substituir Y por Z, ampliar tela, redesenhar região, mudar estação / hora do dia), e barra de qualidade (draft / portfolio / impressão), saída:

1. Estratégia de máscara. Máscara de pincel explícita, SAM 2 clique / caixa de solicitação, Grounded-SAM em uma frase de texto, ou RMBG (para remoção de fundo). Razão de uma frase.
2. Modelo base + modo. SD-Inpaint / SDXL-Inpaint / Flux-Fill / Flux-Context para edições de instruções, ou SDEdit nível de ruído (0,3 / 0,6 / 0,9) se não houver máscara.
3. Descreva toda a imagem após a edição, não apenas o novo conteúdo. Inclua um prompt negativo.
4. CFG + resistência + pena. Pena de máscara 8-16 px; CFG ~ 5-7 para tinta SDXL, 3-4 para Flux. Força 0,8-1,0 para regeneração completa, 0,3-0,5 para conservação.
5. Gardails. NSFW / deepfake / marca registrada de detecção gancho, face-swap política porta, reversibilidade (salva a máscara + semente).

Recusar-se a enviar edições de identidade em uma figura pública reconhecível sem verificação explícita de políticas. Recusar-se a pintar uma imagem sem pelo menos 30% da tela original como âncora (contexto muito pequeno faz o modelo alucinar). Marque qualquer SDEdit executado com t / T &gt; 0,7 e objetivo de fidelidade "preserva sujeito" como uma probabilidade de desacordo.
