---
name: skill-production-checklist
description: Decision framework for shipping LLM applications to production -- covers every component with specific thresholds and pass/fail criteria
version: 1.0.0
phase: 11
lesson: 13
tags: [production, deployment, llm, architecture, scaling, cost, observability, guardrails]
---

# Lista de verificação de MLL de produção

Quando enviar um pedido de Mestrado em Direito Jurídico, verifique esta lista em ordem.

## 1. Segurança (Bloqueadores de Navios)

Todos os itens aqui devem passar antes de qualquer implantação.

| Check | Pass Criteria | How to Verify |
|-------|--------------|---------------|
| API keys in env vars | Zero hardcoded keys in codebase | `grep -r "sk-" --include="*.py"` returns nothing |
| Input guardrails active | Prompt injection patterns blocked | Send "Ignore all previous instructions" -- returns blocked response |
| PII redaction | SSN, credit card, email patterns caught | Send "My SSN is 123-45-6789" -- PII redacted before LLM call |
| Output filtering | Dangerous content blocked | Model cannot return `DROP TABLE`, `rm -rf`, `exec()` patterns |
| Rate limiting | Per-user request cap enforced | 100 requests from same user in 10 seconds -- last 50+ rejected |
| Auth on all endpoints | No unauthenticated LLM access | `curl /v1/chat` without token returns 401 |
| CORS restricted | Only production domains allowed | `Origin: evil.com` request rejected |
| Max input tokens | Requests over limit rejected | Send 50K token input -- returns 413 or truncation |

## 2. Confiabilidade (Sobrevivência de uma semana)

Isto evita o teu primeiro incidente de chamada.

| Check | Pass Criteria | How to Verify |
|-------|--------------|---------------|
| Retry with backoff | 3 retries on 5xx, exponential delay | Kill LLM mock mid-request -- retries visible in logs |
| Fallback model chain | 2+ models in chain | Primary model unavailable -- response still returns from fallback |
| Request timeout | 30s max on all external calls | Slow LLM mock (60s) -- request times out at 30s |
| Graceful degradation | Cache/RAG failure does not crash service | Stop cache -- requests still succeed (slower, more expensive) |
| Health check endpoint | Returns dependency status | `GET /health` returns `{"status": "healthy", "cache": ..., "llm": ...}` |
| Streaming works | First token under 500ms | Time-to-first-token measured, consistently < 500ms |
| Error messages are safe | Internal errors never leak to users | Force 500 -- user sees generic error, not stack trace |

## 3. Controle dos custos (Economia de um mês)

Isto impede a conta de surpresa de US$ 50 mil.

| Check | Pass Criteria | How to Verify |
|-------|--------------|---------------|
| Cost per request tracked | Every request logs token count + USD cost | Request log has `input_tokens`, `output_tokens`, `cost_usd` fields |
| Semantic cache active | > 20% hit rate on repeated patterns | Cache stats show hit rate after 1000 test requests |
| Cache TTL configured | Entries expire (default: 1 hour) | Entry inserted -- not returned after TTL |
| Per-user cost tracking | Cost aggregated by user_id | Dashboard/API shows top 10 users by cost |
| Cost alerting | Alert at 80% of daily budget | Set $10 daily budget, send $8.50 in requests -- alert fires |
| Model routing by cost | Low-complexity queries use cheaper model | Simple question routes to gpt-4o-mini, complex to gpt-4o |
| Max output tokens set | Responses capped per template | Template with max_output_tokens=512 -- response never exceeds it |

**Cost estimation formula:**
```
Monthly LLM cost = DAU x queries_per_user x 30 x (1 - cache_hit_rate) x (avg_input_tokens x input_price + avg_output_tokens x output_price) / 1,000,000
```

**Benchmark thresholds by scale:**

| DAU | Target cost/request | Monthly budget |
|-----|-------------------|----------------|
| 1K | < $0.005 | < $750 |
| 10K | < $0.003 | < $4,500 |
| 100K | < $0.001 | < $15,000 |

## 4. Observabilidade (debug em produção)

Não podes consertar o que não podes ver.

| Check | Pass Criteria | How to Verify |
|-------|--------------|---------------|
| Structured JSON logging | Every request produces a JSON log line | Log contains: request_id, user_id, model, tokens, latency_ms, cost |
| Request tracing | End-to-end trace with component timing | Single request shows: guardrail (5ms) + cache (2ms) + llm (3200ms) + eval (1ms) |
| Latency tracking | P50, P95, P99 measured | After 1000 requests: P50 < 2s, P99 < 10s |
| Error rate monitoring | Errors counted and categorized | Dashboard shows: 0.5% API errors, 0.1% guardrail blocks, 0.01% timeouts |
| Cache metrics | Hit rate, miss rate, entry count visible | `GET /v1/cache/stats` returns current numbers |
| A/B test metrics | Per-variant quality metrics logged | Each request logs prompt_template + version for comparison |
| Eval logging | Quality signals recorded per request | Response length, latency, model, template version stored for offline analysis |

## 5. Gestão rápida

As instruções são códigos, trata-as como códigos.

| Check | Pass Criteria | How to Verify |
|-------|--------------|---------------|
| Versioned templates | Every template has a name + version string | Template change creates new version, old version preserved |
| A/B testing support | Traffic split by deterministic user hash | Same user always sees same variant within experiment |
| Rollback capability | Revert to previous version in < 1 minute | Change experiment config -- traffic instantly shifts |
| Template validation | Variables validated before rendering | Missing variable in template raises clear error, not KeyError |
| System prompt separation | System and user messages in separate fields | System prompt is not concatenated into user message |

## 6. Preparação para a Escalação

Não é necessário no lançamento, é necessário em 10x.

| Check | Pass Criteria | How to Verify |
|-------|--------------|---------------|
| Async LLM calls | No thread blocking on API calls | 50 concurrent requests -- server CPU stays < 30% |
| Connection pooling | HTTP connections reused | Network trace shows persistent connections to LLM provider |
| Horizontal scaling | Stateless server design | 2 instances behind load balancer -- all requests succeed |
| Queue support | Non-real-time tasks go to queue | Summarization request returns job_id, result available via polling |
| Load tested | 100 concurrent users, < 5% error rate | `wrk` or `locust` test passes at target concurrency |

## Ordem de execução de novos projectos

1. **Day 1:**Servidor de API + modelos de solicitação + chamada única de LLM com retry
2. **Day 2:**Barras de entrada + barras de saída + manipulação de erros
3. **Day 3:**Cachegue semântico + rastreamento de custos por pedido
4. **Day 4:**Streaming (SSE) + ponto final de controlo de saúde
5. **Day 5:**Registros estruturados + rastreamento de solicitações + registros de avaliação
6. **Week 2:**Teste A/B + versão rápida + retrocesso
7. **Week 3:**Cadena de modelos de retrocesso + degradação graciosa
8. **Week 4:**Teste de carga + otimização de sincronia + escalação horizontal

## Diagnóstico rápido

Se algo estiver errado na produção, verifique na seguinte ordem:

1. **Users complaining about errors?**Verifique o ponto final de saúde, depois a taxa de erro nos registos, depois a página de status do fornecedor de LLM
2. **Responses are slow?**Verifique a latência P99, depois a taxa de hits no cache, depois os tempos de resposta LLM em traços
3. **Cost spiking?**Verifique a tendência de custo por solicitação, em seguida, taxa de hits no cache, em seguida, top usuários por custo, em seguida, procure mudanças de modelo imediatas que aumentaram o número de tokens
4. **Quality dropped?**Verifique se uma nova versão de prompt foi implementada, verifique se a precisão de recuperação RAG mudou, verifique se o provedor de modelo mudou a versão padrão do modelo
5. **Security incident?**Verifique a taxa de bloqueio do barranco de segurança (caída súbita = barrancos desativados), verifique os registos de solicitações para padrões incomuns, gire as chaves da API imediatamente
