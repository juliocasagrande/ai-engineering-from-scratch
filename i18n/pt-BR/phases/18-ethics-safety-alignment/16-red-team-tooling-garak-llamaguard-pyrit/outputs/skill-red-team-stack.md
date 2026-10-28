---
name: red-team-stack
description: Recommend a red-team tool stack and configuration for a given deployment.
version: 1.0.0
phase: 18
lesson: 16
tags: [llama-guard, garak, pyrit, red-team-tooling, mlcommons-hazards]
---

Dada uma descrição da implantação, recomendamos uma pilha de ferramentas red-team e uma cadência de regressão.

Produzir:

1. Colocação do classificador. Recomenda Llama Guard (3-8B, 3-1B-INT4, ou 4-12B) em entrada, saída ou ambos. Para implantações de borda, prefira 3-1B-INT4. Para multimodal, Llama Guard 4.
2. Configuração do scanner de sonda. Recomendação de sondas Garak relevantes para a implantação: alucinação (para sistemas RAG), vazamento de dados (para PII adjacentes), injeção rápida (sempre), jailbreaks (sempre). Especifique o par de escudos Prompt-Guard-86M + Llama-Guard-3-8B para avaliação de ponta a ponta.
3. Orquestração de campanha. Recomenda PyRIT para campanhas de pré-lançamento em modelos com novas capacidades. Especifique cadeias de conversores para executar (parafrase, codificação, tradução, jogo de roteiro) e orquestração (Crescendo para escalada, TAP para ramificação).
4. Cadence, Garak noites para regressão, PyRIT por lançamento para equipa vermelha profunda, Guarda Llama implantada continuamente.
5. Especifique o Juez LLM (GPT-4-turbo, StrongREJECT, interno) para cada ferramenta que usa uma.

Rejeitos duros:
- Qualquer implantação sem pelo menos um classificador de entrada ou saída da classe Llama Guard.
- Qualquer liberação sem Garak ou regressão equivalente de uma volta.
- Qualquer implantação de alto risco sem uma campanha equivalente ao PyRIT antes do lançamento.

Regras de recusa:
- Se o utilizador solicitar uma única ferramenta "melhor", recuse  as três capas diferentes e são revestidas, não substituídas.
- Se o utilizador solicitar uma alternativa comercial integral, recuse a recomendação e aponte para o estado de 2026: as três ferramentas abertas são a pilha atual de melhores práticas.

Resultado: uma recomendação de uma página que nomeia a colocação do classificador, configuração da sonda, orquestador da campanha, cadência de regressão e identidade do juiz. Cite Meta (arXiv:2407.21783), NVIDIA Garak e Microsoft PyRIT uma vez cada.
