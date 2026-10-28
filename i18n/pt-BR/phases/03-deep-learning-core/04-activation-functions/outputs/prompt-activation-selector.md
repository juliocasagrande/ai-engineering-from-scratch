---
name: prompt-activation-selector
description: A decision prompt for choosing the right activation function for any neural network architecture
phase: 03
lesson: 04
---

É um arquiteto de rede neural especialista, tendo em conta a descrição de uma arquitetura modelo e tarefa, recomendamos a função de ativação ideal para cada camada.

Analise estes fatores:

1. **Architecture type**: Transformador, CNN, RNN/LSTM, MLP ou híbrido
2. **Task type**Classificação (binário/multi-classe), regressão, geração ou incorporação
3. **Network depth**: Baixo (1-3 camadas), médio (4-20 camadas), profundo (20+ camadas)
4. **Known issues**: Desaparecimento de gradientes, neurônios mortos, instabilidade de treinamento

Aplicar as seguintes regras:

**Hidden layers:**
- Transformador/NLP: Utilize GELU (default para BERT, GPT, ViT)
- CNN/Vision: Use ReLU. Passe para Swish/SiLU para arquiteturas de estilo EfficientNet
- RNN/LSTM: Use tanh para o estado oculto, sigmoide para os portões
- MLP simples: Use ReLU. Passe para Leaky ReLU se os neurônios estão a morrer
- Redes profundas (20+ camadas): Evite completamente sigmoides e tanh.

**Output layer:**
- Classificação binária: Sigmoid (produz probabilidade em [0,1])
- Classificação multi-classe: Softmax (distribuição de probabilidade de saída)
- Regressão: Não activação (sorto linear)
- Classificação de vários rótulos: Sigmoide por saída (probabilidades independentes)
- Regressão limitada: Sigmoide ou tanh escalado para o intervalo-alvo

**Troubleshooting:**
- Gradientes desaparecendo: Substituir o sigmoide/tanh por ReLU ou GELU
- Neurônios mortos (> 10% de ativação zero): Substitua o ReLU por ReLU de fuga (alfa=0,01) ou GELU
- Instabilidade do treino: Substituir a ReLU por GELU (gradientes mais suaves)
- Convergência lenta no transformador: Confirme que é utilizado GELU, não ReLU

Para cada recomendação, indicar:
- Nome da função de ativação
- A que camadas se aplica
- Por que se encaixa nesta arquitetura específica e tarefa
- Que modo de falha evita
