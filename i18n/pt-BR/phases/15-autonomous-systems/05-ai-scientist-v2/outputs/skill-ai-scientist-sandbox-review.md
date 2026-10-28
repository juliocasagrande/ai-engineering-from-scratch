---
name: ai-scientist-sandbox-review
description: Lista de revisão de dois portões para as saídas de agentes do ciclo de pesquisa antes que qualquer coisa saia da caixa de areia.
version: 1.0.0
phase: 15
lesson: 5
tags: [ai-scientist, research-agent, sandbox, peer-review, disclosure]
---

Dado um resultado de pesquisa autônomo (hipótese, código, experimentos, números, esboço de papel) produzido por um ciclo de estilo AI-Scientist-v2, produzir uma revisão de dois portões: auditoria de caixa de areia (algo sai?) mais auditoria de pesquisa (é o trabalho som?).

Os dois portões são identificados diretamente nas auditorias abaixo: **Sandbox gate = item 1**O artigo 2.o **Research gate = items 2 (Experiment audit) + 3 (Polish audit)**Os itens 4 a 5 regem o que acontece depois de ambos os portões passarem.

Produzir:

1. **Sandbox gate.** Antes de qualquer artefato sair da caixa de areia:
   - Lista todas as ligações de rede feitas e o seu alvo.
   - Inventar todos os arquivos que o loop escreveu fora do seu diretório de trabalho.
   - Confirme a contenção do Docker / seccomp / gVisor para a execução completa.
   - Confirme que nenhum subprocesso escapou da supervisão da caixa de areia.
   Se algum cheque falhar, bloqueie a exportação; eleve para um humano.
2. **Experiment audit.** Leia o código da experiência, não o papel:
   - Verifique cada experimento que se alega ter sido executado e os números relatados são reprodutíveis.
   - Verifique se os experimentos falhados foram relatados como falhas, não re-enfrentados como resultados negativos após o fato.
   - Verifique se o rótulo "novidade" na ideia é resistente a uma pesquisa de literatura por um especialista em domínio humano.
3. **Polish audit.** Leia os números:
   - Certifique-se de que os dados de cada figura vieram de uma experiência registrada, não de uma reescritura em fase de poluição.
   - Os eixos, escalas e anotações confirmam que correspondem aos dados subjacentes.
   - Marque qualquer figura cuja legenda afirma mais do que os dados suportam.
4. **Disclosure plan.** Se o artefato for destinado à distribuição externa:
   - - Diz que o artefato é de autor de agente.
   - Indicar as ferramentas utilizadas (família de modelos, versão de ciclo).
   - Divulgar o revisor humano que verificou e o que verificou.
5. **Negative-release decision.** Se o artefato falhar em qualquer etapa de auditoria, o padrão é não liberar.

Rejeitos duros:
- Qualquer submissão que salte qualquer porta.
- Qualquer artefato onde os registos de execução do loop estão faltantes ou incompletos.
- Qualquer figura que não possa ser rastreada a uma execução específica de experimento.
- Qualquer alegação de novidade que um perito de domínio não tenha verificado.

Regras de recusa:
- Se a corrida não tiver Docker ou isolamento equivalente, rejeite e precise ser re-estruturada numa caixa de areia isolada.
- Se o usuário não puder produzir registos de execução para a fase do experimento, rejeite  o papel não pode ser revisado.
- Se o canal de distribuição proposto for um local de revisão por pares e o utilizador propõe não divulgar a autoria do agente, recusar e exigir a divulgação.

Formatos de saída:

Retorna um relatório de dois portões:
- **Sandbox gate verdict** (PASS/BLOCK, com justificação)
- **Research gate verdict** (Cobre auditoria de experimentação (2) e auditoria polaca (3)) (PASS / BLOCK / REQUIRES_EXPERT, com notas por verificação)
- **Disclosure plan** (nome do revisor humano)
- **Release decision** (liberar / manter / rejeitar)
- **Next action** (quem faz o quê até quando)
