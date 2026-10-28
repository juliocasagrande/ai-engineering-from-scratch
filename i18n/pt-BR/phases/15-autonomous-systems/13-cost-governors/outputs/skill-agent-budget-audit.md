---
name: agent-budget-audit
description: Auditar a pilha de governadores de custos de uma missão de agente e identificar as camadas faltantes antes de permitir a execução desatendida.
version: 1.0.0
phase: 15
lesson: 13
tags: [cost-governors, denial-of-wallet, budgets, claude-code-sdk, agent-governance]
---

Tendo em conta a implantação de agentes proposta, auditá-la em função da pilha de governadores de custos, comparando-a com as 12 camadas de referência e de bandeira, que não existem, não estão adequadas ou estão excessivamente ajustadas.

Produzir:

1. **Layer inventory.** Para cada uma das doze camadas de referência (título máximo por solicitação, orçamento de tokens por tarefa, orçamento por dólar por tarefa, limite máximo por ferramenta, limite máximo de iteração, limite máximo de rodamento por minuto/hora/dia/mês, limite de velocidade, roteamento em camadas, cache de prompt, janela de contexto, pontos de verificação HITL, interruptor de eliminação), indicar se está configurado e a que valor.
2. **Failure-mode mapping.** Para cada falha na escala temporal (loop de fuga, vazamento lento, liberação ruim, aumento legítimo), nome a camada específica que a pega e quão rápido.
3. **Tool-specific caps.** Lista todas as ferramentas que o agente pode chamar. Para cada uma, nome um limite por sessão e uma razão. Qualquer ferramenta sem um limite explícito é um ciclo aberto.
4. **Alert thresholds.** Separado dos limites: a que taxa de despesa um ser humano é chamado?$1,200 → $O problema de crescimento foi de semana em semana, não de limite mensal.
5. **Kill-switch path.** Quando um cap disparar, o que acontece? limpar abortar, reverter, alerta, re-habilitar o procedimento. confirmar o interruptor de externo do agente (o agente não pode editar seu próprio cap).

Rejeitos duros:
- Qualquer implantação autónoma sem um orçamento de dólares por tarefa.
- Qualquer corrida de longo horizonte sem controlo sem limite de velocidade.
- Superfícies de ferramentas sem tampa por ferramenta em uma nova adição de ferramentas (< 30 dias).
- O agente pode modificar os interruptores de morte.
- Capitação mensal como única capitação (todas as outras escalas de tempo não são guardadas).

Regras de recusa:
- Se o utilizador não puder avaliar um pior caso com os preços do modelo atual, recusar e exigir uma estimativa do custo.
- Se o orçamento proposto exceder a perda aceitável da organização por um único erro, recusar e exigir um limite inferior.
- Se o utilizador tratar o classificador de modo automático (Lessão 10) como um substituto para os orçamentos, rejeite.

Formatos de saída:

Retorno de uma auditoria de governador de custos com:
- **Layer table** (nome da camada, configuração y/n, valor)
- **Failure-mode coverage** (4 fileiras: ciclo / vazamento / liberação / aumento)
- **Per-tool caps** (ferramenta, chapéu, razão)
- **Alert thresholds** (taxa, proprietário, canal)
- **Kill-switch path** (trigger, ação, procedimento de reativação)
- **Readiness** (produzir / montar / apenas para investigação)
