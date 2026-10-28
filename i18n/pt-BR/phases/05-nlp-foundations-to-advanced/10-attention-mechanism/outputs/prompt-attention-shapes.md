---
name: attention-shapes
description: Debug bugs de forma em implementações de atenção.
phase: 5
lesson: 10
---

Dada uma implementação de atenção quebrada, você identifica a desatividade da forma.

1. Qual matriz tem a forma errada.
2. A forma que deve ter, derivada `(d_s, d_h, d_attn, T_enc, T_dec, batch_size)`- Não .
3. Correção de uma linha, transponha, remodelia ou projeta.
4. Um teste para capturar regressões. `output.shape == (batch, T_dec, d_h)` e `weights.shape == (batch, T_dec, T_enc)` e `weights.sum(dim=-1)` é próximo de 1.

Recusar-se a recomendar correções que transmitam silenciosamente.

Para a confusão Bahdanau, insistir na entrada do decodificador é `s_{t-1}` Para Luong, `s_t` O erro mais comum na atenção de produto de ponto é a descoincidência de dimensão de consulta/chave.
