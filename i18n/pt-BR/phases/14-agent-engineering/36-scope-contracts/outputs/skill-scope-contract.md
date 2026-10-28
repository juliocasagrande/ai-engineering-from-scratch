---
name: scope-contract
description: Gerar contratos de alcance por tarefa com globos permitidos/proibidos, critérios de aceitação e plano de retrocesso, além de um verificador global-consciente preparado para CI que funciona em cada agente diferencial.
version: 1.0.0
phase: 14
lesson: 36
tags: [scope, contract, globs, diff-check, ci]
---

Tendo em conta uma descrição da tarefa e um layout de repo, produzir um contrato de âmbito e um verificador de diferença.

Produzir:

1. `scope_contract.json` Para a tarefa com campos: `task_id`- Não . `goal`- Não . `allowed_files` (globes), `forbidden_files` (globes), `acceptance_criteria`- Não . `rollback_plan`- Não . `approvals_required`- Não .
2. `tools/scope_check.py` que toma um caminho de contrato e uma lista de arquivos tocados e retorna um `ScopeReport` Mais uma saída não zero em qualquer violação.
3. Passo CI (`.github/workflows/scope-check.yml` O sistema de verificação de fusão de diferença (ou equivalente) é executado.
4. `outputs/scope/closed/<task_id>.json` Convênios de arquivo, por isso, contratação de nave com o histórico de mudanças.

Rejeitos duros:

- Um contrato sem `forbidden_files`O espaço negativo faz parte do contrato.
- Um contrato que lista caminhos brutos em vez de globos para diretórios de código.
- A. `rollback_plan` campo vazio ou "ver runbook".
- As aprovações enumeradas como "casos a casos". Os limites de aprovação devem ser numerosos.

Regras de recusa:

- Se a descrição da tarefa não restringir uma região do repo, recusar a autorização `allowed_files` Só a partir da descrição.
- Se o repo não tiver comando de teste, recusar adicionar `acceptance_criteria` Um contrato que não pode ser verificado é um desejo.
- Se o tempo de execução do agente não puder respeitar os limites de aprovação (sem ser humano no circuito), suprima a lacuna antes da expedição; o escopo de infiltração nas ações requeridas pela aprovação será o fracasso dominante.

Estrutura de saída:

```
<repo>/
├── scope_contract.json
├── outputs/scope/closed/
│   └── T-XXX.json
├── tools/
│   └── scope_check.py
└── .github/
    └── workflows/
        └── scope-check.yml
```

Conclui com "o que ler a seguir" apontando para:

- Lição 37 para feedback de tempo de execução que liga comandos voltar ao contrato.
- Lição 38 para o portal de verificação que consome o relatório de âmbito.
- Lição 39 para o agente revisor que audita o arquivo de contratos fechados.
