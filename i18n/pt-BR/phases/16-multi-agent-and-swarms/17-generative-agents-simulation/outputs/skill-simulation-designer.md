---
name: simulation-designer
description: Design a generative-agent simulation (Smallville-style) for a given scenario. Specifies memory schema, reflection cadence, plan horizon, spatial/social constraints, and evaluation metrics.
version: 1.0.0
phase: 16
lesson: 17
tags: [multi-agent, simulation, generative-agents, emergence, memory]
---

Dado um cenário que exige um comportamento emergente de uma população de agentes (simulação social, NPCs de jogos, ensaio de políticas, dinâmica de mercado), desenhe a simulação.

Produzir:

1. **Population size and heterogeneity.**N agentes; que compartilham um modelo base versus diferente; famílias rápidas; distribuição de papéis. Smallville usou 25 agentes homogéneos com personalidades individualizadas; populações maiores se beneficiam da heterogeneidade.
2. **Memory schema.**Campo por entrada: `(ts, kind, content, importance, embedding_ref, source_ids)`- constante de decadência recente; procedimento de pontuação de importância; métrica de relevância (cosina com modelo X incorporado). Política de retenção para compactação.
3. **Reflection cadence.**Trigger: soma da importância não processada > limiar, ou todas as observações N, ou tick periódico. Número de reflexões por trigger. Template de resposta de reflexão.
4. **Plan horizon.**Níveis de acção de dia/hora/dia. Que são obrigatórios; quais opcionais. Trigador de revisão: uma nova observação com um limiar de importância que contradiz o plano ativo.
5. **World model.**Gradeira espacial, gráfico social, restrições de recursos. O que constitui uma observação (linha de visão, conversa, notificação).
6. **Seed goals.**Os agentes são plantados com quais prioridades. Objetivos sobrepostos que podem competir; objetivos não competitivos que devem coexistir.
7. **Budget.**Chamadas de LLM por agente (observa + retira + reflete + plano + ato). Tokens esperados por tick por agente. Custo total de simulação para ticks T.
8. **Evaluation metric.**Crençabilidade (rator humano), taxa de realização de metas, eventos de coordenação contados, violações das normas espaciais como sinal de falha.

Rejeitos duros:

- Projetos sem codificação explícita de normas espaciais / sociais. A arquitetura os violará (falhas de loja fechada, banheiro único do Park 2023).
- Desenhos com memória mutável. A memória deve ser apenas apêndice; correções são novas entradas.
- Os projetos que executam reflexão a cada marcação. Isto é ineficiente no orçamento; a reflexão é cara e os gatilhos devem ser baseados em limiares.
- Simulações em N (> 50) sem estratégia de compactação de memória.

Regras de recusa:

- Se o cenário requer a execução de tarefas emergentes em vez de comportamentos sociais emergentes, recomende-se o supervisor / papéis / padrões primitivos em vez disso (Fase 16 · 05-08).
- Se o orçamento permite < 100 chamadas de LLM por tick total, recomendamos N = 3-5 com interações densas em vez de populações maiores.
- Se o cenário não se beneficiar da emergência (tarefa estritamente escrita), recomendamos ferramentas de agente único.

Resultado: um resumo de design de uma página. Comece com um resumo de uma frase ("Simulação de estilo Smallville: 15 agentes heterogêneos, reflexão na soma de importância > 120, horizonte de plano de 3 níveis, grade espacial com restrições de capacidade, medida por acreditável + eventos de coordenação. ") , em seguida, as oito seções acima.
