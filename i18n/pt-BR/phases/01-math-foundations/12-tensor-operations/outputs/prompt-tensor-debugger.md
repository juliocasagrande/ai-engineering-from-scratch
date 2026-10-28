---
name: prompt-tensor-debugger
description: Step-by-step debugging prompt for tensor shape errors in deep learning code
phase: 1
lesson: 12
---

Tenho um erro de forma tensorial no meu código de aprendizado profundo.

**Error message:**[Paste o erro aqui]

**My tensor shapes:**
- - Não, não.
- - Não, não.

**The operation I'm trying to do:**Descreva-o.

- Não .

Ao depurar, siga este processo exato:

**Step 1: Identify the operation type.**
Qual operação produziu o erro?
- Multiplicação de matriz / camada linear (dimensões internas devem corresponder)
- Transmissão (alignado a direita, cada dim deve ser igual ou 1)
- Concatenação (todas as dims correspondem, exceto a dimensão do gato)
- Convolução (expeita posição específica de nível e de canal)
- Reformulação (tem de ser preservada a totalidade dos elementos)

**Step 2: Write out the shape contract.**
Para a operação identificada, escrever explicitamente as formas esperadas:
```
matmul(A, B): A is (..., m, k), B is (..., k, n) -> (..., m, n)
broadcast(A, B): align right, each pair must be (equal) or (one is 1)
cat([A, B], dim=d): all dims match except dim d
Linear(in_f, out_f): input last dim must equal in_f
Conv2d(in_c, out_c, k): input must be (B, in_c, H, W)
```

**Step 3: Find the mismatch.**
Comparar as formas reais com o contrato e identificar a dimensão exata que viola a regra.

**Step 4: Choose the minimal fix.**
Escolha desta mesa:

| Symptom | Fix |
|---|---|
| Missing batch dimension | `.unsqueeze(0)` |
| Missing channel dimension | `.unsqueeze(1)` |
| Extra size-1 dimension | `.squeeze(dim)` |
| Inner dims wrong for matmul | `.transpose(-1, -2)` or check weight shape |
| Need NCHW from NHWC | `.permute(0, 3, 1, 2)` |
| Need NHWC from NCHW | `.permute(0, 2, 3, 1)` |
| Flatten spatial dims for linear | `.flatten(1)` or `.reshape(B, -1)` |
| Split heads: (B,T,D) to (B,H,T,D/H) | `.reshape(B, T, H, D//H).transpose(1, 2)` |
| Merge heads: (B,H,T,D/H) to (B,T,D) | `.transpose(1, 2).reshape(B, T, H*(D//H))` |
| Non-contiguous tensor with .view() | `.contiguous().view(...)` or use `.reshape(...)` |

**Step 5: Verify the fix.**
Mostre as formas resultantes em cada etapa. Confirme que os elementos totais são preservados em qualquer remodelação. Confirme que o contrato de forma da operação está agora satisfeito.

**Step 6: Check for silent bugs.**
Mesmo que as formas coincidam, verifique:
- A transmissão está acontecendo ao longo do eixo previsto (não acidental)
- A redução é a soma sobre a dimensão certa
- A dimensão do lote (dim 0) sobrevive ao longo de toda a passagem para a frente
- Transpose + reshape é usado (não apenas reshape) quando a ordem de dimensões é importante

Formatar a sua resposta como:
```
OPERATION: [what operation failed]
EXPECTED: [shape contract]
ACTUAL: [what shapes were provided]
MISMATCH: [which dimension, why]
FIX: [exact code]
RESULT: [shapes after fix]
```
