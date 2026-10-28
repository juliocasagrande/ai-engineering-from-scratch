---
name: skill-perceptron
description: Compreender o padrão de percepção e quando usar arquiteturas de camada única versus multi-camada
version: 1.0.0
phase: 3
lesson: 1
tags: [perceptron, neural-networks, classification, deep-learning]
---

# O padrão de Perceptron

Um perceptron calcula uma soma ponderada de entradas mais um viés, depois aplica uma função de passo para produzir uma saída binária.

```
output = step(w1*x1 + w2*x2 + ... + wn*xn + bias)
```

## Quando um único perceptron é suficiente

- O problema é linearmente separavel: uma linha reta (ou hiperplano) pode dividir as duas classes
- Portas lógicas: E, OU, NÃO, NAND
- Decisoes simples de limiar: "a pontuao é acima de X?"
- Classificadores binários de dados agrupados em duas regiões não superpujadas

## Quando você precisa de várias camadas

- O problema não é linearmente separavel: nenhuma linha única pode separar as classes
- Problemas de XOR e paridade
- Qualquer tarefa que precise de um raciocínio "isto, mas não aquele" (combinações de condições)
- Classificação do mundo real: imagens, texto, áudio - quase sempre não lineares

## Lista de verificação das decisões

1. Pode traçar um único limite entre as aulas?
   - Sim: trabalhos de perceptron único
   - Não: é preciso pelo menos duas camadas
2. Pode o problema ser decomposto em E/O de decisões lineares mais simples?
   - Esta decomposição diz-lhe a estrutura mínima da rede
   - XOR = (A OR B) E (NOT (A E B)) = 3 perceptrões em 2 camadas
3. Para problemas com mais de duas classes, você precisa de um nó de saída por classe

## A regra da formação

```
error = expected - predicted
weight_new = weight_old + learning_rate * error * input
bias_new = bias_old + learning_rate * error
```

Se a previsão for correta, nada muda. Se for errado, os pesos mudam para reduzir o erro. Isso só funciona para perceptores de camada única.

## Erros comuns

- Tentando aprender padrões não lineares com um único perceptron (nunca convergirá)
- Estabelecer a taxa de aprendizagem demasiado alta (pesos oscilam) ou muito baixa (a formação demora para sempre)
- Esquecer o termo "bias" (sem ele, o limite de decisão deve passar pela origem)
- Confusão entre a convergência de percepção (garantida para dados linearmente separaveis) e a convergência geral de rede neural (não garantida)
