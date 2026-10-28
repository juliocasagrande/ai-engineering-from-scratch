---
name: vla-action-format-picker
description: Pick an action format (discrete bin, FAST, flow-matching, dual-system) and VLA family (RT-2, OpenVLA, π0, GR00T) for a robot task.
version: 1.0.0
phase: 12
lesson: 21
tags: [vla, rt-2, openvla, pi0, groot, action-tokenization]
---

Dada uma tarefa robótica (manipulação, navegação, humanoide de todo o corpo), contagem DOF, exigência de taxa de controle e restrição de computação, escolha um formato de ação e uma família VLA.

Produzir:

1. Formatos de acção: bin discretos para tarefas simples de um braço, FAST para trajetórias sensíveis à velocidade, combinação de fluxo para um controlo contínuo e suave, sistema duplo para humanoides.
2. RT-2 (cerrado), OpenVLA (aberto 7B), π0 (fluxo aberto), GR00T N1 (humanoide de sistema dual aberto).
3. Fasibilidade da taxa de controlo. A correspondência do formato de transmissão para o controlo necessário em Hz. O disco discreto não pode fazer mais de 10 Hz num modelo 7B.
4. Mix de dados de treinamento. Co-fine-tune ratio (web VQA: robot). Começar a 0,5:1, sintonizar por tarefa.
5. LoRA em ~500-1000 demos de tarefas; perfeito em ~10 mil demos.
6. Portas de segurança, verificações de camada de controlo exigidas fora do VLA.

Rejeitos duros:
- Recomendo VLA sem especificação de camada de segurança.
- A reivindicação de tokenization discretos-bin é rápido o suficiente para o controlo de 30 Hz.
- Propõe a combinação de fluxos sem restrições de suavidade adequadas.

Regras de recusa:
- Se o requisito de velocidade de controlo for superior a 50 Hz num modelo <=7B com formato de bin discretos, rejeite; recomende-se π0 ou uma cabeça especializada.
- Se o robô tiver > 30 DOF (humanoide), rejeite arquiteturas de fase única; precise de sistema duplo (GR00T).
- Se o orçamento não puder permitir um pré-treino em escala Open X-Embodiment, rejeite o VLA desde o zero; recomende ajustar o OpenVLA.

Resultado: plano de uma página com formato de ação, seleção de VLA, verificação de taxa de controle, mistura de co-fina-tune, portas de segurança.
