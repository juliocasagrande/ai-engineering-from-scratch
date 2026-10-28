---
name: voice-cloner
description: Pick cloning approach (zero-shot / conversion / adaptation), consent artifact, watermark, and safety filters for a voice-cloning deployment.
version: 1.0.0
phase: 6
lesson: 08
tags: [voice-cloning, voice-conversion, watermark, consent, safety]
---

Tendo em conta a tarefa (linguagem, comprimento de referência disponível, orçamento de adaptação, restrições de licença, estado de consentimento, escala de implantação), a saída:

1. Aproximação: clone de tiro zero (F5-TTS / VibeVoice / Orpheus / OpenVoice V2) · conversão de voz (tono-color kNN-VC / OpenVoice V2) · adaptação de alto-falantes (XTTS v2 + LoRA / VITS completa afinidade).
2. Preparação de referência: comprimento necessário, SNR (≥ 20 dB), mono 16 kHz+, trancação silenciosa, `ref_text`Rejeita referências de música.
3. Artigo de consentimento. Consentimento registrado explícito do proprietário de voz. Modelo: nome + data + finalidade + âmbito + procedimento de revogação. Armazenar 7+ anos.
4. Marca de água. Carga útil de 16 bits em cada saída. Configure o detector em CI para verificar a presença antes de publicar áudio.
5. Filtros de segurança: entidade de nome (celebridade / político / menor) rejeição imediata; limite de taxa por usuário por hora; registro de auditoria de cada geração de clones; interruptor de eliminação.

Recusar a clonação de navios sem uma estratégia de marca de água. Recusar a clonação de nomes de celebridades / políticos / menores, independentemente de reivindicações de consentimento. Recusar referências abaixo de 3 s ou SNR &lt; 20 dB. Recusar F5-TTS para implantações comerciais (CC-BY-NC). Recusar clonação translingual sem marcar explicitamente a lacuna de transferência de sotaque.

Exemplo de entrada: "Aplicação de acessibilidade: deixe os pacientes com ALS bancarem a voz enquanto ainda falam, depois falem através do TTS após a perda de voz. Inglês, EUA".

Exemplo de saída:
- Abordagem: OpenVoice V2 (MIT, zero-shot, 6 s referência).
- Preparação de referência: gravação de clips de 5 × 6 s em condições de qualidade de estúdio (sala silenciosa, microfone USB, 24 kHz). Armazenar transcrições crudas +. Construir referência centróide para estabilidade.
- Consentimento: assinatura digital + confirmação em vídeo que ateste a finalidade ("reutilização de voz pós-diagnóstico"), armazenada em volume criptografado com retenção de 10 anos. Linha de abertura de revogação.
- Marca de água: AudioSeal codificação de carga útil de 16 bits `patient_id`+ `clip_id`O detector funciona em cada geração em IC.
- Segurança: filtro de nome de entidade de hardware; registro de cada geração; ROI limitado à instância de aplicativo de login do paciente.
