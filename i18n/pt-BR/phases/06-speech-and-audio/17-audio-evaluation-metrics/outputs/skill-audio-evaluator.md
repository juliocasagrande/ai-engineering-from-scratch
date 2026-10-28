---
name: audio-evaluator
description: Escolha métricas, referências, regras de normalização e formato de relatório para qualquer lançamento de modelo de áudio.
version: 1.0.0
phase: 6
lesson: 17
tags: [evaluation, wer, mos, utmos, eer, der, fad, mmau, leaderboard]
---

Dada a tarefa (ASR / TTS / clonagem / verificador-auditor / diarização / classificação / música / LALM / streaming S2S), saída:

1. Metrica primária: WER · MOS · UTMOS · SECS · EER · DER · MAP · FAD · MMAU-Pro precisão · latência P95.
2. Metricas secundárias. 1-3 eixos adicionais (velocidade, diversidade, robustez) e razão.
3. Regra de normalização: minúsculas, faixa de pontuação, expansão de números, colapso do espaço em branco.
4. Referência pública: o ranking canônico a ser relatado (Open ASR, TTS Arena, MMAU-Pro, VoxCeleb1-O, AudioSet, LongAudioBench, etc.).
5. Encontro interno. Dados de domínio mantidos com amostras N; desagregação demográfica / faixa acústica.
6. Formatos de comunicação. Distribuição (P50/P95/P99 para latência; recall por classe para classificação; por categoria para MMAU).

Rejeitar a avaliação de um único número para latência (percêntulos de relatório). Rejeitar somente agregado para classificação (relatar por classe). Rejeitar lançamentos TTS sem MOS / UTMOS e SECS (quando se clona). Rejeitar lançamentos ASR sem uma especificação de normalização WER. Rejeitar lançamentos de música com apenas FAD  sempre emparelhado com o painel MOS humano.

Exemplo de entrada: "Liberar um novo TTS conversacional inglês-espanhol. Preciso convencer a equipe que é melhor do que a linha de base cartesia-sônica existente".

Exemplo de saída:
- Primário: UTMOS (produtos de áudio em par com 50 pedidos por língua) + MOS de painel humano (20 ouvintes por língua, A/B cego vs linha de base).
- Secundário: mediana TTFA & P95 (deve corresponder com a linha de base); SECS &gt; 0,80 vs uma referência de voz fixa (sem regressão de alto-falantes); WER em viagem de ida e volta ASR (Whisper-large-v3-turbo) &lt; 2% por idioma, inglês e espanhol (ambos são segmentados por espaço, então WER se encaixa; use CER para línguas sem limites de palavras).
- Normalização: `EnglishTextNormalizer` do `openai-whisper` O pacote para o inglês e os seus `BasicTextNormalizer` A lição de "Relação de Redação de Redação" é uma lição de "Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação de Redação. `wer()` assistente é apenas ASCII, então use estes normalizadores (ou um avaliador externo) para espanhol.
- Referência pública: TTS Arena (Inglês) e Artificial Analysis Speech para posicionamento relativo do ELO.
- Em casa: 200 mensagens contínuas (100 por língua) que cobrem dinheiro, datas, nomes de produtos, narração de duas frases, leitura emocional, código-switched. 10 vozes demográficas.
- Relatório: nota de divulgação com título (UTMOS + MOS), histograma P50/P95 TTFA, SECS CDF, WER/CER por categoria, chamadas de modo de falha (compromissos com código com interrupção falharam em X%).
