---
name: alm-picker
description: Pick an audio-language model, benchmark subset, output modality (text vs speech), and guardrails for an audio-understanding task.
version: 1.0.0
phase: 6
lesson: 10
tags: [alm, lalm, qwen-omni, audio-flamingo, gemini-audio, mmau]
---

Dada a tarefa (discurso / som / música / multi-audio / áudio longo, modalidade de saída, latência, licença), saída:

1. Modelo: Qwen2.5-Omni-7B · Qwen3-Omni · SALMONN · Áudio Flamingo 3 · AF-Next · LTU · GAMA · Gemini 2.5 Pro (API) · GPT-4o Audio (API). Razão de uma frase.
2. Subconjunto de referência para validar. MMAU-Pro fala / som / música / multi-áudio · LongAudioBench · AudioCaps · ClothoAQA. Escolha o eixo que corresponda à tarefa do usuário.
3. Modalidade de saída. Apenas texto · texto + fala (Qwen-Omni, GPT-4o Audio). Orçamento para um decodificador de fala adicional, se necessário.
4. Guardrails. Rejeita as instruções que exigem comparação de áudio múltipla quando a pontuação de áudio múltipla do seu modelo é de &lt; 30% (quase aleatória). Diarice antes do LALM para &gt; entradas de 10 minutos.
5. Escalação. Quando deve esta tarefa voltar a um modelo especializado  Suspirar para transcrição, BEATs para classificação, pyannote para diarização.

Recusar enviar tarefas de comparação de áudio múltipla sem verificar as pontuações do seu modelo &gt; 40% no subconjunto de áudio múltipla MMAU-Pro. Recusar áudio longo (&gt; 10 min) sem diarização upstream. Marque qualquer implantação que use números relatados pelo fornecedor sem reverificação independente.

Introdução de exemplo: "Auditoria da conformidade: transcrever registos de 10 minutos de chamadas bancárias + detectar se o agente leu a divulgação obrigatória".

Exemplo de saída:
- Modelo: Whisper-large-v3-turbo para transcrição + Gemini 2.5 Pro (via API) para verificação de QA sobre a transcrição. LALM direto em áudio bruto é tentador, mas a precisão LALM de áudio longo cai além de 10 minutos.
- Subconjunto de referência: MMAU-Pro subconjunto de fala (Gemini 2.5 Pro = 73,4%)  cobre o eixo de raciocínio de fala.
- Modalidade de saída: somente de texto.
- Guardrails: diário com pyannote 3.1 primeiro; enviar segmentos por alto-falantes separadamente; registro de pontuação de confiança por chamada.
- Escalação: se uma chamada não conseguir verificar a divulgação, encaminhar-se para o revisor humano em vez de bandeira autônoma.
