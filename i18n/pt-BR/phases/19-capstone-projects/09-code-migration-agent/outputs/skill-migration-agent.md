---
name: migration-agent
description: Build a repo-level code migration agent that combines deterministic recipes with an agent fallback loop, passes MigrationBench, and publishes a failure taxonomy.
version: 1.0.0
phase: 19
lesson: 09
tags: [capstone, code-migration, openrewrite, libcst, migrationbench, agent, sandbox]
---

Dado um repo Java 8 ou Python 2, produzir um ramo migrado (para Java 17 ou Python 3.12) com um conjunto de testes verde e regressão de cobertura mínima.

Construir um plano:

1. Pass determinista: OpenRewrite (Java) ou libcst (Python) executa reescrituras mecânicas primeiro. Compromete-se como a "receita" com uma diferença limpa.
2. Sandbox Daytona: tempo de execução do alvo pré-instalado; construção por ramo; montagem de fonte somente para leitura.
3. Loop de Agentes: LangGraph ou OpenAI Agents SDK sobre Claude Opus 4.7 + GPT-5.4-Codex. Ferramentas: `run_build`- Não .`read_file`- Não .`edit_file`- Não .`run_test`- Não .`git_diff`- Classificar falhas (profundidade, sintaxe, teste, ferramenta de construção), aplicar correcção direccionada, reinicialização.
4. Limites de orçamento: 30 min, 8 dólares, 20 voltas.`budget_exhausted`com a diferença de corrente.
5. Teste + porta de cobertura: construção verde e depois teste verde; a cobertura não deve cair mais de 2%.
6. PR aberto com receita-compromissado + agente compromete + comentário resumido.
7. Taxonomia de falhas: tag por relatório de `{dep_upgrade_required, build_tool_drift, custom_annotation, test_flake, syntax_edge_case, budget_exhausted, coverage_regression}`- Não .
8. 50 repos em MigrationBench; publicar taxa de aprovação por classe, custo por repos e preservação da cobertura; comparar versus linha de base apenas determinista.

Rubrico de avaliação:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | MigrationBench pass rate | 50-repo subset pass@1 |
| 20 | Test-coverage preservation | Mean coverage delta vs base branch |
| 20 | Cost per migrated repo | Mean $/repo on passing runs |
| 20 | Agent / deterministic-tool integration | Fraction of fixes handled by OpenRewrite vs agent |
| 15 | Failure analysis write-up | Taxonomy completeness with exemplars |

Rejeitos duros:

- O OpenRewrite lida com o mecanismo 70 a 80% mais barato e mais confiável do que qualquer agente.
- Regressões de cobertura acima de 2% tratadas como passagens.
- As relações públicas que unem mudanças mecânicas e de autor do agente num único compromisso.
- Relatório de taxa de passagem sem uma linha de base determinista apenas correspondente nos mesmos 50 repos.

Regras de recusa:

- Recusar-se a empurrar forçadamente um ramo migrado sobre a base.
- Recusar-se a abrir uma PR cujo informador não tenha dado a volta verde na caixa de areia.
- Recusar-se a executar em repositorios corporativos sem licença explícita para modificar.

Resultado: um repo contendo o pipeline de migração de duas camadas, os registros de execução do MigrationBench de 50 repos, o painel de taxonomia de falhas, uma execução de base com base apenas em determinismo, e uma redação sobre as três classes de falhas mais comuns e a alteração da receita que eliminaria cada uma.
