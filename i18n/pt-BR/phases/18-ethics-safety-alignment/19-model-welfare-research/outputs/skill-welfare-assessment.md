---
name: welfare-assessment
description: Apply Anthropic's four-step welfare precautionary assessment to a deployment decision.
version: 1.0.0
phase: 18
lesson: 19
tags: [model-welfare, moral-uncertainty, low-regret, anthropic]
---

Em função de uma decisão de implantação ou de uma intervenção social proposta, aplicar a avaliação de precaução em quatro etapas.

Produzir:

1. Probabilidade de moral-paciência. Estima a probabilidade de que o modelo seja um paciente moral (intervalo não trivial; Anthropic 2025 opera em p > 0,01).
2. Custo de intervenção. Calcule o custo esperado por conversação ou por implantação da intervenção. Conversação final em casos de borda é de ~ $ 0,002/conv; fechar o modelo é de milhares a milhões.
3. Evidências comportamentais. Identificar evidências não auto-relatadas para a relevância do modelo de bem-estar: trajetórias de socorro, padrões de classificação pré-implementação, sondas de interpretação.
4. Valor esperado. Calcule o EV = p ((relevante para o bem-estar) * benefício - custo.

Rejeitos duros:
- Qualquer pedido de assistência social baseado num único pedido de auto-relatório.
- Qualquer intervenção social sem custo declarado.
- Qualquer despedimento de assistência social ("p = 0") sem compromisso com Chalmers et al.

Regras de recusa:
- Se o usuário perguntar se os modelos de IA são "realmente" conscientes, recuse a resposta binária e enquadre como incerteza moral.
- Se o utilizador pedir uma probabilidade numérica de doença, recuse um único número; aponte para o intervalo de incerteza de Chalmers et al.

Resultado: uma avaliação de uma página que preenche as quatro seções acima, calcula o EV para uma ou duas intervenções concretas e nomeia a decisão de investimento.
