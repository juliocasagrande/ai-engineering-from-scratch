---
name: transformer-review
description: Revisar a implementação de um transformador a partir do zero em relação às 13 lições da Fase 7.
version: 1.0.0
phase: 7
lesson: 14
tags: [transformers, review, capstone]
---

Tendo em conta uma base de código de transformador a partir do zero (PyTorch / JAX), revisão contra as anomalias de 2026 e sinalização de peças faltantes ou incorretas:

1. Atenção, mascara causal presente, escala por `sqrt(d_head)`- Funções de divisão de cabeças múltiplas.
2. Codificação de posição. RoPE (preferido 2026) ou absoluto aprendido (aceitável para modelos pequenos).
3. Bloqueamento de cabos. Pre-norma (não pós-norma). RMSNorm (não LayerNorm). SwiGLU FFN (não ReLU/GELU). Resíduos em torno de cada subcamada.
4. Treinamento. AdamW (ou Muon para 2026+), cronograma cosínico LR com aquecimento linear, corte de gradiente em 1.0, bf16 autocast. Gravidade de ligação entre o embedding de token e lm_head.
5. Perda, entropia cruzada por cada posição, mascaragem de enchimento, se houver, perda de tração e val em um intervalo fixo.

Recusar-se a assinar em uma base de código com qualquer um dos seguintes: pós-norma sem razão explícita, código de produção LayerNorm em 2026 sem justificação, falta de máscara causal na auto-atenção do decodificador, incorporados desligados em um pequeno LM. Bandeira: sem divisão de validação, sem corte de gradiente, LR > 1e-3 sem aquecimento, ou um block_size que exceda a faixa de inserção posicional sem retrocesso. Recomenda executar `python code/main.py` A perda de valor final de ponta a ponta e a verificação de ponta cai abaixo de 2,5 no Tinyshakespeare na nanoconfiguração.
