---
name: rollback-rehearsal
description: Design a rollback-rehearsal test for a proposed autonomous workflow and audit the checkpoint backend for audit-trail persistence.
version: 1.0.0
phase: 15
lesson: 16
tags: [checkpointing, rollback, idempotency, eu-ai-act-article-14, durable-execution]
---

Tendo em conta um fluxo de trabalho autónomo de longo horizonte proposto, desenhe um teste de ensaio de retrocesso que comprova que a pilha de retrocesso + pré-condição + verificação + retrocesso funciona realmente de ponta a ponta e auditore o backend do checkpoint para a preparação do regulador.

Produzir:

1. **Rehearsal script.**Testes concretos que a) iniciam o fluxo de trabalho, b) o interrompem no meio do trabalho, c) retomam, d) afirmam os incêndios de ação exatamente uma vez, e) injetam uma falha de verificação, f) afirmam os incêndios de retrocesso e o estado é restaurado.
2. **Idempotency audit.**Confirmar que a chave de idempotencia é derivada do conteúdo da proposta (Lessão 15) e utilizar a lógica de comitamento para estados de execução explícitos (`pending`-> `executing`-> `committed`- Não .`failed` Reservar/bloquear pela chave de independência antes do efeito colateral e marcar `committed`só após a verificação dos efeitos secundários.
3. **Precondition inventory.**Lista todas as condições prévias que o fluxo de trabalho deve verificar novamente no tempo de compromissos.
4. **Verify inventory.**Para cada ação consequente, nomear a leitura específica que confirma o efeito colateral ocorrido. "Returned 200" não é aceitável.
5. **Rollback inventory.**Para cada ação consequente, classifique o rollback como operação dentro da banda, compensação ou alerta fora da banda.

Rejeitos duros:
- Fluxos de trabalho sem ensaios de retrocesso.
- Os controles de segurança que perdem dados no despliegue.
- Compromete caminhos onde o status é escrito após a execução, não antes.
- "Verified" indica que só verifica o código de devolução da chamada de ferramenta.
- Verificações de pré-condição que executam apenas no tempo proposto, não no tempo de compromisso.

Regras de recusa:
- Se o utilizador não executar o roteiro de ensaio pelo menos uma vez na fase de ensaio, recusar a implantação da produção.
- Se o usuário não puder produzir o esquema de armazenamento do ponto de verificação, recuse e precise de documentação do esquema primeiro.
- Se o fluxo de trabalho depender de um ponto de controlo em memória (sem persistência), recusar.

Formatos de saída:

Retorna um plano de ensaio com:
- **Test script outline**(pasos com afirmações)
- **Idempotency table**(compostação chave, ordem de redacção do estado)
- **Precondition table**(verificar, quando avaliado, consequência)
- **Verify table**(Ação, leia que confirma)
- **Rollback table**(ação, tipo, estado-alvo)
- **Backend attestation**(localização, sobrevivência-desenvolvimento y/n, consulta-pronta y/n)
- **Readiness**(produzir / montar / apenas para investigação)
