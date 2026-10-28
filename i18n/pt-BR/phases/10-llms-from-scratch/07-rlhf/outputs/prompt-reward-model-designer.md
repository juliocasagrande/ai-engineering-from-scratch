---
name: prompt-reward-model-designer
description: Design reward model training pipelines for RLHF alignment
version: 1.0.0
phase: 10
lesson: 7
tags: [rlhf, reward-model, ppo, alignment, human-feedback, preference-learning]
---

# Recompensa para o Modelo de Design

Ao construir um pipeline RLHF para alinhar um modelo de linguagem para um comportamento alvo (utilidade, capacidade de codificação, segurança, honestidade), use esta estrutura para projetar o protocolo de coleta de dados, treinar o modelo de recompensa e configurar o PPO.

## Requisitos de entrada

Fornecer:
- **Target behavior**(por exemplo, "assistente útil e inofensivo", "experto em codificação Python", "questionamento e resposta médica com segurança")
- **Base model**(por exemplo, Llama 3 8B após SFT, Mistral 7B Chat)
- **Reward model size**(normalmente do mesmo tamanho ou maior que o modelo de política)
- **Annotation budget**(horas humanas ou pares de comparação disponíveis)
- **Compute budget**(horas de formação de modelo de recompensa + PPO)

## Passo 1: Coleção de dados de preferência

### Protocolo de anotação

1. **Prompt selection**: Amostra da distribuição de formação SFT mais indicações de saída de distribuição (10-20% novidade)
2. **Response generation**: Gerenar 2-4 respostas por pedido usando o modelo SFT com diferentes temperaturas (0,3, 0,7, 1,0)
3. **Comparison format**: Mostre aos anotadores exatamente 2 respostas e pergunte: "Qual resposta é melhor?"
4. **Criteria rubric**: Definir o que "melhor" significa para o seu caso de uso

### Modelo de rubrica

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Helpfulness | 40% | Does it answer the question completely and correctly? |
| Harmlessness | 25% | Does it avoid harmful, biased, or misleading content? |
| Honesty | 20% | Does it acknowledge uncertainty rather than hallucinate? |
| Conciseness | 15% | Is the response an appropriate length for the question? |

Ajustar os pesos para o seu caso de uso. Um assistente de codificação pode pesar a correcção em 60% e a concisionidade em 20%.

### Orientações para o tamanho dos dados

| Scale | Comparison Pairs | Annotator Hours | Expected RM Accuracy |
|-------|-----------------|-----------------|---------------------|
| Minimum viable | 5,000-10,000 | 400-800 | 60-65% |
| Production v1 | 20,000-50,000 | 1,600-4,000 | 65-72% |
| Production v2 | 100,000-500,000 | 8,000-40,000 | 72-78% |

O InstrutorGPT usou 33.000 comparações de 40 empreiteiros. O artigo inicial da Anthropic usou 22.000 de 20 anotadores. O acordo entre os anotadores é tipicamente de 70-75% - o modelo de recompensa não pode exceder os níveis de acordo humano.

### Controle de qualidade

- **Agreement filtering**: Descarregar pares em que menos de 70% dos anotadores concordam
- **Annotator calibration**: Execute rodadas de calibração com pares conhecidos antes da anotação real
- **Bias detection**: Monitore se os anotadores preferem consistentemente respostas mais longas, linguagem formal ou padrões específicos
- **Adversarial examples**: Incluir exemplos de 5 a 10% destinados a capturar os anotadores que não estão lendo cuidadosamente

## Passo 2: Arquitetura Modelo de Recompensa

### Decisoes de Arquitetura

| Decision | Recommendation | Rationale |
|----------|---------------|-----------|
| Base architecture | Same transformer as the policy | Weight initialization from SFT checkpoint gives strong starting features |
| Output head | Single linear projection from last hidden state | Scalar reward from the most complete position representation |
| Model size | >= policy model size | Smaller RM produces unreliable signals that destabilize PPO |
| Initialization | SFT checkpoint with new output head | Pre-trained features capture language quality already |

### Configuração de formação

| Parameter | Range | Notes |
|-----------|-------|-------|
| Learning rate | 1e-5 to 5e-5 | Lower than SFT because the task is simpler |
| Epochs | 1-3 | Overfitting is a major risk with limited comparison data |
| Batch size | 64-256 | Each "example" is a pair, so effective data is 2x |
| Loss function | Bradley-Terry: -log(sigmoid(r_preferred - r_rejected)) | Standard for pairwise comparisons |
| Validation split | 10-20% | Monitor accuracy on held-out pairs |

### Metricas de avaliação

1. **Pairwise accuracy**: Que fracção dos pares de preferências mantidos fora classifica corretamente a RM?
2. **Margin distribution**: Planejar a distribuição de (r_preferido - r_rejeitado). Deve ser centrado acima de 0 com poucos negativos.
3. **Calibration**O sigmoid (preferido - rejeitado) está próximo da probabilidade de preferência humana real?
4. **OOD generalization**A precisão deve diminuir < 10%.

## Passo 3: Configuração de PPO

### Hiperparametros

| Parameter | Typical Value | Effect of Being Too High | Effect of Being Too Low |
|-----------|--------------|-------------------------|------------------------|
| KL coefficient (beta) | 0.01-0.05 | Model barely learns, stays too close to SFT | Reward hacking, degenerate outputs |
| Learning rate | 5e-6 to 3e-5 | Training instability, divergence | Slow convergence, wasted compute |
| Clip ratio (epsilon) | 0.1-0.3 | Large, potentially destabilizing updates | Very conservative updates, slow learning |
| PPO epochs per batch | 1-4 | Overfitting to current batch | Underutilizing each batch |
| Generation batch size | 128-512 | Memory issues | Noisy gradient estimates |
| Max response length | 256-1024 | Slow generation, memory issues | Truncates useful responses |

### Painel de monitoramento

Seguir estas métricas durante o treinamento de PPO:

1. **Mean reward**A redução significa instabilidade.
2. **KL divergence**Deve ficar abaixo de 10 a 20 nats.
3. **Response length**Aumentar monótono = hacking de recompensa por verbosidade.
4. **Entropy**A entropia da distribuição dos tokens deve diminuir lentamente.
5. **Reward model agreement**: Ponha as respostas do PPO com o modelo de recompensa; o acordo deverá melhorar.

### Banderas vermelhas durante a PPO

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Reward increases but outputs degrade | Reward hacking | Increase KL coefficient, retrain RM on adversarial examples |
| KL divergence explodes | Learning rate too high or KL coefficient too low | Reduce lr, increase beta |
| Response length grows monotonically | RM rewards verbosity | Add length penalty to reward, retrain RM with length-controlled pairs |
| All responses become identical | Mode collapse | Increase generation temperature, reduce PPO epochs |
| Reward oscillates wildly | PPO instability | Reduce learning rate, increase clip ratio |

## Passo 4: Validação de ponta a ponta

Antes de implantar um modelo treinado em RLHF:

1. **A/B test vs SFT**Exercer os modelos SFT e RLHF em mais de 200 instruções de teste. Ter mais de 3 avaliadores compararem as respostas. O modelo RLHF deve ganhar > 60% das vezes.
2. **Safety evaluation**A análise de dados sobre as indicações adversárias conhecidas (abandono de prisão, solicitações prejudiciais) deve ser rejeitada adequadamente.
3. **Regression check**: Execute benchmarks padrão (MMLU, HumanEval, MT-Bench) para confirmar que o modelo RLHF não perdeu capacidades principais.
4. **Forgetting check**Aumento deve ser < 10% em relação ao modelo SFT.
5. **Length analysis**A diferença entre a duração média da resposta entre os modelos SFT e RLHF é que, se o RLHF for > 50% mais longo, o modelo de recompensa provavelmente tem um viés de verbosidade.
