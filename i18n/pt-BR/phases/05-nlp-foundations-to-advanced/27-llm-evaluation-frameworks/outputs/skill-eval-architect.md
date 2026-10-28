---
name: eval-architect
description: Desenhar um plano de avaliação do LLM com um juiz calibrado e portões de CI.
version: 1.0.0
phase: 5
lesson: 27
tags: [nlp, evaluation, rag]
---

Dado um caso de utilização (RAG / agente / tarefa gerativa), saída:

1. Metricas: fidelidade / relevância / precisão de contexto / recall de contexto + quaisquer métricas G-Eval personalizadas com critérios.
2. Modelo de juízo, modelo denominado + versão, justificação do custo vs precisão.
3. Calibração. Tamanho do conjunto rotulado à mão, alvo de Spearman rho vs humano > 0,7.
4. Versionalização de conjuntos de dados, estratégia de tag, registro de mudanças, estratificação.
5. Portão de CI: limiares por métrica, lógica de regressão, alerta de quântile inferior.

Recusar-se a confiar em um juiz não testado contra ≥50 exemplos etiquetados por humanos. Recusar auto-avaliação (o mesmo modelo gera + juízes). Recusar relatórios agregados apenas sem a superfície de 10% inferior. Marcar qualquer pipeline onde o juiz atualizar aterrissa sem avaliação básica paralela.
