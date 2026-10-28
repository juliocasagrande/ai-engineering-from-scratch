---
name: bargainer-designer
description: Desenhar um protocolo de negociação: qual agente narra, qual componente gera ofertas, como os scratchpads privados se separam das mensagens públicas, qual é o limite redondo e como a taxa de transação é monitorada.
version: 1.0.0
phase: 16
lesson: 16
tags: [multi-agent, negotiation, bargaining, contract-net, OG-Narrator]
---

Tendo em conta um cenário de negociação ou de mercado de tarefas (ação de negócios de duas partes, leilão de N-partes, atribuição de tarefas de rede de contratos), elabore o protocolo.

Produzir:

1. **Mechanism.** Uma negociação de dois partidos, um leilão de N-bidder, uma transmissão de contrato ou uma coalizão de vários partidos.
2. **Offer generator.** Determinista (concessão de estilo Zeuthen, equilíbrio de Rubinstein, cronograma linear simples) ou LLM-prompted.
3. **Narration layer.** O que o Mestrado em Direito Jurídico contribui: o enquadramento amigável com os seres humanos, as táticas de persuasão, a personalidade.
4. **Private vs public channels.** Como os vestígios de raciocínio são mantidos fora do contexto da contraparte. "Scratchpad privado" + "mensaje público" como dois campos.
5. **Round bound.** O máximo de 3 a 5 rodadas para duas partes.
6. **Reservation and BATNA discipline.** As duas partes devem saber o preço da reserva. Se a outra parte investigar, o narrador do LLM não deve revelar.
7. **Deal-rate monitoring.** Taxa de transacção de base prevista para este protocolo (cita um número dos referências de negociação: intervalo de 27% a 89%, dependendo do papel da MLL).
8. **Escalation.** Rondas abaixo do limiar, violações do ZOPA, ou rota de violação de regras para um agente mediador ou humano.

Rejeitos duros:

- Qualquer projeto em que o LLM calcula a oferta numérica sem uma queda determinista. arXiv:2402.15813 mostra que isso produz taxas de negócios de ~27%.
- Qualquer projecto sem canais públicos e privados separados.
- Qualquer projeto com rodadas ilimitadas, que garanta resultados orientados à conformidade.
- Desenhos que permitem que um único agente mantenha tanto o estado de comprador quanto de vendedor (negociação de roleplay).

Regras de recusa:

- Se a tarefa não tiver remuneração numérica (negociação qualitativa, termos de contrato), a decomposição OG-Narrador pode não ser aplicada.
- Se o utilizador não puder implementar um scratchpad separado (arquitetura de chamada única LLM), marque explicitamente o risco de vazamento e recomenda uma arquitetura de duas chamadas.
- Se a negociação for contrária a uma parte que pode mentir, recomenda um agente mediador e ofertas registadas para auditoria.

Output: um resumo de uma página. Comece com um resumo de uma frase ("Badgain de duas partes: Zeuthen oferece gerador + narrator LLM, limite de 5 rodadas, scratchpad separado, alerta de taxa de negócios abaixo de 85%. ") , em seguida, as oito seções acima.
