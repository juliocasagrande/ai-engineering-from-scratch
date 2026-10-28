---
name: edge-target-picker
description: Escolha um alvo de inferência de borda (Apple ANE, Qualcomm Hexagon, WebGPU/WebLLM, NVIDIA Jetson) e corrija o formato de quantização dado dispositivo, modelo e orçamento de latência.
version: 1.0.0
phase: 17
lesson: 12
tags: [edge, ane, hexagon, webgpu, webllm, jetson, core-ml, qnn, nvfp4]
---

Dada a plataforma de implantação (iOS, Android, navegador, robótica/automóveis/servidor de ponta), modelo e orçamento de latência/memória, produz uma recomendação de objetivo de ponta.

Produzir:

1. Alvo. Nomear o NPU/GPU específico (ANE, Hexagon, WebGPU, Jetson Orin Nano / AGX / Thor). Justificar com a plataforma e a cobertura de tempo de execução de 2026.
2. O limite máximo de largura de banda. Compute o limite máximo de decodificação teórico: bandwidth_GB_s / model_size_GB. Compare com o requisito de tok/s do usuário. Se o limite estiver abaixo do requisito, rejeite ou propor uma quantização menor / mais rígida.
3. Formatos de quantização: escolha Q4 GGUF (browser/edge CPU), Core ML INT4 + FP16 (ANE), QNN INT8/INT4 (Hexagon), ou NVFP4 + FP8 KV (Jetson Thor / Edge-LLM).
4. Nomear o conversor exato (Core ML converter, Qualcomm AI Hub, MLC-LLM para WebLLM, TensorRT-LLM Edge compilador).
5. Prestação de conteúdo. Indique o conteúdo máximo que se encaixa junto com pesos na RAM do dispositivo. Para casos de uso de longo contexto, especifique quantização de KV (Q4 KV) ou rejeita.
6. Fallback. Quando o dispositivo estiver incapaz ou WebGPU não estiver disponível (Firefox Android, navegadores mais antigos), especifique o fallback da API do lado do servidor com a mesma interface compatível com o OpenAI.

Rejeitos duros:
- Promete-se um toque/s acima do limite de largura de banda.
- Alvo de ANE diretamente através de um tempo de execução não-Core ML em 2026.
- Supondo que o WebGPU esteja em todos os navegadores. A cobertura de 2026 é de ~70-75% móvel; sempre especifique o fallback.

Regras de recusa:
- Se o modelo for >6 GB e o alvo é um telefone (4-8 GB de RAM), rejeite  propor um modelo menor ou quantização agressiva primeiro.
- Se o pedido for conteúdo de 128K em um modelo 7B no iPhone, rejeitar  dispositivo RAM não pode caber sem Q4 KV mais atenção da janela deslizante.
- Se a implantação requer transmissão de longo contexto no Android através do WebGPU e o usuário requer suporte ao Firefox, recusar e exigir o Chrome ou um servidor de retrocesso.

Output: um plano de uma página de nomeação do alvo, limite, quantização, conversor, orçamento contextual, retrocesso.
