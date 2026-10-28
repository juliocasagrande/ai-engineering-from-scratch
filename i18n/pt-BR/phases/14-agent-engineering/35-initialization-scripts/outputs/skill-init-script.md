---
name: init-script
description: Interview a project and emit a deterministic init_agent.py with five probes plus a CI workflow that refuses to launch the agent if any probe fails.
version: 1.0.0
phase: 14
lesson: 35
tags: [init, probes, ci, workbench, fail-loud]
---

Dado um repo, o produto agente e sua superfície de dependência produzem um script de inicialização e um cablagem CI específicos para o projeto.

Produzir:

1. `tools/init_agent.py`com estas sondas: versão de tempo de execução, dependências listadas, resolubilidade de comando de teste, ambiente necessário, estado de arquivo de frescura.
2. `init_report.json`O esquema é documentado ao lado do script.`(name, status: pass|warn|fail, detail)`- Não .
3. `.github/workflows/agent-init.yml`(ou equivalente) que executa o script e bloqueia o trabalho do agente em qualquer sonda de gravidade de falha.
4. A.`pre-task`O agente de execução pode ligar antes de cada sessão começar.
5. Documentação em `docs/init.md`Uma lista de todas as sondas, a sua gravidade e como corrigir uma falha.

Rejeitos duros:

- Os sondas que chamam a rede sem um tempo de espera.
- Essonda que requer chamadas de LLM.
- Um código de saída não zero que a embalagem engole.
- Os sondas que tocam o estado sem idempotencia, duas corridas seguidas devem produzir relatórios idênticos.

Regras de recusa:

- Se o projeto não tiver comando de teste, recuse-se a enviar o script. Adicione a lacuna à auditoria do banco de trabalho em vez disso.
- Se a lista contém segredos, o roteiro imprimirá, recusará e forçará a redação.
- Se uma sonda demora mais de três segundos em uma corrida seca, a descoberta do tempo deve ser exposta antes de ser enviada.

Estrutura de saída:

```
<repo>/
├── tools/
│   ├── init_agent.py
│   └── pre_task.sh
├── docs/
│   └── init.md
└── .github/
    └── workflows/
        └── agent-init.yml
```

Conclui com "o que ler a seguir" apontando para:

- Lição 36 para o contrato de âmbito de aplicação por tarefa que utiliza os dados do relatório init `repo_paths`- Não .
- Lição 37 para o loop de feedback de tempo de execução que consome o comando de teste resolvido.
- Lição 38 para o portal de verificação que depende da passagem das sondas.
