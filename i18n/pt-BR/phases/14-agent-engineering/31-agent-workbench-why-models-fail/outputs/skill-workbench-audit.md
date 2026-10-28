---
name: workbench-audit
description: Auditar um repo para as sete superfícies de trabalho de agentes e relatar as que estão ausentes, parciais ou saudáveis antes de qualquer trabalho de agente começar.
version: 1.0.0
phase: 14
lesson: 31
tags: [workbench, audit, reliability, agent-engineering]
---

Dado um caminho do repositório e o produto agente que irá funcionar dentro dele, auditem as sete superfícies do banco de trabalho e produzam um relatório de prontidão.

As sete superfícies:

1. Instruções: um arquivo raiz que o agente lê primeiro (por exemplo: `AGENTS.md`), em breve, que conduz a regras mais profundas.
2. Estado: um arquivo durável e legível por máquina que registra tarefas, arquivos tocados, bloqueadores, ação seguinte.
3. Ámbito de aplicação: um contrato por tarefa que enumere arquivos permitidos, arquivos proibidos, critérios de aceitação, plano de reestruturação.
4. Feedback: um corredor que capta comando, stdout, stderr, código de saída e reintegra o resultado no loop.
5. Verificação: um portal que executa testes, feixe, verificação de tipo, fumo e confirma os critérios de aceitação.
6. Revisão: uma segunda passagem com um papel diferente, o construtor não pode marcar o seu próprio trabalho.
7. O "Handoff" é um artefato que resume o que mudou, o porquê, o que ficou e a próxima melhor ação.

Produzir:

- Uma pontuação por superfície: 0 faltando, 1 parcial, 2 saudáveis.
- Três prioridades ordenadas por alavancagem: qual a superfície faltante, se adicionada primeiro, elimina os modos de falha mais.
- A. `workbench_audit.json` Relatório legível por máquina mais um `workbench_audit.md` Resumo legível ao ser humano.
- Um parche de inicialização para a superfície mais fraca: a menor alteração de arquivo que move a pontuação de 0 para 1.

Rejeitos duros:

- Resultados "saudados" sem um processo de processo ou referência.
- Uma única superfície combinada de "agente de configuração".
- Salto de verificação porque os testes são lentos.

Regras de recusa:

- Se o repo não tiver nenhum comando de teste, rejeite a pontuação de verificação e deixe-a como uma constatação de bloqueio.
- Se o repo não tiver histórico de controle de versão, rejeite a pontuação de entrega e deixe-a como um achado bloqueador.
- Se o produto agente for executado como root ou com acesso a arquivos ilimitado, rejeite a pontuação de alcance até que uma caixa de areia ou lista de escrita seja definida.

Estrutura de saída:

```
workbench-audit/
├── workbench_audit.json
├── workbench_audit.md
├── patches/
│   └── <weakest-surface>.patch
└── README.md
```

Conclui com "o que ler a seguir" apontando para:

- Lição 32 para o layout mínimo de repo.
- Lição 33 para as instruções de superfície em profundidade.
- Lição 38 para o portal de verificação.
