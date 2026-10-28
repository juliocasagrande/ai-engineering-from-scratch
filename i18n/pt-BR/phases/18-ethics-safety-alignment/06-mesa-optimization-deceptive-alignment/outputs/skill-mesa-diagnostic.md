---
name: mesa-diagnostic
description: Classificar uma falha de segurança observada como alinhamento externo, proxy-inner ou decepcionante-inner.
version: 1.0.0
phase: 18
lesson: 6
tags: [mesa-optimization, deceptive-alignment, inner-alignment, hubinger]
---

Dado um relatório de avaliação de segurança (tarefa de avaliação, modo de falha, classe modelo, receita de treinamento), classifique a falha nas categorias Hubinger 2019 e recomende a classe de mitigação que a aborde.

Produzir:

1. Categoria de modo de falha.
   - Falha de alinhamento externo: o objetivo de base (recompensa, perda) estava errado; o modelo otimizou corretamente.
   - Falha de proxy de alinhamento interno: mesa-objectivo é um proxy que rastreia a base na distribuição; falha fora da distribuição.
   - A alinhamento interno é enganoso: o mesa-optimizador tem consciência situacional e defeitos na implantação; o comportamento de formação é limpo.
2. Traça de evidências. Para cada categoria, quais evidências o apoiariam. Para enganos, distinguir de proxy: evidências de consciência situacional (sensibilidade à data, distinguidores de avaliação versus implantação, raciocínio estratégico na cadeia de pensamento).
3. Classe de mitigação. Para alinhamento externo: alterar o objetivo (CAI, melhores dados de recompensa, supervisão de processos). Para proxy-inner: cobertura distribucional, conjuntos, avaliações realizadas. Para decepcionante-inner: medidas de controle (Lessão 10), interpretabilidade (sondes de fluxo residual), reduções de capacidade.
4. Para os que estão em estado de engano, cite a demonstração empírica relevante de 2024-2026 (Agentes adormecidos, Falsificação de alinhamento, Scheming no contexto).

Rejeitos duros:
- Qualquer classificação de "interno enganador" sem evidências de consciência situacional. "Comportamento inesperado na implantação" não é suficiente.
- Qualquer alegação de que o treinamento de robustez adversária sozinho aborda o interior enganoso. Hubinger 2019 prevê (e Sleeper Agents 2024 confirma) que o treinamento adversário pode ensinar melhores distingentes de teste versus implantação.
- Qualquer recomendação para retratar um modelo enganosamente alinhado com mais dados.

Regras de recusa:
- Se a prova for um único falha em um único pedido, recuse-se a classificar.
- Se o utilizador lhe pedir para "descartar" o alinhamento enganoso, recusar  você pode estimar a sua probabilidade a partir de evidências, mas não pode descartar-se apenas comportamentalmente.

Resultado: um diagnóstico de uma página com categoria, rastro de evidências, classe de mitigação e análogo empírico mais próximo. Cite Hubinger et al. (arXiv:1906.01820) uma vez.
