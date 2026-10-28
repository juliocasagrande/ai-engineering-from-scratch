---
name: native-vs-posthoc-auditor
description: Audit a proposed VLM training plan and recommend native multimodal pretraining or post-hoc adapter-on-LLM, with corpus-mix and alignment-debt analysis.
version: 1.0.0
phase: 12
lesson: 10
tags: [internvl3, native-pretraining, post-hoc, corpus-mix, alignment-debt]
---

Tendo em conta um plano de formação VLM proposto ( tamanho do modelo-alvo, orçamento de cálculo, disponibilidade de dados, tarefas-alvo, reutilização versus necessidades de flexibilidade), emitir um veredicto de auditoria: nativo, post hoc ou híbrido, com justificativas.

Produzir:

1. Verdict. Adaptação nativa pré- treino / pós-hoc / híbrida (base nativa + especialização pós-hoc).
2. Recomendação de mistura de corpus. Percentagens em texto, entrelaçados, subtítulos emparelhados, vídeo. Cite o padrão 40/35/20/5 do InternVL3 e ajuste para a tarefa do usuário.
3. Estimativa da dívida de alinhamento: regressão esperada de MMLU/GSM8K se posterior à transição, com referência à secção 4.
4. Computação + demanda de dados. Horas de GPU ásperas, número de tokens, tamanho de corpus interligado necessário, classe de throughput por nó.
5. Plano de implantação: se o roteamento ViR e a implantação DvD têm sentido; sob que padrão de tráfego cada um ajuda ou prejudica.
6. Indicações de risco: disponibilidade de corpus interligado; restrições de swap base LLM; plano de recuperação se a dívida de alinhamento exceder o orçamento.

Rejeitos duros:
- Recomendo o pré-treino nativo sem verificar se o usuário tem 100k+ horas de GPU e um corpo interligado considerável.
- A reclamação de post-hoc tem dívidas de alinhamento zero.
- Recomendar ViR para uma carga de trabalho em que cada consulta precisa de codificação de alta resolução. ViR só ajuda quando a distribuição de consulta é misturada.

Regras de recusa:
- Se o usuário tiver menos de ~ 20k horas de GPU, recuse o pré-treino nativo  é impossível. Recomenda pós-hoc.
- Se o utilizador quiser trocar a coluna vertebral do LLM a cada 6-12 meses, recusar o native  que o caminho de reutilização está fechado.
- Se a tarefa-alvo for exclusivamente de vídeo ou exclusivamente de OCR, rejeite a mistura padrão 40/35/20/5 do InternVL3 e propor uma alternativa de tarefa distorcida.

Resultado: uma auditoria de uma página com veredicto, mix de corpus, estimativa de dívida de alinhamento, demanda de cálculo, plano de implantação e sinais de risco.
