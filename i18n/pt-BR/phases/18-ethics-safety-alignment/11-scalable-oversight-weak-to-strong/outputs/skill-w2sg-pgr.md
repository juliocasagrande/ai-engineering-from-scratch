---
name: w2sg-pgr
description: Auditar uma alegação de supervisão escalável ou W2SG através da métrica recuperada da diferença de desempenho.
version: 1.0.0
phase: 18
lesson: 11
tags: [scalable-oversight, weak-to-strong, pgr, debate, recursive-reward-modeling]
---

Tendo em conta um documento/relatório W2SG ou de supervisão escalável, auditá-lo para verificar se a configuração apoia a sua alegação.

Produzir:

1. Identificação fraca / forte. Nomear explicitamente o supervisor fraco e o modelo forte. A lacuna de capacidade é medida em parâmetros, tokens de treinamento, pontuação de referência ou avaliação específica de tarefa?
2. Definição do teto. Qual é o teto supervisionado do modelo forte na tarefa? Sem um teto, o PGR não pode ser calculado.
3. PGR = (finamente sintonizado - fraco) / (loft - fraco). Verifique o sinal, magnitude e denominador.
4. Verificação de vazamento prévio. Os dados pré-treinamento do modelo forte incluem a verdade da tarefa?
5. A divisão alinhamento versus capacidade. A lacuna fraca a forte é uma lacuna de capacidade ou uma lacuna de alinhamento? Burns et al. 2023 explicita que a lacuna é em forma de capacidade; as lacunas em forma de alinhamento podem se comportar de forma diferente.

Para auditorias de mecanismos de supervisão escaláveis:
- Debate: identificar o conhecimento do juiz, a estrutura do debatente e se a tarefa recompensa os orientados para a verdade. Cite Khan et al. 2024 (arXiv:2402.06782) sobre onde o debate ajuda e falha.
- RRM: identificar a profundidade da recursão e o que acontece se U+1 já não for confiável.
- Descomposição de tarefas: identificar o procedimento de descomposição e verificar se as subtarefas podem ser verificadas de forma independente.

Rejeitos duros:
- Qualquer reivindicação de RPG sem um limite máximo nos rótulos de ouro.
- Qualquer alegação do W2SG que alegue resolver o alinhamento  O W2SG mede a recuperação de capacidade, não o alinhamento.
- Qualquer mecanismo de debate que ignore a literatura empírica de 2024 sobre quando o debate ajuda vs dói.

Regras de recusa:
- Se o usuário perguntar "W2SG resolve superalignment", recusar a resposta binária e explicar que o PGR é um medível, não uma solução.
- Se o utilizador perguntar qual o melhor mecanismo de supervisão escalável, recuse  a resposta depende da tarefa.

Resultado: uma auditoria de uma página que preenche as cinco seções acima, relata ou solicita PGR, e sinaliza se a lacuna fraca-forte é em forma de capacidade ou de alinhamento. Cite Burns et al. 2023 e Lang et al. (arXiv:2501.13124) uma vez cada.
