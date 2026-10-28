---
name: duplex-pipeline
description: Escolha uma arquitetura de duplex completo (Moshi) versus pipeline (VAD + STT + LLM + TTS) para uma carga de trabalho de agente de voz.
version: 1.0.0
phase: 6
lesson: 15
tags: [moshi, hibiki, full-duplex, voice-agent, streaming]
---

Dado o volume de trabalho (alvo de atraso, necessidades de chamada de ferramentas, cobertura de linguagem, orçamento de hardware, nuvem vs. edge), saída:

1. Arquitetura. Duplex completo (Moshi / GPT-4o em tempo real / Gemini Live) vs. pipeline (LiveKit + STT + LLM + TTS, lição 12). Razão de uma frase.
2. Modelo: Moshi · Hibiki · Hibiki-Zero · Sesame CSM · GPT-4o em tempo real · Gemini 2.5 Live · pipeline tradicional. Razão.
3. Escala, custo de GPU por sessão (Moshi tem um slot), sessões simultâneas máximas, impacto de arranque a frio.
4. Caminho de chamada de ferramentas. Se necessário  pipeline híbrida (duplex + LLM externo para chamadas de ferramentas) ou pipeline pura. Explique a compensação.
5. Cobertura de linguagem. Os modelos duplex completos têm suporte linguístico estreito; os canais herdam a capacidade multilíngue do LLM.

Rejeitar arquitetura completa duplex-só para agentes empresariais que precisam de ferramenta de chamada / recuperação  Moshi é um modelo de diálogo, não um framework de agente. Rejeitar pipeline-só para agentes de conversação sub-250 ms  os estágios somam. Rejeitar Moshi para &gt; 4 sessões simultâneas em uma GPU  hits contenção.

Exemplo de entrada: "Companião de voz para aprendizagem de idiomas  prática de fluência conversacional. Inglês + francês. &lt; 250 ms capacidade de resposta. 10k atividades diárias".

Exemplo de saída:
- Arquitetura: duplex completo (Moshi). Requisito de latência sub-250 ms + fluência de conversação se encaixa nos pontos fortes de Moshi.
- Modelo: Moshi. EN + FR ambos bem suportados. Licença CC-BY 4.0.
- Escala: uma GPU L4 por 4-6 sessões simultâneas → ~ 1500 GPUs no pico para 10k DAU em 10% de simultânea. Planeje o modo de luz no dispositivo usando Kyutai Pocket TTS + local Whisper para o caminho silencioso.
- Chamando ferramentas: mínimo  "revelar sugestão gramatical" e "traduzir esta frase" pode ser encaminhado através de um pequeno sidecar LLM; a maior parte da interação é um diálogo aberto onde Moshi brilha.
- Cobertura linguística: EN + FR (nativa); ES / DE / JP através da adaptação Hibiki-Zero (1000 horas de áudio necessárias por nova língua).
