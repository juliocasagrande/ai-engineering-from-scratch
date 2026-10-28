---
name: finops-plan
description: Desenhar um programa de LLM FinOps  esquema de atribuição (usuário/tarefa/arrendante + quatro camadas de tokens), escada de execução de três níveis e métrica unitária (custo por resolvido / artefato).
version: 1.0.0
phase: 17
lesson: 27
tags: [finops, cost-attribution, multi-tenant, kill-switch, unit-economics, rate-limit]
---

Dada a superfície do produto, os níveis de inquilinos, os gastos mensais e o estado atual de atribuição, produzem um plano FinOps.

Produzir:

1. Esquema de atribuição. `user_id`- Não . `task_id`- Não . `route`- Não . `tenant_id` Em um caso de "computador de rede", o número de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de rede de
2. Metrica de unidade. Defina a métrica de resultado do produto  custo por bilhete resolvido, custo por artefato, custo por tarefa do agente, custo por sessão.
3. Escala de execução: limite de taxa por inquilino (2-3x máximo), limite de gastos diários (1,5-3x contrato), interruptor de eliminação em pontuação z > 4.
4. Painel de controle. 5 visualizações principais: gasto per capita hoje, custo por tarefa, resultado por usuário, impacto na taxa de cache, rotação de modelo dividida.
5. Auditoria de otimização em pilhas. Verificar o cache (fase 17 · 14), lote (fase 17 · 15), roteamento (fase 17 · 16), gateway (fase 17 · 19) estão todos envolvidos.
6. Revisão da cadência. Semanal: maiores gastos + anomalias. Mensal: economia unitária por inquilino. Quartal: re-triagem de cargas de trabalho em interativas/semi/parto.

Rejeitos duros:
- Envio sem atribuição no local de chamada. Recusar  etiquetado retroativo perde ~ 10-30% do gasto.
- Recusar  requer quatro camadas de divisão de tokens.
- O interruptor de extinção sem base de pontuação z. Recusar  requer estatísticas de linha de base antes de se armar.

Regras de recusa:
- Se o produto tiver < 10 inquilinos, a execução completa de vários inquilinos  requer primeiro a atribuição básica de inquilinos.
- Se o custo/resultado não for definido, rejeite o painel de instrumentos  escolha primeiro uma métrica unitária.
- Se um inquilino único for > 40% do gasto total, é necessário uma revisão de economia unitária específica antes de os planos serem enviados.

Resultado: um plano de uma página com esquema de atribuição, métrica unitária, escada de execução, painel de instrumentos, auditoria de otimização empilhada, cadência de revisão.
