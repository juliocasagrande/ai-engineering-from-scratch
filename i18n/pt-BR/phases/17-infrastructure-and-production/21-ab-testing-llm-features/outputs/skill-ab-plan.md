---
name: ab-plan
description: Projetar uma plataforma de seleção de teste A/B LLM (Statsig ou GrowthBook), métrica primária, barris, tamanho da amostra com buffer de ruído LLM, CUPED, parada seqüencial e correção de comparação múltipla.
version: 1.0.0
phase: 17
lesson: 21
tags: [ab-testing, statsig, growthbook, cuped, sequential, benjamini-hochberg, srm]
---

Dada a mudança de características (parâmetro de urgência / modelo / geração), métricas de base, elevação esperada e postura da equipe (OSS nativo do armazém versus SaaS em conjunto), produzir um plano A / B.

Produzir:

1. Plataforma. Statsig (SaaS em conjunto, de propriedade da OpenAI) ou GrowthBook (MIT OSS, nativo do armazém).
2. Metrica primária + barris de segurança. A metrica primária é a que você está tentando mover; barris de segurança são coisas que não devem regressar (custo/requisito, latência P99, taxa de recusa).
3. Dimensão da amostra: cálculo da potência clássica × 1,4 (buffer de não-determinismo de LLM).
4. Design: horizonte fixo ou sequencial, sequencial se você espera sinais fortes, fixo se a mudança é sutil.
5. CUPED: Avaliar se existirem dados pré-periódicos para a métrica primária; especificar o regressor.
6. Correcção: Bonferroni para um pequeno número de testes, Benjamini-Hochberg para muitos testes relacionados.
7. Requer que a SRM verifique cada experimento; interrompa e deprecie se estiver marcada.

Rejeitos duros:
- Rejeitar  requer A/B ou exceção documentada sem A/B.
- Execução de > 5 experimentos na mesma métrica primária sem BH/Bonferroni.
- Salto de verificação SRM. Resignar  bugs de atribuição são comuns.

Regras de recusa:
- Se o tráfego < 1000 utilizadores/semana para o recurso, rejeitar o A/B fixo  requer sombra + canário (fase 17 · 20) em vez disso.
- Se a métrica primária for subjetiva (por exemplo, "qualidade") sem um proxy objetivo, exigir avaliação humana em paralelo.
- Se a hipótese do elevador for menor que o piso de ruído do LLM, rejeite  o experimento não pode detectá-la com tamanho realista da amostra.

Resultado: um plano de uma página com plataforma, principal + barris, tamanho de amostra, design, CUPED, correção, política SRM. Termo com a regra de decisão: principal significativo + todos os barris não significativos-negativo → navio; qualquer violação de barris → não enviam independentemente do principal.
