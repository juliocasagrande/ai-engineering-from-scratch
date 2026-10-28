---
name: load-test-plan
description: Desenhar um teste de carga realista LLM  ferramenta de escolha (LLMPerf, k6, GenAI-Perf, guidellm), construir quatro padrões (estabilizado, rampa, ponta, remoção) e gate em CI.
version: 1.0.0
phase: 17
lesson: 22
tags: [load-testing, llmperf, k6, genai-perf, guidellm, llm-locust, ci-gate]
---

Dado o volume de trabalho (ponto final, SLA para TTFT/TPOT/erro), escala-alvo (concurrência, RPS) e postura CI (gate de PR ou apenas de liberação), produzir um plano de teste de carga.

Produzir:

1. Ferramenta. LLMPerf para rodadas de linha de base; k6 + extensão de streaming para portões CI; GenAI-Perf para rodadas de referência NVIDIA; guidelellm para grandes sinteticos. LLM-Locust apenas se já no Locust.
2. Distribuição de entrada de tokens de entrada de tráfego real (se disponível) ou distribuição publicada (ShareGPT / HumanEval). Proibir loop-with-one-prompt.
3. Quatro padrões: estável, rampa, ponta, remoção, para cada um: RPS alvo, duração, modo de falha esperado.
4. Portão CI. limiares específicos: TTFT P95 < X, 5xx < 5%, TPOT < Y. Tempo de execução por PR: 3-5 min.
5. Alinhamento métrico. Observe se a ferramenta de relatórios é de estilo GenAI-Perf (ITL exclui TTFT) ou LLMPerf-style (ITL inclui TTFT). Escolha uma e mantenha-se consistente.
6. Um arquivo de script (k6 JS, LLMPerf CLI) comprometido com o repo.

Rejeitos duros:
- Teste de carga com indicações uniformes.
- Test de carga sem suporte de streaming. Refuse  LLM endpoints estão em streaming por padrão.
- Comparar números entre ferramentas sem reconhecer diferenças de definição métrica.

Regras de recusa:
- Se a equipa tiver a intenção de executar o estoque de Locust sem a extensão do LLM-Locust, recuse a armadilha de GIL.
- Se o orçamento da porta CI for < 60s por PR, rejeite o enxaguamento completo  propor um estado estável rápido mais enxaguamento noturno separado.
- Se os dados de distribuição imediatos não estiverem disponíveis, exigir uma distribuição publicada documentada (ShareGPT) e notar a suposição.

Resultado: um plano de uma página com ferramenta, distribuição rápida, quatro padrões com metas, limites de entrada de CI, alinhamento métrico.
