---
name: checkpoint-save-resume
description: Pontos de controlo atômicos, fragmentados, com captura completa de GNR, para que uma corrida morta retoma no meio da época com a mesma trajetória de perda.
version: 1.0.0
phase: 19
lesson: 47
tags: [training, durability, resume, sharded-state]
---

## Quando utilizar

Qualquer treinamento que dure mais do que o tapete do relógio do cluster, qualquer execução que tenha de sobreviver a um reinicio de nós, qualquer modelo muito grande para uma única carga útil.

## Forma da carga útil

```python
{
  "schema": "ckpt.v1",
  "model": model.state_dict(),
  "optimizer": opt.state_dict(),
  "scheduler": sched.state_dict(),
  "state": {"step": int, "epoch": int, "batch_in_epoch": int, "losses": [float, ...]},
  "rng": {"python": ..., "numpy": ..., "torch_cpu": ..., "torch_cuda": ...},
  "wall_saved_at": time.time(),
}
```

## Salvo atômico

1. Escreva a carga útil para um arquivo temporário único no mesmo diretório do alvo.
2. `os.replace(tmp, target)` para trocar atomicamente.
3. Nunca escreva directamente ao nome do alvo.

## Descrição em fragmentos

- `model.shard-NNN.pt` por fragmento, rotulagem de teclas ou divisão por grupo de parâmetros.
- `meta.pt` O motor de transporte de veículos de transporte aéreo é um motor de transporte aéreo de veículos de transporte aéreo.
- `index.json` Carregas `sha256` Por cada fragmento e por `meta.pt`- Não .
- O carregador verifica cada hash antes de se fundir e rejeita os caminhos de fragmentos fora do diretório de pontos de verificação.
- Carregar todos os arquivos com `torch.load(path, map_location="cpu", weights_only=True)`Mantenha o estado de RNG como listas simples para sobreviver ao carregador de peso.

## Resumo de meados da época

- Salvar `(epoch, batch_in_epoch)` ao lado `step`- Não .
- Restaurar o estado de RNG antes do primeiro lote da época retomada.
- Avança rápido o gerador para os lotes consumidos.

## Modos de falha

- Renomeamento de dispositivo cruzado: não atômico, perder o arquivo anterior.
- Esquecer RNG: perdas retomadas divergem da linha de base.
- Esquecer o estado do optimizador: o próximo passo está a espreitar.
- Aponte o ponto de controlo errado: mantenha o último K mais o melhor.
- Carregamento com `weights_only=False`A: `.pt` O ficheiro é um problema, por isso um ponto de controlo não confiável executa o código à carga.
