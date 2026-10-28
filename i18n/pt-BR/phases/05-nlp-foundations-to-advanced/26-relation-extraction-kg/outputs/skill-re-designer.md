---
name: re-designer
description: Desenhar um gasoduto de extracção de relações com proveniência e canonização.
version: 1.0.0
phase: 5
lesson: 26
tags: [nlp, relation-extraction, knowledge-graph]
---

Dado um corpus (domínio, língua, volume) e utilização posterior (KG-RAG, análise, conformidade), a saída:

1. Extractor. baseado em padrões / supervisionado / LLM / AEVS híbrido. Razão ligada à precisão vs. alvo de retirada.
2. Ontologia. Lista de propriedades fechada (Wikidata / domínio) ou aberta IE com passagem de canonização.
3. Cada triplo tem o código de origem, não é negociável para auditoria.
4. Estratégia de fusão: identificação da entidade canónica + identificação da relação + qualificações temporais; política de dedup.
5. Avaliação: Precisão/recolha em 200 triples rotulados à mão + taxa de alucinação em amostra extraída do LLM.

Recusar qualquer oleoduto de RE baseado em LLM sem verificação de tempo (provença da fonte). Recusar o fluxo de saída de IE aberto para um gráfico de produção sem canonização. oleodutos de bandeira sem qualificação temporal em relações com limite de tempo ( empregador, cônjuge, posição).
