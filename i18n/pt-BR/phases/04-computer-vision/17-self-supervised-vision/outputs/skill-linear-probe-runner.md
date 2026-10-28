---
name: skill-linear-probe-runner
description: Write the complete linear-probe evaluation for any frozen encoder and labelled dataset
version: 1.0.0
phase: 4
lesson: 17
tags: [self-supervised, evaluation, linear-probe, pytorch]
---

# Corredor de Probe Linear

Avaliação das características de um codificador congelado através da formação de um único classificador linear no topo.

## Quando utilizar

- Comparar os pontos de controlo auto-supervisionados.
- Qualidade do recurso de rastreamento durante as épocas pré-treinamento.
- Decidir se um codificador pré-treinado é bom o suficiente para uma tarefa de baixo fluxo sem ajuste fino.

## Input

- `encoder`: congelado `nn.Module`Retorno de uma característica de dim fixa por imagem.
- `feature_dim`: dimensão da saída do codificador.
- `train_dataset`: conjunto de dados rotulado (imagem, classe_id).
- `val_dataset`: conjunto prolongado.
- `num_classes`As classes de tarefas.
- `epochs`: normalmente 100 para imagens em escala ImageNet, 50 para conjuntos de dados menores.

## Passo

1. Configurar o codificador para o modo eval e `requires_grad=False`em todos os parâmetros.
2. Extrair os conjuntos de treinamento e val uma vez.
3. Treinar um`nn.Linear(feature_dim, num_classes)`sobre as características armazenadas em cache com SGD + cronograma cosínico.
4. Hiperparametros padrão: `lr=0.1`- Não .`momentum=0.9`- Não .`weight_decay=0`- Não .`batch_size=1024`A sonda linear é surpreendentemente sensível a`lr` varrer se a precisão for pobre.
5. Relata a precisão de val no final do treino.

## Modelo de saída

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torch.optim import SGD
from torch.optim.lr_scheduler import CosineAnnealingLR

def extract(encoder, loader, device="cpu"):
    encoder.eval()
    feats, labels = [], []
    with torch.no_grad():
        for x, y in loader:
            f = encoder(x.to(device)).cpu()
            feats.append(f)
            labels.append(y)
    return torch.cat(feats), torch.cat(labels)


def linear_probe(encoder, feature_dim, train_loader, val_loader,
                 num_classes, epochs=50, lr=0.1, device="cpu"):
    for p in encoder.parameters():
        p.requires_grad = False

    f_train, y_train = extract(encoder, train_loader, device)
    f_val, y_val = extract(encoder, val_loader, device)

    head = nn.Linear(feature_dim, num_classes).to(device)
    opt = SGD(head.parameters(), lr=lr, momentum=0.9, weight_decay=0)
    sched = CosineAnnealingLR(opt, T_max=epochs)

    ds = torch.utils.data.TensorDataset(f_train, y_train)
    train_iter = DataLoader(ds, batch_size=1024, shuffle=True)

    best_val = 0.0
    for ep in range(epochs):
        head.train()
        for x, y in train_iter:
            x, y = x.to(device), y.to(device)
            loss = F.cross_entropy(head(x), y)
            opt.zero_grad(); loss.backward(); opt.step()
        sched.step()

        head.eval()
        with torch.no_grad():
            acc = (head(f_val.to(device)).argmax(-1).cpu() == y_val).float().mean().item()
        best_val = max(best_val, acc)
    return best_val
```

## Relatório

```
[linear probe]
  encoder:     <name + pretrain checkpoint>
  feature_dim: <int>
  epochs:      <int>
  best_val_top1: <float>
```

## Regras

- Nunca atualize pesos do codificador durante a sonda linear; isso seria um ajuste fino, não uma sonda.
- Precomputa recursos uma vez; Re-treinamento do codificador em cada época desperdiça 100x computação.
- Use o SGD com cronograma cosínico e sem perda de peso; Adam às vezes tem um desempenho inferior aqui.
- Esvaziar taxas de aprendizagem pelo menos uma vez por família de codificadores; o ideal varia entre os métodos SSL.
