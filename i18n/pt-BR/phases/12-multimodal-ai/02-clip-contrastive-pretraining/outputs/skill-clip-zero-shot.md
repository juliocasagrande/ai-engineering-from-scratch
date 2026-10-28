---
name: clip-zero-shot
description: Execute classificação de imagem de tiros zero com um ponto de verificação CLIP / SigLIP, produzindo previsões classificadas com pontuações de semelhança.
version: 1.0.0
phase: 12
lesson: 02
tags: [clip, siglip, zero-shot, vision-language]
---

Dadas uma lista de imagens (caminhos de arquivo ou URLs) e uma lista de nomes de classes candidatos, produzir uma classificação de tiro zero classificada usando um ponto de verificação CLIP ou SigLIP declarado.

Produzir:

1. Construção rápida. Para cada classe, formule modelos de texto N (default: `a photo of a {class}`- Não . `a picture of a {class}`- Não . `an image of a {class}`). Embed cada prompt com o codificador de texto e média para formar o protótipo de classe.
2. Embedagem de imagem. Embed cada imagem de entrada com o codificador de visão declarado. Normalize ambos os lados para o comprimento da unidade.
3. Previsões classificadas. Computa a semelhança cosínica entre cada inserção de imagem e cada protótipo de classe. Retorna o top-1 e top-5 com pontuações.
4. Metadados do ponto de controlo. Nomear o ponto de controlo exacto utilizado em Hugging Face (por exemplo, `openai/clip-vit-large-patch14` ou `google/siglip2-so400m-patch14-384`) e a resolução que espera.
5. Nota de honestidade: indicar que o zero-shot em classes fora da distribuição pré-treino é improvável; superficial top-1 pontuação como um proxy de confiança e avisar quando é inferior a 0,2 .

Rejeitos duros:
- Qualquer uso que enquadre a saída como um rótulo definitivo para classes não na lista fornecida pelo chamador.
- As alegações sobre as pontuações em diferentes pontos de controlo são comparáveis; a pontuação SigLIP e CLIP em diferentes escalas.
- A usar imagens conhecidas por conter pessoas sem uma política de consentimento.

Regras de recusa:
- Se o telefonista solicitar a classificação em categorias médicas, legais ou de segurança crítica (diagnóstico, identidade, atributos protegidos), recusar e redirecionar para modelos supervisionados com trilhas de auditoria.
- Se o chamador fornecer um único nome de classe (classificação de uma só direcção sem alternativas), rejeitar  zero-shot precisa de pelo menos dois candidatos para ser significativo.
- Se o ponto de controlo não for especificado, recusar e perguntar qual dos (CLIP, OpenCLIP, SigLIP, SigLIP 2) mais qual escala.

Resultado: uma lista classificada de 5 principais previsões por imagem com pontuações de similaridade cosínea, nome do ponto de verificação, modelos de prompt usados e uma bandeira de confiança.
