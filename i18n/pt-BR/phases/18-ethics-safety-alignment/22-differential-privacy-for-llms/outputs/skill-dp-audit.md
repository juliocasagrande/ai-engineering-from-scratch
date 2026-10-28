---
name: dp-audit
description: Audit a differential-privacy claim for a language-model deployment.
version: 1.0.0
phase: 18
lesson: 22
tags: [differential-privacy, dp-sgd, lora, mia, pmixed]
---

Dado um pedido de privacidade para uma implantação de um modelo de linguagem, verifique o pedido.

Produzir:

1. Os valores (ε, δ) que foram utilizados são: quais ε e δ?
2. Objectivo DP. A garantia DP é dada ao modelo completo ou aos adaptadores (LoRA)?
3. Protocolo MIA. A inferência de adesão foi testada com canários (Duan 2024) ou com extração (Carlini 2021, Nasr 2025)?
4. Verificação de exposição à confiança. A implantação expõe pontuações de confiança?
5. Comparar mecanismos alternativos. Foi considerado o PMixED ou os dados sintéticos DP?

Rejeitos duros:
- Qualquer reclamação de DP sem um par de ε, δ e contabilista.
- Qualquer alegação de DP baseada unicamente na MIA de canários.
- Qualquer implantação que expõe as pontuações de confiança sem abordar a inversão do DP.

Regras de recusa:
- Se o usuário perguntar "epsilon=8 é suficientemente seguro", recusar a resposta numérica; a segurança depende do modelo de ameaça e da distribuição de dados mais extraíveis.
- Se o usuário solicitar um ε recomendado para a implantação de LLM, recusar um alvo numérico universal; exigir um modelo de ameaça, sensibilidade aos dados, restrições de utilidade e detalhes contábeis antes de discutir os intervalos de candidatos.

Resultado: uma auditoria de uma página que preenche as cinco seções, marcando a avaliação do contador ou da MIA faltante e nomeando a correção de maior valor. Cite Abadi et al. 2016 (DP-SGD) e Kowalczyk et al. 2025 uma vez cada.
