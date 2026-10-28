---
name: framework-diff
description: Compare a new safety framework or release note against RSP v3.0, PF v2, FSF v3.0.
version: 1.0.0
phase: 18
lesson: 18
tags: [rsp, pf, fsf, frontier-safety, safety-case]
---

Dado um novo quadro de segurança, política ou nota de lançamento, compare-o com o Anthropic RSP v3.0, OpenAI PF v2, DeepMind FSF v3.0 ao longo dos cinco eixos estruturais.

Produzir:

1. Estrutura de níveis. O quadro define limites de capacidade discretos?
2. O valor de avaliação do RBC é o que é necessário?
3. O limite de pesquisa de IA é "investigador de nível de entrada" (Anthropic AI R&D-2) ou "acelerar substancialmente a escala" (Anthropic AI R&D-4)?
4. A adaptação ao concorrente. O quadro permite a redução dos requisitos se os concorrentes embarcarem sem salvaguardas comparáveis?
5. A estrutura do caso de segurança. É necessário um caso de segurança escrito?

Rejeitos duros:
- Qualquer quadro de segurança sem limites de capacidade por nível.
- Qualquer quadro que omita uma referência cruzada de governança externa (AISI do Reino Unido, CAISI dos EUA, Escritório da UE para a IA).
- Qualquer quadro que afirme "nós nos alinhamos com todos os quadros publicados" sem números de limiar específicos.

Regras de recusa:
- Se o utilizador perguntar qual é o quadro "melhor", recusar a classificação e apontar para o alinhamento estrutural.
- Se o utilizador solicitar uma recomendação numérica sobre o limiar, os limiares de rejeição  são específicos de laboratório e dependem da sua infraestrutura de medição.

Output: uma comparação lado a lado de uma página contra os três quadros, lacunas sinalizadas e uma recomendação específica de limiar para adicionar. Cite RSP v3.0, PF v2, FSF v3.0 uma vez cada.
