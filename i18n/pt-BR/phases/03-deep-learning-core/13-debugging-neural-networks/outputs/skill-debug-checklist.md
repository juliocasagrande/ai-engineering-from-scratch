---
name: skill-debug-checklist
description: Decision-tree checklist for debugging neural network training failures
version: 1.0.0
phase: 3
lesson: 13
tags: [debugging, neural-networks, training, diagnostics, deep-learning]
---

# Lista de verificação de defeitos de rede neural

Protocolo de depuração sistemática para quando o treinamento falhar. Trabalhe através destes em ordem - a maioria dos bugs são capturados nos primeiros 3 passos.

## Antes do treino (prevenção de bugs)

1. A arquitetura do modelo impresso e os parâmetros contam.
2. Execute uma única passagem para a frente com entrada aleatória.
3. Verifique se os rótulos são do tipo d correto (CrossEntropyLoss precisa de Long, BCELoss precisa de Float)
4. Verificar a normalização dos dados: as entradas devem ter média próxima a 0 e std próxima a 1
5. Imprimir 5 pares aleatórios.
6. Confirmar que a divisão de trem/teste não tem amostras duplicadas

## Teste de ultra-ajuste de um lote (60 segundos, detecta 80% dos bugs)

1. Tome 8 a 32 amostras do seu conjunto de treinamento
2. Treinar 200 passos com uma taxa de aprendizagem razoável
3. A precisão do treino deve atingir 100%
4. Se falhar: o bug está no seu modelo, função de perda ou ciclo de treinamento - não os seus dados ou hiperparâmetros
5. Se passar: proceder à formação completa

## Perdas não diminuindo

1. Verifique a taxa de aprendizagem. Tente 3 valores: corrente/10, corrente, corrente*10
2. Impressão de normas de gradiente por camada. Todos os zeros significam rede morta ou gráfico separado
3. Verifique .`requires_grad=True`Verifique isso.`loss.backward()`é chamado
4. Verifica isso .`optimizer.zero_grad()`é chamado antes `loss.backward()`
5. Verifica isso .`optimizer.step()`é chamado depois `loss.backward()`
6. Verificar os parâmetros do modelo são passados para o optimizador: `optimizer = Adam(model.parameters())`

## Perda é NaN ou Inf

1. Reduzir a taxa de aprendizagem em 10x
2. Adicionar epsilon a todas as ligações log()`torch.log(x + 1e-7)`
3. Adicionar epsilon a todas as divisões: `x / (y + 1e-8)`
4. Previsões de Clamp: `torch.clamp(pred, 1e-7, 1 - 1e-7)`antes da perda BCE
5. Utilização`torch.autograd.detect_anomaly()`Para encontrar a operação exata
6. Verificar NaN nos dados de entrada: `assert not torch.isnan(x).any()`

## Oscilação de perdas

1. Reduzir a taxa de aprendizagem em 3-10x
2. Aumentar o tamanho do lote (reduzir o ruído do gradiente)
3. Adicionar cortes de gradiente: `torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)`
4. Cambio de SGD para Adam (LR adaptativo por parâmetro)
5. Adicionar o aquecimento da taxa de aprendizagem para os primeiros 5-10% da formação

## Super-ajustamento (aceleração do trem alta, aceleração do ensaio baixa)

1. Adicionar o abandono (comece com p=0,1, aumenta para 0,5)
2. Adicionar perda de peso ao optimizador: `Adam(params, weight_decay=1e-4)`
3. Reduzir o tamanho do modelo (menos camadas ou camadas mais estreitas)
4. Adicionar a ampliação de dados
5. Utilize paragem precoce: paragem quando a perda de validação aumenta por 5 ou mais épocas
6. Verificação de vazamento de dados entre o trem e os conjuntos de ensaio

## Subequipamento (tanto no trem como no ensaio)

1. Aumentar a capacidade do modelo (mais camadas, camadas mais largas)
2. Trem para mais épocas
3. Aumentar a taxa de aprendizagem (cuidadosamente)
4. Remover a regularização temporariamente para verificar que o modelo pode aprender
5. Verifique se o seu modelo é expressivo o suficiente para a tarefa

## Neurônios mortos da ReLU

1. Verifique a fração de ativações zero por camada. >50% é um problema
2. Passe para LeakyReLU(0.01) ou GELU
3. Use a inicialização Kaiming para pesos
4. Reduzir a taxa de aprendizagem (as grandes atualizações podem empurrar os neurônios para a zona morta)
5. Adicionar normalização de lote antes das funções de ativação

## Referência rápida: pontos de partida da taxa de aprendizagem

| Optimizer | Task | Starting LR |
|-----------|------|------------|
| Adam | Training from scratch | 1e-3 |
| Adam | Fine-tuning pretrained | 1e-5 |
| SGD + momentum | Training from scratch | 1e-1 |
| SGD + momentum | Fine-tuning pretrained | 1e-3 |
| AdamW | Transformer training | 3e-4 |

## Referência rápida: efeitos do tamanho do lote

| Batch size | Gradient noise | Memory | Generalization |
|-----------|---------------|--------|---------------|
| 8-16 | High (noisy) | Low | Often better |
| 32-64 | Moderate | Moderate | Good default |
| 128-256 | Low (smooth) | High | May need warmup |
| 512+ | Very low | Very high | Needs LR scaling |

## Quando nada funciona

1. Simplificar o modelo para uma camada oculta.
2. Simplificar os dados para 100 amostras.
3. Substitua a sua perda por MSE.
4. Substitua o seu optimizador com SGD ((lr=0.01).
5. Substitua os seus dados com dados sintéticos (por exemplo, y = x[0] > 0).
6. Se nenhuma dessas coisas funcionar: o bug está no código que não está a ver (carregamento de dados, pré-processamento, formas de tensor)
