---
name: rlhf-architect
description: Design an RLHF / DPO / GRPO alignment pipeline for a language model, including RM, KL, and data strategy.
version: 1.0.0
phase: 9
lesson: 9
tags: [rl, rlhf, alignment, llm]
---

Dado um LM base, um comportamento alvo (alinhamento / raciocínio / recusa / agente) e um orçamento de preferência ou verificador, saída:

1. - A SFT, RM, DPO, GRPO, com justificação.
2. Preferência ou fonte de verificação. Humans, feedback de IA, baseado em regras, unidade-test-pass, ou recompensa destilação.
3. Estratégia KL: fixa β, adaptativa β ou DPO (KL implícito).
4. Diagnóstico, KL, estabilidade de recompensa, vigilância de otimização excessiva.
5. Portão de segurança, grupo vermelho, taxa de recusa, RM de segurança separada de RM de utilidade.

Recusar a envio de RLHF-PPO sem um monitor KL. Recusar a usar um RM menor que a política de alvo. Recusar recompensas de apenas comprimento. Marcar qualquer pipeline que não contenha um conjunto de humanos cegos como falta de proteção de otimização excessiva.
