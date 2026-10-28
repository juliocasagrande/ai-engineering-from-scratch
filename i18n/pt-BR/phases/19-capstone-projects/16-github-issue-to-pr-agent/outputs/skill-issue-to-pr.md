---
name: issue-to-pr
description: Build an async GitHub issue-to-PR agent that runs in a cloud sandbox, reproduces the build, verifies tests, and opens review-ready PRs within strict per-repo budgets.
version: 1.0.0
phase: 19
lesson: 16
tags: [capstone, async-agent, github, fargate, daytona, swe-bench, budget, safety]
---

Dado um repositório GitHub com problemas rotulados `@agent fix this`, enviar um agente de nuvem auto-hostado que transforma cada problema rotulado em um PR pronto para revisão com credenciais de alcance e custo limitado.

Construir um plano:

1. Aplicação GitHub com token de grãos finos: questões rw, publicações de relações públicas, conteúdo rw, fluxos de trabalho leitura. Não pressão forçada. Proteção de ramo no principal impede a escrita direta.
2. O receptor Webhook (Lambda ou Fly.io) filtra os eventos de etiqueta / comentários de relações públicas e as fileiras para o SQS.
3. O Dispatcher impõe limites de $ e de conta de PR por cada repórter por dia; faz uma tarefa de ECS Fargate por cada trabalho permitido.
4. Inferência ambiental: detecta linguagem + gerenciador de pacotes + tempo de execução dos conteúdos de repo. Sintetize um arquivo docker à volante se ausente.
5. Daytona ou caixa de areia E2B por tarefa.`git worktree`+ Agente de ramo.
6. Loop de agente (mini-swe-agent ou SWE-agent v2 sobre Claude Opus 4.7 ou GPT-5.4-Codex). Ferramentas: ripgrep, tree-sitter repo-map, read_file, edit_file, run_tests, git. Caps: $20, 30 voltas, 30 min.
7. Verificar: IC completa em caixa de areia; cobertura delta via jacoco / coverage.py; etiqueta `needs-review`se o delta < -2%; parar se a CI estiver vermelha.
8. PR aberto através da API GitHub com raciocínio, resumo diferente, URL de rastreamento, custo, voltas.
9. Observabilidade: rastreamento de dados de longo prazo por relações públicas; registro de segredos; painel de instrumentos de orçamento por relações.
10. Evaluação em 30 questões internas sementes; comparação com Agentes de Background Cursor e Agentes SWE remotos da AWS em um subconjunto compartilhado de três questões.

Rubrico de avaliação:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | Pass rate on 30 issues | End-to-end success (CI green + coverage OK) |
| 20 | PR quality | Diff size, coverage delta, style conformance |
| 20 | Cost and latency per resolved issue | $/PR and wall-clock/PR |
| 20 | Safety | Scoped token, per-repo budget, no force-push, credential hygiene |
| 15 | Operator UX | Rationale comments, retry affordance, @-mention follow-up |

Rejeitos duros:

- Qualquer agente que possa forçar, exclusão difícil.
- Dispensadores que ignoram os cheques de orçamento.
- Os PRs abriram-se sem que a informação completa tenha passado na caixa de areia.
- Arquivos de rastreamento que contenham tokens ou PII não editados.

Regras de recusa:

- Recusar a instalação sem protecção do ramo no principal.
- Recusar-se a executar sem um orçamento diário por repórter (dolares e conta de PR).
- Recusar a reutilização de correções falhadas automaticamente; todas as reutilizações exigem uma reutilização de etiqueta humana.

Resultado: um repo contendo o GitHub App, o webhook receiver, o dispatcher + orçamento ledger, a definição de tarefa Fargate, o gerente de ciclo de vida da sandbox, o mini-swe-agent loop, a execução de avaliação de 30 questões, uma comparação lado a lado contra os Agentes de Background Cursor e os Agentes de SWE remotos da AWS, e um escrito nomeando as três principais falhas de construção de inferência e a alteração de síntese do Dockerfile que reduziu cada um.
