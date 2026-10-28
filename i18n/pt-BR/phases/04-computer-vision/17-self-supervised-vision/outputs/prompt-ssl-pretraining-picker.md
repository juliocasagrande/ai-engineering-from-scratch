---
name: prompt-ssl-pretraining-picker
description: Pick SimCLR / MAE / DINOv2 given dataset size, compute, and downstream task
phase: 4
lesson: 17
---

É um selector de pré-treino auto-supervisionado.

## Input

- `unlabelled_images`: quantas estão disponíveis
- `backbone`ResNet: ViT
- `downstream_task`Classificação , detecção , segmentação , recuperação .
- `compute_gpu_hours`: orçamento aproximado de formação

## Precedência

Avalie as regras de cima para baixo; primeiro jogo vence. Regras anteriores curto-circuito posteriores. Todas as fronteiras numéricas são não-superposições: uma regra que diz `< 1,000,000`Nunca dispara para o valor exato de 1.000.000  que vai para a próxima banda.

## Decisão

1. `compute_gpu_hours < 200`-> **do not run SSL from scratch**Nenhuma receita SSL converge nesse orçamento.`method: none, use_pretrained: DINOv2, reason: compute_budget_too_small`- Não .

2. `unlabelled_images < 100,000`-> **do not run SSL**Um posto de controlo pré-treinado domina tudo o que se pode treinar aqui.`method: none, use_pretrained: DINOv2`- Não .

3. `downstream_task == retrieval`-> **DINOv2**. A separabilidade linear das características DINOv2 é a mais forte entre os espinhos; esta regra invade todas as regras de espinhos que seguem.

4. `downstream_task in [detection, segmentation]`E ...`backbone == ViT`-> **MAE**As metas de reconstrução densas alinham-se com a previsão densas.

5. `downstream_task in [detection, segmentation]`E ...`backbone == ResNet`-> **DenseCL**(contrastante com cabeça de projecção densa) ou **PixPro**Se nenhum estiver disponível na sua pilha, volte para **MoCo v3**e documentar a descoincidência.

6. `backbone == ResNet`(resistentes casos de classificação) -> **MoCo v3**- Não .

7. `backbone == ViT`E ...`unlabelled_images >= 100,000,000`E ...`compute_gpu_hours >= 5,000`-> **DINOv2-style**Baixa para MAE se o computador cair abaixo de 5.000 horas de GPU.

8. `backbone == ViT`E ...`1,000,000 <= unlabelled_images < 100,000,000`E ...`compute_gpu_hours >= 1,000`-> **MAE**- Não .

9. `backbone == ViT`E ...`100,000 <= unlabelled_images < 1,000,000`-> **use a pretrained DINOv2 checkpoint**Não re-treinar de novo.`method: none, use_pretrained: DINOv2`- Não .

## Output

```
[pretraining]
  method:          SimCLR | MoCo v3 | DINO | DINOv2 | MAE | DenseCL | PixPro | none
  use_pretrained:  <checkpoint name if method == none>
  epochs:          <int if method != none>
  batch:           <int>
  aug:             <list>
  eval:            linear_probe | kNN | fine-tune

[warnings]
  - <compute headroom>
  - <batch size floor for contrastive methods>
  - <downstream mismatch when a fallback was selected>
```

## Regras

- Nunca recomendamos SimCLR com tamanho de lote < 1024; em lotes menores, a estrutura de fila do MoCo se acelera mais rapidamente e aterrissa com qualidade semelhante.
- Quando ?`compute_gpu_hours`se for fornecido, incluir sempre uma verificação de sanidade de uma linha contra as faixas conhecidas de horas de GPU do método escolhido; indicar explícitamente o orçamento insuficiente.
- Não misture "emite um método" e "utilize pré-entrenado" na mesma linha.`none`E o posto de controlo pré-treinado é a saída.
- Se um caminho de retorno na regra 5 foi tomado (ResNet + tarefa densa), note a desatividade teórica para que o leitor saiba por que uma variante densa-específica teria sido preferível.
