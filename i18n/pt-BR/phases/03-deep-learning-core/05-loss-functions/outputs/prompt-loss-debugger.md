---
name: prompt-loss-debugger
description: A diagnostic prompt for debugging loss curves and training failures
phase: 03
lesson: 05
---

Se tiver uma descrição de uma curva de perda ou comportamento de treinamento, diagnostique o problema e recomenda uma solução.

Padrões comuns e suas causas:

**Loss is NaN or infinity:**
- log(0) em entropia cruzada: Adicionar recorte de epsilon (max(eps, previsão))
- Gradientes de explosão: adicionar cortes de gradientes (max_norm=1.0)
- Taxa de aprendizagem demasiado elevada: Reduzida em 10x
- Superfluo numérico em softmax: Subtrair logit máximo antes de exp

**Loss decreases then suddenly spikes:**
- Taxa de aprendizagem demasiado elevada para a região actual de perda
- Correcção: Adicionar aquecimento da taxa de aprendizagem (rampa linear durante os primeiros 1-10% dos passos)
- Correcção: Passe para o cronograma de decomposição cosínica
- Correcção: Reduzir a taxa de aprendizagem em 3-5x

**Loss plateaus and never improves:**
- Neurônios mortos (ReLU): Verifique as estatísticas de ativação, passe para GELU
- Gradientes desaparecidos: Verifique as normas de gradientes por camada
- Função de perda errada: MSE na classificação se manterá em 0,25, para binário equilibrado
- Taxa de aprendizagem muito baixa: aumento de 3 a 10 vezes

**Training loss decreases but validation loss increases:**
- Oficinação: Adição de desconexão (p=0,1-0,3), declínio de peso (0,01), ou aumento de dados
- Reduzir a capacidade do modelo (menos camadas ou tamanho oculto menor)
- Adicionar paragem precoce com paciência = 5-20 épocas

**Loss is very high and barely decreasing:**
- Descoincidência de codificação de rótulos: Verifique se os objetivos correspondem às expectativas da função de perda
- Softmax aplicado duas vezes: Se utilizar F.cross_entropy, NÃO aplicar softmax manualmente
- Sinal errado: A perda deve usar probabilidade de registro negativo, não positiva

**All predictions are the same value (e.g., 0.5):**
- MSE sobre classificação: transição para entropia cruzada
- Rede morta: verifique a inicialização, assegure que as ativações não sejam zero
- Solução apenas bias: ignorando as entradas da rede, verificando a normalização das entradas

Para cada diagnóstico:
1. Identificar a causa raiz mais provável
2. Fornecer uma correção específica com alterações de código ou hiperparâmetro
3. Explique como verificar a correção funcionou
4. Sugerir monitorização para evitar a recorrência
