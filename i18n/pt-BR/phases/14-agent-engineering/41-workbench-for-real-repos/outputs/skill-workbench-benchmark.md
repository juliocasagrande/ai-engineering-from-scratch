---
name: workbench-benchmark
description: Executa a mesma tarefa através de canais orientados apenas para o momento e com base no banco de trabalho no próprio aplicativo de amostra de um projeto e emite um relatório de cinco resultados antes/após.
version: 1.0.0
phase: 14
lesson: 41
tags: [benchmark, before-after, evaluation, workbench, sample-app]
---

Dado um repo, um produto agente e uma pequena aplicação de amostra, produzem um arame de avaliação portátil que compara apenas o prompt com os canais guiados por banco de trabalho.

Produzir:

1. `eval/sample_app/`  um modelo de aplicação de viabilidade mínima extraído do domínio do projecto.
2. `eval/run_prompt_only.py` e `eval/run_workbench.py` que cada um tome uma descrição da tarefa e retorne um `TaskOutcome`- Não .
3. `eval/report.py` que opera os dois canais e escreve `before-after-report.md` Mais `comparison.json`- Não .
4. Fluxo de trabalho de informação que falha quando os resultados do banco de trabalho regressam a um conjunto de tarefas fixo.
5. `docs/benchmark.md` O que é que é uma regressão?

Rejeitos duros:

- Um ponto de referência com apenas um pipeline.
- Resultados expressos em percentagens sem denominador. `n / m`- Não .
- Uma aplicação de amostra em que o produto agente foi treinado.
- Relatórios que escondem falsos negativos, tarefas onde apenas o prompt foi mais rápido devem ser enumerados.

Regras de recusa:

- Se o projecto não tiver um comando de aceitação, recuse-se a enviar o índice de referência.
- Se o conjunto de canais de trabalho ocupa mais de 3 vezes o conjunto de canais de apenas-pronto na tarefa média, superficial que a descoberta; o banco de trabalho precisa de simplificação, não o modelo.
- Se o arnes não puder funcionar offline, recuse-se a ligar-o para o CI.

Estrutura de saída:

```
<repo>/
├── eval/
│   ├── sample_app/
│   ├── run_prompt_only.py
│   ├── run_workbench.py
│   └── report.py
├── outputs/eval/
│   ├── before-after-report.md
│   └── comparison.json
├── docs/benchmark.md
└── .github/workflows/benchmark.yml
```

Conclui com "o que ler a seguir" apontando para:

- Lição 42 para o pacote de pedra que agrupa todas as superfícies utilizadas pelo gasoduto do banco de trabalho.
- A lição 19 (SWE-bench, GAIA, AgentBench) para os macro-referências complementa esta.
- Lição 30 (Divulgação de Agentes de Evaluação) para os ciclos de avaliação em curso uma vez que o índice de referência é conectado.
