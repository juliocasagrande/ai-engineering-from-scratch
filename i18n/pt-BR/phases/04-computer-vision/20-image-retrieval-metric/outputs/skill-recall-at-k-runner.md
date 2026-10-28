---
name: skill-recall-at-k-runner
description: Write a clean evaluation harness for recall@K with train/val/gallery splits and proper data contract
version: 1.0.0
phase: 4
lesson: 20
tags: [retrieval, evaluation, recall, faiss]
---

# Recall@K Runner

Transforme uma pasta de imagens de consulta e galeria, além de rótulos, em um número recall@K reprodutível.

## Quando utilizar

- Primeiro indicador de recuperação para uma nova espinha dorsal.
- Seguimento da qualidade de incorporação em épocas de sintonia fina.
- Comparar dois sistemas de recuperação no mesmo conjunto de dados.

## Input

- `query_images`: lista de caminhos.
- `gallery_images`: lista de caminhos (a consulta pode ou não se sobrepor).
- `query_labels`- Não .`gallery_labels`: identificação de classe ou instância.
- `encoder_fn`: chamável `image -> embedding`(precomputado ou em directo).
- `ks`: lista como `[1, 5, 10]`- Não .

## Passo

1. Encode todas as imagens de galeria uma vez, salva-as como um conjunto de galerias.
2. Encode todas as imagens de consulta.
3. L2 - normalizar os dois conjuntos de inserções.
4. Para cada consulta, calcular similaridade com todos os itens da galeria.
5. Classificar descendo, tomar o máximo.
6. Para cada K, verifique se qualquer um dos itens da galeria de cima K compartilha o rótulo da consulta.
7. Relatório `recall@K = fraction of queries that had at least one correct neighbour in top K`- Não .

## Modelo de saída

```python
import numpy as np
from sklearn.preprocessing import normalize

def encode_all(images, encoder_fn, batch=32):
    out = []
    for i in range(0, len(images), batch):
        embs = encoder_fn(images[i:i + batch])
        out.append(embs)
    return np.concatenate(out)


def recall_at_k(query_emb, gallery_emb, q_labels, g_labels,
                ks=(1, 5, 10), query_ids=None, gallery_ids=None):
    if len(query_emb) == 0 or len(gallery_emb) == 0:
        return {f"recall@{k}": 0.0 for k in ks}

    g_label_set = set(g_labels.tolist())
    keep = np.array([lbl in g_label_set for lbl in q_labels])
    if not keep.any():
        return {f"recall@{k}": 0.0 for k in ks}

    q_emb_f = query_emb[keep]
    q_lab_f = q_labels[keep]
    q_id_f = query_ids[keep] if query_ids is not None else None

    q = normalize(q_emb_f)
    g = normalize(gallery_emb)
    sims = q @ g.T

    if q_id_f is not None and gallery_ids is not None:
        self_mask = q_id_f[:, None] == gallery_ids[None, :]
        sims = np.where(self_mask, -np.inf, sims)

    top_k_max = min(max(ks), g.shape[0])
    if top_k_max <= 0:
        return {f"recall@{k}": 0.0 for k in ks}

    top = np.argpartition(-sims, top_k_max - 1, axis=1)[:, :top_k_max]
    sorted_top = np.take_along_axis(
        top, np.argsort(-sims[np.arange(len(q))[:, None], top], axis=1), axis=1
    )
    out = {}
    for k in ks:
        k_eff = min(k, top_k_max)
        hits = np.any(g_labels[sorted_top[:, :k_eff]] == q_lab_f[:, None], axis=1)
        out[f"recall@{k}"] = float(hits.mean())
    return out


def evaluate(query_images, query_labels, gallery_images, gallery_labels, encoder_fn, ks=(1, 5, 10)):
    q_emb = encode_all(query_images, encoder_fn)
    g_emb = encode_all(gallery_images, encoder_fn)
    return recall_at_k(q_emb, g_emb, np.array(query_labels), np.array(gallery_labels), ks)
```

## Relatório

```
[evaluation]
  num queries:   <int>
  num gallery:   <int>
  embedding_dim: <int>

[recall]
  recall@1:  <float>
  recall@5:  <float>
  recall@10: <float>
```

## Regras

- Normalizar as incorporações antes de calcular a semelhança; FAISS IndexFlatIP em vetores normalizados é igual a cosino.
- Quando o rótulo de verdade fundamental de uma consulta estiver ausente da galeria, excluí-lo; caso contrário, a recall é trivialmente limitada abaixo de 1.
- Se a consulta e a galeria se sobrepõem, exclui a própria consulta de seu próprio top-K ou você mede auto-similaridade, não recuperação.
- Para o`num_queries > 10,000`, batch o matmul de semelhança para evitar OOM.
