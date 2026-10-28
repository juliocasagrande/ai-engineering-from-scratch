---
name: feedback-runner
description: Wrap shell commands with deterministic stdout/stderr/exit/duration capture, persist a JSONL record per command, and refuse to advance the agent loop when feedback is missing.
version: 1.0.0
phase: 14
lesson: 37
tags: [feedback, subprocess, runner, jsonl, loop-control]
---

Dado um projeto que executa comandos shell dentro de um loop de agente, produzir um runner de feedback e o JSONL que ele escreve.

Produzir:

1. `tools/run_with_feedback.py`exposição`run_with_feedback(command: list[str], agent_note: str, timeout_s: float) -> FeedbackRecord`- Não .
2. `feedback_record.jsonl`localização sob o banco de trabalho, um registro por linha.
3. `tools/feedback_loader.py`que retorna os registos N mais recentes para a tarefa ativa.
4. A.`loop_can_advance(record) -> bool`Ajudar o agente a ligar antes de reivindicar o sucesso.
5. Os testes abrangem: caminho de sucesso, saída não zero, tempo de saída, falta de binário, truncamento determinista de cabeça/cauda.

Rejeitos duros:

- `shell=True`- Em qualquer lugar do corredor.
- Truncation que depende do relógio de parede ou amostragem aleatória.
- Registros sem`duration_ms`As sondas lentas são o primeiro sinal de um banco de trabalho embuído.
- Um carregador que retorna uma lista ilimitada. Cap no último N ou paginate.

Regras de recusa:

- Se o projeto divulgar segredos através de um estudo, recuse-se a enviar o corredor sem um passo de redação.
- Se o projeto tiver comandos que podem ficar pendurados indefinidamente, recuse-se a enviar sem um prazo de entrega padrão e uma lista explícita de desbloqueio.
- Se o executor estiver dentro de um trabalhador com estado compartilhado, recuse-se a pular um bloqueio de arquivo em torno do apêndice JSONL.

Estrutura de saída:

```
<repo>/
├── feedback_record.jsonl
└── tools/
    ├── run_with_feedback.py
    ├── feedback_loader.py
    └── test_feedback_runner.py
```

Conclui com "o que ler a seguir" apontando para:

- Lição 38 para o portal de verificação que consome os registos.
- Lição 39 para o agente de revisão que lê os comentários quando marcou uma corrida.
- Lição 23 para as convenções OTel GenAI para adicionar ao lado da telemetria uma vez que o feedback é sólido.
