---
name: skill-rectified-flow-trainer
description: Write a complete rectified-flow training loop with AdaLN DiT and Euler sampling
version: 1.0.0
phase: 4
lesson: 23
tags: [diffusion, rectified-flow, DiT, training]
---

# Treinador de fluxo rectificado

Produzir um ciclo de treinamento limpo e mínimo que treinaria com sucesso um pequeno DiT com fluxo rectificado em qualquer conjunto de dados de tensores de imagem.

## Quando utilizar

- Reprodução dos objectivos de formação SD3 / FLUX em pequena escala.
- Compartilhamento de fluxo rectificado versus DDPM com base nos mesmos dados.
- Construção de um modelo de fluxo rectificado personalizado para um domínio não padrão (médico, satélite).

## Input

- `model`: um `nn.Module`- Tomei .`(x, t)`E devolver uma velocidade prevista.
- `dataset`: um iterável de imagens limpas no domínio do modelo.
- `optimizer`: AdamW com `lr=1e-4`- Não .`weight_decay=0.01`- Não .`betas=(0.9, 0.99)`- Não .
- `scheduler`: cosin com aquecimento, padrão 1000 passos de aquecimento.

## Passo de formação

```python
def rectified_flow_train_step(model, x0, optimizer, device):
    model.train()
    x0 = x0.to(device)
    n = x0.size(0)
    t = torch.rand(n, device=device)                     # uniform in [0, 1]
    epsilon = torch.randn_like(x0)
    x_t = (1 - t[:, None, None, None]) * x0 + t[:, None, None, None] * epsilon
    target_v = epsilon - x0                              # velocity target
    pred_v = model(x_t, t)
    loss = F.mse_loss(pred_v, target_v)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    return loss.item()
```

## Amostragem (Euler)

```python
@torch.no_grad()
def sample(model, shape, steps=20, device="cpu"):
    model.eval()
    x = torch.randn(shape, device=device)
    dt = 1.0 / steps
    t = torch.ones(shape[0], device=device)
    for _ in range(steps):
        v = model(x, t)
        x = x - dt * v
        t = t - dt
    return x
```

## Dicas

- Utilização`torch.rand`uniforme`t`; amostragem ponderada de `t`A ajuda é ligeira, mas não é necessária para começar.
- A EMA dos pesos dos modelos é prática padrão; manter `ema_model`com decomposição de 0,9999.
- Orientação sem classificador para modelos condicionais: com 10% de probabilidade, substituir o condicionamento por um embuxo vazio/nulo durante o treinamento; em combinação de inferências `v_uncond + w * (v_cond - v_uncond)`com`w`- Por volta de 3 a 5.
- Para o treinamento de estilo LDM (FLUX, SD3), todo o ciclo é executado num espaço latente da AEV; o`x0`acima é realmente`VAE.encode(image)`- Não .
- Convergência típica em um conjunto de dados de brinquedos 32x32, 2000-5000 passos.

## Relatório

```
[rectified flow training]
  steps:        <int>
  final loss:   <float>
  ema decay:    <float>
  vae?:         yes | no
  cfg dropout:  <fraction>

[sampling]
  default steps: 20
  schnell / turbo target: 4
  full quality reference: 50+ (for comparison only)
```

## Regras

- Nunca traçar fluxo rectificado com um alvo de velocidade de imagem-espaço em RGB `uint8`dados; normalize para zero média, variância unitária primeiro.
- Sempre registar perdas de treinamento por tempo-passo-bucket; se os primeiros tempos (quase 0) tiverem perdas maiores do que os últimos (quase 1) a parametrização de velocidade é provavelmente mal programada.
- Não misture o alvo de velocidade de fluxo rectificado com o alvo de ruído DDPM no mesmo ciclo de treinamento; escolha um.
- Use o treinamento bfloat16 em GPUs Ampere +; float16 às vezes produz graus NaN em fluxo rectificado devido à magnitude de velocidade.
