---
name: refine-loop
description: Configure um loop de avaliador-optimizador (Self-Refine / CRITIC) dada tarefa, disponibilidade do verificador e orçamento de iteração.
version: 1.0.0
phase: 14
lesson: 05
tags: [self-refine, critic, evaluator-optimizer, guardrails, iteration]
---

Dada uma tarefa, um orçamento de iteração e o verificador disponível (apenas baseado em ferramentas ou auto-evaluado), emitir instruções e uma política de parada para um ciclo de avaliador-optimizador.

Produzir:

1. Gerador de prompt. Produtor determinista para a primeira saída. Indique explicitamente a tarefa, o formato de saída e as restrições.
2. Se as ferramentas estiverem disponíveis (busca, execução de código, testes, calculadora, verificação de tipo), especifique como chamá-las e como produzir uma crítica estruturada (JSON com: pass/fail, violações[], sugerido_fixes[]). Se apenas auto-eval estiver disponível, marque explicitamente o risco de auto-refinamento de selo de borracha e use um estilo de prompt estruturalmente diferente (por exemplo, adversário "encontrar pelo menos uma falha").
3. Refiner prompt. Deve referir-se a saídas e críticas anteriores (história). A declaração "não repita um modo de falha marcado em iterações anteriores" é obrigatória.
4. A conjunção: verificador passa OR (auto-val diz bem E iterações >= 2) OR iterações >= max_iterations. Nunca única condição.
5. Anéis de observabilidade. Registre cada iteração como um espaço de OpenTelemetry GenAI (avaliação, otimização) por lição 23, para que a trajetória completa de refinamento seja auditável.

Rejeitos duros:

- O mesmo aviso para o gerador e o crítico.
- Não há limite de iteração. Loops infinitos de refinamento queimam tokens; sempre limite a 4 por padrão.
- Verificador de prompt que pede para o feedback de prosa de forma livre. JSON estruturado apenas  pass/fail mais violações detalhadas.
- O papel mostra que a qualidade cai sem ele.

Regras de recusa:

- Se a tarefa não tiver verificador e não tiver forma de construí-lo, recuse-se a CRITIC e note que Auto-Refine é a opção mais fraca disponível  avise o usuário sobre o risco de selos de borracha.
- Se max_iterations >= 10, recusar e recomendar rearquitetar a tarefa. Refinar para convergência além de 3-4 passes é geralmente um sinal de que o prompt do gerador está errado.
- Se o verificador chamar ferramentas destrutivas (shell, git write), recusar e exigir um limite de caixa de areia (Lessão 09).

Saída: um único bloco de configuração com todas as instruções, política de parada e lista de ferramentas, além de uma nota de "o que ler a seguir" apontando para a lição 16 (OpenAI Agents SDK guardrails), lição 12 (Anthropic evaluator-optimizer), ou lição 30 (desenvolvimento de agente orientado por valores) com base no objetivo de implantação.
