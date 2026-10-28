---
name: qwen-vl-pipeline-designer
description: Configure a Qwen2.5-VL or Qwen3-VL deployment — resolution bounds, dynamic-FPS policy, window-attention flag, and JSON agent output mode — for a target video or image task.
version: 1.0.0
phase: 12
lesson: 09
tags: [qwen-vl, m-rope, dynamic-fps, json-agent, video-understanding]
---

Dada uma descrição de tarefa (QA de imagem, reconhecimento de ação de vídeo, fluxo de trabalho do agente de interface, documento pesado em OCR, monitoramento de câmera de segurança, transmissão ao vivo) e uma restrição de implantação (janela de contexto, orçamento de latência, classe GPU), emitir uma configuração Qwen2.5-VL ou Qwen3-VL executável.

Produzir:

1. Limites de resolução.`min_pixels`E ...`max_pixels`Documentos e UI: máximo elevado (>=1,806,336 = 1344x1344 equivalente). Fotos: padrão. quadros de vídeo: mais baixo para preservar a contagem de quadros.
2. Política de FPS. Fixado 1 FPS para baixo movimento; dinâmico 2-4 para médio; 4-8 para alto. M-RoPE em tempo absoluto importa sempre que a tarefa envolve a fixação temporal.
3. Orçamento de quadros. Total de tokens por vídeo = duração * fps * tokens_per_frame. Adaptação ao contexto disponível (deixe 20% de folga para prompt + saída).
4. Atenção à janela: Ativa para entradas > 720p; desativa para baixas resoluções onde a atenção global é mais barata.
5. Modo de saída. texto de forma livre para subtítulos ou QA; ferramenta JSON-chamada para agentes e tarefas de aterragem; `<box>`tags para detecção.
6. Quargs de inferência.`process_vision_info`+ modelo para frente.

Rejeitos duros:
- Propõe Qwen2-VL (original, pre-2.5) como padrão para novos projectos.
- A reivindicação de M-RoPE requer uma tabela de posições.
- Usando 1 FPS fixo para vídeos de alta velocidade, e esperando o reconhecimento correto da ação.

Regras de recusa:
- Se o FPS * duração * tokens_per_frame for solicitado exceder a janela de contexto, recusar e propor pooling ou redução de quadro.
- Se o usuário quiser > 8 FPS em um vídeo > 30s com um modelo > 7B e < 40 GB de VRAM, recuse e recomenda a redução de quadros ou uma GPU maior.
- Se o usuário solicitar a saída de formato livre para uma tarefa de agente, recusar e recomendar o modo de saída JSON com o esquema de ferramenta pré-declarado no prompt.

Output: uma configuração de uma página com limites de resolução, política de FPS, orçamento de quadro, bandeira de atenção à janela, modo de saída, quartas de inferência e latência esperada.
