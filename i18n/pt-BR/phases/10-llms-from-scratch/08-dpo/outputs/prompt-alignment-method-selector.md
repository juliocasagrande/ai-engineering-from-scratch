---
name: prompt-alignment-method-selector
description: Choose the right alignment method (SFT, RLHF, DPO, KTO, ORPO, SimPO) for your use case
version: 1.0.0
phase: 10
lesson: 8
tags: [alignment, dpo, rlhf, kto, orpo, simpo, preference-optimization, fine-tuning]
---

# Selector de Método de Alineação

Ao escolher um método de alinhamento para um modelo de linguagem, use esta estrutura para avaliar os seus requisitos de dados, computação e qualidade, e selecione o método que melhor se adapte às suas restrições.

## Requisitos de entrada

Fornecer:
- **Base model**(por exemplo, Llama 3 8B, Mistral 7B, Qwen 2.5 72B)
- **Starting point**(modelo base, ou já SFT'd?)
- **Available data**(pares de instrução, pares de preferência, classificações não emparelhadas ou nenhuma)
- **Compute budget**(horas de GPU, número de GPUs)
- **Quality target**(bom o suficiente para protótipo, competitivo com código aberto, estado da arte)
- **Timeline**(dias, semanas, meses)

## Matriz de decisão

### Seleção rápida

| Your Situation | Recommended Method | Why |
|---------------|-------------------|-----|
| No preference data, only instruction pairs | SFT only | You can't align without preference signal |
| < 5,000 preference pairs, limited compute | DPO | Simpler pipeline, works well with small data |
| Unpaired feedback (thumbs up/down only) | KTO | Only method that works without pairwise comparisons |
| Want alignment in a single training run | ORPO | Combines SFT + alignment, no reference model |
| Memory-constrained (can't fit reference model) | SimPO | No reference model needed |
| Large-scale, multi-objective alignment | RLHF (PPO) | Separate reward model captures complex preferences |
| Iterative alignment with online data | RLHF (PPO) | Can generate, rate, and retrain in a loop |
| Post-RLHF refinement | DPO | Fine-tune an RLHF model on targeted preferences |

### Comparação pormenorizada

| Method | Data Requirement | Models in Memory | Training Loops | Stability | Best Scale |
|--------|-----------------|-----------------|----------------|-----------|------------|
| SFT | Instruction pairs (10K+) | 1 | 1 | High | Any |
| RLHF | Preference pairs (20K+) | 3-4 | 3 | Low | Large (70B+) |
| DPO | Preference pairs (5K+) | 2 | 2 (SFT + DPO) | High | Small-Medium (7B-70B) |
| KTO | Unpaired ratings (5K+) | 2 | 2 (SFT + KTO) | High | Any |
| ORPO | Preference pairs (10K+) | 1 | 1 | High | Small-Medium |
| SimPO | Preference pairs (5K+) | 1 | 2 (SFT + SimPO) | High | Small-Medium |

## Configuração específica do método

### FFT

- **When to stop**Após 1-3 épocas ou quando a perda de validação cessa de diminuir
- **Key hyperparameter**: Taxa de aprendizagem (1e-5 a 5e-5, menor para modelos maiores)
- **Critical detail**: Tokens de instrução de máscara na perda
- **Gotcha**: Mais de 3 épocas causam memorização; mistura de 2-5% de dados pré-formação

### RLHF (PPO)

- **When to use**Você tem pares de comparação de 20K+, precisa de alinhamento multi-objetivo, ou quer aprendizado online iterativo
- **Key hyperparameters**: coeficiente KL (0,01-0,05), índice de clipes PPO (0,1-0,3), taxa de aprendizagem (5e-6 a 3e-5)
- **Critical detail**: O modelo de remuneração deve ser >= tamanho do modelo de política
- **Gotcha**: O PPO é instável; monitorar as divergências KL e as curvas de recompensa continuamente

### DPO

- **When to use**: Você tem pares de preferências e quer um pipeline mais simples do que RLHF
- **Key hyperparameter**: Beta (0,1-0,5; menor = maior desvio da referência permitido)
- **Critical detail**: O modelo de referência deve ser uma cópia congelada do ponto de controlo SFT
- **Gotcha**Muito sensível à beta; faça uma varredura sobre [0,05, 0,1, 0,2, 0,5]

### Técnico de gestão

- **When to use**Só temos rótulos "bons" ou "ruins" sem comparações em pares.
- **Key hyperparameter**: Beta (same como DPO), multiplicador de aversião à perda (1.5x em respostas ruins)
- **Critical detail**: Necessidades de um equilíbrio aproximado entre bons e maus exemplos (40-60% dividido)
- **Gotcha**: Sem pares, o sinal de gradiente é mais fraco; pode precisar de mais dados do que o DPO

### ORPO

- **When to use**Você quer pular SFT inteiramente e ir direto da base para alinhado
- **Key hyperparameter**: Lambda (peso do termo preferencial versus termo SFT)
- **Critical detail**: Necessita de etiquetas de instrução E pares de preferências num conjunto de dados
- **Gotcha**: O objetivo combinado pode ser difícil de equilibrar; se a perda de SFT dominar, o alinhamento é fraco

### Simpo

- **When to use**Configuração com restrição de memória onde não pode manter um modelo de referência
- **Key hyperparameter**: Beta, gama (exponente de normalização de comprimento)
- **Critical detail**: A normalização de comprimento impede que o modelo favoreça respostas curtas
- **Gotcha**Não há âncora de modelo de referência, o modelo pode deslocar-se mais longe; monitore cuidadosamente

## Modelos de Pipeline

### Modelo 1: Protótipo rápido (1-2 dias)

```
Base Model -> SFT (1 epoch, 10K examples) -> DPO (3 epochs, 5K pairs)
```

Computação: ~4 horas de GPU para o modelo 7B no A100
Qualidade: instrução sólida, alinhamento de preferências básicos

### Modelo 2: Qualidade da produção (1-2 semanas)

```
Base Model -> SFT (2 epochs, 50K examples) -> DPO (5 epochs, 20K pairs) -> Eval -> Iterate
```

Computação: ~40 horas de GPU para 7B, ~200 horas de GPU para 70B
Qualidade: Competitiva com modelos RLHF de código aberto

### Modelo 3: Estado da técnica (1-3 meses)

```
Base Model -> SFT (2 epochs, 100K+ examples) -> RLHF (PPO, 50K+ pairs) -> DPO (targeted refinement) -> Eval -> Iterate
```

Computação: ~ 500+ horas de GPU para 70B
Qualidade: aproximação do alinhamento dos modelos de fronteira

### Modelo 4: Dados mínimos (1-2 dias)

```
Base Model -> SFT (1 epoch, 5K examples) -> KTO (unpaired thumbs up/down from users)
```

Computação: ~ 2 horas de GPU para 7B
Qualidade: Melhor do que apenas a SFT com custos gerais mínimos de recolha de dados

## Protocolo de avaliação

Após o alinhamento, avaliar através destas dimensões:

1. **Preference win rate**Comparar modelo alinhado com modelo SFT em mais de 200 instruções de teste com juízes humanos.
2. **Benchmark retention**: MMLU, HumanEval ou referências específicas de domínio. Não deve cair > 5% do valor de base da SFT.
3. **MT-Bench or AlpacaEval**A comparação com as linhas de base publicadas.
4. **Safety evaluation**: Teste contra as solicitações adversárias, as brechas de prisão e as categorias de solicitações prejudiciais.
5. **Response diversity**Messa a entropia das respostas em 100 pedidos.

## Modos comuns de falhas

| Symptom | Cause | Method-Specific Fix |
|---------|-------|-------------------|
| Verbose, padded responses | Reward model / implicit reward favors length | DPO: increase beta. RLHF: add length penalty. SimPO: adjust gamma. |
| Model agrees with everything | Sycophancy from preference data bias | Add preference pairs where the correct response disagrees with the user |
| Refuses benign requests | Over-alignment on safety data | Reduce safety example proportion, add more benign-refusal pairs |
| Outputs are nearly identical to SFT | Beta too high (DPO/KTO) or KL coefficient too high (PPO) | Lower beta / KL coefficient; the model isn't learning |
| Training loss oscillates | Learning rate too high or insufficient data | Reduce lr by 2-3x; increase preference data |
