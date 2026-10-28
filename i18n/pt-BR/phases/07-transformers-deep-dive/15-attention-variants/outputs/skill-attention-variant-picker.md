---
name: attention-variant-picker
description: Escolha uma topologia de atenção completa / deslizante / escassa / diferencial para um novo modelo dado o comprimento do contexto, as exigências de recuperação e o perfil de computação.
version: 1.0.0
phase: 7
lesson: 15
tags: [attention, transformer, long-context, inference, memory]
---

# Atenção Variante Picker

Ajudar um desenvolvedor a escolher e justificar uma topologia de atenção para um novo transformador, ou para um existente que eles estão estendendo para um contexto mais longo.

## Input para recolha

1. **Target context length** A formação e a inferência (muitas vezes diferentes  muitos modelos treinam a 16K e se estendem a inferência).
2. **Retrieval demand** Em uma escala de 15: 1 = chat puro, 5 = agulha em manto de feno / RAG / código com longo contexto de repositório.
3. **Inference memory budget** tolerância de cache KV por pedido (bytes por token por camada é a unidade certa).
4. **Training cost tolerance**  a formação de SWA a partir do zero é barata; a adaptação da atenção diferencial num modelo pré-treinado é cara.
5. **Hardware target**  Hopper+ tem FlashAttention-3 completo, Ada tem FA2, GPUs mais antigas são mascaradas.

## Regras de decisão

- **Context ≤ 16K and retrieval ≤ 3**Não otimizem prematuramente.
- **Context 16–128K and retrieval ≤ 3**: SWA + global misturado em 5:1, janela 1024 (forma Gemma 3).
- **Context > 128K**: SWA completa com uma camada global a cada 46 camadas, mais interpolação de posição / escalação YaRN (Lessão 04).
- **Retrieval = 5 and training budget allows**A diferença de atenção é considerada apenas nas quatro camadas superiores (metade do KV duplicando, a maior parte da vitória da cancelamento do banheiro).
- **You're shipping a public API**Prefira padrões estáveis (completo, SWA, Gemma-3 mix).
- **You can't change the base model**A SWA pode ser adaptada à inferência através de mascaramento; diferencial e escassos não podem.

## Sempre bandeira

- Os modelos de SWA puros abaixo de 7B geralmente perdem de forma mensurável em referências de raciocínio.
- O tamanho da janela < 512 quase nunca é certo.
- Os relatórios de atenção diferencial no artigo são sobre modelos pequenos (37B).
- Cada variante interage com a escalação RoPE/YaRN (Lessão 04).

## Formatos de saída

Retorno:

1. **Recommendation**  uma única topologia com nome (por exemplo, "Gemma-3 mix, W=1024, 5:1 SWA:global").
2. **Justification**  mapear cada entrada para a regra de decisão acima.
3. **KV cache estimate**  no contexto-alvo, em bytes por token por camada e em GB no lote 1.
4. **Migration path**  se o modelo base já for treinado, como adaptar.
5. **Known risks**  quais valores de referência/cargas de trabalho podem regredir.
