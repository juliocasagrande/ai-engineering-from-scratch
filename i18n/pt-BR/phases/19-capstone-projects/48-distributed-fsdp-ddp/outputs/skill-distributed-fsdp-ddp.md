---
name: distributed-fsdp-ddp
description: Bring up multi-rank training with a from-scratch DDP wrapper and an FSDP parameter sharding sketch on the gloo or nccl backend.
version: 1.0.0
phase: 19
lesson: 48
tags: [distributed, ddp, fsdp, collectives]
---

## Quando utilizar

O modelo cabe em um dispositivo, mas você precisa de mais capacidade de produção (DDP). O modelo não cabe em um dispositivo (FSDP).

## Fazer aparecer o grupo de processos

```python
os.environ["MASTER_ADDR"] = "127.0.0.1"
os.environ["MASTER_PORT"] = str(port)
dist.init_process_group(backend="gloo", rank=rank, world_size=world_size)
```

`gloo`é o backend da CPU; `nccl`Ambos implementam a mesma superfície coletiva.

## Envolver o modelo

1. Na posição 0, construam o modelo da sua semente.
2. Envolva-o com a concha DDP.
3. O concha é.`__init__`chamadas`dist.broadcast(p.data, src=0)`para cada parâmetro e buffer.
4. Depois de cada`loss.backward()`O treinador chama .`sync_grads()`- Não .
5. `sync_grads()`chamadas`dist.all_reduce(p.grad, op=SUM)`E ...`p.grad.div_(world_size)`- Não .
6. Otimizador passo em cada posição com o mesmo gradiente médio.

## Parâmetros de fragmentos (esquisa do FSDP)

1. Aplanar cada parâmetro, pad para um múltiplo de `world_size`- Não .
2. Mantenha o seu fragmento localmente; solte o resto.
3. Antes de avançar,`dist.all_gather(...)`Para reconstruir o tensor completo em cada nível.
4. Depois de avançar, solte o tensor completo.

## Modos de falha

- Salto da transmissão: as fileiras começam a partir de diferentes intros, divergem silenciosamente.
- Esquecer de dividir após a soma: gradientes escalados por world_size, passo otimizador muito grande.
- Usando renomeamento de dispositivos cruzados para pontos de controlo: não atômico; mesma lição 47 armadilha.
- Misturar tensores CPU e CUDA no mesmo colectivo: desajuste de backend, pendências de execução.
