---
name: production-rag
description: Deploy a regulated-domain RAG chatbot with role + jurisdiction filtering, prompt caching, guardrails, and live drift monitoring.
version: 1.0.0
phase: 19
lesson: 08
tags: [capstone, rag, chatbot, regulated, llama-guard, nemo-guardrails, ragas, langfuse]
---

Dado um corpus de domínio regulamentado (contratos legais, protocolos de ensaios clínicos, apólices de seguro ou similares), implantar um chatbot que responda com citações verificáveis, respeita as políticas de acesso ao papel e jurisdição e é monitorado para a deriva.

Construir um plano:

1. Analisar o corpus com docling ou Unstructured; encaminhar documentos visualmente ricos através do ColPali.
2. Indice denso (Voyage-3 ou Nomic-embed-v2) em pgvector + pgvector; BM25 escasso através de Tantivy.
3. Agente de conversação Wire LangGraph: retrieve (filtro por função + jurisdição, híbrido denso + BM25, fusão de rango recíproca), re-ranque (bge-reranker-v2-gemma-2b ou Voyage rerank-2), sintetizador (Claude Sonnet 4.7 com cache rápido).
4. Assemble as instruções com prefixos estáveis: preâmbulo do sistema -> bloqueio de política -> contexto re-ranqueado -> consulta do usuário.
5. Guardrails: Llama Guard 4 em entrada e saída, NeMo Guardrails v0.12 para questões fora do domínio e proibidas por políticas, Presidio PII scrub em saída, pós-filtro de aplicação de citações.
6. Construa um conjunto de ouro com 200 perguntas com a etiqueta de especialistas com (resposta, citações).
7. Construir uma equipa vermelha de 50 pessoas (PAIR, TAP, extracção de PII, fora do domínio, sondas transversais).
8. Arize Phoenix drift dashboard de rastreamento de recuperação nDCG e fidelidade de citação semanal; alerta em queda de 5%.
9. Relatório de custos de Langfuse: taxa de acessos de caché de instrução, tokens por consulta, $/quest por fase.

Rubrico de avaliação:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | RAGAS faithfulness + answer relevance | Online scores on the 200-question golden set |
| 20 | Citation correctness | Fraction of answers with verifiable source anchors |
| 20 | Guardrail coverage | Llama Guard 4 pass rate + jailbreak suite result |
| 20 | Cost / latency engineering | Prompt-cache hit rate, p95 latency, $/query |
| 15 | Drift monitoring dashboard | Live Phoenix dashboard with weekly retrieval-quality trend |

Rejeitos duros:

- Qualquer chatbot que divulgue dados entre jurisdições.
- As instruções de síntese quebram prefixos do cache (política de reordenação entre sistema e contexto).
- Configurações de guarda-pista sem rodadas de equipa vermelha registadas.
- Respostas sem citações; citações sem âncoras verificáveis.

Regras de recusa:

- Recusar-se a ser implantado num domínio regulamentado sem etiquetas de jurisdição em cada pedaço.
- Recusar-se a treinar a recuperação em questões de ouro etiquetadas por especialistas.
- Recusar-se a declarar "conformista" sem uma matriz explícita de aplicabilidade SOC2/HIPAA/GDPR no README.

Resultado: um repo contendo o pipeline de ingestão, o agente de conversação LangGraph, o conjunto de 200 perguntas, a equipe vermelha de 50 respostas, o painel de controle de deriva Phoenix, o painel de custo Langfuse, e um texto que nomeia os três principais padrões de quebra de citações que você observou e a recuperação ou correção de pedido para cada um.
