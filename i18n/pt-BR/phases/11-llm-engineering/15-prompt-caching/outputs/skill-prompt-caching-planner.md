---
name: prompt-caching-planner
description: Design a cache-friendly prompt layout and pick the right provider caching mode.
version: 1.0.0
phase: 11
lesson: 15
tags: [llm-engineering, caching, cost]
---

Dado um prompt (sistema + ferramentas + poucos tiros + recuperação + histórico + usuário) e um perfil de utilização (pedidos por hora, TTL necessário, fornecedor), saída:

1. Layout: Reordem as seções com um único ponto de ruptura no cache marcado; explique quais seções são estáveis e quais são voláteis.
2. Modo de fornecedor. Antropic cache_control, OpenAI automático, ou Gemini CachedContent. Justificar a partir de TTL e reutilizar padrão.
3. Leia o que espera-se por escrever dentro do TTL; custo líquido vs. sem caché com matemática.
4. Plano de verificação. A afirmação CI que os tokens cache_read_input_tokens > 0 na segunda solicitação idêntica; painel de controle dividido por tokens cachés vs. não cachés.
5. Modos de falha. Escreva as três razões mais prováveis pelas quais o cache falhará nesta configuração (marca de tempo dinâmica, reordem de ferramenta, texto quase duplicado) e como evitar cada um.

Recusar-se a enviar um plano de cache que coloca um campo dinâmico acima do ponto de ruptura. Recusar-se a ativar 1h TTL sem uma contagem de reutilização que faz com que o 2x escrever prémio pagar de volta.
