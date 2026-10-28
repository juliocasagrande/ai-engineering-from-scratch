---
name: benchmark-reader
description: Read a multi-agent benchmark claim skeptically. Grades the claim on benchmark selection, contamination, baselines, statistical significance, task diversity, and cost disclosure.
version: 1.0.0
phase: 16
lesson: 24
tags: [multi-agent, benchmarks, evaluation, SWE-bench, MARBLE]
---

Dado um pedido publicado ou interno de desempenho de referência de vários agentes, classifique o pedido e as advertências de superfície.

Produzir:

1. **Benchmark + split identification.**Qual referência (MARBLE, COMMA, MedAgentBoard, AgentArch, SWE-bench Pro, SWE-bench Verified, custom)? Qual divisão (completa, prolongada, limpa de contaminação)?
2. **Contamination status.**Se o valor de referência for anterior ao período de tempo de ensaio, indicar o risco de contaminação e descontar a alegação.
3. **Baseline quality.**O sistema não é sintonizado, é uma ablação, não uma linha de base.
4. **Statistical significance.**N ensaios, intervalos de confiança ou erros padrão, p-valor ou equivalente.
5. **Task diversity.**Uma tarefa, um domínio ou muitos?
6. **Cost disclosure.**Tokens por tarefa, relógio de parede por tarefa, custo em dólares por tarefa. Uma solução de 90% a 20 vezes o custo é uma decisão de negócio; sem custo, a reivindicação é incompleta.
7. **Letter grade + one-sentence verdict.**

   - **A:**Passa-se os seis controlos; a alegação é provavelmente robusta.
   - **B:**Uma fraqueza: a alegação é plausível com advertenças notadas.
   - **C:**Duas fraquezas; a alegação é sugestiva, mas precisa de replicação.
   - **D:**Três ou mais fraquezas; a alegação não é prova.
   - **F:**Questão de desqualificação (contaminação em divisão não divulgada, não existem estatísticas, não há linha de base).

Rejeitos duros:

- As alegações que citam "SWE-bench" sem especificar Verified vs Pro. A lacuna de mais de 40 pontos torna este relatório ambíguo inaceitável.
- "Nosso sistema faz X%" é um número, não um resultado.
- Reclamações baseadas em menos de 20 ensaios para sistemas multi-agentes.
- Reclamações não declaradas de custos para sistemas multi-agentes.

Regras de recusa:

- Se o índice de referência não estiver disponível ao público e o utilizador não tiver rastro de auditoria interna, não pode ser atribuído um grau.
- Se a alegação for de um artigo atualmente sob revisão por pares (pre-impressão do arXiv, não submetida), rebaixar a classificação de uma letra como precaução até replicação.
- Se o utilizador for o próprio requerente que solicita uma auditoria, efetuar a auditoria diretamente; indicar quando a reivindicação ainda não está pronta para publicação.

Resultado: um cartão de nota de uma página. Comece com um resumo de uma frase ("Grado: C  boa escolha de referência, linhas de base adequadas, mas sem verificação de contaminação e sem divulgação de custos. "), em seguida, as sete seções acima.
