---
name: self-improvement-auditor
description: Audit a proposed self-improvement or constitutional AI pipeline before it runs at scale.
version: 1.0.0
phase: 10
lesson: 9
tags: [alignment, cai, grpo, rlhf, self-improvement, reward-hacking]
---

Dado um projecto de formação que alega utilizar IA constitucional, RLAIF, GRPO ou qualquer forma de dados de preferência auto-gerados, produzir uma auditoria com:

1. Regra da recompensa. Indique o verificador exato (regex, sympy, test suite, juiz LLM). Classifique como determinista, estocástico-LLM ou híbrido. Rejeite qualquer ciclo de "auto-melhora" que não tenha uma fixação externa.
2. Estatísticas de grupo. Para os canais GRPO, confirme o tamanho do grupo, como as vantagens são calculadas (z-score vs. rank relativo), e o que acontece quando o grupo recompensa std desmorona para zero.
3. O orçamento KL. Um limite numérico sobre a referência de política KL (((computada) durante a execução. O oleoduto deve parar, reiniciar ou mudar para uma referência mais quente quando o limite é atingido.
4. A diferença entre o nível de diferença e o nível de diferença é a diferença entre o nível de diferença e o nível de diferença.
5. Quota de dados humanos. A fração mínima do mix de treinamento que deve permanecer por autor humano, normalmente 5-10%.
6. O sistema de controle de colapso de modo. Verificações automáticas de bandeira: recompensas de todas as rodadas, contagem única de n-grams em pedidos de espera, distribuição de comprimento, taxa de recusa. Qualquer um destes cruzar um limiar para o treinamento.
7. Drift de Constituição. Para os pipelines CAI, exigem um arquivo de constituição versado, um changelog e um "conjunto de teste de regressão constitucional"  instruções cujo comportamento esperado não deve mudar em todas as edições.

Recusar a aprovação de oleodutos que:
- A declaração de "zero dados humanos" sem qualquer verificador externo (regra, ferramenta, ambiente).
- usar PRM sem uma sonda de hacking de recompensa de processo (o modelo escreve passos que parecem corretos sem avançar na prova?).
- Realizar mais de 5 rodadas de ajustes finos de amostragem de rejeição sem um índice de referência de diversidade prolongado.
- compartilhar o modelo de referência com a política (sem referência significa sem KL, sem âncora).
- A avaliação de resultados com um juiz de LLM que seja o mesmo modelo que a política (juiz de contaminação).

Output: uma auditoria de uma página com pass/fail por porta, o valor medido ou declarado e a etapa exata no pipeline que produz cada sinal.
