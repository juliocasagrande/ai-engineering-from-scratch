---
name: skill-conv-shape-calculator
description: Walk a CNN spec layer by layer and report output shape, receptive field, and parameter count for every block
version: 1.0.0
phase: 4
lesson: 2
tags: [computer-vision, cnn, architecture, debugging]
---

# Calculador de forma conv

Um ajudante determinista para planejar ou depurar uma CNN. Dada uma forma de entrada e uma lista de especificações de camadas, formas de rastreamento, campos receptivos e parâmetros contam sem executar o modelo.

## Quando utilizar

- Está a projetar uma nova CNN e quer verificar todas as amostras abaixo em um tamanho limpo.
- Lendo um papel e traduzindo a sua tabela de arquitetura em código.
- Uma espinha dorsal pré-treinada bate com uma desajuste de forma na cabeça do classificador e você precisa saber qual camada mudou o tamanho espacial.
- Comparar duas espinhas sobre eficiência dos parâmetros antes do treino.

## Input

- `input_shape`- Não .`(C, H, W)`- Não .
- `layers`: lista ordenada de dictos de camadas.
  - `{type: "conv", c_out, k, s, p, groups=1, bias=true}`
  - `{type: "pool", mode: "max"|"avg", k, s, p=0}`
  - `{type: "adaptive_pool", out_h, out_w}`
  - `{type: "flatten"}`
  - `{type: "linear", out_features, bias=true}`

## Passo

1. **Initialise trace**com`(C, H, W)`, campo receptivo `1`, passo eficaz `1`, parâmetros cumulativos `0`- Não .

2. **For each layer**, atualizada na seguinte ordem:
   - Computação`C_out`(conv/linear), ou transportar `C_in`através (poalha).
   - Compute a saída espacial usando `(H + 2P - K) / S + 1`para condomínios e piscinas, `out_h/out_w`para piscina adaptativa, `(1, 1)`para a forma de saída plana `(C * H * W, 1, 1)`antes do linear e escalar `1x1`para linear.
   - Atualizar o campo receptivo e o passo eficaz:
     - Conv/pool: `RF_new = RF_old + (K - 1) * effective_stride`- Não .`effective_stride *= S`- Não .
     - Piscinas adaptativas: tratem-se como piscinas com efetividade `S = H_in / out_h`(Rondão para baixo). `RF_new = RF_old + (H_in - 1) * effective_stride_old`- O que é ?`effective_stride *= S`. Observe que a RF da piscina adaptativa é igual à extensão espacial anterior.
     - Planos / lineares: RF e passo efetivo não são mais significativos; congelar-os aos valores antes do plano e omitir de linhas subsequentes.
   - Parâmetros de computação:
     - Conv: `C_out * (C_in / groups) * K * K + (C_out if bias else 0)`- Não .
     - Linear: `out_features * in_features + (out_features if bias else 0)`- Não .
     - Polar e plano: 0.

3. **Detect problems**e os sinalizar:
   - Dimensões de saída não inteiras (passo/padding desalinhado).
   - `H_out <= 0`Antes do fim da pilha.
   - Campo receptor superior ao tamanho da entrada (computação perdida possível após esse ponto).
   - Subitamente, 10x salta em parâmetros por camada que sugerem o plano de canal errado.

4. **Report**como tabela única:

```
idx  layer                C_in  C_out  K  S  P  H_out  W_out  RF    params     cum_params
1    conv 3x3 s=1 p=1     3     32     3  1  1  224    224    3     896        896
2    conv 3x3 s=2 p=1     32    64     3  2  1  112    112    7     18,496     19,392
3    pool max 2x2         64    64     2  2  0  56     56     11    0          19,392
...
```

5. **Summary line**: final `(C, H, W)`, campo de recepção final, parâmetros totais, avisos.

## Regras

- Sempre retorne números inteiros para tamanhos espaciais. Se a fórmula produz um não inteiro, sinalize como um erro e não pisar silenciosamente.
- Quando ?`groups > 1`, verificar`C_in % groups == 0`E ...`C_out % groups == 0`; caso contrário, erro.
- Para con-`groups == C_in`), etiquetar no `layer`Coluna para que o leitor veja por que os parâmetros são baixos.
- Se o utilizador fornecer BatchNorm ou camadas de ativação, ignore-as para efeitos de forma, mas adiante os parâmetros (`2 * C`por BatchNorm).
- Nunca adivinhe as definições padrão para campos faltantes.`k`- Não .`s`- Não .`p`Em todas as convas e piscinas.
