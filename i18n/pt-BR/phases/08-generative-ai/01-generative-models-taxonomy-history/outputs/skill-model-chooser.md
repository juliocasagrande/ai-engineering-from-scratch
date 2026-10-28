---
name: generative-model-chooser
description: Pick a generative-model family, backbone, and hosted alternative for a given task and budget.
version: 1.0.0
phase: 8
lesson: 01
tags: [generative, taxonomy]
---

Dado uma descrição de tarefa (modalidade, domínio, orçamento de latência, orçamento de computação, sinal de condicionamento), saída:

1. Família. Explicito-tractable, explícito-aproximado (VAE / difusão), implícito (GAN), pontuação / fluxo de correspondência, ou token-AR. Razão de uma frase ligada à modalidade + latência.
2. Um modelo de pesos abertos pré-entrenados que o usuário pode ajustar hoje (por exemplo, Stable Diffusion 3, Flux.1-dev, AudioCraft 2, StyleGAN3, 3D Gaussian Splatting).
3. Três APIs de produção classificadas por qualidade / custo / atraso de troca (fal.ai, Replicate, Estabilidade, Runway, Veo, Kling, ElevenLabs, etc.).
4. Modo de falha: a patologia conhecida para a família escolhida (colapso de modo, viés de exposição, deriva de amostra, artefatos de tokenizer, jogo de pontuação CLIP).
5. Orçamento: horas de treinamento em um único A100, custo de inferência por amostra, piso VRAM.

Recusar recomendar um GAN quando a tarefa requer pontuação de probabilidade. Recusar recomendar autoregressivos sobre-pixels para uso em tempo real de alta resolução. Marque qualquer recomendação para "treinar a partir do zero" se a coluna vertebral aberta listada já cobre o domínio.
