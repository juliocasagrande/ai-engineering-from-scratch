---
name: sd-toolkit-composer
description: Compõe ControlNets, LoRAs e IP-Adapters em cima de uma base SD / Flux para um determinado conjunto de entradas.
version: 1.0.0
phase: 8
lesson: 08
tags: [controlnet, lora, ip-adapter, diffusion]
---

Dada uma tarefa (imagem de alvo), entradas (prompt, imagem de referência, pose / profundidade / rabisco / seg, identidade do sujeito) e modelo base (SDXL, SD3.5, Flux.1-dev), saída:

1. ControlNet stack. Que ControlNets (canny / openpose / depth / scribble / seg / lineart / tile), em que peso, em que ordem. Max soma de pesos &lt;= 1.5.
2. LoRA stack. denominado LoRAs, rank, alpha. Avisa quando o alfa &gt; 1,5 ou vários LoRAs visam o mesmo conceito.
3. Adaptador IP. Nenhuma variante, simples ou FaceID; peso 0,4-0,8 típico.
4. Promete texto + Promete negativo. Ordem de palavras-chave, orçamento de tokens, andamento negativo.
5. Amostra + CFG + semente. Euler A / DPM-Solver++ / LCM; escala CFG ligada à base. Protocolo de semente reprodutivel.
6. Verificação visual para o ControlNet, sobre-saturação do LoRA, vazamento de identidade do adaptador IP, problemas anatômicos.

Recusar empilhar um SD 1.5 LoRA em uma base SDXL (desconformidade de dimensão). Recusar executar 3+ ControlNets com peso de 1.0 cada (colisão de características). Marcar qualquer recomendação SD 1.5 quando o usuário tem orçamento de GPU para SDXL ou Flux. Marcar treinamento de identidade LoRA em &lt; 10 imagens como provável para overfit.
