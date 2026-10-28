---
name: handoff-generator
description: Gerar pacotes de transferência de final de sessão a partir de artefatos de banco de trabalho, produzindo tanto o Markdown leitível pelo ser humano quanto o JSON leitível pela máquina teclado para os sete campos canônicos.
version: 1.0.0
phase: 14
lesson: 40
tags: [handoff, generator, session-end, packet, next-action]
---

Dada uma mesa de trabalho (estado, veredicto, revisão, registro de feedback, dif), produzir um gerador de transferência de final de sessão conectado ao tempo de execução do agente.

Produzir:

1. `tools/generate_handoff.py` exposição `generate_handoff(snapshot) -> (markdown, payload)`- Não .
2. `outputs/handoff/<session_id>/handoff.md` e `handoff.json`- Não .
3. `handoff.schema.json` que abrange os sete campos necessários e o formato de cauda de feedback.
4. Escrito de gancho de final de sessão que executa o gerador e se recusa a fechar a sessão se algum campo estiver faltando.
5. `docs/handoff.md` A lista dos sete campos, as suas fontes e a política de corte.

Rejeitos duros:

- Uma transferência sem um `next_action`Os relatórios de status disfarçam-se de envenenamento na próxima sessão.
- Um gerador que escreve a mão o resumo.
- Um pacotamento de marcação que diverge do JSON. JSON é a fonte; marcação é um renderização de JSON.
- Uma cauda de feedback maior que 30 entradas. O registro completo está no controle de versão; o pacote deve permanecer pequeno.

Regras de recusa:

- Se o relatório de verificação estiver faltando, recuse-se a gerar o pacote.
- Se o relatório de revisão estiver ausente e se esperasse um revisor humano, recusar e exigir primeiro a aprovação da revisão.
- Se o resumo da diferença estiver vazio, mas a sessão durou mais de 5 minutos, surgir a anomalia antes de gerar; suspeitar de uma sessão em que não se tenha realizado nenhuma operação.

Estrutura de saída:

```
<repo>/
├── outputs/handoff/<session_id>/
│   ├── handoff.md
│   └── handoff.json
├── tools/generate_handoff.py
├── handoff.schema.json
└── docs/handoff.md
```

Conclui com "o que ler a seguir" apontando para:

- Lição 41 para exercício de ponta a ponta num aplicativo de amostra de estilo real.
- Lição 42 para embalar o gerador no pacote de banco de trabalho de pedra.
- Lição 29 (Production Runtimes) para cablar o final da sessão em fila, evento e trigger cron.
