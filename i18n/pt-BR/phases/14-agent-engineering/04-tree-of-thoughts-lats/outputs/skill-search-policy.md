---
name: search-policy
description: Escolha uma estratégia de pesquisa (ReAct, ToT, LATS, evolutiva) dada a forma da tarefa, o orçamento de token e a qualidade do avaliador.
version: 1.0.0
phase: 14
lesson: 04
tags: [tree-of-thoughts, lats, mcts, search, value-function]
---

Dada uma forma de tarefa (resposta única / resposta múltipla / aberta), um orçamento de token e um avaliador disponível (teste escalar / heurística / auto-evaluação), produzir uma recomendação de estratégia de pesquisa com parâmetros concretos.

Produzir:

1. Decisão. Uma das seguintes: ReAct linear, ToT de feixe (com largura de feixe k), BFS ToT (com profundidade máxima), DFS ToT com poda, MCTS LATS (com iterações e UCT c), pesquisa evolutiva (apenas se o avaliador for programático e verificável).
2. Para cada estratégia, valores numéricos em concreto: largura do feixe, limite de profundidade, fator de ramificação K, implementações por nível, UCT c (default 1.4), tempo de espera.
3. Função de valor. Especifique exatamente o que marca um nó. Opções: taxa de aprovação no teste unitário, distância numérica ao alvo, pontuação LLM com formato (certo/probabvel/impossível ou 1,10 ou voto), ou recompensa ambiental.
4. Estimativa do orçamento dos tokens. Tokens de pior caso = branching_factor ^ depth * avg_prompt_tokens. Mostre o número. Se exceder o orçamento do usuário, recomende uma estratégia mais barata.
5. Modos de falha. Para cada estratégia escolhida, lista os dois principais modos de falha e suas mitigações (por exemplo, LATS + evaluador ruidoso -> adicionar verificação baseada em ferramentas por CRITIC, lição 05).

Rejeitos duros:

- Recomendação de pesquisa quando o avaliador não é confiável (apenas auto-evaluado, sem verdade básica).
- Definir o fator de ramificação K acima de 5 sem razão convincente. K=3-5 é o padrão de papel; K=10 explode o custo.
- Aplicar LATS para tarefas de estilo chat. A pesquisa não ajuda a conversação Q&A sem alvo programático.
- A busca evolutiva sem uma aptidão verificável pela máquina. AlphaEvolve é interessante apenas quando a aptidão é programática (exercícios executados, velocidade medida, teorema de verificação).

Regras de recusa:

- Se o orçamento do token < 5x o custo de uma única trajetória, recuse a pesquisa e recomenda ReAct + Reflexion (Lessão 03).
- Se o orçamento de atraso do relógio de parede for < 10 segundos, recuse o LATS e recomende ReAct.
- Se a tarefa for a busca de informações, recuse a pesquisa e recomende a ReWOO (Lessão 02).

Resultado: um bloco de recomendações (estratégia escolhida, parâmetros, função de valor, estimativa orçamental) mais uma nota "o que ler a seguir" apontando para a lição 05 (CRITIC) para a confiabilidade dos avaliadores, a lição 11 (AlphaEvolve) para as variantes evolutivas ou a lição 30 (desenvolvimento orientado por valores) para a validação de níveis de referência.
