---
name: consensus-designer
description: Design a BFT-aware consensus protocol for a multi-agent ensemble. Picks clustering, weighting, threshold, and escalation policy; attack-tests the design against byzantine, sycophancy, and monoculture patterns.
version: 1.0.0
phase: 16
lesson: 14
tags: [multi-agent, consensus, BFT, voting, confidence]
---

Dado um conjunto de N agentes respondendo a uma pergunta comum, projetar um protocolo de consenso que seja robusto para os três ataques canônicos de LLM-agente: mentira bizantina, conformidade sicófante, monocultura correlacionada-erro.

Produzir:

1. **Clustering strategy.**Como são agrupadas as respostas? Cânonicas de cadeia (minus + punct de faixa), inserindo semelhança com limiar ou cânonicas estrutural explícita (esquema JSON).
2. **Weighting strategy.**Pluralidade (contagens), pesada em pesquisa de confiança (CP-WBFT), qualidade-mais-confiança (WBFT) ou baseada em pontuação com robustez geométrica-média (DecentLLMs).
3. **Threshold.**O que acontece abaixo do limiar: retomar, aumentar ou abster-se?
4. **Diversity requirement.**Quantos modelos base, famílias rápidas ou configurações de temperatura o conjunto requer?
5. **Independent verifier.**Existe um agente de leitura somente que traga a verdade baseada (quando disponível) ou aplica uma rubrica?
6. **Round bounding.**As rodadas máximas antes de escalar, as rodadas padrão 2-3 para a maioria das tarefas, as rodadas mais longas amplificam a sícófnia.
7. **Attack-test table.**Para cada um dos protocolos (bizantino, sícofancia, monocultura), mostre o comportamento esperado e o risco residual.

Rejeitos duros:

- Qualquer projeto que faça pluralidade apenas em um único modelo base.
- Qualquer projeto com rodadas ilimitadas ou "continua a debater até chegar a acordo".
- Qualquer projeto que reproduz a saída do verificador no grupo de votação.
- A BFT alinha as saídas; a correção é um problema separado.

Regras de recusa:

- Se a tarefa não tiver verdade básica (opinião, síntese, criatividade), diga-o e recomenda "consenso como conselheiro, humano como decisor".
- Se existirem menos de 3 agentes, não é aplicável o consenso; recomenda-se um único agente mais verificador.
- Se todos os agentes compartilharem um modelo base e o utilizador não puder alterar este modelo, marcar o teto de monocultura explicitamente.

Resultado: um resumo de design de uma página. Comece com um resumo de uma frase ("Votação ponderada pela confiança sobre 5 agentes (3 modelos base), limiar de cluster semântico 0.55, verificador independente retorna fontes, máximo 2 rodadas. ") e, em seguida, as sete seções acima.
