---
name: failure-detector
description: Generate failure-mode detectors for agent traces, wired to a trace store, tagging the five industry-recurring modes plus domain-specific signatures.
version: 1.0.0
phase: 14
lesson: 26
tags: [failure-modes, masft, detection, observability]
---

Dado um domínio de produto e uma loja de rastreamento, produzir detectores para modos de falha do agente.

Produzir:

1. Detector por modo: `hallucinated_action`- Não .`scope_creep`- Não .`cascading_errors`- Não .`context_loss`- Não .`tool_misuse`- Não .`success_hallucination`- Não .
2. Detetores específicos de domínio (por exemplo, "criou um PR sem vincular um problema" para uma ferramenta de desenvolvimento, "enviou um e-mail a > 5 destinatários sem confirmação" para uma ferramenta de marketing).
3. Tagger que aplica todos os detectores a cada rastro e emite uma distribuição.
4. Alerta baseada em limiar: se >=5% dos traços atuais marcar um modo, página ou abrir um bilhete.
5. Reter amostras: para cada rastreamento etiquetado, manter entradas + saídas + instantâneos de estado para revisão do operador.

Rejeitos duros:

- Detectores que exigem chamadas de LLM por rastro na produção. Use detectores baseados em padrões; reserve o juiz de LLM para revisão de amostras.
- Tagging apenas em crash. A maioria das falhas produzem saída válida. São necessárias verificações de assinatura no conteúdo + estado.
- Armazenamento de vestígios marcados sem redação de PII. As amostras de falhas têm o pior conteúdo; esfregar antes de armazenamento.

Regras de recusa:

- Se o utilizador quiser "todos os traços armazenados para sempre", recuse por razões de custo + conformidade.
- Se o produto não tiver uma linha de base de "bom conhecido", rejeite as alertas de derivação.
- Se os detectores não estiverem modificados, recuse-se.

Output: `detectors.py`- Não .`tagger.py`- Não .`alerts.py`- Não .`retention.py`- Não .`README.md`A conclusão é com "o que ler a seguir" apontando para a lição 24 (backends de observabilidade) ou a lição 27 (injecção rápida) para os modos de falha adversária.
