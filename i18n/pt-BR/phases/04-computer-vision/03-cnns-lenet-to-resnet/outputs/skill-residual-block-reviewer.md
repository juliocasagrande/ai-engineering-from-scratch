---
name: skill-residual-block-reviewer
description: Revisar um bloco residual PyTorch para verificar a correcção da ligação de saltos, a colocação do BN, a ordem de ativação e o alinhamento da forma
version: 1.0.0
phase: 4
lesson: 3
tags: [computer-vision, resnet, code-review, pytorch]
---

# Revisor de blocos residuais

Um revisor focado para qualquer PyTorch `nn.Module` Aparece os quatro erros que explicam quase todas as reescrituras quebradas da ResNet.

## Quando utilizar

- Alguém escreveu um BasicBlock ou Garganta de Botelha personalizado e a perda é NaN ou a precisão está presa.
- Está a transportar um bloco de um quadro para outro e quer verificar a equivalência.
- Está a rever uma PR que altera os recursos internos da ResNet (pré-ativação, excitação, alias anti).
- Um modelo corre bem em entrada de tamanho CIFAR, mas falha na resolução ImageNet porque o atalho é errado.

## Input

- Uma definição de classe PyTorch, quer como texto fonte quer como um caminho importável.
- Opcional `variant`- Não . `basic` - Não. `bottleneck` - Não. `preact` - Não. `seblock`- Não .

## Quatro cheques

### 1. Alinhamento de forma de atalho

Para qualquer bloco com `stride != 1` ou `in_channels != out_channels`, o caminho de atalho **must** ser um módulo de correspondência de forma  tipicamente um 1x1 conv mais BN. Um nu `nn.Identity()` Neste caso, é um erro de desajuste de forma garantido no tempo de adição.

Diagnóstico:
```
[shortcut]
  detected:  nn.Identity | 1x1 Conv + BN | 1x1 Conv + BN + ReLU | other
  required:  shape-matching Conv if (stride != 1 or in_c != out_c) else Identity
  verdict:   ok | wrong | unnecessarily heavy
```

### 2. Colocação de BN em relação à adição

A adição `out + shortcut(x)` Tem de acontecer. **before** O último ReLU (pós-ativação, ResNet original) ou o último ReLU deve estar completamente ausente (pre-ativação ResNet v2). Um bloco que aplica ReLU no ramo principal e depois adiciona um atalho bruto produz uma faixa de ativação assimétrica que prejudica o treinamento.

Diagnóstico:
```
[activation order]
  pattern:  post-act (conv-BN-ReLU-conv-BN-add-ReLU) | pre-act (BN-ReLU-conv-BN-ReLU-conv-add) | other
  verdict:  ok | suspect
```

### 3. Preconceitos nas camadas de convecção

Os Convs seguidos imediatamente pela BatchNorm devem ter `bias=False`. A beta do BN já parâmetra o preconceito, de modo que um preconceito extra conv desperdiça os parâmetros e pode retardar a convergência.

Diagnóstico:
```
[bias]
  convs with BN and bias=True: <count>
  recommended fix: set bias=False on those layers
```

### 4. ReLU e autograd no local

`nn.ReLU(inplace=True)` O tensor que será adicionado ao atalho sobreescreve valores que ainda podem ser necessários para a adição residual. `inplace=True` que não é seguido por uma camada que produz um novo tensor antes da adição.

Diagnóstico:
```
[in-place]
  risky inplace ops: <list>
  fix: inplace=False before the residual add
```

## Relatório

```
[block-review]
  variant:       basic | bottleneck | preact | se | other
  shortcut:      ok | wrong | heavy
  activation:    ok | suspect
  bias-bn:       ok | <N> convs need bias=False
  in-place:      ok | <N> risky ops
  summary:       one sentence
```

## Regras

- Não reescreva o bloco, apenas informe.
- Se o bloco for correto, digamos `ok` Não há sugestões.
- Se várias coisas estão erradas, enumere-as na ordem acima (em primeiro lugar, porque é a causa mais comum de acidentes).
- Nunca marque uma variante de pré-ativação deliberada ou de excitação de compressão como errada quando o usuário a especificou.
