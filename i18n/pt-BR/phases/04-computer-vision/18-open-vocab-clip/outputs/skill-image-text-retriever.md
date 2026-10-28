---
name: skill-image-text-retriever
description: Build an image embedding index with any CLIP checkpoint; support query-by-text and query-by-image
version: 1.0.0
phase: 4
lesson: 18
tags: [clip, retrieval, faiss, zero-shot]
---

# Retirador de imagem-texto

Transforme uma pasta de imagens em um índice pesquisável usando embutidos CLIP.

## Quando utilizar

- Construir uma pesquisa de imagem de tiros zero num catálogo interno.
- Desduplicar imagens quase idênticas, incorporando distância.
- Construir um componente rápido "encontrar semelhante" sem um conjunto de dados rotulado.

## Input

- `image_folder`: directório de arquivos de imagem.
- `clip_model`Abraços: Face ID como`openai/clip-vit-base-patch32`ou `google/siglip-base-patch16-224`- Não .
- `index_type`Flat IVF HNSW.
- `embedding_dim`: deduzido do modelo.

## Passo

1. Carregar o modelo CLIP e o pré-processador.
2. Encode em batches todas as imagens na pasta. Salve as incorporações como (N, D) float32 + lista de nomes de arquivos.
3. Construir um índice FAISS sobre os incorporados. Use o produto interno em vetores normalizados L2 para a semelhança cosínica.
4. Expor duas interfaces de consulta:
   - `search_by_text(text, k)`- Encher o texto, procurar.
   - `search_by_image(image_path, k)`- Embuchar a imagem, procurar.

## Modelo de saída

```python
import os
import glob
import numpy as np
import torch
from PIL import Image
from transformers import CLIPModel, CLIPProcessor
import faiss


class ImageTextRetriever:
    def __init__(self, model_name="openai/clip-vit-base-patch32"):
        self.model = CLIPModel.from_pretrained(model_name).eval()
        self.processor = CLIPProcessor.from_pretrained(model_name)
        self.dim = self.model.config.projection_dim
        self.index = None
        self.filenames = []

    @torch.no_grad()
    def _encode_images(self, paths, batch=16):
        embs = []
        for i in range(0, len(paths), batch):
            imgs = [Image.open(p).convert("RGB") for p in paths[i:i + batch]]
            inputs = self.processor(images=imgs, return_tensors="pt")
            out = self.model.get_image_features(**inputs)
            out = out / out.norm(dim=-1, keepdim=True)
            embs.append(out.cpu().numpy())
        return np.concatenate(embs).astype(np.float32)

    @torch.no_grad()
    def _encode_text(self, texts):
        inputs = self.processor(text=texts, return_tensors="pt", padding=True)
        out = self.model.get_text_features(**inputs)
        out = out / out.norm(dim=-1, keepdim=True)
        return out.cpu().numpy().astype(np.float32)

    def build_index(self, folder, index_type="flat"):
        exts = ("*.jpg", "*.jpeg", "*.png", "*.webp", "*.bmp")
        files = []
        for ext in exts:
            files.extend(glob.glob(os.path.join(folder, ext)))
        self.filenames = sorted(files)
        embs = self._encode_images(self.filenames)
        if index_type == "IVF":
            quantizer = faiss.IndexFlatIP(self.dim)
            nlist = min(256, max(4, len(embs) // 32))
            self.index = faiss.IndexIVFFlat(quantizer, self.dim, nlist)
            self.index.train(embs)
        elif index_type == "HNSW":
            self.index = faiss.IndexHNSWFlat(self.dim, 32, faiss.METRIC_INNER_PRODUCT)
        else:
            self.index = faiss.IndexFlatIP(self.dim)
        self.index.add(embs)

    def search_by_text(self, text, k=5):
        q = self._encode_text([text])
        dist, idx = self.index.search(q, k)
        return [(self.filenames[i], float(d)) for d, i in zip(dist[0], idx[0])]

    def search_by_image(self, image_path, k=5):
        q = self._encode_images([image_path])
        dist, idx = self.index.search(q, k)
        return [(self.filenames[i], float(d)) for d, i in zip(dist[0], idx[0])]
```

## Relatório

```
[retriever]
  model:          <name>
  num_images:     <int>
  dim:            <int>
  index_type:     flat | IVF | HNSW
  index_size_mb:  <float>
```

## Regras

- Sempre normaliza as incorporações L2 antes da indexação; o produto interno do FAISS em vetores normalizados é igual à semelhança cosínica.
- Para < 100k imagens, `IndexFlatIP`É o mais simples e rápido.
- Para 100k-10M, `IndexIVFFlat`É o padrão de troca.
- Para > 10 M, utilizar HNSW ou uma variante quantizada de produto.
- Nunca reconstruir o índice em cada consulta; inserir uma vez, pesquisar muitas vezes.
