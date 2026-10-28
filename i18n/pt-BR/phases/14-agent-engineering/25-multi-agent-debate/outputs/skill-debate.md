---
name: debate
description: Estabelecer um debate multi-agente com N debaters, R rodadas, topologia configurável (mesha completa, estrela, anel), e uma regra de convergência.
version: 1.0.0
phase: 14
lesson: 25
tags: [debate, multi-agent, society-of-minds, sparse-topology]
---

Dada uma classe de perguntas e um objetivo de precisão, estabeleça um protocolo de debate.

Produzir:

1. `Debater` A Comissão deve, por conseguinte, dar início a uma análise de que os dados relativos aos produtos de origem são de natureza a permitir que os produtos de origem sejam utilizados em conformidade com o artigo 107.o, n.o 1, do Regulamento (CE) n.o 1069/2009 e, em caso de alteração do Regulamento (CE) n.o 1069/2009 do Parlamento Europeu e do Conselho.
2. Corredor redondo: maça completa, estrela ou topologia de anel.
3. Regra de convergência: maioria-voto, ponderada pela confiança, ou supermajoridade-com-recaída.
4. Ronda 1 - Discordância forçada: cada debateiro retorna uma proposta distinta, se possível.
5. Contabilidade de custos: operações de crítica totais + custo de tokens por pergunta.

Rejeitos duros:

- Todos os debatedores com o mesmo impulso e o mesmo modelo.
- Messa completa com N >= 6 sem custo de verificação.
- Não há regra de convergência. Returnar a resposta R redonda do debatedor 0 não é convergência.

Regras de recusa:

- Se o produto for sensível à latência (orçamento < 1s), recuse o debate.
- Se a classe de perguntas é uma simples pesquisa factual (capital, data, definição), rejeite o debate.
- Se os debatedores não tiverem desacordo após a primeira rodada sobre qualquer questão no conjunto de avaliação, rejeitem o protocolo.

Output: `debater.py`- Não . `topology.py`- Não . `convergence.py`- Não . `runner.py`- Não . `README.md` Explicando a escolha de N/R, a racionalização da topologia e as medições de custo versus precisão no conjunto de avaliação. Conclui com "o que ler a seguir" apontando para a lição 12 (patrões de fluxo de trabalho) se a tarefa for mais simples, ou a lição 28 (patrões de orquestração) para incorporar o debate em um sistema maior.
