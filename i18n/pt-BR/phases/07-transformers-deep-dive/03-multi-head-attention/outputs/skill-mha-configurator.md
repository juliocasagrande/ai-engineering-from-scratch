---
name: mha-configurator
description: Recomenda-se a contagem de cabeças, a contagem de cabeças de KV e a estratégia de projecção (MHA/MQA/GQA/MLA) para um novo transformador.
version: 1.0.0
phase: 7
lesson: 3
tags: [transformers, attention, mha, gqa]
---

Dado o padrão do transformador (orçamento do parâmetro, tamanho oculto) `d_model`, comprimento do contexto-alvo, memória do dispositivo de inferência, prioridade de formação versus inferência), saída:

1. Uma variante de projeção, uma de: MHA, GQA, MQA, MLA. Razão de uma frase ligada às restrições de cache KV.
2. Geometria da cabeça. `n_heads`- Não . `n_kv_heads`- Não . `d_head`Os valores devem satisfazer `d_model = n_heads * d_head` e `n_heads % n_kv_heads == 0`- Não .
3. Estimação do cache KV. Bytes por token por camada (fp16) para a variante escolhida no comprimento do contexto de destino. Flag se um lote excede a memória do dispositivo de destino.
4. Inicialização. Escala Xavier / Kaiming para matrizes Q, K, V, O. Observe se os termos de viés estão incluídos (a maioria dos modelos 2026 os deixa cair).
5. Anel de ensaio: uma única tarefa sintética (por exemplo, padrão de cabeça de indução) `A B A ? → B`) que uma versão de duas camadas treinada desta configuração deve resolver a ≥ 95%.

Recusar-se a recomendar `d_head < 32`  a dinâmica da atenção se rompe. `n_heads > 16` para comprimentos de contexto superiores a 32K, sem especificar explicitamente o preço do cache KV e sugerindo GQA ou MLA. Recusar-se a sugerir MLA para modelos com parâmetros 1B, a menos que o usuário esteja explicitamente comparando.
