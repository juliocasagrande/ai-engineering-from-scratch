---
name: state-schema
description: Gerar esquemas JSON específicos para o estado do agente e o painel de tarefas, um Python StateManager com escritos atômicos e um andaime de migração para que os arranhões do esquema não possam corromper o banco de trabalho.
version: 1.0.0
phase: 14
lesson: 34
tags: [state, schema, json-schema, atomic-writes, migrations]
---

Dado um repo e o produto do agente que corre dentro dele, produzir arquivos de estado de esquema-primeiro para o banco de trabalho.

Produzir:

1. `schemas/agent_state.schema.json` cobrindo as chaves necessárias, os valores de status permitidos, a disciplina array versus zero, e um `schema_version` Número inteiro.
2. `schemas/task_board.schema.json` cobrindo padrão de identificação de tarefa, proprietários autorizados, status autorizados e matrizes de aceitação.
3. `tools/state_manager.py` exposição `load`- Não . `commit`, e `update` com temp-and-rename atômico escreve.
4. `tools/migrate_state.py` Equipamento para o próximo esquema de choque, falha-loud se o arquivo é de uma versão desconhecida.
5. `agent_state.json` e `task_board.json` sementes em `schema_version: 1` E um novo atraso.

Rejeitos duros:

- Um esquema sem um `schema_version` As migrações não são opcionais.
- Permitir `null` onde é esperada uma matriz. `null` é um erro de tempo de escrita mascarado como dados.
- Um escritor que usa simples `open(path, "w")`A Atomic escreve apenas; os arquivos parciais corromperam a fonte da verdade.
- Armazenar tokens, transcrições de chat ou PII dentro do estado.

Regras de recusa:

- Se o repo não tem controle de versão, recuse-se a enviar arquivos de estado.
- Se o projecto não tiver pelo menos um comando de aceitação para validar o `done` A transição, recusa a `status: done` Valor enum. Adição `done` Sem um cheque de aceitação é teatro.
- Se o projeto pretende compartilhar o estado entre processos sem uma estratégia de bloqueio, a descoberta de superfície antes do envio; renomeamento atômico é necessário, mas não suficiente.

Estrutura de saída:

```
<repo>/
├── agent_state.json
├── task_board.json
├── schemas/
│   ├── agent_state.schema.json
│   └── task_board.schema.json
└── tools/
    ├── state_manager.py
    └── migrate_state.py
```

Conclui com "o que ler a seguir" apontando para:

- Lição 35 para o script de inicialização que chama o gerente no início.
- Lição 38 para o portal de verificação que diz estado para concluir o resultado.
- Lição 40 para o gerador de transferência que consome o mesmo esquema.
