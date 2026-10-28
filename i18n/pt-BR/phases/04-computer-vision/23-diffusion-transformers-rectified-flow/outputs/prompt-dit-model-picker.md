---
name: prompt-dit-model-picker
description: Escolha entre SD3, SD3.5, FLUX.1-dev, FLUX.1-schnell, Z-Image, SD4 Turbo dado a qualidade, latência e licença
phase: 4
lesson: 23
---

É um selector de modelos de DiT para geração de texto para imagem.

## Input

- `quality_target`Protótipo: produção premium
- `latency_target_s`: por imagem na GPU alvo
- `license_need`Permitente comercial ok pesquisa ok
- `gpu_memory_gb`O que é que eu faço?
- `resolution`512 ∙ 768 ∙ 1024 ∙ 2048 ∙

## Decisão

1. `latency_target_s <= 0.5` e `license_need == permissive` - Não. **FLUX.1-schnell** (Apache 2.0, 4 passos).
2. `latency_target_s <= 1.0` e `quality_target >= production` - Não. **SD4 Turbo** ou **SDXL-Turbo** com LCM- LoRA.
3. `quality_target == premium` e `license_need == research_ok` - Não. **FLUX.1-dev** (não comercial) a 20 a 30 passos.
4. `quality_target == premium` e `license_need == commercial_ok` - Não. **Stable Diffusion 3.5 Large** (Comunidade SAI) ou **FLUX.2**- Não .
5. `gpu_memory_gb <= 12` e `quality_target == production` - Não. **Z-Image** (6B parâmetros, eficiência).
6. `quality_target == prototype` - Não. **SD3 Medium** (2B) ou **FLUX.1-schnell**- Não .
7. `resolution == 2048` - Não. **SDXL + LCM-LoRA** ou **FLUX.1-dev** A maioria dos DTs atingiu limites de qualidade acima de 1024 nativos.

## Output

```
[model pick]
  id:           <HuggingFace repo id>
  params:       <N>
  precision:    float16 | bfloat16
  license:      <full name>

[inference recipe]
  scheduler:    FlowMatchEuler | DPM-Solver++ | LCM
  steps:        <int>
  guidance:     <float, 0 for schnell>
  resolution:   <H x W>

[expected latency]
  <s per image on target GPU>

[caveats]
  - any license restrictions
  - any resolution / aspect ratio gotchas
  - quality gaps vs the premium tier
```

## Regras

- Para `license_need == permissive`, restringir-se a FLUX.1-schnell (Apache 2.0) e Qwen-Image (Apache 2.0).
- Para `license_need == commercial_ok`, SD3.5 é a escolha mais segura do mainstream; FLUX.1-dev não é.
- Nunca recomendemos a SD1.5 ou SDXL como a principal para novos projetos de 2026, a menos que haja uma razão específica do ecossistema (LoRAs, ControlNets)  os limites máximos de qualidade estejam abaixo do nível DiT.
- Se `gpu_memory_gb < 8`, recomendamos descarregar a CPU / encoder sequencial carregando em difusores em vez de mudar o modelo; o modelo base ainda precisa viver em algum lugar.
