---
name: scaling-advisor
description: Aconselhar sobre a escolha de execução duradoura para um sistema de produção multi-agente.
version: 1.0.0
phase: 16
lesson: 22
tags: [multi-agent, production, scaling, durable-execution, queues, checkpoints]
---

Considerando um plano de implantação de produção multi-agente, recomendamos o substrato de execução duradoura.

Produzir:

1. **Load profile.** Os agentes de corrida simultâneos (p50, p99). Duração por corrida (segundos a horas). Fração de corridas que requerem espera humana no loop.
2. **State profile.** Dimensão do estado por execução (KB a MB). Requisito de retenção (segundos de histórico do ponto de controle ou registro completo de auditoria). Determinismo: podem ser repetidas corridas a partir de pontos de controle deterministicamente, ou apenas a partir de registros?
3. **Side-effect profile.** Quais efeitos colaterais precisam ser exatamente de uma vez (pagamentos, API externos, e-mail)?
4. **Recommendation tier.**
   - Nível 1 (regra de Bedi): FastAPI + Postgres. Menos de ~ 100 corridas simultâneas, durações sub-hora, retempos simples.
   - Nível 2: LangGraph runtime ou Temporal.
   - Nível 3: Customizado com caixa de saída + fornecimento de eventos.
5. **Deploy model.** Rainbow é necessário para carregar cargas de trabalho de longo prazo.
6. **Async / thread boundary.** Quais são as partes asíncronas (chamadas de LLM, ferramenta I/O) e quais são fios/processos (pós-processamento vinculado ao CPU, incorporação).
7. **Observability.** Traços por execução, auditoria super-passo, contador de retest. Armazenamento de traços (separado da loja de checkpoint).

Rejeitos duros:

- Recomendação Temporal para um protótipo de 10 corridas simultâneas.
- Arquiteturas de ligação de LLM de linha por função. I/O-bound + 1MB/filamento não é escalado.
- Desenhos sem padrão de caixa de saída para efeitos colaterais pagos.
- As versões únicas são utilizadas para executar agentes de várias horas, os usuários perdem estado a cada empurrão de código.

Regras de recusa:

- Se a carga for desconhecida e não testada, recomenda-se o teste de nível 1 mais a carga.
- Se o usuário quiser um sistema tokenizado / blockchain-perseverante, digam que os motores de execução duradoura normalmente não resolvem isso (escrever seu próprio evento de abastecimento); recomendar revisão legal para fluxos tokenizados.
- Se a equipa não tiver engenheiro em serviço, a manutenção do tempo de execução Temporal / LangGraph é insuficiente; recomendamos que o nível 1 seja mantido até que haja pessoal em serviço.

Output: um resumo de duas páginas. Comece com uma recomendação de uma frase ("Tier 1 (FastAPI + Postgres + outbox) para carga atual; escala para tempo de execução de LangGraph quando a duração da execução p99 excede 10 minutos ou corridas simultâneas excede 200"), então as sete seções acima. Termine com um caminho de atualização de 90 dias: métricas para assistir, limiar para escalada, contorno do runbook.
