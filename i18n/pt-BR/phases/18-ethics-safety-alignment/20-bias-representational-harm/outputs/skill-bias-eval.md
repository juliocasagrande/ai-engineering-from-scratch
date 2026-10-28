---
name: bias-eval
description: Audit a bias evaluation report across metric categories, intersectionality, and debias mechanism.
version: 1.0.0
phase: 18
lesson: 20
tags: [bias, fairness, weat, intersectionality, mechanistic-interpretability]
---

Tendo em conta um relatório de avaliação de preconceito ou uma alegação de equidade, auditoria em toda a estrutura de três categorias de Gallegos et al. 2024 e na literatura interseccionalidade 2024-2025.

Produzir:

1. Cobertura métrica. A avaliação inclui pelo menos uma métrica de cada categoria: baseada em embutidos (estilo WEAT), baseada em probabilidade (estereótipo de log-probabilidade), baseada em texto gerado (medida de tarefas a jusante)?
2. A avaliação distingue os danos representativos dos danos atribuídos? Um relatório que mede apenas a produção estereotipada não mede a alocação de recursos a jusante.
3. Cobertura de interseccionalidade. Os eixos interseccionais são avaliados, ou apenas por um único eixo (somente gênero, apenas raça)?
4. Mecanismo de Debias. Se o debiasing for aplicado, identifique se funciona em embebimentos (projeção), neurônios MLP (Yu & Ananiadou 2025), recursos SAE (Ahsan & Wallace 2025), cabeças de atenção (UniBias 2024), ou filtragem de saída pós-hoc. Estima o custo de capacidade geral.
5. Diversidade do eixo. Segundo a meta-crítica de 2025, o viés binário de gênero é sobre-estudo em relação a outros eixos. A avaliação abrange a deficiência, religião, migração ou eixos de identidade multilingües?

Rejeitos duros:
- Qualquer alegação "debiada" baseada numa única categoria métrica.
- Qualquer alegação de equidade sem avaliação interseccional.
- Qualquer intervenção debias sem um delta de capacidade geral.

Regras de recusa:
- Se o usuário perguntar se o seu modelo é "livre de viés", recusar a alegação binária; viés é uma propriedade contínua com múltiplas métricas.
- Se o utilizador solicitar uma operação debias recomendada, recusar uma única recomendação  A escolha depende de onde o viés vive (embedamentos, neurônios, cabeças, saídas).

Resultado: uma auditoria de uma página preenchendo as cinco seções, marcando categorias métricas faltantes e recomendando a avaliação adicional única de maior valor. Cite Gallegos et al. 2024 e um documento de interseccionalidade 2024-2025 uma vez cada.
