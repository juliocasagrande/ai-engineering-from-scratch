---
name: runtime-shape
description: Pick a production runtime shape (request-response, streaming, queue, event, cron, durable) and wire observability.
version: 1.0.0
phase: 14
lesson: 29
tags: [production, runtime, queue, event, durable, observability]
---

Dada uma classe de tarefas (durada esperada, contagem de etapas, tipo de gatilho, orçamento de latência), escolha a forma de tempo de execução.

Decisão:

1. < 30s, espera do utilizador -> **request-response**- Não .
2. UX progressiva ou voz -> **streaming**- Não .
3. Minutos a horas, o usuário não espera -> **queue-based**- Não .
4. Reativa a eventos externos -> **event-driven**- Não .
5. Serviços de limpeza periódica -> **cron**- Não .
6. Qualquer um dos acima onde o custo de reinicialização é alto -> adicionar **durable execution**- Não .

Produzir:

1. O andaime de forma na tua pilha.
2. Observabilidade: OTel GenAI (Lessão 23), cablado de backend (Lessão 24).
3. Para fila: DLQ + política de retentagem + métrica de profundidade da fila.
4. Para evento: registro de assinantes explícito + caminho de repetição.
5. Para cron: arquivo de bloqueio ou bloqueio distribuído para evitar corridas sobrepostas.
6. Para duradouro: backend de checkpointer + semântica de resumo.

Rejeitos duros:

- HTTP sincrono para uma tarefa de 5 minutos. Os usuários desligam; os trabalhadores se acumulaem.
- Em fila sem DLQ. Os empregos falhados desaparecem.
- Trabalho de fundo sem rastro de exportação.
- "Não há estado duradouro, vamos tentar novamente". Horizontes longos devem ser um ponto de controle.

Regras de recusa:

- Se o produto tiver requisitos de repetição SLA +, rejeite topologia de enxame + tempo de execução não duradouro.
- Se a tarefa for vinculada ao cumprimento, rejeite a execução de eventos sem rastro de auditoria.
- Se o usuário quiser cron + sem bloqueio, recuse. As corridas cron superpuestas são duplicadas no melhor dos casos, corrupção de dados no pior.

Resultado: andamio de execução + ganchos de observabilidade + README com SLA, política de retest, escolha de checkpointer. Terceiro com "o que ler a seguir" apontando para a lição 23 (OTel), lição 24 (observabilidade) ou lição 17 (Agentes gerenciados para a longa duração hospedada).
