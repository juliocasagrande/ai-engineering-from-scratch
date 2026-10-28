---
name: video-brief
description: Traduza um vídeo breve em um modelo + prompt + plano de fotos para um gerador de vídeo de 2026.
version: 1.0.0
phase: 8
lesson: 10
tags: [video, diffusion, sora, veo, kling]
---

Dado um vídeo breve (durada, relação de aspecto, estilo, assunto, plano de câmera, necessidades de áudio, barra de fidelidade, orçamento), saída:

1. Modelo + hospedagem. Sora, Veo 3, Kling 2.1, Runway Gen-3, Pika 2.0, CogVideoX, HunyuanVideo, WAN 2.2, ou Mochi-1. Razão de uma frase ligada à duração / qualidade / licença.
2. Apresentação de um esquadrão de câmera (a) de câmera (estabelecimento, rastreamento, guindaste, guindaste, porta-mãe), (b) assunto + ação, (c) iluminação + estilo, (d) interruptor de tipo negativo.
3. Plano de disparo. Single-clip vs. multi-shot, frame-key ou first-frame anchors, I2V vs T2V por disparo.
4. Semente + reproducibilidade. Semente por injecção, pin de versão, repo de ferramentas.
5. Lista de verificação de qualidade, quadro por quadro para o piscar, consistência de identidade, violações físicas, conformidade com a marca de água.
6. Audio. Nativo no Veo 3, de outra forma, forjado (ElevenLabs, Suno, ou caules licenciados + pass de sincronização de lábios).

Recusar-se a prometer 10s de movimento contínuo em 1080p em um nível livre (Pika / Kling / Runway cap em 10s; corridas mais longas são costuradas). Recusar-se a gerar semelhanças de pessoas reais sem um lançamento. Marque qualquer breve que implica geração 4K em tempo real em 2026 - melhor atual é ~ 30s geração por clip de 6s em 1080p em um endpoint hospedado.
