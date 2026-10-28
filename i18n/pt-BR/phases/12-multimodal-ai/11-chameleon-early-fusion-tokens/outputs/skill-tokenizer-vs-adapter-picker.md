---
name: tokenizer-vs-adapter-picker
description: Pick between Chameleon-style early fusion (shared-vocab tokenizer) and LLaVA-style late fusion (adapter on frozen LLM) for a VLM project.
version: 1.0.0
phase: 12
lesson: 11
tags: [chameleon, early-fusion, vq-vae, late-fusion, adapter]
---

Dado um produto específico (só compreensão ou compreensão+geração), qualidade de imagem alvo (post social / revista / impressão / transmissão) e orçamento de custos (formação + inferência), recomendamos a família Chameleon ou a família LLaVA com um esboço de arquitetura concreto.

Produzir:

1. Verdict. família de fusão precoce (Chameleon / Emu3 / AnyGPT) ou de fusão tardia (LLaVA / BLIP-2 / Qwen-VL).
2. Tokenizer pick (para veredictos de fusão precoce). VQ-VAE (Chameleon), MAGVIT-v2, IBQ, ou SBER-MoVQGAN; citar o teto de reconstrução esperado no PSNR.
3. QK-Norm, colocação de abandono, LayerNorm para fusão precoce em escala.
4. Estimativa de custos: horas de treinamento de GPU e latência de inferência por imagem versus a alternativa de fusão tardia.
5. O limite máximo de qualidade de geração. Intervalo de PSNR/FID que o utilizador pode esperar; se a barra de qualidade do produto é acessível com tokens discretos ou necessita de geração contínua (estilo de Transfusão).
6. Migração: se o usuário crescer e a fusão tardia se tornar limitadora (eles precisam de saída de imagem), como será a migração.

Rejeitos duros:
- Recomendo o estilo chameleão para produtos que só compreendem.
- Propondo VQ-VAE com K<4096 para geração de imagens de produção.
- A afirmação de inferência de fusão precoce é gratuita. O decodificador VQ adiciona 50-200ms por imagem gerada, muitas vezes mais do que o tempo de saída do LLM.

Regras de recusa:
- Se o utilizador quiser geração de imagem de qualidade máxima (FID < 15, pronto para impressão), rejeite tokens discretos e aponte para Transfusão / Diffusão Estabilizada 3 / MMDiT (Lessão 12.13).
- Se o produto nunca precisar de saída de imagem, recusar a fusão precoce  a complexidade é injustificada.
- Se o utilizador quiser ligar pesos de Llama / Qwen LLM existentes, recusar a fusão precoce  requer o pré- treino de um modelo novo.

Resultado: plano de uma página com veredicto, escolha de tokenizer, lista de verificação de estabilidade, estimativa de custos, limite de qualidade, caminho de migração.
