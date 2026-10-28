---
name: verification-gate
description: Gerar um portal de verificação determinista que combina escopo, regra e artefatos de feedback em uma única verificação_report.json por tarefa, além de um fio CI que se recusa a fundir sem um veredicto verde.
version: 1.0.0
phase: 14
lesson: 38
tags: [verification, gate, deterministic, ci, override-log]
---

Tendo em conta os critérios de aceitação de um projecto e os artefatos existentes no banco de trabalho, produzir o portal de verificação e anular o registro de auditoria.

Produzir:

1. `tools/verify_agent.py` exposição `verify(task_id, artifacts) -> VerdictReport`Função pura, determinista, sem chamadas de LLM.
2. `outputs/verification/<task_id>.json` como a única fonte de veredicto da verdade.
3. `tools/override.py` que anexa as entradas de sobreposição assinadas a `outputs/verification/overrides.jsonl` (deve incluir razão, identificação de utilizador, timestamp, código de localização).
4. Fluxo de trabalho de informação que falhe `passed: false` e aparece no relatório em linha.
5. `docs/verification.md` Lista de cada cheque, a sua gravidade, o seu artefato de origem e a política de anulação.

Rejeitos duros:

- Um cheque que chama um LLM. O portão é a canalização determinista; o julgamento do LLM pertence ao revisor.
- Um caminho de desvio que o agente pode seguir sem uma entrada assinada.
- Um relatório de verificação que omita os caminhos dos artefatos consumidos.
- Os resultados da gravidade do bloco podem reduzir silenciosamente o fluxo de trabalho.

Regras de recusa:

- Se o projeto não tiver um comando de aceitação, recuse-se a enviar o portão até que exista um.
- Se o relatório de regra não existir, recuse-se a ignorar a verificação de regra; falha fechada.
- Se o registro de feedback não existir, recuse-se a ignorar a verificação de aceitação; os registros faltantes são, em si mesmos, um bloco.
- Se as entradas de sobreposição não forem controladas por versão, recuse-se a transmitir o caminho de sobreposição; as sobreposições fora do registro derrotam o portal.

Estrutura de saída:

```
<repo>/
├── tools/
│   ├── verify_agent.py
│   └── override.py
├── outputs/verification/
│   ├── overrides.jsonl
│   └── <task_id>.json
├── docs/verification.md
└── .github/workflows/verify.yml
```

Conclui com "o que ler a seguir" apontando para:

- Lição 39 para o agente crítico que retoma depois de um veredicto verde.
- Lição 40 para o gerador de transferência que inclui o veredicto no pacote.
- Lição 41 para executar o gate contra um modelo de aplicativo de estilo real.
