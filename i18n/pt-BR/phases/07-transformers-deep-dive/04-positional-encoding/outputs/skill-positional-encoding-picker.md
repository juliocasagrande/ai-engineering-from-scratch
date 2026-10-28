---
name: positional-encoding-picker
description: Escolha a codificação posicional (RoPE, ALiBi, sinusoidal) + estratégia de escalagem, tendo em conta a duração do contexto e o orçamento de formação.
version: 1.0.0
phase: 7
lesson: 4
tags: [transformers, positional-encoding, rope, alibi]
---

Dado um modelo de transformador (longoura do contexto-alvo na inferência, comprimento do contexto treinado, exigência de extrapolação, orçamento de ajuste em tokens), saída:

1. Código base, um dos RoPE, ALiBi, sinusoidal, aprendido-absoluto, razão de uma frase.
2. Hiperparametros. `base` Valor, `d_head` Se ALiBi: fórmula de inclinação. `max_len`- Não .
3. Estratégia de extensão. Se o alvo > treinado: fator de escalação consciente do NTK, configuração YaRN, especificação LongRoPE ou relação de interpolação de posição. Indique o orçamento de token de ajuste fino.
4. Plano de ensaio: objetivo de taxa de passagem de NIAH (agulha em uma pilha de feno) no contexto máximo, perplexidade dentro de X da linha de base de comprimento treinado.
5. O que fazer se a avaliação de longo contexto falhar: retrain com um maior `base`, mudar para ALiBi, ou captar o comprimento do contexto implantado.

Recusar recomendar sinusoidal ou aprendido-absoluto para novos modelos em 2026  eles não extrapolam e cada pilha moderna assume RoPE ou ALiBi. Recusar escalar RoPE além de 8× comprimento treinado sem um estágio de sintonia fina. Recusar enviar uma configuração de contexto longo sem uma execução NIAH no comprimento completo implantado.
