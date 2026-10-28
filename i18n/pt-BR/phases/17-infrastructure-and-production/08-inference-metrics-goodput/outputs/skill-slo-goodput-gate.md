---
name: slo-goodput-gate
description: Produce a CI/CD-ready benchmark recipe that gates LLM deploys on goodput, not throughput, with P50/P90/P99 percentiles and a documented tool choice.
version: 1.0.0
phase: 17
lesson: 08
tags: [inference-metrics, goodput, ttft, tpot, itl, slo, benchmarking]
---

Dada uma carga de trabalho (modelo, hardware, simultaneidade de destino, tipo de interação de uso  streaming chat / one-shot / voice / agent), produzir um gate SLO baseado em goodput para CI / CD.

Produzir:

1. Especificações SLO. Três limiares: TTFT P99 limitado, TPOT P99 limitado, E2E P99 limitado. Escolha valores defensiveis do tipo de interação (chat de streaming: TTFT 500 ms, TPOT 25 ms, E2E 3 s; voz: TTFT 300 ms mais apertado; agente: E2E 5 s mais solto).
2. Recepta de referência. escolha de ferramentas (LLMPerf ou GenAI-Perf  indicar o que você escolhe e por que). Distribuição rápida (média + stddev de tokens de entrada e saída). Varagem de concorrência (25%, 50%, 100%, 150% do alvo).
3. Calculação de potência. Fórmula: fracção das solicitações que satisfazem simultaneamente as três restrições.
4. Para cada métrica, informe P50, P90, P99 (nunca significa sozinho).
5. Nota de armadilha da ferramenta. Indique se a ferramenta inclui ou exclui o TTFT da ITL. Corrige a definição antes de comparar entre equipes.
6. Logicagem de gate. CI passa se goodput >= meta AT simultaneidade meta. Flag se goodput degrada mais de 5 pts entre 100% e 150% simultaneidade  indica que falta espaço de teste de carga.

Rejeitos duros:
- Recusar e exigir goodput.
- - Não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não, não,
- Excluir o nome da ferramenta e a versão da ferramenta.
- Compartilhar apenas a simultânea meta; sempre fazer a varredura.

Regras de recusa:
- Se o utilizador não tiver um SLO escrito, recuse-se e escreva primeiro um baseado no tipo de interação.
- Se a distribuição de prompt for "identical prompt em um loop", rejeite  esta é a armadilha de uniformitade de prompt.
- Se o valor de referência for < 30 corridas ou < 100 pedidos por corrida, rejeitar-se-á como estatisticamente insuficiente.

Resultado: uma lista de prazos, receita de referência, escolha de ferramentas, modelo de relatório percentil e regra de passagem/falha do CI. Concluir com um parágrafo "o que medir a seguir" que nomeia uma curva de goodput vs concurrency, sensibilidade à distribuição rápida ou comparação de cauda/desliga de preenchimento em pedaços, dependendo da fraqueza conhecida.
