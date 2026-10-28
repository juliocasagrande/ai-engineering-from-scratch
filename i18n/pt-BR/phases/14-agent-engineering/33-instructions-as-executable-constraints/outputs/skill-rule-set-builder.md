---
name: rule-set-builder
description: Interview a project owner, classify their existing prose instructions into five operational categories, and emit a versioned agent-rules.md plus a Python checker stub.
version: 1.0.0
phase: 14
lesson: 33
tags: [rules, instructions, constraints, checker, workbench]
---

Tendo em conta o repo e as instruções de prosa existentes (`AGENTS.md`- Não .`CONTRIBUTING.md`O processo de elaboração de um documento de trabalho (construído por um grupo de trabalho) é um processo de elaboração de uma regra de cinco categorias que o banco de trabalho pode executar.

As cinco categorias:

1. `startup` o que deve ser verdade antes do início do trabalho.
2. `forbidden`O que nunca deve acontecer.
3. `definition_of_done` o que prova que a tarefa está concluída.
4. `uncertainty`O que o agente faz quando não tem certeza.
5. `approval`- o que requer a assinatura humana.

Produzir:

1. `docs/agent-rules.md`com um .`##`Cada regra tem um título.`category`- Não .`check`, e uma descrição de uma linha.
2. `tools/rule_checker.py`com um `RuleChecker`classe que expõe um método por `check`Cada método requer um`TurnTrace`dataclass e retornos `bool`- Não .
3. `tools/rule_report.py`Corredor que carrega regras, corre o comprovador em um rastreamento, emite um `rule_report.json`- Não .
4. Um arquivo de notas de migração: quais linhas de prosa se tornaram quais regras, que foram retiradas como aspiracionais, porquê.

Rejeitos duros:

- Regras sem um`check`As regras de aspiração só pertencem aos documentos de incorporação, não ao conjunto de regras de banco de trabalho.
- Uma única regra de "tenha cuidado", especifique uma categoria e verifique ou remova.
- Os controlos de regras devem ser deterministas e baratos para poderem ser executados a cada turno.
- Arquivos de regra de mais de 200 linhas.`agent-rules.{startup,forbidden,done,uncertainty,approval}.md`e rota de um índice-mãe.

Regras de recusa:

- Se o produto agente não puder fornecer um `TurnTrace`(sem instrumentos), recusar a transferência do controlador até pelo menos `read_state_file`- Não .`edited_files`, e `tests_exit_code`são gravadas.
- Se as instruções existentes forem principalmente aspiracionais (> 50%), a descoberta antes de emitir regras será superficial.
- Se uma regra for adicionada por causa de um único incidente passado, anexe o identificador do incidente para que a revisão futura possa decidir se ainda é necessária.

Estrutura de saída:

```
<repo>/
├── docs/
│   └── agent-rules.md
├── tools/
│   ├── rule_checker.py
│   └── rule_report.py
└── docs/migration-notes.md
```

Conclui com "o que ler a seguir" apontando para:

- Lição 36 para contratos de âmbito de aplicação por tarefa que alargam a categoria proibida.
- Lição 38 para portas de verificação que consomem o relatório de regra.
- Lição 39 para o agente revisor que pontua o cumprimento das regras.
