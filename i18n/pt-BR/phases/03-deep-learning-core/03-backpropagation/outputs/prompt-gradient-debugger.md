---
name: prompt-gradient-debugger
description: Diagnóstico e resolução de problemas de gradiente em redes neurais - gradientes desaparecendo, gradientes explodindo e valores NaN
phase: 03
lesson: 03
---

Descreveremos um problema de treinamento e diagnosticaremos sistematicamente a causa raiz e sugeriremos soluções.

## Protocolo de diagnóstico

Quando eu descrevo um problema de gradiente, siga esta sequência:

### 1. Classificar o Sintoma

Determine em que categoria se enquadra o problema:

- **Vanishing gradients**Perder planícies cedo, as camadas iniciais têm gradientes quase zero, as camadas profundas aprendem mas as camadas rasas não
- **Exploding gradients**A perda chega ao infinito, os pesos tornam-se NaN, o treinamento diverge após alguns passos.
- **NaN gradients**A perda torna-se NaN, camadas específicas produzem saídas de NaN, aparece de repente durante o treinamento
- **Dead neurons**Os gradientes são exatamente zero (não apenas pequenos), neurônios específicos nunca se ativam, a perda deixa de melhorar

### 2. Verifique os suspeitos habituais (em ordem)

Para gradientes que desaparecem:
- Função de ativação (sigmoide/tanh em redes profundas saturado -- passar para ReLU/GELU)
- Taxa de aprendizagem muito baixa (existem gradientes, mas as atualizações são muito pequenas para importar)
- Inicialização do peso (pesos iniciais muito pequenos compõem o encolhimento)
- Rede muito profunda para a escolha de ativação
- Normalzação de lote faltando entre as camadas

Para gradientes de explosão:
- Taxa de aprendizagem muito alta
- Inicialização de peso muito grande
- Não há cortes de gradiente (adjunta torch.nn.utils.clip_grad_norm_)
- Esquecer conexões faltantes em redes profundas
- Escala de função de perda (reduzção= 'suma' vs 'média')

Para gradientes NaN:
- Divisão por zero na função de perda (add epsilon: log(x + 1e-8))
- Excesso numérico em exp() (entrada de sujeira para sigmoide/softmax)
- Taxa de aprendizagem excessiva que provoca sobrepeso
- Vêctores de comprimento zero na normalização
- Inf * 0 em operações enmascaradas

Para neurônios mortos:
- ReLU com inicialização negativa (neurônios começam a morrer e permanecem mortos)
- A taxa de aprendizagem muito alta empurrou pesos para além da recuperação
- Use Leaky ReLU, ELU ou GELU em vez de ReLU de baunilha
- Verifique a inicialização do peso (He init para ReLU, Xavier para sigmoide/tanh)

### 3. Forneça o código de diagnóstico

Dê-me um código específico para executar que irá revelar o problema:

```python
for name, param in model.named_parameters():
    if param.grad is not None:
        grad_mean = param.grad.abs().mean().item()
        grad_max = param.grad.abs().max().item()
        print(f"{name:40s} | mean: {grad_mean:.2e} | max: {grad_max:.2e}")
```

### 4. Sugerir correções (classificadas por probabilidade)

Lista de correções de mais provável para menos provável.
- O que mudar
- Por que isso corrige o problema
- Impacto esperado na formação

## Formatos de entrada

Descreva o seu problema com:
- Arquitetura de rede (camadas, ativações, profundidade)
- Função de perda
- Otimizador e taxa de aprendizagem
- O que você observa (curva de perda, magnitude de gradiente, mensagens de erro específicas)
- Quantas épocas antes do problema aparecer

## Formatos de saída

1. **Diagnosis**Uma frase que nomeia a causa raiz
2. **Evidence**O que na sua descrição aponta para esta causa
3. **Fix**: Modificações de código a aplicar, classificadas por probabilidade
4. **Verification**Como confirmar que a correcção funcionou
