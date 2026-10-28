---
name: fairness-criterion
description: Identificar quais critérios de equidade invocam uma alegação e auditar as suposições associadas.
version: 1.0.0
phase: 18
lesson: 21
tags: [fairness, demographic-parity, equalized-odds, counterfactual-fairness, impossibility]
---

Em função de uma alegação ou política de equidade, identifique qual é o critério invocado, de que suposições depende a alegação e o que os teoremas de impossibilidade implicam para os restantes critérios.

Produzir:

1. Identificação de critérios. Marcar a alegação como tendo como alvo uma das seguintes: paridade demográfica, probabilidades igualadas, igualdade de precisão de utilização condicional, equidade individual, equidade contrafactual.
2. Auditoria de taxa base. Quais são as taxas base por grupo na implantação? Sob taxas base desiguais, aplica-se a impossibilidade Chouldechova / KMR 2017: nenhum modelo satisfaz os três critérios do grupo.
3. A taxa de juro de base é igual a uma taxa de juro de base, que é igual a uma taxa de juro de base, que é igual a uma taxa de juro de base.
4. A seleção é específica de tarefa e é uma decisão política, não estatística.
5. A legalidade da intervenção. Se a alegação usa raciocínio contrafactual, são envolvidas intervenções sobre atributos protegidos?

Rejeitos duros:
- Qualquer alegação "justa" sem identificação de critérios.
- Qualquer alegação de "todos os critérios de justiça satisfeitos" sob taxas de base desiguais sem reconhecer Chouldechova / KMR 2017.
- Qualquer alegação de equidade contrafactual sem um DAG causal publicado.

Regras de recusa:
- Se o utilizador perguntar qual é o critério de equidade "o certo", recusar a classificação e explicar que é uma escolha política.
- Se o utilizador perguntar se um modelo é "justo", recusar a alegação binária; a equidade é criterial-relativa.

Resultado: uma auditoria de uma página preenchendo as cinco seções acima, marcando a impossibilidade, se aplicável, e nomeando a escolha de política implícita na reivindicação. Cite Dwork et al. 2012, Kusner et al. 2017, Chouldechova 2017 uma vez cada uma conforme apropriado.
