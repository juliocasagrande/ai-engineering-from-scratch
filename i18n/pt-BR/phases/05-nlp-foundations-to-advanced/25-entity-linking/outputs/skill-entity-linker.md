---
name: entity-linker
description: Desenhar uma entidade que conecte o pipeline  KB, gerador candidato, desambiguador, avaliação.
version: 1.0.0
phase: 5
lesson: 25
tags: [nlp, entity-linking, knowledge-graph]
---

Dado um caso de utilização (domínio KB, língua, volume, orçamento de latência), saída:

1. Base de conhecimentos. Wikidata / Wikipedia / KB personalizado. Data de versão. Cadença de atualização.
2. Gerador de candidato. Alias-index, embutida ou híbrida.
3. Disambiguador. Contexto anterior, baseado em incorporação, gerativo ou LLM-promptado.
4. Estratégia de NIL: limiar de pontuação máxima, classificador ou candidato explícito de NIL.
5. Avaliação. Menção de recall @ 30, precisão top-1, detecção de NIL F1 no conjunto de retenção.

Recusar qualquer pipeline de EL sem uma linha de referência-recall (você não pode avaliar um desambiguador sem saber que o candidato gen apareceu na entidade certa). Recusar qualquer pipeline usando EL com LLM-promptado sem saída limitada para ids KB válidas. Sistemas de bandeira onde o viés de popularidade afeta entidades minoritárias (por exemplo, conflitos de nome) sem ajuste fino de domínio.
