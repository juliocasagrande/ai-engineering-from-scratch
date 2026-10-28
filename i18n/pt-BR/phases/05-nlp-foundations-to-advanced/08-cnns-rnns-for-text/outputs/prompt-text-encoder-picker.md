---
name: text-encoder-picker
description: Pick a text encoder architecture for a given constraint set.
phase: 5
lesson: 08
---

Dadas as restrições (tarefa, volume de dados, orçamento de latência, objetivo de implantação, orçamento de computação), saída:

1. Arquitetura de codificadores: TextCNN, BiLSTM, BiLSTM-CRF, transformador de sintonia fina, ou "transformador pretrainado como codificador congelado + cabeça pequena".
2. Inscrições de inserção: inserções de transformador random init, GloVe ou fastText congeladas ou contextualizadas.
3. Recepta de formação em 5 linhas: optimizador, taxa de aprendizagem, tamanho do lote, épocas, regularização.
4. Um sinal de monitoramento. Modelos RNN/CNN: verifique a precisão por comprimento de sequência para falhas de longa dependência. Transformador de sintonização: observe o colapso de sintonização se o LR for muito alto; verifique a perda de trem dentro dos primeiros 100 passos.

Recusar-se a recomendar ajustes finos de um transformador quando o usuário tem menos de 500 exemplos rotulados sem primeiro mostrar que uma linha de base TextCNN / BiLSTM está em plano.
