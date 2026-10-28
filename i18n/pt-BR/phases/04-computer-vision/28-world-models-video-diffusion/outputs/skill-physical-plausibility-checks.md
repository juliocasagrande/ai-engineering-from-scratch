---
name: skill-physical-plausibility-checks
description: Automated checks for object permanence, gravity, and continuity on any generated video before shipping
version: 1.0.0
phase: 4
lesson: 28
tags: [video-generation, quality, physics, evaluation]
---

# Verificações de Plausibilidade Física

As instalações de produção de vídeo gerado precisam de barris de segurança automatizadas.

## Quando utilizar

- Qualquer produto que gera vídeo a partir de mensagens de texto ou imagem.
- Automatização de QA em um endpoint de API de geração de vídeo.
- Monitoramento da deriva de qualidade de um modelo de vídeo após ajustes finos ou uma atualização do modelo base.

## Input

- `video`: um tensor `(T, H, W, 3)`ou um caminho para um mp4.
- Informações de referência opcionais: número esperado de objetos, descrição inicial de cena.

## Cheques

### 1. Permanência do objeto
Rastrear todas as detecções em quadros com SAM 3.1 Object Multiplex. Marca quando uma faixa estável desaparece por <=3 quadros e reaparece  o modelo perdeu o objeto temporariamente. Falha dura quando um objeto desaparece perto do centro do quadro (não em uma borda); falha suave nas bordas.

### 2. A suavidade de movimento
O fluxo óptico entre quadros consecutivos deve ser principalmente contínuo. Os picos de fluxo repentinos por pixel indicam teletransporte.

### 3. Gravidade / apoio
Para objetos detectados como sólidos (alimentos, bolas, ferramentas), verifique se a sua posição vertical não aumenta na ausência de uma ação de levantamento.

### 4. Consistência da identidade
Para pessoas ou personagens, use um reconhecimento facial incorporado em quadros. A semelhança cosínica deve permanecer > 0,8 em janelas de 5 quadros para uma identidade persistente. Abaixo do limiar significa que o personagem foi transformado.

### 5. Mãos e membros
Execute um estimador de postura (Lessão 21). Encosto de bandeira onde uma mão tem > 5 ou < 4 dedos visíveis; onde um braço duplica-se entre os encosto; onde os membros se cruzam através de uma superfície.

### 6. Tradução de texto (se solicitado por instância)
Se o pedido do usuário incluía uma cadeia em citações, OCR os quadros gerados e calcular CER contra a cadeia solicitada.

## Relatório

```
[plausibility]
  video frames:           <T>
  permanence violations:  <N>
  smoothness violations:  <N>
  gravity violations:     <N>
  identity drift:         <N of 5-frame windows>
  limb anomalies:         <N>
  OCR CER vs requested:   <float>

[verdict]
  ship | hold | reject

[samples for review]
  frame ranges where each failure occurred
```

## Regras

- Não bloqueie com dureza qualquer verificação; pontuações agregadas e mantenha o vídeo para revisão quando as anomalias totais excederem um limiar.
- O peso de deriva de identidade e violações de permanência mais alto  os usuários notam-nos primeiro.
- Taxas de falhas de registro por verificação ao longo do tempo; uma tendência crescente geralmente significa que o modelo base foi atualizado ou a distribuição rápida mudou.
- Nunca excluir o vídeo sinalizado; guarde-o para depuração de modelos e pós-mortem.
- Para conteúdos sensíveis (pessoas, crianças, figuras públicas), é necessário que cada vídeo seja revisado por um ser humano, independentemente da pontuação.
