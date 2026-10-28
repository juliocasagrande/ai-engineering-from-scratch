---
name: chaos-plan
description: Projetar um plano de engenharia de caos LLM Verificar os pré-requisitos, construir quatro aviões, escolher ferramenta, começar com três experimentos seguros, fazer cumprir os portões de segurança de avião.
version: 1.0.0
phase: 17
lesson: 24
tags: [chaos-engineering, litmuschaos, chaosmesh, harness, llm-chaos, game-day]
---

Dada a pilha (Kubernetes / VMs / gerenciados), maturidade SLI / SLO, qualidade de observabilidade e maturidade da equipe em chamada, produz um plano de caos.

Produzir:

1. Verificar o SLI/SLO definido, a observabilidade com fios, o rollback automatizado, os runbooks estruturados, a rotação em chamada.
2. Quatro planos. Nomear as ferramentas para cada plano (controle, alvo, segurança, observabilidade).
3. Três experiências iniciais, começam com a capsula de morte, depois o provedor 429, depois a sobrecarga de memória, cada uma com limite de raio de explosão, duração, critério de sucesso.
4. Portas de segurança: taxa de queimação (> 2x prevista), raio de explosão (< 30% da frota), marcação de identificação de rastro, janelas de supressão.
5. Cadence, pequeno canário semanal, dia de jogo mensal, auditoria de resiliência trimestral.
6. Tooling. LitmusChaos (OSS, CNCF graduado), Chaos Mesh (OSS, CNCF sandbox), Harness Chaos (AI-assistido comercial), AWS FIS / Azure Chaos Studio (nativo gerenciado em nuvem).

Rejeitos duros:
- A produção de caos sem os cinco requisitos pré-requisitos.
- Experimentos sem tampas de raio de explosão.
- Experimentos sem marcação de identificação de rastreamento.

Regras de recusa:
- Se a equipe nunca executou um experimento bem sucedido em encenar, rejeite o caos de produção até que um seja verde em encenar.
- Se o volume de incidentes já for elevado (> 2 semanas), rejeite o caos adicionado  estabilizar-se primeiro.
- Se a equipa não tiver SLO, precise SLO antes de qualquer experimento.

Resultado: um plano de uma página com verificação de pré-requisitos, ferramentas de quatro planos, três experimentos iniciais, portas de segurança, cadência.
