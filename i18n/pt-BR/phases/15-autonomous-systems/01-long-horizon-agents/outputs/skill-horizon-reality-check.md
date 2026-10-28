---
name: horizon-reality-check
description: Given a task you want to hand to an agent, decide whether the current frontier's horizon covers it with enough margin.
version: 1.0.0
phase: 15
lesson: 1
tags: [autonomous-agents, metr, time-horizon, reliability, deployment]
---

Dado uma tarefa autónoma proposta (o que o agente deve fazer, quanto tempo um perito humano levaria, qual o custo da falha), produzir uma verificação da realidade sobre se o horizonte do modelo fronteiriço actual realmente o abrange.

Produzir:

1. **Expert-time estimate.**Se não conseguirem estimar o tempo de conclusão, recuse-os e redirecione-os para que primeiro medam uma pequena amostra.
2. **Headroom ratio.**Divida o horizonte de 50% METR do modelo escolhido pela estimativa de tempo de especialistas. Marque qualquer relação abaixo de 4x  com probabilidade de sucesso de 50%, você quer uma margem generosa. Em relação a 2x ou abaixo, recuse a implantação a menos que o HITL esteja no loop em cada ação significativa.
3. **Reliability budget.**Estimar o comprimento de trajetória nas chamadas de ferramenta, em seguida, calcular o sucesso de ponta a ponta na confiabilidade por passo 0,95, 0,99, 0,995. Se o comprimento da tarefa exceder o limiar de sucesso de 50% na sua confiabilidade por passo suposta, exigir pontos de verificação ou dividir a tarefa.
4. **Eval-vs-deploy adjustment.**Aplicar uma diferença de 20-40% entre o horizonte de referência e o horizonte de implementação contextual. Citar o estudo de alinhamento de 2024 da Anthropic ou o Relatório Internacional de Segurança da IA de 2026 ao justificar para as partes interessadas.
5. **Required controls.**Com base no headroom, enumere o conjunto mínimo de controles: limite de orçamento, limite de iteração, interruptor de eliminação, pontos de controle HITL, tokens canários e cronograma de auditoria de trajetória.

Rejeitos duros:
- Qualquer implantação em relação ao horizonte inferior a 2x sem HITL em cada ação consequente.
- Qualquer alegação de que um modelo "pode fazer" uma tarefa baseada apenas no horizonte do METR. O horizonte é a marca de 50% numa curva logística; falhas de cauda são garantidas.
- Tratar os horizontes do METR como um piso em vez de um teto.

Regras de recusa:
- Se o utilizador não puder estimar o tempo de expertos para a tarefa, recuse-se e peça-lhe que primeiro medra uma pequena amostra.
- Se a tarefa proposta custar mais do que o orçamento do usuário no pior dos casos, ao preço do modelo completo, recuse e recomenda controles orçamentais da lição 13 antes de prosseguir.
- Se o utilizador descrever uma tarefa que toca a ações irreversíveis (transações financeiras, dados de produção, e-mails para clientes) sem qualquer camada HITL, recusar.

Formatos de saída:

Retorna um breve memorando com:
- **Task summary**(uma frase)
- **Expert-time estimate**(com unidades)
- **Headroom ratio**(com número explícito)
- **End-to-end reliability estimate**(tabela a três taxas por etapa)
- **Minimum controls**- Não .
- **Go / hold / no-go**(veredicto explícito mais justificação de uma sentença)
