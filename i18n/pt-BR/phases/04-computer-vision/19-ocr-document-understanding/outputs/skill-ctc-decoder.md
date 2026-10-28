---
name: skill-ctc-decoder
description: Escrever codificadores CTC de busca de raio e ganância desde o zero, incluindo a normalização de comprimento
version: 1.0.0
phase: 4
lesson: 19
tags: [ocr, ctc, decoding, sequence-models]
---

# Descódigo CTC

Produza duas rotinas de decodificação para as saídas CTC: gananciosa (rápida) e feixe (melhor nas entradas ruidosas).

## Quando utilizar

- A execução de inferência OCR em saídas CRNN personalizadas.
- Compartilhar um modelo de OCR pré-treinado com diferentes decodificadores.
- Implementar uma simples busca de feixe sem puxar o código ctc.

## Input

- `log_probs`: (T, N, C) log-softmax sobre vocab (índice 0 = branco por convenção).
- `vocab`: lista de caracteres C.
- `beam_width` (só o feixe): normalmente 5 a 10.

## Descódigo ganancioso

```python
def greedy_ctc_decode(log_probs, vocab, blank=0):
    preds = log_probs.argmax(dim=-1).transpose(0, 1).cpu().tolist()
    out = []
    for seq in preds:
        decoded = []
        prev = None
        for idx in seq:
            if idx != prev and idx != blank:
                decoded.append(vocab[idx])
            prev = idx
        out.append("".join(decoded))
    return out
```

## Descódigo de busca de feixe

```python
import heapq
import math

def beam_ctc_decode(log_probs, vocab, beam_width=5, blank=0):
    T, N, C = log_probs.shape
    lp = log_probs.cpu()
    results = []
    for n in range(N):
        beams = {("",): (0.0, -math.inf)}  # (prefix_tuple) -> (p_blank, p_nonblank)
        for t in range(T):
            logits_t = lp[t, n]
            new_beams = {}
            for prefix, (p_b, p_nb) in beams.items():
                for c in range(C):
                    p = logits_t[c].item()
                    if c == blank:
                        nb = p_b + p
                        nnb = p_nb + p
                        upd = new_beams.get(prefix, (-math.inf, -math.inf))
                        new_beams[prefix] = (
                            _logsumexp(upd[0], _logsumexp(nb, nnb)),
                            upd[1],
                        )
                    else:
                        last = prefix[-1] if prefix else ""
                        char = vocab[c]
                        if char == last:
                            # Case 1: stay on same prefix (collapse from p_nb)
                            upd = new_beams.get(prefix, (-math.inf, -math.inf))
                            new_beams[prefix] = (upd[0], _logsumexp(upd[1], p_nb + p))
                            # Case 2: extend prefix via blank-separated repeat ("a_a" -> "aa")
                            new_prefix = prefix + (char,)
                            upd = new_beams.get(new_prefix, (-math.inf, -math.inf))
                            new_beams[new_prefix] = (upd[0], _logsumexp(upd[1], p_b + p))
                        else:
                            new_prefix = prefix + (char,)
                            upd = new_beams.get(new_prefix, (-math.inf, -math.inf))
                            nb = _logsumexp(p_b, p_nb) + p
                            new_beams[new_prefix] = (upd[0], _logsumexp(upd[1], nb))
            beams = dict(heapq.nlargest(
                beam_width,
                new_beams.items(),
                key=lambda kv: _logsumexp(kv[1][0], kv[1][1]),
            ))
        best = max(beams.items(), key=lambda kv: _logsumexp(kv[1][0], kv[1][1]))[0]
        results.append("".join(best))
    return results


def _logsumexp(a, b):
    if a == -math.inf: return b
    if b == -math.inf: return a
    m = max(a, b)
    return m + math.log(math.exp(a - m) + math.exp(b - m))
```

## Regras

- O índice em branco no CTC é 0 por convenção no PyTorch's `nn.CTCLoss`- Não .
- A busca de feixe melhora a precisão em entradas de baixa confiança; nas entradas limpas a melhoria é < 1% CER.
- Nunca poda o feixe abaixo de 5; o comércio de latência de precisão aplania abaixo disso.
- Ao executar uma pesquisa de feixe dentro de um orçamento de latência apertado, desça para o ganancioso; o impacto de qualidade é pequeno na maioria dos dados de produção OCR.
- Para vocabulários grandes (CJK com mais de 3000 caracteres), passe para `ctcdecode` (C++) em vez da versão Python pura acima; o feixe Python rapidamente se torna o gargalo de engarrafamento.
