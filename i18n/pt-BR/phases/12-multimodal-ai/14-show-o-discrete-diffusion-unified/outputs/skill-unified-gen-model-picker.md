---
name: unified-gen-model-picker
description: Pick between Show-o / Transfusion / Emu3 / Janus-Pro families for a product that needs both multimodal understanding and generation with open weights.
version: 1.0.0
phase: 12
lesson: 14
tags: [show-o, masked-diffusion, unified, t2i, inpainting]
---

Dado um produto que precisa de compreensão + geração unificada (VQA, legendas, T2I, opcionalmente inpainting) com restrição de pesos abertos e um orçamento de latência, escolha uma família de modelos e emite uma configuração de referência.

Produzir:

1. Veredicto da família: Show-o (difusão discreta mascarada), Transfusão / MMDiT (difusão contínua), Emu3 / Camaleão (discreto autoregressivo) ou Janus-Pro (encodadores descoplados).
2. 16 passos para Show-o, 20 para Transfusão, 1024+ para Emu3.
3. Suporte de pintura. Show-o é gratuito; Transfusão adiciona um canal de máscara; Emu3 precisa de uma sintonia fina separada.
4. Para famílias discretas, recomendamos IBQ / MAGVIT-v2 / SBER; para contínuo, recomendamos o VAE do SD3.
5. Estabilidade de treino: a perda de dois (transfusão) precisa de ajuste de peso; a perda única do Show-o é mais limpa.
6. Migração quando o usuário cresce, do Show-o à Transfusão quando a qualidade se torna o limite.

Rejeitos duros:
- Proporcionar Emu3 / Chameleon quando a latência de inferência é <10s por imagem. Autoregressivo sobre ~ 1024 tokens é muito lento.
- A afirmação de Show-o coincide com a Transfusão na qualidade da imagem de fronteira.
- Recomendação de Difusão Estabil para um produto que necessita de VQA.

Regras de recusa:
- Se o usuário quiser <2s por geração de imagem, recuse o Show-o e recomenda a Diffusion estável + um VLM separado para compreensão. Aceite a complexidade do modelo múltipla.
- Se o utilizador desejar " melhor qualidade de classe " com pesos abertos, recuse o Show- o / Emu3 e recomenda a família de Transfusão (MMDiT) ou o JanusFlow.
- Se o utilizador não puder comprometer-se com um tokenizer (temor de licenciamento, limite de qualidade), recuse-se a famílias exclusivas e recomenda a Transfusion.

Resultado: uma página com veredicto familiar, orçamento de passo, suporte de pintura, recomendação de tokenizer, plano de estabilidade e caminho de migração.
