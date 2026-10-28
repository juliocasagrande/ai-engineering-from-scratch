---
name: hybrid-picker
description: Escolha entre Transformer puro, híbrido de estilo Jamba e SSM puro para uma determinada carga de trabalho.
version: 1.0.0
phase: 10
lesson: 21
tags: [jamba, mamba, ssm, hybrid, long-context, memory-budget, architecture]
---

Dada a especificação da carga de trabalho (profil de comprimento de contexto p50/p99, mix de tarefas, orçamento de memória por GPU, capacidade de transmissão alvo, prioridade qualidade versus velocidade), recomendamos entre um transformador puro (+ MoE + MLA), um híbrido de estilo Jamba e um modelo Mamba puro.

Produzir:

1. Balde de comprimento de contexto: curto (menos de 16k), médio (16k-64k), longo (64k-256k) ou ultra-longo (256k-plus).
2. Recomendação de arquitetura. Escolha um de Transformer puro, híbrido 1: 7, híbrido 1: 3, híbrido 1: 15, ou Mamba puro. Justifique usando o balde de contexto mais as exigências de recall de conteúdo da tarefa.
3. Verifique o orçamento de memória. Compute o cache KV + estado SSM no contexto de destino. Confirme que se encaixa no acelerador de destino após a contabilização de pesos e memória de ativação (normalmente 10-20 GB em cima de pesos e cache KV).
4. A divulgação de compromissos de qualidade. Documente o custo de qualidade do nível de esparcidade escolhido. Híbridos abaixo da proporção 1: 7 degradam na recuperação no contexto em quantidades mensuráveis; Mamba pura falha em algumas tarefas de rastreamento de estado.
5. Compatibilidade com a pilha de inferência. Confirme que a arquitetura escolhida é suportada pela pilha de alvo (vLLM, TensorRT-LLM, SGLang, llama.cpp).

Rejeitos duros:
- O custo geral da arquitetura não é justificado.
- Mamba pura para tarefas de referência cruzada de raciocínio pesado ou de documentos múltiplos.
- Sub-1:15 proporções híbridas.
- Qualquer recomendação que não se ajuste ao orçamento de memória computada do acelerador especificado.

Regras de recusa:
- Se a carga de trabalho for genuinamente misturada em contexto curto e longo, rejeite a recomendação híbrida e recomenda o transformador puro (com MLA se possível)  híbridos brilhar em carga de trabalho de contexto longo especificamente.
- Se o acelerador for de consumo (24 GB ou menos), rejeite os modelos de tamanho híbrido e recomenda um pequeno híbrido destilado ou um transformador puro quantizado.
- Se a carga de trabalho for de geração de batch-1 sensível à latência e o modelo for novo (não existe caminho de implantação), rejeite e recomende um transformador puro com um suporte adequado com decodificação especulativa (fase 10 · 15) como o caminho mais simples.

Resultado: uma recomendação de uma página listando conteúdo contextual, escolha de arquitetura, cache KV no contexto-alvo, divulgação de compromissos de qualidade e compatibilidade de pilhas de inferência.
