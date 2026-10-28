---
name: prompt-vision-preprocessing-audit
description: Turn any model card or dataset card into a checklist of the preprocessing invariants a vision pipeline must honour
phase: 4
lesson: 1
---

Se tiver um modelo de cartão, um conjunto de dados ou uma seção de pré-processamento de papel, extrair a lista completa de invariantes que o pipeline de serviço deve respeitar, na seguinte ordem:

1. **Input shape**- altura, largura e quaisquer suposições de relação de aspecto fixa.
2. **Channel order** RGB ou BGR. Nomear a biblioteca com que o modelo foi treinado (torchvision, OpenCV, timm) e a convenção de canais que implica.
3. **Dtype** uint8, float16, float32. O modelo é quantizado (int8, int4)?
4. **Value range** [0, 255], [0, 1], ou [-1, 1]. Extrair se os pixels são divididos por 255, por 127,5, ou deixado crudo.
5. **Standardization** média por canal e etc. Cite os números exatos. Se as estatísticas da ImageNet, nomei-os explicitamente.
6. **Resize policy** Dimensão de lado mais curto + colheita central, dimensão e pad ou alongamento direto. Incluir o tamanho do alvo e o método de interpolação.
7. **Color space** RGB, YCbCr, escala de cinza ou outros. Marque quaisquer modelos que operem apenas em Y (super-resolução) ou em espaço LAB.
8. **Axis layout** NCHW, NHWC ou sem lote.

Para cada invariante, saída:

```
[inv] <name>
  value:  <exact value from the source>
  source: <file, section, or line>
  risk:   <what fails silently if this is wrong>
```

Em seguida, elabore um resumo de pré-processamento de uma linha na forma:

```
load -> convert(<colorspace>) -> resize(<size>, <interp>) -> crop(<size>) -> /<divisor> -> -mean /std -> transpose(<layout>) -> dtype(<dtype>)
```

Regras:

- Cita números exatos. Nunca redondeie as estatísticas da ImageNet para dois decimais.
- Se o cartão estiver silencioso em uma invariante, marque-o `unspecified`e adicionar-o a uma seção "questions to solve" na parte inferior.
- Os riscos de falha silenciosa da bandeira são explícitos: troca de canal, falta de padronização e layout errado são os três bugs de produção mais comuns.
- Se o cartão diz "pré-processamento padrão" sem especificar, é uma invariante não especificada.
- Quando duas fontes discordam (papel vs código), confie no código e note a discordância.
