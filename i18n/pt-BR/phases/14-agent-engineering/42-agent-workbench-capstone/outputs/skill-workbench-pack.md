---
name: workbench-pack
description: Generate a project-tuned drop-in agent workbench pack — rules sharpened to the team's history, scope globs matched to the repo, rubric dimensions extended with one domain-specific entry.
version: 1.0.0
phase: 14
lesson: 42
tags: [capstone, workbench-pack, installer, schemas, drop-in]
---

Dado um repo, o histórico de incidentes da equipa, e o produto do agente a correr dentro dele, emitem um agente sintonizado, um banco de trabalho e um instalador.

Produzir:

1. `agent-workbench-pack/`Directório correspondente ao layout canônico: AGENTS.md, docs/, schemas/, scripts/, bin/, README.md, VERSION.
2. A.`bin/install.sh`que se recusa a crampar uma embalagem existente sem`--force`E escreve.`.workbench-version`- Para o repo alvo.
3. Versões de projetos ajustados de `agent-rules.md`(com pelo menos uma regra por categoria derivada dos últimos seis incidentes da equipa),`reviewer-rubric.md`(com uma sexta dimensão de domínio), e `scope_contract.schema.json`(com globos específicos de projectos).
4. A.`lint_pack.py`O texto que falha na derivação entre os textos e os esquemas ou entre a versão e os esquemas"`schema_version`- Não .
5. Integração opcional de CI que instala o pacote em ramos de demonstração e executa o portal de verificação contra uma tarefa conhecida.

Rejeitos duros:

- Um pacote contendo tarefas específicas de projeto.
- Um pacote ligado a um único fornecedor SDK. apenas framework-agnostic; SDK cablagem é o trabalho do repo alvo.
- Um instalador que muda os arquivos do estado.
- Regras sem função de controlo correspondente.

Regras de recusa:

- Se o histórico de incidentes estiver vazio, recuse-se a enviar um sintonizado.`agent-rules.md`Use o padrão canônico e superficial o espaço.
- Se o CI do repo alvo for incompatível com a instalação (não `.github/workflows/`, sem equivalente), recusar o passo CI opcional e documentar o caminho manual.
- Se a equipa usar um garfo privado da embalagem, recuse-se a escrever um instalador público.

Estrutura de saída:

```
agent-workbench-pack/
├── AGENTS.md
├── docs/
├── schemas/
├── scripts/
├── bin/install.sh
├── lint_pack.py
├── VERSION
└── README.md
```

Conclui com "o que ler a seguir" apontando para:

- Lição 41 para o índice de referência antes/após esta embalagem melhora.
- Lição 30 (Driven-Eval Agent Development) para o ciclo de avaliação que consome os veredictos do grupo.
- [SkillKit](https://github.com/rohitg00/skillkit)para distribuir o pacote entre 32 agentes de IA.
