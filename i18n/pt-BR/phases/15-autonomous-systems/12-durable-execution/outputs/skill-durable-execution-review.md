---
name: durable-execution-review
description: Revisar a implantação de um agente de longa duração proposta para obter a forma correta de execução duradoura (atividades, determinismo, backend de checkpoint, estado de entrada humana, HITL-on-resume).
version: 1.0.0
phase: 15
lesson: 12
tags: [durable-execution, workflows, checkpointing, temporal, langgraph, agents-sdk]
---

Dada uma implantação de agente de longa duração proposta (Temporal + OpenAI Agents SDK, LangGraph com checkpointer PostgreSQL, Microsoft Agent Framework, Claude Code Routines, Cloudflare Durable Objects ou um equivalente interno), auditem o projeto contra o padrão de execução durável.

Produzir:

1. **Activity inventory.** Lista todas as atividades (chamadas de LLM, chamadas de ferramentas, solicitações HTTP, gravação de arquivo). Para cada uma, confirme que ela é envolvida como uma atividade com política de retry, prazo de tempo e chave de idempotency. chamadas de LLM Raw fora do envelope de atividade são um buraco de confiabilidade.
2. **Workflow determinism.** Identifique todas as leituras não deterministas dentro do código do fluxo de trabalho (relógio de parede, aleatório, estado externo). Cada uma deve ser registrada como uma atividade de efeito colateral para que a repetição retorne o mesmo valor.
3. **Checkpoint backend.** Nomear o backend (PostgreSQL, SQLite, Redis, Durable Objects). Confirmar que sobrevive às implementações. SQLite é apenas dev. Redis requer configuração AOF ou snapshot. Cloudflare Durable Objects são transparentes, mas exigem uma disciplina chave única.
4. **Human-input state.** As pausas de confirmação para o HITL são um estado de fluxo de trabalho de primeira classe, não um ciclo de pesquisa. `interrupt()` A Comissão propõe que a Comissão adopte um regulamento que, em conformidade com o artigo 107.°, n.° 1, do Tratado, adopte um regulamento que, em conformidade com o artigo 107.°, n.° 1, do Tratado, reinicie a sua aplicação.
5. **HITL-on-resume policy.** Para qualquer currículo após um acidente, indique se é necessário um novo HITL antes de executar a próxima atividade. Sem isso, execução duradoura mais uma aprovação concedida antes do acidente podem reiniciar uma ação aprovada quando o contexto mudar.

Rejeitos duros:
- Utilização do SDK de agentes em que as chamadas de LLM não são incluídas como atividades.
- As back-ups do checkpoint não sobrevivem a uma implantação.
- Fluxos de trabalho que incorporam relógio de parede ou aleatórios sem envolvimento de atividades.
- A entrada humana modelada como um ciclo de pesquisa em vez de um sinal.
- Corridas de longo horizonte (mais de uma hora) sem política de HITL-on-resume.
- Funciona sem interruptor de eliminação de orçamento (Lessão 13) em camadas acima da durabilidade.

Regras de recusa:
- Se o utilizador propõe um fluxo de trabalho duradouro sem idempotencia explícita em actividades de efeitos colaterais, recusar e exigir primeiro as chaves de idempotencia.
- Se o utilizador não puder apresentar um teste de repetição (fluxo de trabalho de execução, crash no meio da execução, repetição, não afirmar efeitos colaterais duplos), recusar e exigir esse teste antes da produção.
- Se o utilizador propõe uma corrida de 24 horas sem supervisão sem ponto de controlo HITL, recuse-se. A degradação de 35 minutos (nota da lição 12) torna este um problema de confiabilidade mesmo que a durabilidade seja correta.

Formatos de saída:

Retorna um memorando de revisão do projeto com:
- **Activity table** (atividade, política de retomada, tempo de espera, chave de impotência)
- **Determinism audit** (leitações não deterministas e como cada um é tratado)
- **Checkpoint backend** (nome, sobrevivência-desenvolvimento y/n, estado do teste de repetição)
- **HITL state shape** (Estado de primeira classe / votação / desaparecido)
- **HITL-on-resume policy** (explicito, com raciocínio)
- **Readiness** (produzir / montar / apenas para investigação)
