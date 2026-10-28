---
name: structured-output-designer
description: Desenhe um esquema JSON compatível com o modo estritamente compatível, além de um modelo Pydantic para um alvo de extração de texto livre, com rejeição de tipo e manipulação de tentativa de novo.
version: 1.0.0
phase: 13
lesson: 04
tags: [structured-output, json-schema, pydantic, strict-mode, extraction]
---

Dado um objetivo de extração de texto livre (facturas, currículos, bilhetes de suporte, resumos de pesquisa), produzir um contrato de extração pronto para produção: JSON Schema 2020-12, modelo Pydantic, manipulador de recusa e política de retest.

Produzir:

1. JSON Schema 2020-12. Todas as propriedades digitadas. `required` lista todas as propriedades. `additionalProperties: false` Em todos os objetos. Enums utilizados para conjuntos de valores fechados. `$ref`Não há ambiguidade . `oneOf` - Não . `anyOf`- Validado em conformidade com os requisitos do modo rigoroso do OpenAI.
2. BaseModel Pydantic v2. Espelho do esquema com tipos Python. `model_json_schema()` deve produzir um esquema equivalente a (1).
3. - Gestor de recusa. `Refusal(reason: str, category: str)` Lista das categorias: `safety`- Não . `input_mismatch`- Não . `insufficient_info`- Não .
4. Política de retest. Três formas de retest: a) injetar erros de validação e retestar uma vez (fora do modo rigoroso); b) aceitar a recusa como final (modo rigoroso); c) escalar para um modelo mais forte em recusa repetida.
5. Vectores de teste: dez entradas que cobrem caminho feliz, campos adversários, entrada parcial e um caso de recusa-trigger.

Rejeitos duros:
- Qualquer esquema com campos não digitalizados.
- Qualquer esquema faltando `additionalProperties: false`- Leia alucinações.
- Qualquer esquema usando `oneOf` Sem um campo discriminatório, decodificação ambígua.
- Qualquer modelo Pydantic sem o seu esquema JSON ida e volta verificado.

Regras de recusa:
- Se o domínio-alvo incluir dados de identificação pessoal sem finalidade documentada, recusar e encaminhar para a fase 18 (ética) para o argumento de base legal.
- Se o usuário pedir um esquema que não possa ser expresso no JSON Schema 2020-12 (por exemplo, gráficos arbitrários recorrentes), recuse e propor a relaxamento expressivel mais próxima.
- Se o objetivo de extração for "extrair dados estruturados de qualquer coisa", recuse e peça o domínio específico.

Resultado: um contrato de uma página com o esquema JSON, a classe Pydantic, a política de recusa e retentagem e os dez vetores de teste.
