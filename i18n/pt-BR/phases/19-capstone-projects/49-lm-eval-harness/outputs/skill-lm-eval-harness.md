---
name: lm-eval-harness
description: Aproveite o modelo de avaliação de linguagem mínimo com especificação de tarefas JSONL, cinco métricas, adaptador intercâmbio e saída JSON do quadro de liderança.
version: 1.0.0
phase: 19
lesson: 49
tags: [evaluation, metrics, leaderboard, harness]
---

## Quando utilizar

Compare dois modelos, dois pontos de verificação ou dois modelos de instruções com um conjunto fixo de tarefas.

## Especificações de tarefas

Uma linha JSONL por exemplo:

```json
{"id": "ex-001", "prompt": "...", "targets": ["..."], "metric": "exact_match", "extras": {}}
```

Todos os exemplos de um arquivo compartilham uma métrica. O nome do arquivo é o nome da tarefa.

## Metricas

| Metric | Signature | Use for |
|--------|-----------|---------|
| exact_match | normalize lower + whitespace, equality | Arithmetic, factoid answers |
| substring_contains | target must appear in normalized prediction | Free-form generation with anchor words |
| multiple_choice | first letter match | A/B/C/D style questions |
| rouge_l | LCS F1 over tokenized text | Summary, paraphrase |
| code_exec | run prediction's `f` on io_pairs, count matches | Code generation |

Todas as métricas de retorno flutuam em [0,0, 1.0].

## Adaptador

```python
class Adapter(Protocol):
    name: str
    def generate(self, prompts: list[str]) -> list[str]: ...
```

O adaptador é o único código específico do modelo.

## JSON do quadro de liderança

String de esquema, timestamp, pontuações por tarefa e latência, média geral. Incluir registros por exemplo ao comparar corridas para que as regressões de nível de previsão sejam visíveis.

## Modos de falha

- Retorno métrico fora de [0, 1]: pontuação geral torna-se ininterpretável.
- Metricas misturadas em um arquivo de tarefa: incêndios de afirmação; manter uma métrica por arquivo.
- code_exec sem espaço de nomes restrito: execução arbitrária de código.
- Sem cadeia de esquema: evolução do formato quebra painéis de controle para baixo.
