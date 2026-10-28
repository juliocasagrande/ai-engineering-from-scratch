---
name: seq2seq-design
description: Desenhar um pipeline de sequência para sequência para uma determinada tarefa.
phase: 5
lesson: 09
---

Dado uma tarefa (tradução, resumo, parafrase, reescritura de perguntas), saída:

1. Arquitetura. O encoder-decoder de transformador treinado (BART, T5, mBART, NLLB) é o padrão.
2. - O ponto de partida.`facebook/bart-base`- Não . `google/flan-t5-base`- Não . `facebook/nllb-200-distilled-600M`O ponto de controlo corresponde à tarefa e à cobertura linguística.
3. Estratégia de decodificação: ganância por resultados deterministas, busca de feixe (largura 4-5) para qualidade, amostragem com temperatura para diversidade.
4. Um modo de falha para verificar antes da expedição. O viés de exposição manifesta-se como deriva de geração em saídas mais longas; amostra 20 saídas em comprimento de 90 percentil e globo ocular.

Recusar-se a recomendar a formação de um sequência de 2 segundos a partir do zero para exemplos paralelos inferiores a ~ 1M. Marcar qualquer pipeline que use decodificação gananciosa para conteúdo orientado para o usuário como frágil (repetências gananciosas e loop).
