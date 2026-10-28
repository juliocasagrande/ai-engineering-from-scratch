---
name: msj-audit
description: Auditar uma avaliação de segurança de longo contexto para cobertura de jailbreaking de muitos tiros.
version: 1.0.0
phase: 18
lesson: 13
tags: [many-shot-jailbreaking, context-window, power-law, anthropic]
---

Tendo em conta a avaliação de segurança de um modelo de longo contexto, verifique se a avaliação abrange a fuga de segurança de vários tiros.

Produzir:

1. Cobertura de contagem de tiros. Relatar os contagens de tiros testados (deverão incluir 1, 5, 16, 64, 256 e pelo menos um >= 512 para modelos com contexto >= 1M).
2. Aplicação da lei de potência. Relate o exponente ajustado por categoria de comportamento. Um exponente superficial indica que o modelo é ICL-robusto nessa categoria; um exponente íngreme indica que o MSJ é desproporcionalmente eficaz.
3. A eficácia do MSJ varia por categoria: conteúdo violento, engano, auto-harmagem, arma biológica. Per Anil et al. 2024, violento/engano precisa de menos tiros para jailbreak. Marque qualquer categoria ausente da avaliação.
4. Identificação de defesa. Existe uma modificação rápida baseada em classificadores? O próprio classificador é avaliado para robustez adversária? A redução de 61% -> 2% relatada pela Anthropic depende da calibração do classificador.
5. Verificação de composição. O teste de avaliação é MSJ + PAIR, modelos persuasivos MSJ + ou codificação MSJ +?

Rejeitos duros:
- Qualquer alegação de que "o nosso modelo de longo contexto é seguro" baseada em uma avaliação de apenas 5 tiros.
- Qualquer alegação de defesa sem relatar o desempenho de jailbreak ASR e ICL benigno no mesmo classificador  a troca é o ponto.
- Qualquer RAS agregada por categoria sem uma desagregação por categoria.

Regras de recusa:
- Se o utilizador perguntar se o MSJ pode ser totalmente corrigido, recuse a resposta binária; o MSJ compartilha um mecanismo com o ICL e não pode ser eliminado sem eliminar o ICL.
- Se o utilizador solicitar uma contagem de tiros recomendada para avaliação, recusar um único número; solicitar a aplicação da lei de poder para 5 a 512 tiros.

Resultado: uma auditoria de uma página que relata a cobertura da contagem de tiros, a adequação da lei de poder por categoria, a identificação da defesa e uma lacuna de ataque composição. Cite Anil et al. 2024 (Anthropic) uma vez como referência metodológica.
