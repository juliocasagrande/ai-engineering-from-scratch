---
name: skill-constitutional-rules-engine
description: Declarative YAML rules engine for output constraints with severity, explanation, fixer operations, and structured diff
version: 1.0.0
phase: 19
lesson: 86
tags: [safety, rules, constitutional]
---

# Regras constitucionais Motor

Uma constituição é um arquivo da YAML.`name`- Não .`severity`(baixo, médio, alto),`applies_when`(predicado), `must`(predicado), `explanation`, e opcionais `fix`- Não .

## Predicados

Atômico:

- `contains_regex`- Não .`not_contains_regex`
- `starts_with_regex`- Não .`ends_with_regex`
- `max_words`- Não .`min_words`

Componente:

- `all_of: [...predicates]`
- `any_of: [...predicates]`
- `not_: predicate`

## Operações fixas

- `append_if_missing: <suffix>`
- `prepend_if_missing: <prefix>`
- `replace_regex: { pattern: <regex>, replacement: <text> }`

## Motor de saída

`Engine.evaluate(text) -> EngineReport`Retorna um `RuleResult`por regra com `status`em `pass`- Não .`violation`- Não .`not_applicable`- Não .`report.violations()`filtros de violações e `report.max_severity()`Retorna a pior gravidade presente.

## Artifacto

`outputs/rules_report.json`O Comité de Administração da União Europeia (CE) deve apresentar uma proposta de directiva relativa à aplicação da directiva relativa à protecção dos consumidores.
