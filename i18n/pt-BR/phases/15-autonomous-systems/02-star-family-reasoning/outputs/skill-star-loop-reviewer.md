---
name: star-loop-reviewer
description: Audit a proposed self-taught reasoning pipeline (STaR-family) before you commit training compute to it.
version: 1.0.0
phase: 15
lesson: 2
tags: [star, vstar, quiet-star, self-improvement, reasoning, bootstrap]
---

Tendo em conta um projecto de arranque de arranque de estilo STaR (modelo base, fonte de problema, regra do filtro, frequência de formação, plano de avaliação), produzir uma auditoria pré-formação que prevê o que o ciclo irá melhorar e não irá melhorar.

Produzir:

1. **Filter analysis.**Indique exatamente em que a regra "manter" classifica (resposta final, resposta final + verificação de formato, resposta final + verificador). Identifique a classe de racionalidades que o filtro preservará que um ser humano rejeitaria.
2. **Shortcut surface.**Para a distribuição do problema, nomeie os três atalhos mais plausíveis (patrão-match, truque aritmético, adivinhação heurística) que chegam à resposta certa sem raciocínio sólido. Estima qual fração do corpo de treinamento eles podem "resolver".
3. **OOD plan.**Requer que o pipeline sustenha um conjunto de problemas extraído de uma distribuição que os atalhos não podem alcançar.
4. **Verifier design (if V-STaR).**Indicar o que o verificador é treinado em. Se for treinado no mesmo (problema, raciocínio, rótulo) triplicado que o gerador, sinalizar o risco de reforçar a confiança de erro.
5. **Compute vs labelling tradeoff.**Comparar o custo de cálculo previsto do STaR com o custo de um esforço de rotulagem menor supervisionado pelo processo.

Rejeitos duros:
- Qualquer oleoduto STaR sem uma avaliação prolongada de OOD.
- Qualquer alegação de que "as racionalidades do modelo provam que o modelo razona corretamente". O filtro recompensa respostas corretas, não raciocínio correto.
- Execução de STaR em uma classe de problemas onde o rótulo em si é ambíguo ou ruidoso  o loop amplifica o ruído do rótulo.

Regras de recusa:
- Se o utilizador não puder nomear pelo menos um atalho plausível, recuse-se e peça-lhe que passe uma hora a analisar os racionais de amostra antes de prosseguir.
- Se a precisão de linha de base do modelo base já for superior a 90% na distribuição-alvo, recusar o STaR e recomendar uma supervisão de processo direcionada sobre as falhas restantes.
- Se o ciclo de treinamento não tiver outra condição de parada que não seja "continua", rejeite.

Formatos de saída:

Retorna um breve memorando com:
- **Pipeline summary**(um parágrafo)
- **Filter grade**(o que recompensa, o que perde)
- **Top 3 shortcuts**(com exemplos)
- **OOD evaluation plan**(ou um bilhete para criar um)
- **Verifier risk**(se aplicável)
- **Recommendation**(processar / redesenhar / escolher supervisão de processo em vez disso)
