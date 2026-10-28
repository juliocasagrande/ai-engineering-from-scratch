---
name: spec-decode-picker
description: Escolha uma estratégia de decodificação especulativa (vanilha / Medusa / EAGLE / lookahead) e sintoniza parâmetros para uma nova carga de trabalho de inferência de LLM.
version: 1.0.0
phase: 7
lesson: 16
tags: [inference, decoding, latency, speculative, optimization]
---

# Especulativo de decodificação

Ajudar um engenheiro a escolher entre vacina especulativa, Medusa, Eagle, ou lookahead decodificação, e sintonizar `N` (longoura do projecto) para uma carga de trabalho específica.

## Input para recolha

1. **Verifier model** - que MLL produz a produção final.
2. **Workload type** - código, chat, saída estruturada, resumo. Determina a taxa de aceitação.
3. **Sampling strategy** A amostragem de alta T degrada a aceitação.
4. **Hardware target**  O orçamento de memória determina se pode caber um modelo de projeto separado.
5. **Engineering budget** Medusa e Eagle precisam de ajustes finos; a vanilha e o olho-de-cabeça não.
6. **Latency target**  chat interativo (< 500ms TTFT, < 50ms por token) vs batch (transputa-primeiro).

## Regras de decisão

- **Quick start, no training**: Draft de baunilha com modelo 1B3B da mesma família. 2× típico.
- **You can fine-tune**: EAGLE-2 ou EAGLE-3 usando os estados ocultos do verificador. 34× típico.
- **You can fine-tune but can't run two models**Medusa (capas extra no verificador).
- **No training budget, no draft model available**- Descifrar com cabeça de olho.
- **Batch-heavy serving**A importância da bateria continua é maior; os ganhos especulativos diminuem à medida que o lote cresce, porque o verificador já está saturado.
- **High temperature or stochastic sampling**Considerar a N (23) mais baixa ou desativar.
- **Structured output (JSON, code)**A aceitação é alta.

## Apontação

- **N (draft length)**Se α > 0,9, empurre para 7. se α < 0,6, desça para 3.
- **Draft temperature**A análise de amostras não correspondente perde α.
- **Tree depth (EAGLE-2 / Medusa)**: 35 ramos; árvores mais largas ajudam apenas a α > 0,8.
- **Draft model size**A 1B rascunho para um verificador 70B é típico; não ir abaixo do verificador tokenizer / compatibilidade de incorporação.

## Sempre bandeira

- Verifique o rascunho e verifique o tokenizador.
- A descodificação de especificações interage com batches contínuos no vLLM: a aceleração por pedido diminui quando o lote já está saturado.
- A entrada de estado oculto da EAGLE requer controles internos de verificadores; nem sempre exposta através de APIs HF. Prefere-se a vLLM ou SGLang.
- Os cabeças da Medusa precisam de uma regulação supervisionada das próprias saídas do verificador.

## Formatos de saída

Retorno:

1. **Recommendation**  um nome de estratégia e parâmetros de sintonização (por exemplo, "EAGLE-2, N=5, tree_depth=4").
2. **Expected speedup**  com uma suposição α explícita.
3. **Compatibility checks**  correspondência do tokenizer, suporte ao tempo de execução, suporte ao rollback do cache KV.
4. **Fallback plan**  se a estratégia primária não tiver um bom desempenho, o que tentar em seguida.
5. **Measurement plan**  como validar a taxa de aceitação e acelerar uma amostra representativa.
