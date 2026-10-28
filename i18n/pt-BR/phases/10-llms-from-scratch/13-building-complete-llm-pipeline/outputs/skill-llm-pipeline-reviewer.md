---
name: llm-pipeline-reviewer
description: Review an end-to-end LLM training pipeline manifest before a multi-million-dollar run.
version: 1.0.0
phase: 10
lesson: 13
tags: [pipeline, training, manifest, eval-gate, cost, rollback]
---

Dado um manifesto de pipeline de treinamento proposto (YAML ou JSON descrevendo tokenizer, dados, pré-treinamento, SFT, alinhamento, avaliação, quantização e fases de serviço), produzir uma revisão que cobre:

1. Grafico de estágios. Confirme que cada estágio tem entradas e saídas digitadas. Chame dependências faltantes, estado implícito ou qualquer estágio que consuma um diretório nu em vez de um hash de artefato nomeado.
2. Chaena de hash. Verifique que o output_hash do estágio N é igual a um dos input_hashes de cada estágio a jusante. Qualquer desajuste significa que o manifesto é incoerente e o pipeline não deve começar.
3. Portão Eval. Cada métrica na lista de portões deve ser numérica, ter um operador, um limiar e uma fonte de medição. Rejeita qualquer portão que seja subjetivo ("parece bom"), ilimitado (sem limiar) ou medido com base nos dados de treinamento.
4. Segurança de regressão. Os principais benchmarks do novo modelo (MMLU, MATH, HumanEval+, GPQA ou um equivalente específico de domínio) devem ter números de linha de base anexados.
5. O orçamento KL. As fases de alinhamento (RLHF, DPO, CAI, GRPO) devem declarar um limite KL acumulado em relação à referência.
6. Verificação da contaminação. Os dados de formação e os conjuntos de avaliação devem ter uma verificação documentada de sobreposição (paralelas exatas ou 13 gramas).
7. Estimação de custos: estimativa prévia de cada fase mais um total, comparada com o orçamento.
8. Plano de retorno. Para cada etapa, ações nomeadas sobre o fracasso: re-exercício, retorno ao artefato anterior, revisão de entradas e re-exercício para baixo.
9. Armazenamento de artefatos. pontos de verificação, conjuntos de dados, tokenizers, relatórios de avaliação devem ser endereçados por conteúdo (SHA-256).
10. Observabilidade. Cada estágio deve emitir registros estruturados com um ID de rastreamento, nome de estágio, hashs de entrada, hash de saída, relógio de parede e custo.

Banderas vermelhas que interrompem a revisão:
- um portão que carece de uma fonte de medição (portão em uma métrica sem computadores de estágio)
- Uma fase que compartilha um ponto de controlo com uma fase descendente (sem separação de preocupações)
- Uma etapa de alinhamento sem modelo de referência (sem âncora para KL)
- Uma avaliação de LLM como juiz, quando o juiz é a mesma família modelo que a política (contaminação)
- Uma estimativa de custos que exceda o orçamento em mais de 20%
- um plano de reestruturação que consiste unicamente em "re-estruturação a partir do zero"

Resultado: uma revisão de duas páginas com PASS/HOLD por porta, o campo exato de manifesto ou campo faltante que produziu cada veredicto, e a mudança mínima necessária para virar um HOLD em um PASS.
