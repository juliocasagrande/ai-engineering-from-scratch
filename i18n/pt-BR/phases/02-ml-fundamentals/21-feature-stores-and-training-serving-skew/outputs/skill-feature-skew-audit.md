---
name: skill-feature-skew-audit
description: Auditoria de um conjunto de características para viagens no tempo e distorções de formação
version: 1.0.0
phase: 2
lesson: 21
tags: [feature-store, point-in-time, training-serving-skew, leakage, backfill]
---

# Feature Skew Audit

Use esta habilidade quando um modelo tiver uma boa pontuação offline e pior na produção. Também use quando uma equipe adicionar uma loja de recursos e antes de um novo recurso entrar em vigor.

## Passo 1: Mapear os dois caminhos

Para cada característica, escreva duas linhas:

```text
training path: <source table> -> <transformation code> -> <join to labels>
serving path:  <source> -> <transformation code> -> <store or request-time compute>
```

Se as duas linhas tiverem nomes diferentes de código de transformação, marque o recurso "dois caminhos de código".

## Passo 2: Verifique o treinamento para viajar no tempo

- A ligação utiliza o timestamp da etiqueta, não apenas a chave da entidade.
- A junção toma a última linha com o tempo do evento na hora do rótulo ou antes dela.
- A combinação cai em filas mais antigas do que a TTL.
- As linhas de reposição ou de correcção têm um timestamp criado, e a junção ignora as linhas criadas após o tempo de etiqueta.
- As janelas de agregação terminam na hora do rótulo.

Teste rápido: contar as filas de treinamento cuja fila de características é mais tarde do que o rótulo.

## Passo 3: Compare as definições

Para cada característica, compare os dois caminhos nos seguintes pontos:

| Point | Question |
|---|---|
| Window edges | Is each window edge inclusive or exclusive in both paths? |
| Missing values | Do both paths use the same default for no history and for expired values? |
| Units and types | Same currency, same time zone, same integer or float type? |
| Rounding | Same rounding, at the same step? |
| Category mapping | Same vocabulary, same handling of unknown values? |

## Passo 4: Compare a frescura

- Qual é o valor da formação na data de sua marcação, em média e no máximo?
- Qual é o valor da porção no momento da solicitação, em média e no máximo?
- O TTL deve transformar valores antigos em padrões, não servi-los silenciosamente.

Um modelo que treinou valores até uma semana de idade pode comportar-se de forma diferente em valores frescos.

## Passo 5: Messa a desvio

1. Registre os valores de características que o caminho de serviço usou, com a entidade e o tempo de solicitação.
2. Recompõe as mesmas teclas com o caminho de treinamento.
3. Por característica, informe a taxa de desajuste e a diferença absoluta média.
4. Divida a causa com três comparações: leitura de armazenamento versus treinamento, computação nova versus treinamento, segundo caminho versus computação nova.

Marque uma característica quando mais de 1% dos valores diferem, a menos que a diferença seja uma lacuna documentada de frescura.

## Passo 6: Escrever o resultado da auditoria

```text
Feature: <name, version>
Paths: shared definition | two code paths
Time travel: none found | <rows affected and cause>
Definition gaps: <window edges, defaults, units, rounding>
Freshness: training <age>, serving <age>, TTL <days>
Measured skew: <mismatch rate, mean |diff|>
Fix: <move both paths to one registry definition | fix join | align default | align TTL>
```

Fixa ordem: primeiro remova a viagem no tempo, depois move os dois caminhos para uma definição, depois alinha a frescura.
