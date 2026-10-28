---
name: two-loss-trainer-designer
description: Design a Transfusion / MMDiT-style two-loss training setup (NTP on one modality, diffusion on another) with loss weights, mask design, and schedule.
version: 1.0.0
phase: 12
lesson: 13
tags: [transfusion, mmdit, two-loss, flow-matching, hybrid-attention]
---

Tendo em conta uma especificação de treinamento multimodal (dois modalidades, que obtém NTP e que obtém difusão, escala do modelo-alvo, comprimento da amostra-alvo), desenhe uma configuração de duas perdas funcional.

Produzir:

1. Modalidade dividida. Quais são os tokens discretos (NTP) e quais são contínuos (difusão). Justificar por tipo de conteúdo (texto sempre discretos; imagens, áudio, vídeo podem ir em qualquer direção).
2. Mascara de atenção. Desenhe a máscara triangular de bloco para uma sequência de exemplo. Especifique regiões bidirecionais e regiões causais.
3. Pesos de perda. Pesos iniciais para (text_loss, image_loss). Recomendação de sintonização por relação de gradiente-norma de destino. Cite ~ 0,1 padrão da Transfusion.
4. Correspondência de fluxo versus DDPM. Escolha a variante de difusão; correspondência de fluxo para matemática mais simples, fluxo retificado para menos passos de inferência.
5. Plano de inferência. Caminho NTP (análise autoregressiva sobre texto) + caminho de difusão (denominação condicional sobre correções de imagem). Especifique as etapas de denominação (10-30).
6. MMDiT vs Transfusão dividido. Quando adicionar pesos de blocos específicos de modalidade (MMDiT) vs compartilhar completamente (Transfusão); regra geral por contagem de parâmetros.

Rejeitos duros:
- Cada amostra tem uma faixa de imagem diferente e precisa de sua própria máscara triangular.
- Usando DDPM sem fluxo rectificado ou correspondência de fluxo. Ambos precisam de menos passos de inferência e são mais fáceis de sintonizar.
- O valor de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de juro de uma taxa de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de uma de

Regras de recusa:
- Se o usuário só quiser compreender (imagem, texto fora), recuse e recomenda a fusão tardia no estilo LLaVA (Lessão 12.05).
- Se o usuário quiser o modelo <1B, recuse-se a duas perdas e recomenda tokens discretos (Chameleon)  em pequena escala a cabeça de difusão não se encaixa.
- Se o utilizador não puder dar-se ao luxo de inferência dupla (loops de difusão NTP +), recuse e recomenda Show-o (difusão discreta, único loop) ou Emu3.

Resultado: design de uma página com divisão de modalidade, diagrama de máscara, pesos de perda, variante de fluxo, plano de inferência e decisão MMDiT vs. compartilhada.
