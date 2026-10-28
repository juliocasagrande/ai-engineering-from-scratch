---
name: dst-designer
description: Design a dialogue state tracker — schema, extractor, update policy, evaluation.
version: 1.0.0
phase: 5
lesson: 29
tags: [nlp, dialogue, task-oriented]
---

Dado um caso de utilização (domínio, línguas, abertura de vocabulário, necessidades de conformidade), saída:

1. Lista de domínios, slots por domínio, vocabulário aberto versus fechado por slot.
2. Extractor, baseado em regras, LLM com Pydantic, razão.
3. Política de atualização: Regeneração total/incremental; tratamento de correcção; tratamento de negação.
4. Avaliação: Objetivo comum: precisão em um conjunto de diálogos prolongados, precisão/recolha no nível de slots, confusão no slot mais difícil.
5. Fluxo de confirmação: quando pedir explicitamente ao utilizador para confirmar (ações destrutivas, extrações de baixa confiança).

Recusar DST apenas LLM para slots sensíveis à conformidade sem uma verificação secundária baseada em regras. Recusar qualquer DST que não possa reverter um slot na correção do usuário. Esquemas de bandeira sem tags de versão.
