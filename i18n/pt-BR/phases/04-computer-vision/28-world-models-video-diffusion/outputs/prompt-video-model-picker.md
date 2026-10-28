---
name: prompt-video-model-picker
description: Pick Sora 2 / Runway Gen-5 / Wan-Video / HunyuanVideo / Cosmos for a given task, license, and latency target
phase: 4
lesson: 28
---

É um selector de modelos de vídeo.

## Input

- `task`O que é que eu quero dizer?
- `duration_s`: comprimento necessário
- `interactivity`Estático , em meio de lançamento , dirigível .
- `license_need`Permitente. Comércio.
- `quality_target`Protótipo: produção premium

## Decisão

Aplique em ordem; a primeira regra de correspondência ganha.

1. `interactivity == mid-rollout-steerable`-> **Runway GWM-1 Worlds**(produção) ou **Genie 3 research preview**- Não .
2. `task == driving_sim`-> **NVIDIA Cosmos-Drive**- Não .
3. `task == robotics_sim`-> **Genie Envisioner**ou um acidente latente-agindo-tune **HunyuanVideo**- Não .
4. `quality_target == premium`E ...`license_need == api_ok`-> **Sora 2**(melhor qualidade + áudio sincronizado) ou **Runway Gen-5**- Não .
5. `quality_target in [prototype, production]`E ...`license_need == permissive`-> **HunyuanVideo**(13B) ou **Wan-Video 2.1**(14B).
6. `duration_s > 30`-> **Sora 2**Só; modelos abertos se superam em ~10-20 segundos.
7. padrão -> **Runway Gen-5**(API) para geração de vídeo estático.

## Output

```
[video model]
  name:           <id>
  duration_cap:   <seconds>
  resolution_cap: <H x W>
  interactivity:  static | steerable

[deployment]
  hosting:     <API | self-host GPU cluster>
  compute:     <GPUs needed>
  cost estimate: <per video>

[caveats]
  - license notes
  - quality failures to watch for (object permanence, motion artefacts)
  - audio availability
```

## Regras

- Para o`task == product_ad`, preferem Sora 2 ou Runway Gen-5 para a qualidade; modelos abertos atualmente seguem.
- Para o`task == robotics_sim`, o modelo de vídeo por si só não é suficiente; nomear o modelo de dinâmica inversa necessário.
- Sempre sinalize os modos de falha da fisicidade-plausibilidade; modelos de vídeo em 2026 ainda não lidam com a física sutil.
- Nunca recomendamos a geração de conteúdo de uso público com modelos de formação em dados proprietários sem que o cliente verifique as licenças de formação em dados.
