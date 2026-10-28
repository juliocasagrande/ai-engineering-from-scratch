---
name: skill-frame-sampler-auditor
description: Audit a video pipeline's frame sampler for off-by-one, short-clip handling, and crop consistency
version: 1.0.0
phase: 4
lesson: 12
tags: [computer-vision, video, sampling, debugging]
---

# Auditor de amostras de quadros

A amostragem de quadros é onde os canais de vídeo se quebram.

## Quando utilizar

- Estou a escrever um novo carregador de dados de vídeo.
- A precisão de reprodução de números de um papel e de formação é menor do que a relatada.
- Desfazer um modelo de vídeo cuja precisão de avaliação é instável em todas as rodadas.

## Input

- `sampler_code`: Função Python que toma (num_frames_total, T) e retorna índices T.
- `T`: comprimento do clip alvo.
- Casos de ensaio opcionais: `num_frames_total`valores a exercer (por exemplo `[3, T-1, T, T+1, 30, 300, 3000]`)).

## Cheques

### 1. Manutenção de clipes curtos
Alimentação`num_frames_total < T`Todos os índices devolvidos devem estar em`[0, num_frames_total - 1]`A política padrão é repetir o último quadro para as posições restantes.

### 2. Indices de limite
Alimentação`num_frames_total == T`Os índices devolvidos devem ser:`[0, 1, ..., T-1]`- É isso mesmo.

### 3. Distribuição uniforme
Alimentação`num_frames_total == 10 * T`Os índices devolvidos devem aumentar monotonicamente e estar aproximadamente uniformemente distribuídos.

### 4. Limite de janelas densa
Para amostragem densa, alimentação `num_frames_total == 3 * T`Os índices devolvidos devem formar uma janela contígua, nunca atravessando o fim do clip.

### 5. Determinismo
Chamem duas vezes o amostragista com as mesmas entradas e (para amostragistas deterministas) o mesmo RNG. Os índices devem corresponder.

### 6. Consistência das culturas
Se o tubo também retorna uma colheita espacial por quadro, executar o amostragem duas vezes para o mesmo clip com a mesma semente e confirmar que cada quadro usa a mesma caixa de colheita (o mesmo `(x, y, w, h)`A diferença de colheitas por quadro dentro de um clip destrói a coerência temporal e é um classico bug silencioso.

## Relatório

```
[sampler audit]
  name: <function name>
  T:    <int>

[short-clip handling]
  passed | failed (<details>)

[boundary]
  passed | failed

[uniform spacing]
  passed | failed (<stddev of gaps>)

[dense window]
  passed | failed (<details>)

[determinism]
  passed | failed

[crop consistency]
  passed | failed (<per-frame crop varies: yes/no>)

[verdict]
  ok | fix required
```

## Regras

- Nunca marque um amostragem "ok" se o tratamento de clipes curtos apresentar índices fora do alcance.
- Os amostragens densas nunca devem devolver uma janela que atravesse .`num_frames_total - 1`- Não .
- Se a amostra for estocástica (densa), testar determinismo apenas com um RNG sementeado explícito.
- Sugira, mas não corrija silenciosamente, as políticas canônicas: almofada com o último quadro, janela de sujeira para o fim, intervalos redondos de meio aberto.
