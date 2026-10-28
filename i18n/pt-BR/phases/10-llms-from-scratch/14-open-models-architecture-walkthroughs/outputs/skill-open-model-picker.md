---
name: open-model-picker
description: Pick an open LLM family, quantization, and inference stack for a given deployment target.
version: 1.0.0
phase: 10
lesson: 14
tags: [open-models, llama, deepseek, mixtral, qwen, gemma, moe, gqa, mla, quantization]
---

Dado um objetivo de implantação (tipo de GPU, VRAM por GPU, número de GPUs, comprimento de contexto objetivo, latência de p50/p99, pico de solicitações simultâneas) e um perfil de tarefa (chat, código, raciocínio, recuperação de contexto longo, uso de ferramentas), recomendamos um modelo aberto mais uma pilha de serviço com raciocínio explícito sobre cada um dos seis botões arquitetônicos da lição 14.

Produzir:

1. Três candidatos, cada um com parâmetros totais, parâmetros ativos (MoE-consciente), bandeiras de arquitetura (norma / ativação / posição / atenção / MoE / contexto), e a única razão pela qual ele fez a lista.
2. Verificação do orçamento de memória. Para o candidato superior: memória de peso em BF16 e na quantização escolhida; cache KV no contexto-alvo para o tamanho do lote-alvo; espaço de ativação. Parar a recomendação se pesos + cache KV + ativações excederem o VRAM disponível.
3. A escolha de quantização. GPTQ-4bit, AWQ-4bit, FP8 ou BF16. Justificar contra a sensibilidade de precisão da tarefa (code / matemática / tarefas de raciocínio tomam um grande impacto da quantização agressiva do que o chat ou recuperação).
4. Estaca de inferência. vLLM, TensorRT-LLM, SGLang ou llama.cpp. Justificar contra: necessidade contínua de lotes, suporte de decodificação especulativa, compatibilidade de formato de quantização e topologia de único nó versus múltiplos nódos.
5. Verificação de inteligência de throughput. Preencher tokens/sec e decodificar tokens/sec estimativas baseadas na largura de banda de memória da GPU (decodificação) e TFLOPs (preencher). Rejeitar a recomendação se o decodificação de throughput é abaixo do piso do usuário simultâneo do alvo.
6. Outra opção se o candidato superior exceder o orçamento de VRAM ou de transferência.

Rejeitos duros:
- Modelos densos acima de 30B em uma única GPU de consumo de 24 GB sem descarga ou quantização agressiva.
- Modelos de MoE em uma pilha de serviço sem apoio paralelo de peritos.
- Long-context (128k+) em arquiteturas sem GQA ou MLA (KV cache explode).
- Qualquer recomendação que não nomeie a revisão específica do modelo (por exemplo, "Llama 3 8B Instrumento v3.1", não "Llama 3").

Resultado: um modelo de listagem de recomendações de uma página, quantização, pilha, com evidências numeradas para cada decisão. Terceiro com um parágrafo "valor reconsiderar se ... " nomeando a capacidade específica ou parâmetro de implantação que inverteria a escolha.
