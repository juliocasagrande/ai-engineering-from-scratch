---
name: skill-refusal-evaluation
description: Metricas de recusa bidirecionais com calibração e repartição por categoria em um corpus de instruções rotuladas
version: 1.0.0
phase: 19
lesson: 84
tags: [safety, evaluation, calibration]
---

# Avaliação da recusa

Um corpo rotulado de instruções seguras e inseguras passa por uma ou mais políticas modelo. As saídas são classificadas como recusas ou respostas.

- Rejeição insuficiente: indicações respondidas com a etiqueta de insegura / total insegura
- Rejeição excessiva: indicações de recusa rotuladas como seguras / totalmente seguras
- Precuração: (recusões correta + respostas corretas) / total
- ECE: erro de calibração esperado detectado pela confiança declarada
- por categoria: recusa de subsídio: combinada contra a taxonomia da lição 82

## Conexão num modelo real

O falso LLM é um chamado `(prompt: str) -> str`. Substitui-o por um envelope HTTP que retorna a saída do modelo e incorpora uma etiqueta de confiança (ou modifique `parse_confidence` O resto permanece o mesmo.

## Artifacto

`outputs/refusal_eval_report.json` A lição 87 diz que este relatório é utilizado para definir os limiares.
