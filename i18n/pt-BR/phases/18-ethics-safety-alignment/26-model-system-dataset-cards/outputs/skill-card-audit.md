---
name: card-audit
description: Audit a model card, datasheet, or system card for completeness and verifiability.
version: 1.0.0
phase: 18
lesson: 26
tags: [model-card, datasheet, system-card, transparency, mitchell-2019]
---

Dados de um modelo de cartão, ficha de dados ou cartão de sistema, auditoria para a integridade, desagregação numérica e verificabilidade.

Produzir:

1. Cobertura de seções. Verifique se todas as seções canônicas estão preenchidas. Flag faltantes: Considerações éticas é o campo de modelo de cartão mais comumente ignorado (Oreamuno et al. 2023).
2. Desagregação quantitativa. Para as métricas de avaliação, informe se a desagregação é fornecida em fatores demográficos ou de tarefas.
3. A linha de dados. Se o cartão refere dados de treinamento, existe uma folha de dados de acompanhamento (Gebru et al. 2018)?
4. Certificação verificável. Algumas alegações são apoiadas por atestados criptográficos (Laminator 2024, Duddu et al.) ou por outra verificação de terceiros?
5. A pegada de sustentabilidade. O uso de carbono / água / energia é relatado? 2025 emergente ISO / exigência regulamentar.

Rejeitos duros:
- Qualquer modelo de cartão sem considerações éticas.
- Qualquer cartão que cite um conjunto de dados sem folha de dados ou documentação equivalente.
- Qualquer cartão que afirme ser "testado de forma preconceituosa" sem relatórios métricos desagregados.

Regras de recusa:
- Se o usuário perguntar se um cartão é "bom o suficiente", recuse o binário; o bom o suficiente é específico para o público e caso de uso.
- Se o utilizador solicitar um cartão gerado automaticamente, recusar, a menos que seja utilizado um sistema de estilo CardGen (Liu et al. 2024) com revisão humana.

Resultado: uma auditoria de uma página preenchendo as cinco seções, marcando o conteúdo faltante e nomeando a adição mais urgente. Cite Mitchell et al. 2019 e Gebru et al. 2018 uma vez cada.
