---
name: reviewer-agent
description: Estabeleça um papel de agente de revisão com uma rubrica de cinco dimensões que lê artefatos de construção, produz um relatório de revisão estruturada e inicia a revisão humana a partir de uma página escrita em vez de uma em branco.
version: 1.0.0
phase: 14
lesson: 39
tags: [reviewer, rubric, role-separation, second-loop, review-report]
---

Dado que um agente de construção já produz artefatos de banco de trabalho, levantar um revisor que os leia e escreve relatórios estruturados.

Produzir:

1. `agents/reviewer.md` com o sistema de revisão: acesso somente para leitura, rubrica de cinco dimensões, deve citar o caminho do artefato para cada pontuação.
2. `tools/reviewer.py` que carrega `ReviewerInputs` O resultado é o resultado da avaliação de cada dimensão.
3. `outputs/review/<task_id>.json` como o caminho do relatório de revisão canônica.
4. `docs/reviewer-rubric.md` A lista das cinco dimensões, a pergunta a que cada uma responde e as descrições de âncora 0-1-2.
5. Passo de CI que publica o relatório de revisão como um comentário de relações públicas sempre que uma tarefa de construção é encerrada.

Rejeitos duros:

- O espaço entre o construtor e o revisor é todo o sinal; seu colapso destrói a confiabilidade.
- Uma rubrica sem descrições de âncora por pontuação. "Pontuação de 0 a 2" sem âncora se desmorona em vibrações.
- Revisão de relatórios que omitem citações.
- Compartilhar o sistema do construtor.

Regras de recusa:

- Se o construtor não produz o relatório de verificação, recuse-se a executar o revisor.
- Se o projecto tiver menos de três tarefas fechadas, recuse-se a reivindicar que a rubrica seja calibrada.
- Se o revisor for convidado a marcar abaixo de uma confiança mínima, recuse e faça a superfície da dimensão incerta para um ser humano.

Estrutura de saída:

```
<repo>/
├── agents/reviewer.md
├── tools/reviewer.py
├── outputs/review/
│   └── <task_id>.json
├── docs/reviewer-rubric.md
└── .github/workflows/review.yml
```

Conclui com "o que ler a seguir" apontando para:

- Lição 40 para o pacote de entrega que combina verificação + revisão.
- Lição 41 para a tarefa de estilo real que exerce a separação de constructor/revisor de ponta a ponta.
- Lição 05 (Auto-refinamento e CRITIC) para a linha de base de auto-revisão de agente único esta lição melhora.
