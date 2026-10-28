---
name: decoupled-encoder-picker
description: Decide whether a unified VLM should decouple its visual encoders and pick between Janus-Pro, JanusFlow, and InternVL-U.
version: 1.0.0
phase: 12
lesson: 15
tags: [janus-pro, janusflow, internvl-u, decoupled-encoders, unified-model]
---

Dada uma especificação de modelo unificado (entendimento + geração, edição / inpainting opcional), um orçamento de computação e uma restrição de pesos abertos, recomendamos uma arquitetura de codificação descoplada e uma configuração concreta.

Produzir:

1. Seleção de arquitetura: Janus-Pro (geração VQ), JanusFlow (geração de fluxo corrigida), InternVL-U (pre-treinamento nativo + descoplado).
2. Combo de codificador: SigLIP-SO400m para compreensão; MAGVIT-v2 / IBQ VQ para geração discreta; VAE de estilo SD3 para contínuo.
3. Plano de fase de dados: alinhamento de fase 1 (50-100M pares), fase 2 unificada (70M+ pares), instrução de fase 3 (1M+ amostras). Cite o modelo de 5,4x do Janus-Pro + resultado de escalagem de dados 2,8x.
4. Estratégia de encaminhamento.`<understand>`- Não .`<generate>`) ou baseado em classificação de tarefas.
5. Iniciar a partir de um LLM pré-treinado (DeepSeek, Qwen, Llama) em vez de do zero.
6. O limite máximo de qualidade: MMMU (~60 em 7B) e GenEval (~0,80 em 7B para Janus-Pro / ~0,85+ para InternVL-U).

Rejeitos duros:
- Proporcionar um modelo unificado de codificador único (Show-o / Transfusion) quando a barra de qualidade do usuário para ambos os lados é competitiva.
- Recomenda-se o pré-treino desde o zero para um modelo <10B. Reutilizar um corpo de LLM pré-treinado.
- Proporcionar Janus (original) em vez do Janus-Pro para qualquer novo projeto.

Regras de recusa:
- Se o usuário só precisa de compreensão, rejeite o desacoplamento e recomenda a família LLaVA.
- Se o utilizador precisar apenas de geração, recusar e recomendar a Stable Diffusion 3 / Flux  os especialistas ainda ganham na qualidade do T2I.
- Se calcular < 50k horas de GPU, recusar o InternVL-U (requer pré-treinamento nativo) e recomendar o Janus-Pro (reutilizar o LLM pré-treinado).

Resultado: plano de uma página com escolha de arquitetura, combinação de codificadores, plano de estágio, roteamento, init de corpo compartilhado e teto de qualidade.
