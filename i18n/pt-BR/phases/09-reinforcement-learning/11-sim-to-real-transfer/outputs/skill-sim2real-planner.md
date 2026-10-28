---
name: sim2real-planner
description: Plan a sim-to-real transfer pipeline for a given robot + task, covering DR, SI, and safety.
version: 1.0.0
phase: 9
lesson: 11
tags: [rl, sim2real, robotics, domain-randomization]
---

Dada uma plataforma robótica, uma tarefa e acesso a tempo real de hardware, saída:

1. Inventário de lacunas na realidade: fontes suspeitas classificadas por impacto esperado (contato, detecção, atraso de ativação, visão).
2. Parâmetros DR, lista exacta, intervalos, distribuição, justifica cada intervalo contra medições reais.
3. Passo SI. Que parâmetros medir; método de medição.
4. O professor/aluno dividido: que informação privilegiada o professor usa; que obs o aluno usa.
5. Limite de baixo nível, paradas de emergência, controlador de backup.

Recusar-se a implantar sem (a) um teste de simulação de variante de tiro zero, (b) um escudo de segurança, (c) um plano de retrocesso.
