---
name: skill-fine-tuning-guide
description: Decision tree for when and how to fine-tune LLMs with LoRA and QLoRA
version: 1.0.0
phase: 11
lesson: 8
tags: [fine-tuning, lora, qlora, peft, llm-engineering]
---

# Guia de decisão para ajustes

Antes de ajustar o ar, tente estes em ordem:

```
1. Prompt engineering (minutes, $0)
2. Few-shot examples in prompt (minutes, $0)
3. RAG for knowledge retrieval (days, $10-100/month)
4. Fine-tuning with LoRA/QLoRA (days, $5-50 per experiment)
5. Full fine-tuning (weeks, $100-10,000 per run)
```

Só passar para o próximo passo se o anterior for insuficiente.

## Quando ajustar

- O modelo precisa de um estilo ou formato de saída consistente que o prompt não pode alcançar
- Você está destilhando um modelo maior (qualidade GPT-4 de um modelo 8B)
- Questões de latência e exemplos de poucas fotografias adicionam muitos tokens
- Precisamos do modelo para seguir de forma confiável um padrão complexo de raciocínio
- Você tem mais de 1.000 exemplos de alta qualidade do comportamento de entrada-saída desejado

## Quando não se pode ajustar

- O modelo já faz o que você quer com o prompt certo
- Você precisa do modelo para saber os fatos (use RAG em vez)
- Tem menos de 500 exemplos de formação (provavelmente super-ajustados)
- A tarefa muda frequentemente (a reformulação é cara)
- É preciso verificar quais dados influenciaram uma saída específica (a ajuste é uma caixa negra)

## Seleção de método

| GPU VRAM | 7B model | 13B model | 70B model |
|----------|----------|-----------|-----------|
| 16GB (T4) | QLoRA | Not feasible | Not feasible |
| 24GB (3090/4090) | QLoRA or LoRA | QLoRA | Not feasible |
| 40GB (A100) | LoRA or Full | QLoRA or LoRA | QLoRA |
| 80GB (A100/H100) | Full | LoRA or Full | QLoRA or LoRA |

## Lista de verificação de configuração do LoRA

1. Comece com r=16, alfa=32 (seguro por defeito para a maioria das tarefas)
2. Objectivo q_proj e v_proj primeiro (LOR mínimo viável)
3. Utilize taxa de aprendizagem 2e-4 para QLoRA, 5e-5 para LoRA fp16
4. Defina lora_dropout=0,05
5. Trem para 1-3 épocas (mais riscos de sobreajuste)
6. Avalie cada 100 passos num conjunto de tempo
7. Salvar pontos de controlo e escolher os melhores por perda de avaliação

## Erros comuns

- Formação durante demasiadas épocas (overfitting após épocas 2-3 em pequenos conjuntos de dados)
- Utilizando a mesma taxa de aprendizagem que a perfeita sintonização completa (LoRA precisa de LR mais elevado)
- Esquecer a configuração do token do pad (causa perdas de NaN com os modelos Llama)
- Não congelamento do modelo base (desvantagem do objectivo do LoRA)
- Avaliação apenas com base em dados de formação (sempre 10% a 20% para avaliação)
- Salto da linha de base de engenharia de prompt (ajuste de problemas que o prompt já resolve)

## Verificação da qualidade

Após o treino, compare em mais de 200 exemplos:
1. Modelo base com melhor ponta (linha de base)
2. Modelo base com adaptador LoRA (o seu modelo de sintonização)
3. GPT-4 ou Claude com o mesmo comando (loft)

Se o modelo LoRA não ultrapassar a linha de base solicitada, os dados de formação ou a configuração necessitam de trabalho, não de mais cálculo.

## Gestão de adaptadores

- Manter os adaptadores separados para a prestação de várias tarefas (adaptadores de troca por pedido)
- Adaptadores de fusão em pesos base para implantação de tarefas únicas
- Armazenar adaptadores no Hugging Face Hub (10-100 MB, fácil de versão e compartilhamento)
- Resultados dos modelos de ensaio combinados correspondem aos resultados não combinados antes da implantação
- Use TIES-Fusion ou DARE para combinar vários adaptadores em um só

## Formação em desmantelamento de erros

Se a perda não diminuir:
1. Verifique a taxa de aprendizagem (muito baixa para o LoRA, tente 2e-4)
2. Verifique se as camadas LoRA estão realmente recebendo gradientes
3. Confirmar que os pesos do modelo base estão congelados
4. Verificar a formatagem dos dados (o tokenizer deve corresponder ao formato esperado do modelo)

Se a perda diminuir mas a qualidade da avaliação for ruim:
1. Questões de qualidade dos dados de formação (descarga, descarga)
2. Oficinação excessiva (reduzir épocas, aumentar o abandono, adicionar mais dados)
3. Módulos-alvo errados (adicionar camadas de MLP para tarefas complexas)
4. Classificação muito baixa (tente r=32 ou r=64)
