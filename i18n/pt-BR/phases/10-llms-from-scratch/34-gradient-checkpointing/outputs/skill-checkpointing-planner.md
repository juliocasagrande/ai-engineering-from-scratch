---
name: checkpointing-planner
description: Choose an activation recomputation policy per layer (none / selective / full / offload) given a training config and HBM budget.
version: 1.0.0
phase: 10
lesson: 34
tags: [gradient-checkpointing, activation-recomputation, selective-checkpoint, fsdp-offload, training-memory]
---

Dada a configuração de treinamento (contagem de camadas L, tamanho oculto d, comprimento de sequência S, microbatch B, bytes de tipo d por valor, núcleo de atenção, TP de grau tensor paralelo, PP de grau pipeline paralelo, EP de grau perito paralelo se MoE) e o orçamento HBM por categoria após pesos e estado de otimização, saída:

1. Política por camada. Para cada família de camadas na pilha (embedding, attention, FFN, MoE expert, norm, output head) escolha nenhuma, seletiva, completa ou descarregada. Default para seletiva para atenção quando S excede 4_096; default para none em fluxos e normas residuais; default para descarregar em FFN somente quando o tempo de transferência de PCIe medido para as ativações dessa camada é menor do seu tempo de recomputada medido.
2. Tamanho do segmento k. Se o ponto de verificação completo estiver ativado, escolha k como redondo ((sqrt(L)) para custo de camada uniforme, menor k quando a memória de ativação domina o orçamento.
3. Interação FlashAttention. Confirme se o kernel de atenção já recalcula softmax. Se sim, o checkpoint seletivo de atenção compra pouco; rebaixar para nenhum. Indique o kernel pelo nome (FlashAttention-2/3, xFormers memory-efficient, vanilla).
4. Para TP, nomear as ativações que precisam ser coletadas ou resgatadas na recomputação e os bytes de comunicação adicionados por passo. Para PP, confirmar quais estágios do pipeline são verificados de ponta a ponta para inverter microbatches de memória de ativação livre antes de fluir de volta.
5. Matemática do orçamento. Previnha a memória de ativação antes e depois da política (em MB por classificação). Previnha o custo geral do FLOP como porcentagem de fwd +bwd. Rejeita qualquer plano que não se encaixa no orçamento do HBM com 10% de espaço de cabeça.

Recusar o ponto de verificação completo de cada camada quando a seletiva apenas a atenção fecha o orçamento; o perfil mostra que o custo geral do FLOP é muitas vezes maior do que o seletivo para a mesma economia de memória, e a relação exata é específica da carga de trabalho. Recusar descarga quando o tempo de transferência de ativação medido da camada no link PCIe-alvo exceder o tempo de recomputada medido; recomputada ganha. Recusar "checkpoint everywhere" para a formação do PQ8 quando a estrutura escolhida não retrata o histórico; a recomputada irá desviar a escala e silenciosamente corromper os gradientes.

Exemplo de entrada: "L=64, d=8192, S=8192, B=1, bf16, FlashAttention-3, TP=8, PP=4, orçamento HBM por classificação 32 GB após pesos, MoE com 8 especialistas e EP=8."

Exemplo de saída:
- Política por camada: atenção seletiva, FFN nenhuma, especialista em MoE completo, sem incorporação, saída de carga de cabeça.
- Tamanho do segmento: aplicado no MoE apenas em k=8; FLOP overhead 12% no caminho de peritos, 0 em outros lugares.
- Interação FlashAttention: FA-3 já recalcula softmax; seletivo na capa de envoltura, não dentro do núcleo.
- Plano TP/PP: TP recolhe a entrada de atenção na recomputada, 0,3 GB por passo de comunicações extras; PP fase cada ponto de controlo em sua plena frente; PP fase 3 mantém suas ativas para o último retrocesso.
- Matemática orçamental: ativas 38 GB sem política, 11 GB com política.
