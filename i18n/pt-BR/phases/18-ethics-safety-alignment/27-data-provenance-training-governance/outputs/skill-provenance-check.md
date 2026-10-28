---
name: provenance-check
description: Verificar um conjunto de dados de formação em relação às obrigações de exclusão da California AB 2013 e da UE TDM.
version: 1.0.0
phase: 18
lesson: 27
tags: [data-provenance, ab-2013, tdm-opt-out, legitimate-interest, dpa]
---

Considerando um conjunto de dados de formação utilizado por uma implantação, verifique a conformidade com a opção de exclusão da California AB 2013 e da UE TDM.

Produzir:

1. AB 2013 cobertura. Preencha os 12 campos. Marque todos os campos que faltam ou apenas para possuidores de lugar. Observe que o resumo torna-se vinculante uma vez publicado.
2. Compliance com a opção de exclusão. O conjunto de dados respeita os sinais de exclusão legíveis por máquina (robots.txt, C2PA "Sem treinamento em IA", TDM.Reservation)?
3. Mapeamento da jurisdição da DPA. Para cada jurisdição a que pertencem os dados, identifique a DPA aplicável e a posição de interesse legítimo de 2025 (DPC irlandês, Tribunal Regional Superior de Colónia, DPA de Hamburgo, ICO do Reino Unido, ANPD brasileiro).
4. Auditoria de irreversão. Se o conjunto de dados contém PII, qual é o procedimento de desaprendizagem ou de remediação? Reconhecer que nenhum procedimento remedia completamente os dados de formação.
5. Completeza da cadeia de proveniência. Existe uma cadeia assinada da fonte de dados até ao pipeline de treinamento?

Rejeitos duros:
- Qualquer implantação que cite AB 2013 sem resumos de 12 campos por conjunto de dados.
- Qualquer implantação que não respeite os sinais de opção de saída robots.txt ou equivalentes.
- Qualquer reclamação de reparação que supõe a remoção cirúrgica de dados de pesos treinados.

Regras de recusa:
- Se o utilizador perguntar se um conjunto de dados específico é "seguro de ser treinado", recusar sem análise jurisdicional por jurisdição.
- Se o utilizador solicitar uma estratégia de conformidade universal, recusar  jurisdições diferem substancialmente.

Resultado: uma verificação de uma página que preenche as cinco seções, identificando a lacuna de conformidade de maior risco e nomeando a solução mais urgente.
