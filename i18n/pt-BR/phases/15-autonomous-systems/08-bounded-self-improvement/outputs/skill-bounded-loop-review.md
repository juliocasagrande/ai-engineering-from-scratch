---
name: bounded-loop-review
description: Audit a proposed bounded self-improvement loop against the four-primitive stack (invariants, anchor, multi-objective, regression detection).
version: 1.0.0
phase: 15
lesson: 8
tags: [bounded-self-improvement, invariants, alignment-anchor, rsi-safety]
---

Tendo em conta um ciclo de auto-melhoria proposto, pontua-o contra os quatro primitivos delimitantes identificados pelo Workshop RSI ICLR 2026 e produz uma análise de lacunas concreta.

Produzir:

1. **Invariant inventory.**Lista todas as invariantes que o loop impõe. Para cada um, nome (a) o que é verificado, (b) onde o controle é executado (a entrada / saída do agente alcança), (c) o que uma violação faz (refusão dura, pausa, apenas registro).
2. **Anchor identification.**Nomear a âncora de alinhamento (declaração objetiva, constituição, descrição de intenção). Indicar a sua localização de armazenamento e verificar que o loop não pode editá-la.
3. **Multi-objective axes.**Lista todos os eixos que o loop avalia. Confirme que a segurança, a justiça e a robustez estão presentes ao lado do desempenho. Um loop de um único eixo falha nesta verificação.
4. **Regression policy.**Indique a janela histórica, a tolerância por eixo e o que acontece quando uma queda é detectada.
5. **Gap analysis.**Para cada primitivo faltante, prevê qual classe de falha surgirá primeiro. Invariantes faltantes → capacidade contrabandeada ou deriva de ferramenta. Ancor faltante → reinterpretação objetiva.

Rejeitos duros:
- Qualquer ciclo com invariantes zero.
- Qualquer ciclo sem uma âncora de alinhamento fora da superfície de edição.
- Qualquer ciclo que otimize uma única pontuação escalar.
- Qualquer ciclo cuja verificação de regressão lê apenas a partir de seu próprio histórico (o ciclo define "normal").

Regras de recusa:
- Se o usuário tratar "ainda não quebrou" como evidência de segurança, recusar e exigir um design explícito de porta antes de qualquer computação ser gasto.
- Se o utilizador não puder produzir a lista de invariantes em 15 minutos, rejeite  o ciclo não tem invariantes.
- Se o ciclo for proposto para ser executado em produção (afetando usuários reais ou infraestrutura) sem os quatro primitivos, recusar e exigir a fase com monitoramento primeiro.

Formatos de saída:

Retorna uma revisão com pontuação com:
- **Invariant score**(0-5 com lista explícita)
- **Anchor score**(0-5 com método de armazenamento e verificação)
- **Multi-objective score**(0-5 com eixos listados)
- **Regression score**(0-5 com tolerância e janela)
- **Gap analysis**(primeira falha prevista, plano de mitigação)
- **Deployment readiness**(produzir / montar / apenas para investigação)
