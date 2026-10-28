---
name: benchmark-harness
description: Build a SWE-bench-style harness for a codebase with FAIL_TO_PASS / PASS_TO_PASS gating, contamination checks, and step-count metrics.
version: 1.0.0
phase: 14
lesson: 19
tags: [swe-bench, gaia, agentbench, harness, evaluation]
---

Dado um código base e uma lista de pares (bug, fix), construir um arnes de referência que aborda os testes reais de unidade e registra métricas operacionais.

Produzir:

1. Definição por tarefa: `(tid, description, state_before, fail_to_pass_tests, pass_to_pass_tests, solution)`- Não .
2. Um corredor que aplica o patch do agente, executa o conjunto de testes do repo em uma caixa de areia e registra: contagem de passes FTP, contagem de passes PTP, contagem de passos, tokens, relógio de parede, custo.
3. Verificação de contaminação: padrão de correspondência do texto da questão com o corrector produzido; sobreposição de bandeira >=30%.
4. Um repórter que emite pontuações por tarefa e agregadas como JSON, mais P50/P75/P95 passo e custo.
5. Um trabalho de CI que controla todas as relações públicas e falha em >=5% de regressão.

Rejeitos duros:

- Aproveite que relate apenas um único número agregado. Requer resultados por tarefa + distribuições.
- Arneses que executam testes sem caixa de areia.
- Arranque sem porta PASS_TO_PASS. Os parches que quebram outros testes regressam silenciosamente ao produto.

Regras de recusa:

- Se o usuário pedir "apenas a pontuação FAIL_TO_PASS", rejeite. Adicione PASS_TO_PASS; quebrar os testes existentes é uma regressão pior do que perder a correção.
- Se os testes não forem fixados a um compromisso específico, rejeite.
- Se as tarefas se sobrepõem com o texto de questão visto durante o treinamento, marque-o explicitamente.

Output: `tasks.py`- Não .`harness.py`- Não .`contamination.py`- Não .`report.py`- Não .`README.md`Afinal, com "o que ler a seguir", apontando para a lição 30 para desenvolvimento orientado para avaliação no topo do arame.
