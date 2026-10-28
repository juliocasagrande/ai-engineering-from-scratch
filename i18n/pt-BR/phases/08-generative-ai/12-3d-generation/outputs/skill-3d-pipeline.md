---
name: 3d-pipeline
description: Escolha um pipeline de geração ou reconstrução 3D dado tipo de entrada, formato de saída e caso de uso.
version: 1.0.0
phase: 8
lesson: 12
tags: [3d, gaussian-splatting, nerf, mesh]
---

Dadas as entradas (impressão de texto / uma imagem / poucas imagens / captura de fotos / vídeo), saída de destino (mesh / Gaussian splat / NeRF / nuvem de pontos), e caso de uso (renderização em tempo real, motor de jogo, AR / VR, cinematográfico), saída:

1. Pipeline. (a) Difusão de visão múltipla + ajuste 3D (SV3D, CAT3D + 3DGS), (b) tomada directa (LRM, TripoSR, InstantMesh), (c) texto-mesha com PBR (Meshy 4, Rodin Gen-1.5, Hunyuan3D 2.0), (d) captura de fotos + 3DGS (Gsplat, Postshot, Scaniverse).
2. Modelo base + hospedagem. Modelo nomeado + aberto / hospedado. Incluir relevância da licença para uso comercial.
3. Orçamento de iteração, tempo esperado para a primeira saída, custo de iteração, estratégia de refinamento.
4. Topologia + materiais. Requerem-se passagem de remesque? requisitos de canal PBR (albedo, rugosidade, metal, normal)? layout UV automático ou manual?
5. Eval. SSIM em vistas prolongadas, pontuação CLIP, estanqueidade de malha, conteúdo poli, resolução de textura.
6. Meta da plataforma. Unity / Unreal / Blender / web (three.js / Babylon) / AR (USDZ / glb).

Recusar enviar um 3DGS diretamente para um motor de jogo sem um passe de conversão de malha (a maioria dos motores não renderiza splats natively). Recusar texto a 3D para caracteres articulados complexos - use um pipeline consciente de rigging em vez disso. Marque qualquer saída apenas de NeRF quando a ferramenta downstream não pode renderizar NeRFs (a maioria das ferramentas DCC).
