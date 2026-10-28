---
name: attention-shapes
description: Debug shape bugs in attention implementations.
phase: 5
lesson: 10
---

Dada uma implementação de atenção quebrada, você identifica a desatividade da forma.

1. Qual matriz tem a forma errada.
2. Qual deve ser a sua forma, derivada de `(d_s, d_h, d_attn, T_enc, T_dec, batch_size)`- Não .
3. Correção de uma linha, transponha, remodelia ou projeta.
4. Um teste para capturar regressões.`output.shape == (batch, T_dec, d_h)`E ...`weights.shape == (batch, T_dec, T_enc)`E ...`weights.sum(dim=-1)`é próximo de 1.

Recusar-se a recomendar correções que transmitam silenciosamente.

Para a confusão Bahdanau, insista que a entrada do decodificador é `s_{t-1}`Para Luong,`s_t`O erro mais comum na atenção de produto de ponto é a descoincidência de dimensão de consulta/chave.
