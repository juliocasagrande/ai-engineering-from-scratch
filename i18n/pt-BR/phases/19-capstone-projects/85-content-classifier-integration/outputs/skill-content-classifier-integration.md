---
name: skill-content-classifier-integration
description: Three output-side classifiers (toxicity, PII, instruction-leakage) behind a single severity router with block, redact, warn, log actions
version: 1.0.0
phase: 19
lesson: 85
tags: [safety, classifier, output-filter]
---

# Integração do classificador de conteúdo

Três classificadores, um roteador, quatro ações.

## Estrutura do veredicto

```text
ClassifierVerdict
  name: str
  severity: none | low | medium | high
  score: float in [0, 1]
  findings: list[str]
```

## Tabela de acção

| Severity | Action | Effect |
|---|---|---|
| high | block | output replaced by a policy refusal |
| medium | redact | per-classifier redactors applied in order |
| low | warn | output shipped with a soft notice appended |
| none | log | output shipped unchanged, verdict logged |

## Comportamento por classificador

- toxicidade - termos de assédio com limite de espaço em branco e uma pequena verificação de negação na janela esquerda; redacta para `[redacted-language]`
- pii - e-mail, telefone, SSN, cartão Luhn-validado, IPv4; severidade aumenta para SSN e cartão; redacta cada forma para uma etiqueta
- instrução-vazamento - trigram cosino vs um sistema conhecido de urgência; escalas de gravidade com sobreposição; redacta a primeira linha de urgência do sistema

## Artifacto

`outputs/classifier_report.json`Carrega verbo de acção, gravidade, saída editada e lista completa de veredicto por caso.
