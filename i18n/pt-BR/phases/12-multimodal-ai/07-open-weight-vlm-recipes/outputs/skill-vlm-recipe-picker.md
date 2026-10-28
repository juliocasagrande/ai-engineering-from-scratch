---
name: vlm-recipe-picker
description: Escolha uma receita de VLM de peso aberto (encodador, conector, LLM, mix de dados, cronograma de resolução) com citações de tabela de ablação para cada escolha.
version: 1.0.0
phase: 12
lesson: 07
tags: [vlm, mm1, idefics2, molmo, cambrian, prismatic, ablation]
---

Dado um mix de tarefas (OCR, gráfico, agente de UI, raciocínio, grounding), um orçamento de computação (parâmetros LLM, horas de treinamento de GPU ou meta de latência de inferência) e uma restrição de implantação (edge, nuvem, no dispositivo), emitir uma receita completa de VLM de peso aberto com citações.

Produzir:

1. Seleção do encodador. Default SigLIP 2 SO400m/14; concato com DINOv2 ViT-g/14 se a fixação/segmentação estiver na mistura de tarefas; citação da MM1 Tabela 3 e a correspondência do encodador de visão do Cambrian-1.
2. Seleção de conector. MLP de 2 camadas por defeito, a menos que seja restrito por token (então Q-Former 32 consultas); citar a ablação de conector dos VLMs Prismatic mostrando <1 ponto delta.
3. Seleção de LLM. Base no orçamento: Qwen2.5-7B para <10B, Llama-3.1-70B ou Qwen2.5-72B para >30B.
4. Mix de dados: PixMo + ShareGPT4V + Cauldron; cita o resultado detalhado de captura humana de Molmo (+2-3 MMMU sobre destilação na mesma contagem de tokens).
5. Calendário de resolução: Dinâmica por defeito (256-1280) com um pre-treino de alinhamento fixo-384 de fase 1; citação de ablação de resolução Idefics2 (+3-5 DocVQA de AnyRes) e dinâmica M-RoPE Qwen2.5-VL.
6. Fase 1 apenas para projetores, Fase 2 perfeito, Fase 3 específico de tarefas.

Rejeitos duros:
- Recomendar o CLIP ViT-L/14 como codificador padrão sem marcar a sua depreciação em favor do SigLIP 2 para novos projectos.
- Sugerindo Q-Former como um ganho de qualidade sobre MLP. É uma alavanca de orçamento de tokens, não uma alavanca de qualidade.
- Proporcionar capções sintéticas GPT-4V como dados de formação primária quando existem alternativas captadas por humanos.
- A arquitetura de conector explica a variância que realmente vem do conteúdo dos tokens.

Regras de recusa:
- Se o utilizador desejar um VLM 1-3B para tarefas pesadas em razão, recuse e recomenda um LLM maior; limites de razão são fixados pelo LLM.
- Se o utilizador não puder pagar dados detalhados de captação humana, marque explicitamente o limite máximo esperado de 2-3 MMMU e ofereça um retorno de destilação com o melhor esforço.
- Se o mix de tarefas incluir imagens de documentos 4K+ em uma implantação de codificadores congelados, rejeite AnyRes e recomenda um codificador M-RoPE de resolução nativa como Qwen2.5-VL.

Resultado: um cartão de receita de uma página com escolha por eixo, citação de ablação (ID arXiv), plano de estágio de treinamento e intervalo de referência esperado.
