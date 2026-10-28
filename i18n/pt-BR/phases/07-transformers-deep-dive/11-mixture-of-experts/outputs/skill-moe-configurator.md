---
name: moe-configurator
description: Escolha o número de especialistas, o top-k, a estratégia de equilíbrio e o layout compartilhado de especialistas para um novo transformador MoE.
version: 1.0.0
phase: 7
lesson: 11
tags: [transformers, moe, mixture-of-experts, scaling]
---

Dado um modelo de transformador (orçamento total de parâmetros, parâmetros ativos desejados por token, tokens de treinamento disponíveis, hardware de inferência), saída:

1. Descrição do MoE. `n_experts`- Não . `top_k`- Não . `n_shared`. Escolha o mais fino (256+ especialistas, top-8) para as escalas de fronteira; clássico (8 especialistas, top-2) para os menores. Razão de uma frase.
2. Estratégia de equilíbrio. livre de perdas auxiliares (DeepSeek-V3, padrão), perda auxiliar de estilo Switch, ou capacidade de peritos + queda de tokens. `γ` valor se não tiver perda de valor.
3. Plano de paralelo de peritos. Como dividir os peritos em GPUs dados VRAM. Estado por peritos custo VRAM e tamanho total da frota.
4. Precision de roteamento. pontuações do roteador fp32 vs fp16.
5. Verificação de modo de falha. Risco denominado: colapso do roteador, fome de especialistas, gargalhão de rede total, latência de inferência de rotação, pegada de memória do ponto de controlo.

Recusar recomendar MoE para conteúdos de parâmetros ativos abaixo de 4B  ganhos densos em computação combinada. Recusar equilíbrio auxiliar-perda apenas para novos projetos em 2026 (livre de perdas é o padrão). Recusar enviar um MoE sem um plano paralelo de peritos se os parâmetros totais excederem 80 GB. Flag MoE para caminhos de usuário único críticos de latência como provavelmente mais lento do que equivalentes densos.
