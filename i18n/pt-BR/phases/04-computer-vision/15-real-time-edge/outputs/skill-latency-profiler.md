---
name: skill-latency-profiler
description: Escreva um script completo de benchmarking de latência com aquecimento, sincronização, percêntulos e rastreamento de memória
version: 1.0.0
phase: 4
lesson: 15
tags: [edge, deployment, profiling, benchmarking]
---

# Profilador de latência

Produzir um índice de latência disciplinado para qualquer modelo PyTorch.

## Quando utilizar

- Comparar várias espinhas candidatos antes de escolher uma para implantar.
- Antes e depois da quantificação ou poda.
- Após uma alteração do tempo de execução (eager vs ONNX vs TensorRT).
- Gerenar um relatório de preparação para a implantação.

## Input

- `model`Pitola `nn.Module`- Não .
- `input_shape`- Não . `(1, 3, 224, 224)`- Não .
- `device`- Não . `cpu` - Não. `cuda` - Não. `mps`- Não .
- `warmup`- Default 10.
- `iters`- Default 100.

## Cheques

### 1. Calor
Executa o modelo `warmup` Capta a compilação JIT de primeira linha e efeitos de cache frio.

### 2. Sincronização
Para `cuda`- Não . `torch.cuda.synchronize()` antes e depois de cada passagem cronometrada.
Para `mps`- Não . `torch.mps.synchronize()`- Não .

### 3. - O tempo
Utilização `time.perf_counter()` Para a medição de relógios de parede.

### 4. Percentiles
Organizar a lista completa de horários. `p50, p90, p95, p99, mean, std`- Não .

### 5. Memória
Para `cuda`- Não . `torch.cuda.max_memory_allocated()` após a corrida e subtrair qualquer linha de base.
Para `cpu`, uso `tracemalloc` ou `psutil.Process().memory_info().rss` Antes e depois.

### 6. Escavação em lote
Repetir opcionalmente o índice de referência para `batch_size in [1, 4, 16, 32]` Para revelar troca de rendimento versus latência.

## Modelo de saída

```python
import time
import torch
import psutil, os

def profile(model, input_shape, device="cpu", warmup=10, iters=100):
    proc = psutil.Process(os.getpid())
    baseline_rss = proc.memory_info().rss / 1e6

    model = model.to(device).eval()
    x = torch.randn(input_shape, device=device)

    def sync():
        if device == "cuda":
            torch.cuda.synchronize()
        elif device == "mps":
            torch.mps.synchronize()

    with torch.no_grad():
        for _ in range(warmup):
            model(x)
        sync()
        if device == "cuda":
            torch.cuda.reset_peak_memory_stats()

        times = []
        for _ in range(iters):
            sync()
            t0 = time.perf_counter()
            model(x)
            sync()
            times.append((time.perf_counter() - t0) * 1000)

    times.sort()
    mean = sum(times) / len(times)
    std  = (sum((t - mean) ** 2 for t in times) / len(times)) ** 0.5

    def pct(p):
        idx = max(0, min(len(times) - 1, int(len(times) * p) - 1))
        return times[idx]

    report = {
        "p50_ms":  pct(0.50),
        "p90_ms":  pct(0.90),
        "p95_ms":  pct(0.95),
        "p99_ms":  pct(0.99),
        "mean_ms": mean,
        "std_ms":  std,
        "rss_mb":  proc.memory_info().rss / 1e6 - baseline_rss,
    }
    if device == "cuda":
        report["peak_cuda_mb"] = torch.cuda.max_memory_allocated() / 1e6

    return report
```

## Regras

- Sempre se aqueça; nunca confie num primeiro momento.
- Percentiles, não significa  um único outlier pode dobrar a média, mas mal mover p50.
- Use a mesma forma de entrada_forma que a produção; a latência em 224x224 não é a latência em 384x384.
- Para a CUDA, nunca omita `torch.cuda.synchronize()`Os números não têm sentido sem ele.
- Registre a versão da tocha, a versão CUDA e o nome do dispositivo ao lado dos números  que deixam de ser comparáveis de outra forma.
