---
name: skill-cost-patterns
description: Decision framework for LLM cost optimization -- caching strategies, rate limiting, model routing, and budget controls
version: 1.0.0
phase: 11
lesson: 11
tags: [caching, cost-optimization, rate-limiting, model-routing, budget, llm-ops]
---

# Padrões de otimização de custos de LLM

Ao criar um pedido de Mestrado em Direito Jurídico que precise controlar os custos, aplicar este quadro de decisão.

## Quando otimizar

**Optimize immediately when:**
- O gasto mensal do LLM excede US$ 500 ou 10% do orçamento de infraestrutura
- O custo por consulta é superior a 0,01 dólares para um produto de consumo
- O seu sistema de solicitação é mais de 1.000 tokens e enviado com cada pedido
- Mais de 30% das consultas são duplicadas ou quase duplicadas
- Você está a escalar de 100 a 10.000 usuários diários

**Do not optimize yet when:**
- Ter menos de 100 DAU e ainda estar a validar a adequação do produto ao mercado
- O gasto mensal é inferior a 100 dólares e cresce lentamente
- Você ainda está iterando no projeto de prompt (caching bloqueia você em um prompt)

## Seleção de estratégia de caching

### Cachagem exacta

**Use when:**temperatura=0, repetem-se as mesmas instruções, são necessárias saídas deterministas.

```python
key = sha256(json.dumps({"model": m, "messages": msgs, "temp": 0}))
```

- Execução: 30 minutos
- Taxa de hits: 10-25% para a maioria dos aplicativos, 40-60% para bots FAQ
- Latência: < 1ms (requisitação direta)
- Risco: respostas obsoletas em caso de alterações nos dados subjacentes

**Skip when:**temperatura > 0, cada consulta é única, necessários dados em tempo real.

### Caching semântico

**Use when:**Os usuários fazem a mesma pergunta em palavras diferentes, produtos com FAQs pesados, suporte ao cliente.

- Implementação: 2-4 horas (emblematização + semelhança + armazenamento)
- Taxa de impacto: 15-35% em cima do cache exato
- Latência: 10-50ms (embedding + ANN search)
- Risco: falsos positivos (retorno de resposta errada em cache para uma pergunta semelhante mas diferente)

**Threshold guidelines:**
- 0,98+: muito conservador, quase sem falsos positivos, menor taxa de impacto
- 0,95: bom equilíbrio para questões e respostas factuais
- 0,90: agressivo, maior taxa de acidentes mas risco de respostas erradas
- 0,85: apenas para aplicações de baixo risco (sugestões, autocompletamento)

**Skip when:**Cada consulta tem um contexto único (geração de código), as respostas devem refletir os dados mais recentes, o espaço da consulta é ilimitado.

### Cachagem de serviço de fornecedor

**Use when:**Sistema de resposta > 1.024 tokens (OpenAI) ou mínimo específico do modelo, o mesmo prefixo enviado repetidamente.

| Provider | Action | Savings |
|----------|--------|---------|
| Anthropic | Add `cache_control: {"type": "ephemeral"}` to system message | 90% on cached prefix (after 25% write premium) |
| OpenAI | Nothing (automatic) | 50% on cached prefix |
| Google | Use Context Caching API with explicit TTL | ~75% on cached context |

**Skip when:**alterações de pedido de sistema, o pedido é inferior ao mínimo de comprimento.

## Regras de roteamento modelo

### Baseado em palavras-chave (simples, rápidas)

```
simple:  <= 5 words OR matches FAQ keywords -> gpt-4o-mini ($0.15/$0.60)
medium:  general queries, summaries        -> claude-sonnet ($3/$15)
complex: "analyze", "compare", "debug"     -> gpt-4o ($2.50/$10)
```

- Implementação: 1 hora
- Precuração: 70-80%
- Economia: 40-60% dos custos do modelo

### Baseado em embutidos (mais preciso)

Incorporar 50-100 consultas rotuladas por categoria. Classificar novas consultas pelo vizinho mais próximo.

- Implementação: 4-8 horas
- Precision: 85-92%
- Economia: 50-70% dos custos do modelo
- Custo adicional: ~$0,02/1M de tokens para inserções de classificação (negligível)

### Baseado em ML (grado de produção)

Treinar um pequeno classificador (regressão logística ou pequeno BERT) em pares de consulta/modelo histórico.

- Implementação: 1-2 semanas
- Precision: 90-95%
- Economia: 60-75% dos custos do modelo
- Requisitos: dados de formação rotulados do tráfego de produção

## Configuração de limitação de taxa

### Parâmetros do balde de tokens por nível

| Tier | Bucket Size | Refill Rate | Max RPM | Daily Cap |
|------|-------------|-------------|---------|-----------|
| Free | 50K tokens | 500/sec | 10 | 50K |
| Pro | 500K tokens | 5K/sec | 60 | 500K |
| Enterprise | 5M tokens | 50K/sec | 300 | 5M |

### Lista de verificação da execução

1. Armazenar baldes em Redis (não em memória) para aplicativos de várias instâncias
2. Utilização de operações atômicas (MULTI/EXEC) para evitar condições de corrida
3. Retorno .`Retry-After`cabeçalho com respostas de rejeição
4. Seguir os pedidos rejeitados como métrica (> 5% rejeição = limites de nível demasiado apertados)
5. Implementar uma degradação graciosa: rejeitar primeiro pedidos de modelos caros, manter acesso a modelos baratos

## Controle orçamental

### Interruptor de circuito de três limiares

| Threshold | Action | Reversible |
|-----------|--------|------------|
| 70% of monthly budget | Log warning, alert team via Slack/PagerDuty | Yes (auto) |
| 85% of monthly budget | Route all traffic to cheapest model | Yes (auto, next billing cycle) |
| 95% of monthly budget | Serve cached responses only, reject new LLM calls | Yes (manual reset or next cycle) |

### Seguimento dos custos por utilizador

Perfil de custo acumulado por utilizador. utilizadores de bandeiras superiores a 10 vezes a média. Causas comuns:
- Utilizador de energia legítimo (realização do seu nível)
- Localização de injeção rápida (bot enviando solicitações automatizadas)
- Integração ineficiente (cliente retestando em cada erro)

## Campo de rastreamento de custos

Registre todas as chamadas de API com estes campos:

```json
{
  "timestamp": "2026-04-02T10:30:00Z",
  "model": "gpt-4o",
  "input_tokens": 1523,
  "output_tokens": 487,
  "cached_input_tokens": 1024,
  "latency_ms": 1847,
  "cost_usd": 0.006142,
  "user_id": "user_abc123",
  "cache_status": "partial_hit",
  "request_category": "customer_support",
  "complexity_class": "medium",
  "routed_from": "gpt-4o"
}
```

### Metricas-chave do painel de instrumentos

- **Cost per query**(P50, P95, P99) -- por modelo, por característica, por nível de utilizador
- **Cache hit rate**-- exato vs semântico, tendência ao longo do tempo
- **Model distribution**-- % do tráfego por modelo, custo por modelo
- **Budget burn rate**-- gastos correntes versus despesas mensuais previstas à taxa corrente
- **Rejection rate**-- % de pedidos limitados por nível

## Erros comuns

| Mistake | Why it hurts | Fix |
|---------|-------------|-----|
| Caching with temperature > 0 | Non-deterministic outputs, stale cache gives wrong variety | Only cache temp=0 calls, or accept that cached responses lose randomness |
| Semantic cache threshold too low | Returns wrong answers for superficially similar queries | Start at 0.95, lower only after measuring false positive rate |
| No cache invalidation | Responses go stale when underlying data changes | Set TTL (1 hour for dynamic data, 24 hours for static), invalidate on data updates |
| Routing all traffic to cheapest model | Quality drops, users notice | Route by complexity, measure quality per tier, set minimum quality thresholds |
| No per-user limits | One abusive user burns entire budget | Always implement per-user quotas, even if generous |
| Ignoring output tokens | Output costs 2-5x more than input per token | Set max_tokens appropriately, use stop sequences, compress outputs |
| Caching before prompt is stable | Cache fills with responses from old prompts | Only enable caching after prompt is finalized, flush cache on prompt changes |

## Referência de preços (a partir de abril de 2026)

| Model | Input ($/1M) | Output ($/1M) | Cached Input ($/1M) | Best For |
|-------|-------------|--------------|--------------------|---------| 
| gpt-4.1-nano | $0.10 | $0.40 | $0.025 | High-volume simple tasks |
| gpt-4o-mini | $0.15 | $0.60 | $0.075 | Simple routing, classification |
| gemini-2.5-flash | $0.15 | $0.60 | $0.0375 | Budget multimodal |
| claude-haiku-3.5 | $0.80 | $4.00 | $0.08 | Fast mid-tier tasks |
| o4-mini | $1.10 | $4.40 | $0.275 | Reasoning on a budget |
| gemini-2.5-pro | $1.25 | $10.00 | $0.3125 | Long context, multimodal |
| gpt-4o | $2.50 | $10.00 | $1.25 | General purpose, function calling |
| claude-sonnet-4 | $3.00 | $15.00 | $0.30 | Balanced quality/cost |
| claude-opus-4 | $15.00 | $75.00 | $1.50 | Maximum quality, complex reasoning |
