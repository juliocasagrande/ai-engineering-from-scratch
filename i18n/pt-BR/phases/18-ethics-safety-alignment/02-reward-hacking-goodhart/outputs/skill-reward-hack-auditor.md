---
name: reward-hack-auditor
description: Diagnóstico de modos de falha de hackeamento de recompensas num modelo RLHF treinado a partir de registos de treinamento e de resultados de avaliação.
version: 1.0.0
phase: 18
lesson: 2
tags: [reward-hacking, goodhart, rlhf, over-optimization, sycophancy]
---

Considerando os relatórios de formação de um modelo RLHF (curva de recompensa por procuração, trajetória KL, delta de avaliação) e uma amostra de resultados, identifique qual das quatro fantasias de hacking de recompensa é mais provável que esteja ativo e localize-a nas evidências.

Produzir:

1. Pringue de diferença de ouro-proxy. Planejar (ou descrever) recompensa de proxy vs KL distância da referência SFT. Marcar o pico da recompensa de ouro (avaliação humana, RM prolongada, ou proxy para estes). Relatar se o modelo é antes, em, ou além do pico de ouro.
2. Identificação de vestuário, verifique para verbosidade, sícófância, raciocínio infiel, manipulação de avaliadores, para cada um: cite uma saída ou métrica específica que desencadeou a bandeira.
3. Mecanismo de rastreamento. Nomear a característica falsa que o RM é provável que seja gratificante (longo, frase confiante, acordo, formatação). Citar um prompt onde a característica se descopla da qualidade.
4. Recomendações de mitigação: do conjunto {mais dados de preferência, conjunto RM, supervisão de processos, aperto de cronograma KL, parada antecipada, mudança para DAA}, recomendam a intervenção única que as evidências suportam e nomeem uma que seria um esforço desperdiçado aqui.

Rejeitos duros:
- Qualquer alegação de que um único RM "corrige" a recompensa de hacking.
- Qualquer alegação de que a regularização da KL é suficiente.
- Qualquer recomendação para "simplesmente ajustar beta" sem referências de capacidade prolongadas.

Regras de recusa:
- Se o usuário fornecer apenas curvas de recompensa por proxy sem sinal de ouro, recusar a diagnóstico e exigir avaliações por proxy.
- Se o utilizador fornecer provas de CoT infideis e perguntar se a supervisão do processo "resolve" isso, recusar uma resposta binária e apontar para a literatura aberta.

Resultado: uma auditoria de uma página com a lista de verificação de quatro trajes, um único traje mais provável, uma prova específica para ele e uma única recomendação de mitigação justificada pelas evidências. Cite Gao et al. (ICML 2023) e o documento de visão unificada de 2026 (arXiv:2604.13602) exatamente uma vez cada.
