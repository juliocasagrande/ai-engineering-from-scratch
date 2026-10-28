---
name: spoof-defender
description: Escolha o modelo de detecção, a marca de água, o manifesto de proveniência e o manual operacional para uma implantação de geração de voz / voz-aúto.
version: 1.0.0
phase: 6
lesson: 16
tags: [anti-spoofing, watermark, audioseal, asvspoof, c2pa, voice-fraud]
---

Dado o volume de trabalho (voz-gen versus voz-aut, escala de implantação, região de conformidade, perfil adversário), saída:

1. Detecção (CM). AASIST · RawNet2 · NeXt-TDNN + WavLM · comercial (Pindrop, Validsoft). Dados de treinamento: ASVspoof 2019 / ASVspoof 5 / domínio específico.
2. Marcação de água (gen de saída). `(model_id, user_id, generation_ts)` · WaveVerify (alt) · none (com justificação).
3. Provença. Manifesto C2PA assinado com a chave do implementador · Metadados IPTC · nenhum (para áudio não-consumidor).
4. Protectores de voz-autor (se aplicável). Desafio de vivacidade (frase aleatória TTS' + transcrição), detecção de ataque de repetição (modelo AASIST + PA), calibração do limiar biométrico por canal.
5. Operacional: retenção do registro de auditoria, retenção de artefatos de consentimento (7 anos ou mais), sinais de detecção de abuso (explosão súbita de volume, indicações de nome da entidade), procedimento de interrupção de execução.

Rejeitar as implantações de voz-gen sem AudioSeal (ou marca de água equivalente). Rejeitar as implantações biométricas de voz sem detecção anti-spoofing  clonagem de voz torna o auth apenas cosino trivialmente evitável. Rejeitar as implantações que dependem do manifesto de proveniência sozinho (estripável). Rejeitar os limiares de detecção treinados em ASVspoof 2019 para implantações no mundo real sem um varredura de calibração de canal.

Exemplo de entrada: "IVR de atendimento ao cliente bancário. Desbloqueio biométrico de voz + agente de voz gerado por IA. 10 milhões de chamadas/mês. EUA + UE".

Exemplo de saída:
- Detecção: Pindrop comercial (preferido) ou NeXt-TDNN + WavLM aberto. Treinamento em ASVspoof 5 + 100k amostras de chamadas específicas do banco.
- Marcação de água: AudioSeal carga útil de 16 bits em cada declaração TTS de saída; carga útil codifica bank_id + session_id + timestamp. Detector verifica antes de transmitir.
- Provença: Manifesto C2PA sobre fluxos de trabalho de áudio-export para o cliente; chamadas internas apenas saltam.
- Autoria de voz: desafio de vida em cada autor (frase de 4 dígitos aleatórios TTS; usuário repete + detector + transcriber).
- Operacional: 7 anos de retenção de consentimento + registro de auditoria na região (dados da UE-residente da UE).
