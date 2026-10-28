---
name: multi-agent-team
description: Construir uma equipe de software multi-agente com arquiteto, codificadores paralelos, revisor e testador; medir contra o banco SWE Pro e produzir uma entrega pós-mortem.
version: 1.0.0
phase: 19
lesson: 10
tags: [capstone, multi-agent, swe-bench, langgraph, a2a, worktree, roles]
---

Dado um URL de questão do GitHub e um nível de paralelismo, implantar uma equipe de software multi-agente que produz um PR pronto para fusão. Avalie 50 problemas de SWE-bench Pro e publique um histograma de falhas de entrega.

Construir um plano:

1. Tabela de tarefas: arquivo de arquivo (ou Redis) JSONL armazenamento de mensagens digitadas. Tipos de mensagens: plan_request, subtask, diff_ready, review_needed, review_feedback, approved, test_needed, test_passed, test_failed, replan_needed.
2. Arquiteto (Opus 4.7): lê o tema, escreve um plano, emite um DAG de subtarefas com interfaces explícitas (arquivos tocados, funções públicas, impacto de teste).
3. N codificadores (Soneta 4.7): cada um reivindica uma subtarefa, gera uma nova `git worktree add` + Sandbox Daytona, implementa-se de forma independente.
4. Coordenador de fusão: fusão trilateral; solução de conflitos mediada pela LLM apenas em caso de sobreposição de arquivos.
5. Revisor (GPT-5.4): lê a diferença combinada; não pode aprovar as diferenças que foi criado; emite o feedback aprovado ou revisão/revisão encaminhado para o codificador relevante.
6. Tester (Gemini 2.5 Pro): executa a suíte de teste em uma caixa de areia limpa; emite test_passed ou test_failed com artefatos.
7. Contabilidade de transferência: cada mensagem de rol cruzado se torna um espaço de Langfuse com tamanho e modelo de carga útil.
8. Injecte uma sonda de bug óbvia (10% das corridas) para medir a taxa de aprovação falsa do revisor.
9. Execute em 50 números Pro do banco SWE; publique pass@1, o relógio de parede versus linha de base de agente único, desvio de tokens por função, histograma de falha de entrega.

Rubrico de avaliação:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | SWE-bench Pro pass@1 | 50-issue subset pass@1 |
| 20 | Parallel speedup | Wall-clock vs single-agent baseline |
| 20 | Review quality | False-approval rate on injected-bug probe |
| 20 | Token efficiency | Total tokens per solved issue vs single-agent |
| 15 | Coordination engineering | Merge-conflict resolution, handoff-failure histogram |

Rejeitos duros:

- O revisor que pode aprovar as propostas é diferente do autor.
- Relatórios sem uma corrida de base de agente único correspondente. Multicagente tem que ganhar * por dólar*, não apenas pass@1.
- Painéis de tarefas onde as mensagens são cadeias de forma livre em vez de mensagens A2A digitadas.
- Coordenadores de fusão que causam silenciosamente diferenças conflitantes em vez de voltar para replan.

Regras de recusa:

- Recusar-se a executar sem limites orçamentais por função (token + dólar).
- Recusar-se a abrir uma PR cujo testeiro não tenha verificado numa caixa de areia limpa.
- Recusar escalar os codificadores para além de 8 numa única corrida.

Resultado: um repo contendo o painel de tarefas + funcionários de papéis, o registro de execução do SWE-bench Pro de 50 edições, uma execução de linha de base de agente único correspondente, um painel de controle Langfuse com intervalos de rotulagem de roteiros e rupturas de tokens por papel, um relatório de sonda de bugs injetados e um pós-mortem nomeando as três entregas que quebraram com mais frequência e o esquema de mensagem ou mudança imediata que reduziu cada uma.
