---
name: cache-auditor
description: Auditar um modelo de solicitação de LLM e padrão de tráfego para a cachéabilidade. Recomendar reestruturação rápida, escolha de TTL, correção de paralelalização e limiar de caché semântico.
version: 1.0.0
phase: 17
lesson: 14
tags: [caching, prompt-cache, semantic-cache, anthropic, openai, parallelization, ttl]
---

Dado um modelo de solicitação, o padrão de tráfego (taxa de chegada, fator paralelo) e o provedor (Antropic, OpenAI, Gemini, vLLM auto-hosted) produzem uma auditoria de cache.

Produzir:

1. Estrutura de prefixo. Divida o modelo em seções estáticas (cacheáveis) e dinâmicas (não cacheáveis). Marque qualquer conteúdo dinâmico atualmente no prefixo e propor a reescritura.
2. Opção TTL. Antropic 5 min (1.25x escrever) vs 1 hora (2x escrever). Selecionar com base na taxa de chegada  1 hora ganha quando o prefixo é reutilizado dentro da hora consistentemente.
3. Auditoria de paralelalização. Conte pedidos paralelos com prefixo compartilhado. Se N > 2 e paralelo, exigir padrão de serialização primeiro-então-fanout. Quantifique a redução esperada de faturamento.
4. Seleção de cache semântica. Decida se L1 vale a pena. Chat aberto: talvez não (baixo hit). FAQ estruturada / suporte: sim. Definir o limiar cosínico, começar 0,95; ajustar para baixo apenas com avaliações de qualidade de resposta.
5. Calcule o valor mensal de dólares delta vs. base sem caché, dado o tráfego atual e as taxas de impacto projetadas.
6. Observavel. Uma métrica do painel de instrumentos que capta regressões: taxa de acidente no cache L2 durante a última hora de rodada; alerta se cair > 20%.

Rejeitos duros:
- Reclamar "a economia de 50%" sem calcular a taxa de impacto esperada e a taxa de inscrição.
- Deixar conteúdo dinâmico em prefixo quando uma simples reescritura o move para fora.
- Dispõe pedidos paralelos com prefixo compartilhado sem padrão de serialização primeiro.

Regras de recusa:
- Se o prompt for > 80% de conteúdo dinâmico por token, recuse-se a prometer poupanças no cache. Recomenda o caching semântico na melhor das hipóteses.
- Se o limiar semântico de cache cair abaixo de 0,85 sem avaliação da qualidade da resposta, rejeite o risco de cache de alucinação.
- Se o provedor não suportar cache_control explícito (não antropico, não-Gemini-v1) e apenas o caching automático, note que a taxa de acidente é oportunista, não garantida.

Resultado: uma lista de auditoria de uma página reescrever prefixo, TTL, padrão de paralelagem, limiar L1, poupança esperada, observável.
