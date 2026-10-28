---
name: primitive-mapper
description: Mapear qualquer framework ou base de código multi-agente para os quatro eixos primitivos (agente, transferência, estado compartilhado, orquestador).
version: 1.0.0
phase: 16
lesson: 04
tags: [multi-agent, primitives, framework-comparison, architecture]
---

Dada uma estrutura multi-agente (ou uma base de código que usa uma), produzir o mapeamento primitivo de quatro para que o leitor possa entender a estrutura em um parágrafo.

Produzir:

1. **Agent definition.** Como é construído um agente? quais parâmetros? que estado ele carrega? nome a classe exata ou fábrica.
2. **Handoff mechanism.** Qual dos três padrões de transferência usa o retorno da função , bordas do gráfico ou seleção de alto-falantes? se um híbrido, qual é primário? Mostre o código mínimo que desencadeia uma transferência.
3. **Shared state model.** A rede de mensagens completa ou visualização projetada? em memória ou duradoura (checkpointed)? é segura para escritores simultâneos? quem reconcilia conflitos?
4. **Orchestrator type.** Estático, LLM selecionado, manual ou guiado por fila? Se LLM selecionado, que modelo por padrão? Se estático, o gráfico é cíclico ou DAG?
5. **Cross-axis tradeoffs.** Uma frase cada sobre: determinismo, limite de escalabilidade, depurável, modo de falha típico.

Rejeitos duros:

- Qualquer mapeamento que alegue que uma abstração é "nova" sem mostrá-la não se desmorona para uma das quatro primitivas.
- Comparar os quadros que citam apenas os documentos de marketing.
- Declarações como "Framework X é melhor para agentes" sem especificar qual primitivo o framework otimiza.

Regras de recusa:

- Se o quadro for de código fechado e os documentos públicos não expõem a superfície do agente-handoff-estado-orchestrator, afirme que o mapeamento não é possível sem internos.
- Se o utilizador fornecer uma base de código, mas não fornecer um quadro (agentes laminados à mão), mapear a implementação personalizada e indicar qual é o primitivo menos concebido.
- Se o quadro for mais antigo do que 2024 (o AutoGen original v0.2, pré-Swarm) e não for mais mantido, inclua uma nota de uma linha sobre se o seu sucessor preserva o mapeamento.

O resultado: um resumo de um quadro de uma página. Comece com um resumo de uma frase ("Framework X corrige a transferência como borda do gráfico e expõe o estado compartilhado através de um redutor. "), então as cinco seções acima, em seguida, um parágrafo final nomeando qual projeto de produção as primitivas deste quadro se encaixam melhor.
