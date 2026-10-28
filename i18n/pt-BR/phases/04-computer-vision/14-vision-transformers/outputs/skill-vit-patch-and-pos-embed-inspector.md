---
name: skill-vit-patch-and-pos-embed-inspector
description: Verify a ViT's patch embedding and positional embedding shapes match the model's expected sequence length
version: 1.0.0
phase: 4
lesson: 14
tags: [vision-transformer, debugging, pytorch]
---

# Inspector de parche ViT e de inserção posicional

O bug de portação mais comum da ViT: carregar um checkpoint pré-treinado em 224x224 em um modelo configurado para 384x384 (ou vice-versa).

## Quando utilizar

- Ajustar um ViT pré-treinado em resolução não padrão.
- Auditando por que uma porta de peso entre ViT-B/16 e ViT-B/32 falha; o inspector sinalizará a desajuste do tamanho do parche para que o chamador saiba trocar arquiteturas em vez de forçar uma porta.
- Desfazer um ViT que carrega sem erros mas treina mal.

## Input

- `model`: um ViT instantâneo `nn.Module`- Não .
- `expected_image_size`: H x W o modelo verá em produção.
- `patch_size`: tamanho esperado do parche.

## Passo

1. Localize o cache de inserção do parche dentro do modelo.`kernel_size`- Não .`stride`- Não .`in_channels`- Não .`out_channels`- Não .
2. Calcule o número esperado de parches. Para uma imagem quadrada: `(image_size / patch_size)^2`Para um retângulo:`(H / patch_size) * (W / patch_size)`- Requerem .`H % patch_size == 0`E ...`W % patch_size == 0`; caso contrário, emblema e recusa.
3. Localize a inserção posicional aprendida.`(1, N, dim)`- Não .
4. Comparar`N`contra`num_patches + 1`(com CLS) ou `num_patches`Não correspondência significa que o ponto de controlo foi pré-exercido em uma resolução ou tamanho de parche diferente.
5. Verifica isso .`out_channels`do conv do parche é igual `dim`de inserção posicional.
6. Se o modelo for suposto interpolar embutidos posicionais para novas resoluções, verifique a existência da utilidade de interpolação (maior `timm`Os VTs fazem isto automaticamente através de`resize_pos_embed`)).

## Relatório

```
[vit-inspector]
  image_size:         HxW
  patch_size:         <int>
  num_patches (computed): <int>
  patch_conv:         k=<int>  s=<int>  in=<int>  out=<int>
  pos_embed shape:    (1, N, dim)
  has CLS token:      yes | no
  pos_embed N:        <int>    expected: <int>
  verdict:            ok | mismatch

[if mismatch]
  action:  reinitialise pos_embed for new sequence length
  tool:    timm.models.vision_transformer.resize_pos_embed
```

## Regras

- Nunca interpolar silenciosamente sem aviso prévio; superficial a ação para que o utilizador saiba que a estrutura posicional pré-treinada pode ter mudado.
- Se o patch_size não corresponder, recuse-se a recomendar interpolação  troca para a arquitetura correta.
- Não tente corrigir o modelo em seu lugar; informe e sugira.
