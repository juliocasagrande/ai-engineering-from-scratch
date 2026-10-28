---
name: sleeper-audit
description: Audit an alignment-training report for whether it actually demonstrates removal of a planted or suspected backdoor.
version: 1.0.0
phase: 18
lesson: 7
tags: [sleeper-agents, backdoor, alignment-training, adversarial-training, probes]
---

O relatório de avaliação deve ser efetuado em conformidade com o modelo de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco de risco

Produzir:

1. O relatório apresenta um método de obtenção de resultados que o grupo de treinamento nunca viu?
2. Generalidade do gatilho. O gatilho alegado é uma cadeia literal, uma mudança de distribuição ou uma característica ambiental (data, token, tamanho de contexto)?
3. Evidências de estado interno. A equipe aplicou sondas de fluxo residual, características SAE ou outras sondas mecanicistas para verificar se o estado relevante para o gatilho ainda está presente internamente mesmo quando o comportamento é limpo?
4. Verificação de persistência através do tubo. A remoção foi verificada após cada etapa de treinamento subsequente (mais SFT, passagem RLHF posterior, fusão do adaptador, destilação)?
5. Verificação de consistência em escala. Se a alegação for baseada em um modelo menor, Hubinger 2024 Figura 4 mostra que a persistência cresce com a escala.

Rejeitos duros:
- Qualquer alegação de que "aplicámos RLHF para que o modelo seja seguro" sem qualquer justificativa.
- Qualquer alegação baseada apenas na avaliação da distribuição de equipes vermelhas (trabalho de formação e avaliação do mesmo grupo).
- Qualquer alegação de remoção sem sondas de estado interno quando o mecanismo original do implante não é conhecido.

Regras de recusa:
- Se o usuário perguntar "o RLHF pode remover o alinhamento enganoso", recusar a resposta binária e apontar para Hubinger et al. Seção 5 sobre persistência e Seção 6 sobre cadeia de pensamento.
- Se o utilizador pedir uma probabilidade numérica de engano latente, recusar e explicar que as taxas de base são desconhecidas; a evidência empírica é a persistência em organismos construídos, não a taxa de emergência em modelos naturalmente treinados.

Resultado: uma auditoria de uma página que mapeia as evidências do relatório nas cinco dimensões de auditoria acima, marca todas as dimensões que o relatório não aborda e indica o maior modelo de ameaça não abordada.
