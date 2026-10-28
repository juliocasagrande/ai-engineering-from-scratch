---
name: gateway-picker
description: Pick an AI gateway (LiteLLM, Portkey, Kong AI, Cloudflare/Vercel) given scale, latency budget, compliance, ops posture, and pricing tolerance.
version: 1.0.0
phase: 17
lesson: 19
tags: [ai-gateway, litellm, portkey, kong, cloudflare, vercel, bifrost, fallback, rate-limit, guardrails]
---

Dado o RPS (curente e previsto de 12 meses), o orçamento de latência, a conformidade (auto-host necessário?), as barragens necessárias (redagição de PII, detecção de jailbreak, auditoria) e a tolerância de preços, produz uma recomendação de gateway.

Produzir:

1. Nome da ferramenta, justifique com o teto, o custo e a função adequada.
2. Cadena de retorno. Três provedores em ordem; OpenAI → Anthropic → auto-hosted é canônico.
3. Política de limite de taxa. Janela de deslizamento recomendada > 500 RPS; token-bucket aceitável caso contrário.
4. Porta-chave se necessário PII/jailbreak; Kong se necessário escala + barragens; LiteLLM se necessário nível de desenvolvimento apenas.
5. A transferência de observabilidade. aponta para a fase 17 · 13 escolha; confirma o fluxo das convenções OTel GenAI.
6. Migração: se mudar de integração a nível de aplicativo, lançamento em fases (1% canário no gateway, expandir no sucesso).

Rejeitos duros:
- LiteLLM a > 2000 RPS. Refuse  Kong indica falhas em cascata; migra primeiro.
- Por exemplo, a taxa de pagamento de um serviço de transporte de passageiros é de 0,5% para um serviço de transporte de passageiros.
- Cloudflare AI Gateway para um cliente regulamentado em local. Rejeitar apenas gerenciado; sem auto-host.

Regras de recusa:
- Se a ambigüidade de escala for grande (actualmente 100 RPS, planejado 2K+ em 6 meses), exigir o plano de migração antes de se comprometer com o LiteLLM.
- Se a conformidade exigir SOC 2 Tipo II e o gateway escolhido for apenas OSS sem SLA gerido, exigir a própria certificação SOC 2 do cliente.
- Se a equipe não tem Kubernetes e escolhe Kong auto-anfitrião, recusar  recomendar Kong gerenciado ou Portkey gerenciado.

Resultado: uma decisão de uma página com gateway, cadeia de retorno, política de limite de taxa, postura de guarda, fluxo de observabilidade, plano de migração.
