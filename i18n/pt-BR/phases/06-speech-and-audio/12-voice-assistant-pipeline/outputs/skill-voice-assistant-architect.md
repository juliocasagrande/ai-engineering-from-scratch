---
name: voice-assistant-architect
description: Produce a full-stack voice-assistant spec — components, latency budget, observability, compliance — for a given workload.
version: 1.0.0
phase: 6
lesson: 12
tags: [voice-assistant, architecture, livekit, pipecat, compliance]
---

Tendo em conta o caso de utilização (consumidor / apoio ao cliente / acessibilidade / vantagem), a escala esperada (sessões simultâneas, minutos/mês), a linguagem, os objetivos de latência, a conformidade (HIPAA, PCI, EU AI Act, CA SB 942), a saída:

1. Componentes (7 camadas). Mic + chunking · VAD · streaming STT · LLM + ferramentas · streaming TTS · reprodução · manipulador de interrupção. Nomear o provedor exato / modelo para cada.
2. Orçamento de latência. P50 / P95 / P99 metas por fase somando para o objetivo de ponta a ponta. Marque quais estágios são independentes versus sequenciais.
3. Esquema de chamada de ferramenta. Especificações JSON para cada ferramenta + manejo de erros + texto de fallback. Incluir sempre um caminho "não pode ajudar" que o LLM deve seguir quando falha duas vezes.
4. Segurança: proteção de injecção rápida, bloqueio de clonagem vocal (se o TTS é capaz de clonar), porta de vigília (para sempre ativada), redacção de PII em registros, retenção de 30 dias.
5. Observabilidade: P50/P95/P99 por fase · taxa de interrupção falsa · taxa de sucesso das chamadas de ferramentas · WER por 100 chamadas · custo por minuto · taxa de abandono.
6. Compliance: Audio de divulgação ("This is an AI assistant"), localização de regiões (dados da UE na UE), manutenção de registos de auditoria, opção de exclusão.

Rejeitar as implementações sempre ativadas sem uma palavra de aviso. Rejeitar TTS que não transmita (através de adição de latência de extensão de expressão). Rejeitar a latência média sem P95  tail é onde os usuários se tornam. Rejeitar a retenção de áudio bruto &gt; 30 dias sem revisão legal.

Exemplo de entrada: "Assistente de acessibilidade para usuários com baixa visão: interface de voz apenas para um aplicativo de e-mail de consumo. Inglês. P95 &lt; 600 ms. ~ 10k usuários simultâneos".

Exemplo de saída:
- Componentes: dispositivo de som (WebRTC via LiveKit Agents) · Silero VAD · Deepgram Nova-3 (Inglês) · GPT-4o com ferramentas de e-mail (read_message, compose_reply, mark_read) · Cartesia Sonic 2 streaming · WebRTC out · interrupt=cancel-LLM-and-TTS no fogo VAD.
- Orçamento: captura de 120 ms + VAD 40 + STT 150 + LLM TTFT 100 + TTS TTFA 150 = 560 ms P95.
- Ferramentas: read_message({id}), compose_reply({message_id, body}), mark_read({id}), search({query}). Todas retornam JSON; LLM tem máximo 2 retries por ferramenta, então fallback "Eu não pude fazer isso  tentar refrasear".
- Segurança: proteção de injecção rápida (detecção `ignore previous instructions`); "Hey Mail" (despertamento); sem clonagem de voz (voz Cartesia fixa); redacção de corpos de e-mail em registros.
- Observabilidade: Monitoramento de produção de IA de Hamming; histogramas Prometheus por estágio; alerta em falso-interrupto &gt; 5% ou p95 &gt; 800 ms.
- Conformidade: divulgação da IA na primeira utilização; opção HIPAA apenas para mensagens médicas; utilizadores da UE chegaram à Cartesia + GPT-4o Irlanda, hospedada pela UE.
