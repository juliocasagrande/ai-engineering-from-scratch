---
name: skill-noise-schedule-designer
description: Produir um cronograma beta linear, cosino ou sigmoide dado T e nível de corrupção alvo, mais gráfico SNR
version: 1.0.0
phase: 4
lesson: 10
tags: [computer-vision, diffusion, noise-schedule, training]
---

# Projeto de programação de ruído

Um cronograma beta controla a quantidade de sinal retida em cada etapa de difusão.

## Quando utilizar

- Começando uma nova formação de difusão e escolhendo T e beta.
- Descargar um modelo de difusão que produz amostras borbulhas (orágio muito agressivo) ou não aprenda a estrutura (orágio muito leve).
- Comparar desenhos entre documentos que relatam diferentes horários.

## Input

- `T`: número de etapas temporais, normalmente entre 100 e 1000.
- `type`O cosino sigmoide.
- `target_alpha_bar_final`: fração do sinal para manter em t=T, padrão 0,001 (99,9% corrompo).
- Opcional `image_resolution`  As imagens maiores beneficiam de horários que corromperam mais lentamente (horários cozinhos ou mudados).

## Formulhas de programação

### Linear
```
beta_t = beta_start + (beta_end - beta_start) * (t - 1) / (T - 1)
```
Default: beta_start=1e-4, beta_end=0,02 (papel DDPM).

### Cosine (Nichol & Dhariwal, 2021)
```
alpha_bar_t = cos^2((t/T + s) / (1 + s) * pi/2)
beta_t = 1 - alpha_bar_t / alpha_bar_{t-1}
```
S = 0,008. Mantém o sinal por mais tempo; melhor em baixa contagem de passos.

### Sigmoide
```
alpha_bar_t = 1 / (1 + exp(k * (t/T - 0.5)))
```
K = 6 a 12. Boa base média; usada por algumas variantes SDXL.

## Passo

1. Calcule betas por fórmula.
2. Precomputação `alphas`- Não . `alphas_cumprod`- Não . `sqrt_alphas_cumprod`- Não . `sqrt_one_minus_alphas_cumprod`- Não .
3. Calcule SNR_t = alpha_bar_t / (1 - alpha_bar_t); produz um resumo do SNR-over-time.
4. Verificar `alphas_cumprod[T-1]` está dentro de 10% do `target_alpha_bar_final`; ou sintonizar beta_end (linear), s (cosino) ou k (sigmoide) e retry.
5. Relata três pontos de controlo:
   - `t=T*0.25`  Corrupção precoce
   - `t=T*0.5`  No meio do caminho
   - `t=T*0.75`  Próximo final

## Relatório

```
[schedule]
  type:   <name>
  T:      <int>
  beta_start: <float>   beta_end: <float>

[signal retention]
  t=0.25T:  alpha_bar=<X>  SNR=<X>
  t=0.5T:   alpha_bar=<X>  SNR=<X>
  t=0.75T:  alpha_bar=<X>  SNR=<X>
  t=T:      alpha_bar=<X>  SNR=<X>

[warnings]
  - <if alpha_bar collapses before 0.75T>
  - <if beta_end produces NaN in log-SNR>
```

## Regras

- Nunca emitir um horário com qualquer `alpha_bar_t <= 0`; valores de sujeição abaixo de 1e-5 e aviso.
- O cosine é a recomendação padrão para a amostragem com baixo número de etapas (< 30 etapas).
- Linear é o padrão para `quality_target == research`  As linhas de base do MDPD são comunicadas com calendários lineares.
- Quando `image_resolution > 256`, recomendam mudar o cronograma (Chen, 2023) para reter mais sinal em alta resolução.
