---
name: rsi-cycle-pause-spec
description: Specify the conditions under which an RSI pipeline must pause and wait for human review before the next cycle.
version: 1.0.0
phase: 15
lesson: 7
tags: [rsi, self-improvement, alignment, pause-threshold, rsp]
---

Considerando um pipeline proposto de auto-melhoria recursiva, produzir uma especificação de pausa: as condições explícitas que interrompem o ciclo para inspeção humana antes do início do próximo ciclo.

Produzir:

1. **Cycle-level thresholds.**Para cada eixo mensurável (pontuação de capacidade, pontuação de alinhamento, orçamento, comprimento de trajetória, utilização de recursos), define um limiar numérico cuja travessia pausa o ciclo.
2. **Cycle-over-cycle deltas.**Defina limites sobre o quanto um eixo pode se mover em um único ciclo. Um salto de capacidade de 30% ou mais em um ciclo é quase sempre um sinal de jogo de avaliador; pausa e auditoria.
3. **Misalignment gap.**Compute capacidade-menos-alinhamento após cada ciclo. Se a diferença se ampliar em mais de X (operador-conjunto), pausa. Esta é a métrica do simulador em `code/main.py`Exercícios.
4. **Regression watch.**Se um eixo cair mais do que Y em um ciclo, pause. Regressões de capacidade muitas vezes seguem ondas; pegá-los impede a aceleração de progressos falsos.
5. **Human resumption contract.**Antes de o ciclo retomar após uma pausa, exigir que um ser humano nomeado reviste o gatilho de pausa, redefinir os limiares se for caso disso e registar a decisão na trilha de auditoria fora do tubo.

Rejeitos duros:
- Qualquer oleoduto que possa retomar após uma pausa sem ação humana.
- Qualquer limiar que dependa do próprio avaliador interno do loop (o agente pode jogar).
- Qualquer pipeline cujo limite pode ser editado pelo agente.

Regras de recusa:
- Se o utilizador não puder nomear os limiares antecipadamente, recuse-se.
- Se o oleoduto não tiver um avaliador externo (fora do circuito), a detecção de regressão e de surto de rejeição  requer uma visão externa.
- Se o contrato de reabertura proposto for "notificar a equipa e continuar depois de 24 horas", recusar.

Formatos de saída:

Retorna uma especificação de uma página com:
- **Axes and thresholds**(quadro)
- **Cycle-delta limits**(quadro)
- **Misalignment gap formula and threshold**
- **Regression limits**
- **External evaluator**(o que é, quando corre)
- **Resumption contract**(nome do proprietário, lista de verificação, destino do registro)
- **Sign-off line**(que é o proprietário da invariante de pausa)
