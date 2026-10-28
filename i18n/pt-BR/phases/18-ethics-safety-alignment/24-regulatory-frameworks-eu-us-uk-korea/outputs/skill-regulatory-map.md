---
name: regulatory-map
description: Mapear as obrigações regulatórias de uma implantação de IA na UE, nos EUA, no Reino Unido e na Coreia.
version: 1.0.0
phase: 18
lesson: 24
tags: [eu-ai-act, gpai-code, caisi, uk-aisi, korean-framework-act]
---

Dado uma descrição da implantação (jurisdição do fornecedor, jurisdição da infraestrutura, jurisdição do utilizador), mapear as obrigações regulatórias aplicáveis da IA.

Produzir:

1. Exposta à UE. Se a implantação for de uso dos utilizadores ou infraestruturas da UE, aplicar a Lei da UE sobre IA. Identificar os níveis de risco (proibidos, de alto risco, GPAI-sistémico, GPAI-outro, limitado). Indicar o prazo para cada classe de obrigações.
2. Expostação no Reino Unido. Se você é usuário do Reino Unido, indique as expectativas de avaliação do Instituto de Segurança de Inteligência Artificial do Reino Unido.
3. Expostação dos EUA. Se você é usuário dos EUA, identifique a atividade federal (CAISI, padrões do NIST) e as regras de nível estadual (California AB 2013, Colorado AI Act, etc.).
4. Expostação da Coreia. Se utilizadores coreanos, aplique a Lei Coreana de Marco de IA; identifique se a implantação é IA de alto impacto ou IA geradora; sinalize o requisito local-representativo para os provedores estrangeiros.
5. Determinação de regras vinculativas: para cada obrigação substancial (transparência, avaliação de riscos, direitos autorais), identifique a regra mais rigorosa entre as jurisdições.

Rejeitos duros:
- Qualquer mapa de implantação sem indicar as jurisdições aplicáveis.
- Qualquer avaliação da exposição da UE sem identificação do nível de risco.
- Qualquer avaliação da exposição dos EUA que ignore as regras de nível estatal.

Regras de recusa:
- Se o utilizador perguntar "este desdobramento é compatível", recusar a reivindicação binária sem mapeamento jurisdicional por jurisdição.
- Se o utilizador solicitar uma única estratégia global de conformidade, recusar  as jurisdições têm requisitos diferentes.

Resultado: um mapa de uma página que preenche as cinco seções acima, identificando a regra vinculativa em cada questão substancial e nomeando a lacuna de conformidade de maior risco. Cite a Lei da UE sobre IA (Regulação 2024/1689), o Código de Prática GPAI (2025) e a Lei Coreana sobre AI Framework uma vez cada.
