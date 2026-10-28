---
name: ai-sre-plan
description: Projetar um rollout de AI SRE para uma equipe  arquitetura de triagem multi-agente, runbooks estruturados, avaliação adversária, remediação automática estreita e postura de detecção preditiva.
version: 1.0.0
phase: 17
lesson: 23
tags: [ai-sre, multi-agent, runbooks, auto-remediation, adversarial-eval, datadog-bits-ai, neubird, predictive]
---

Dado o tamanho da equipe, o volume de incidentes, a maturidade de observabilidade e a tolerância ao risco, produzir um plano de SRE de IA.

Produzir:

1. Arquitetura. Multi-agente: supervisor + agente de registro + agente métrico + agente de livro de execução + portal humano.
2. Transformação do livro de execução. Mover de Confluência não estruturada para marcado estruturado com sintomas / hipóteses / verificar / seções de ação. versão em git.
3. A escolha de produto. Datadog Bits AI, Azure SRE Agent, NeuBird Hawkeye, Incident.io Autopilot, ou DIY.
4. Espetáculo de remediação automática. Set de segurança estreita (reinicialização de módulo, reimplementação, escala dentro de limites). Lista de negação explícita (topologia, código, IAM, banco de dados). Política como código.
5. Avaliação adversária, especificar dois modelos de acordo para uma remediação automática.
6. Posição de detecção preditiva. se considerar (resultado MIT 89%), nome a política de ativação  pager, pré-desagregação, auto-escala  senão é apenas um painel.

Rejeitos duros:
- Auto-remediação sem portal humano em grandes alterações.
- Os runbooks não estruturados como base de conhecimento.
- "Põe e esquece" enquadramento. Recusar explícitamente abranger o que é e não é autônomo.

Regras de recusa:
- Se o volume de incidentes for < 10/mês, rejeite a implantação completa de SRE  custo excede o benefício. Recomenda-se apenas runbooks estruturados.
- Se a observabilidade da equipe é imatura (logs insuperáveis, métricas escassas), rejeitar  AI SRE amplifica dados ruins.
- Se a equipe propõe "detecção preditiva → auto-remediação" como primeira característica, recuse-se a passar pela questão de política de ativação primeiro.

Resultado: um plano de uma página com arquitetura, plano de runbook, escolha de produto, escopo de remédio automático, porta adversária, postura preditiva.
