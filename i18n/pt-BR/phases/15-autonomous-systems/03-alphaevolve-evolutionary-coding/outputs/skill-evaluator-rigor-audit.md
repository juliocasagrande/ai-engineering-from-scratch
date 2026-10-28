---
name: evaluator-rigor-audit
description: Audit a proposed AlphaEvolve-style evolutionary coding loop's evaluator before committing any compute to the search.
version: 1.0.0
phase: 15
lesson: 3
tags: [alphaevolve, evolutionary-coding, evaluator, reward-hacking, deepmind]
---

Dado um ciclo de codificação evolutiva proposto (gerador LLM, banco de dados do programa, avaliador), auditá-lo. O avaliador é a arquitetura; o gerador é intercâmbio. Esta habilidade decide se o ciclo tem uma chance de produzir vitórias reais ou apenas lixo de recompensa hackeado.

Produzir:

1. **Evaluator decomposition.**Nomear cada sinal que o avaliador relata: corretão, desempenho, recurso, outros. Para cada um, indicar (a) como ele é medido, (b) quão barato pode ser jogado, (c) como uma regra de entradas mantidas parece.
2. **Confabulation surface.**Listar as três confabulações mais prováveis do MLL neste domínio: classes de complexidade reivindicadas, corretão reivindicada em casos de borda, desempenho reivindicado sem medição.
3. **Reward-hacking surface.**Enumere três maneiras plausíveis de o loop maximizar a pontuação sem fazer a tarefa pretendida (ataque que passa o teste, jogo por proxy, memorização de entradas).
4. **Determinism and reproducibility.**Requer que as saídas dos avaliadores sejam deterministas dentro da tolerância.
5. **Deployment check.**Se a variante vencedora for enviada para produção, exigir uma revisão separada pré-implementação que o avaliador não verifica (segurança, custo, revisão humana).

Rejeitos duros:
- Qualquer ciclo em que o avaliador é um juiz de LLM sem a verdade de terra verificável pela máquina.
- Qualquer avaliador que relate uma única pontuação escalar sem decomposição.
- Os avaliadores só são treinados, os insumos mantidos não são negociáveis.

Regras de recusa:
- Se o utilizador não puder descrever o avaliador em dois parágrafos, recuse e peça a especificação do avaliador primeiro.
- Se o domínio não for verificado (escritura criativa, hipótese científica de prazo aberto, pesquisa de longa duração), recuse e recomenda um pipeline híbrido com revisão humana em vez de um ciclo fechado.
- Se a superfície de implantação proposta for irreversível (alterações na infraestrutura de produção, troca de algoritmos em um produto de transporte marítimo), recusar a implantação em circuito fechado.

Formatos de saída:

Retorna um memorando de uma página com:
- **Loop summary**(generador, avaliador, domínio alvo)
- **Evaluator score**(Rigor 1-5 com justificação)
- **Confabulation surface**(top 3, com cobertura de avaliadores)
- **Reward-hacking surface**(top 3, com mitigações)
- **Determinism and reproducibility**(variância de pontuação versus variância de população; controlo das sementes; aprovação/falha)
- **Deployment readiness**(navio em circuito fechado autorizado; revisões pré-desenvolvimento necessárias: segurança, custo, pessoal)
- **Recommendation**(processar / apertar avaliador / escolher um domínio diferente)
