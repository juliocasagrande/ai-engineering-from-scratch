---
name: batch-triager
description: Triage LLM workloads into interactive / semi-interactive / batch lanes, compute stacked discount (batch + cache) savings, and flag mis-triaged workloads.
version: 1.0.0
phase: 17
lesson: 15
tags: [batch-api, openai-batch, anthropic-batches, vertex-batch, triage, cost]
---

Dada uma carga de trabalho (nome, expectativa do usuário de latência, volume de tráfego, estrutura de prompt compartilhada), produzir um plano de triagem + custo.

Produzir:

1. Lane. Interativo (TTFT-bound, sincronização), semi-interativo (minutos OK, fila de sincronização), ou lote (tomada de manhã OK, API lote). Justificar com a expectativa específica do usuário.
2. Custo corrente. Calcule o custo mensal na configuração atual (sincronização, sem cache, etc.).
3. Custo alvo. Calcule o custo após a configuração recomendada (batch + cache ou sincronização + cache). Expressar como % da corrente.
4. Plano de migração. Passo específico do prestador (escolha o que corresponda ao modelo da carga de trabalho, não ambos):
   - OpenAI: migrar para `/v1/batches`. O caching rápido é habilitado automaticamente para os pedidos de resposta elegíveis (tokens ≥1024)  não `cache_control`- Oxalá passe.`prompt_cache_key`para atribuição mais estreita.
   - Antropic: migrar para Batches de Mensagens. Reutilização de cache requer explícito `cache_control`Blocos (por exemplo, `{"type": "ephemeral"}`) sobre os intervalos de pedido em cache; pilhas de desconto de lote com preços em cache.
   - Ambos: instrumento de um acessório de sucesso/falha e de um caminho de transmissão para sincronizar os lotes que não têm a sua janela de rotação.
5. Risco. E se a rotação do lote for de 20 horas no P99? Nomear o comportamento do sistema a jusante (entrega de e-mail, fila de transmissão para sincronização).
6. Observavel. Métrica que detecta erroneamente o triagem: latência de conclusão de trabalhos de lote P95; alerta se > 12 horas.

Rejeitos duros:
- Execução de um pipeline durante a noite em modo sincronizado sem lote quando o usuário só precisa de latência "até manhã".
- Batch promissor para qualquer coisa com uma expectativa de usuário inferior a 15 minutos.
- Ignorar o cache de instruções em uma carga de trabalho de lote com instruções de sistema compartilhadas.

Regras de recusa:
- Se a carga de trabalho for comercializada como "em tempo real", mas a expectativa real do utilizador for de minutos, é necessário uma confirmação explícita antes de recomendar o lote.
- Se a carga de trabalho visa um provedor sem cache imediato em lote (por exemplo, qualquer pila personalizada ou auto-hospedada sem reutilização do prefixo KV), note que apenas o desconto de lote se aplica e recompite sem economias em lote.`cache_control`- Quartos.
- Se a carga de trabalho tiver um SLA de latência rigorosa (por exemplo, P99 < 60s), rejeite bateria directamente  pertence a uma faixa diferente.

Resultado: triagem de uma página com faixa, custo corrente, custo-alvo, etapas de migração, risco, observável.
