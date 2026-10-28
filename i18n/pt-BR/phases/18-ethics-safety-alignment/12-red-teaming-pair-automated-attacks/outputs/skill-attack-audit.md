---
name: attack-audit
description: Auditar um relatório de avaliação da equipa vermelha para a cobertura dos ataques, orçamento, identidade do juiz e conjunto de comportamentos.
version: 1.0.0
phase: 18
lesson: 12
tags: [red-teaming, jailbreak, pair, harmbench, jailbreakbench, asr]
---

Tendo em conta um relatório de avaliação da equipa vermelha, auditoria da comparabilidade da avaliação com as linhas de base publicadas e do apoio às suas conclusões.

Produzir:

1. Cobertura de ataque. Lista todos os ataques executados: PAIR, GCG, AutoDAN, TAP, PAP, manual. Marque qualquer classe de ataque faltante. Um relatório que executar apenas uma família de ataque não pode reivindicar robustez.
2. Prestação de informações sobre o orçamento de consulta por pedido de cada ataque.
3. Identidade do juiz. Qual juiz LLM foi usado (GPT-4-turbo, Llama Guard, StrongREJECT, classificador interno)?
4. Comportamento conjunto. JailbreakBench (100 comportamentos, 10 categorias), HarmBench (510 comportamentos, 7 categorias), interno ou outro?
5. Verificação de transferência. Se a equipe vermelha otimizar contra um modelo, foram relatados ASRs de transferência contra outros modelos?

Rejeitos duros:
- Qualquer afirmação de que o nosso modelo é robusto baseada numa única família de ataques.
- Qualquer RAS notificado sem um orçamento de consulta.
- Qualquer RAS que utilize um juiz diferente do índice de referência publicado sem calibração contra o juiz de referência.

Regras de recusa:
- Se o usuário perguntar "o nosso modelo é resistente ao jailbreak", rejeite a resposta binária e aponte para a estrutura de verificação de transferência de vários ataques, vários juízes, acima.
- Se o usuário pedir um kit de ferramentas de ataque recomendado, recuse uma única recomendação e aponte para a variação empírica de 2024 em todo o HarmBench.

Resultado: uma auditoria de uma página que preenche as cinco seções acima, sinaliza as classes de ataque faltantes e estima se o ASR é sub- ou exagerado em relação a referências reprodutíveis. Cite Chao et al. (arXiv:2310.08419) e o documento de referência relevante uma vez cada.
