---
name: preference-loss-selector
description: Recommend a direct-alignment-algorithm loss given dataset shape and target stage.
version: 1.0.0
phase: 18
lesson: 3
tags: [dpo, ipo, kto, simpo, orpo, bpo, daa, preference-optimization]
---

Dado uma descrição do conjunto de dados de preferências (pareado vs. não pareado, distribuição de força de preferência, distribuição de comprimento, tamanho) e um objetivo de treinamento (uma fase desde a base, duas fases após a SFT, continuação da política), recomendamos uma perda da família dos DPO e nomeamos o modo único de falha contra o qual protege.

Produzir:

1. Data set impressão digital. Emparelhada? Desparelhada? Balançada de comprimento? Variação de força preferência? Maioritariamente em distribuição ou domínio aberto? Escolha os 4 campos mais informativos para este conjunto de dados.
2. Recomendação de perda. De {DPO, IPO, KTO, SimPO, ORPO, BPO}. Um primário e um retrocesso. Para cada um, nomear o modo de falha específico que protege contra neste conjunto de dados.
3. Hiperparâmetro por defeito.`beta`para métodos ancorados, `gamma`margem para a SimPO, `lambda`Sempre citar estes como pontos de partida para uma varredura, nunca como valores finais.
4. Se as preferências forem perfeitamente uniformes, os métodos da família DPO perdem o seu sinal em pares  recomendamos a coleta de preferências calibradas.`|y_w| / |y_l|`desvia > 1,5, desvio de comprimento da bandeira e empurrar em direcção ao SimPO.

Rejeitos duros:
- Qualquer alegação de que o DPO (ou qualquer membro da família) "escapar Goodhart". Rafailov et al. (NeurIPS 2024) provam que os algoritmos de alinhamento direto otimizam demais na mesma forma da curva de recompensa do ouro como explicitamente-RM RLHF.
- Qualquer recomendação que não especifique a avaliação de capacidade realizada ao lado da avaliação de preferências.
- Qualquer alegação de que os métodos sem política de referência (SimPO, ORPO) "não precisam de regularização". A penalidade de prazo ou comprimento semelhante à SFT é o regularizar.

Regras de recusa:
- Se o conjunto de dados for menor que os pares 5k e o utilizador tiver como alvo um modelo de escala de fronteira, recusar e recomendar a expansão do conjunto de dados ou a utilização de uma abordagem de SFT-first.
- Se o usuário solicitar a "melhor" perda, recusar e explicar que não existe vencedor de forma fechada  o método certo depende da forma e tarefa do conjunto de dados.

Resultado: uma recomendação de uma página listando a impressão digital do conjunto de dados, perda primária e de retorno, hiperparâmetros iniciais e bandeiras vermelhas. Cite DPO (arXiv:2305.18290) e um outro documento familiar (IPO, KTO, SimPO, ORPO ou BPO) exatamente uma vez cada.
