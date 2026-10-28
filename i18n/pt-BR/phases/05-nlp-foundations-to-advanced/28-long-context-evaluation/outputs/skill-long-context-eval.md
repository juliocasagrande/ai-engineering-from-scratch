---
name: long-context-eval
description: Design a long-context evaluation battery for a given model and use case.
version: 1.0.0
phase: 5
lesson: 28
tags: [nlp, long-context, evaluation]
---

Dados um modelo-alvo, comprimento do contexto-alvo e caso de utilização, saída:

1. Testes: Gradeira de profundidade × comprimento NIAH; RULER multi-hop; tarefa de domínio personalizada.
2. Profundidades 0, 0, 25, 0, 5, 0, 75, 1,0 em cada comprimento.
3. Metricas: taxa de passagem de recuperação; taxa de passagem de raciocínio; tempo para primeiro token; custo por consulta.
4. Cutoff: comprimento efetivo de recuperação (90% de aprovação) e comprimento efetivo de raciocínio (70% de aprovação).
5. Regressão, arame fixo, reiniciação em cada atualização do modelo, delta de superfície.

Recusar confiar em uma janela de contexto apenas do modelo de cartão. Recusar avaliação apenas NIAH para qualquer carga de trabalho multi-hop. Recusar fornecedor auto-relatado de longo contexto pontuações como evidência independente.
