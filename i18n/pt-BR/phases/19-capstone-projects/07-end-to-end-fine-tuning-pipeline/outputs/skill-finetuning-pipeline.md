---
name: finetuning-pipeline
description: Execute um pipeline de ajuste fino de dados reprodutíveis de SFT a DPO a serviço com ablações, quantização e um modelo de cartão do Modelo 2026 Openness Framework.
version: 1.0.0
phase: 19
lesson: 07
tags: [capstone, fine-tuning, axolotl, trl, dpo, grpo, vllm, eagle-3, mof]
---

Dado um modelo base (Llama 3.1 8B, Qwen3 14B ou Gemma 3 12B) e um conjunto de dados específico de tarefa, construir um pipeline de comando único que produz um endpoint servidor e um modelo de cartão reprodutível.

Construir um plano:

1. Estágio de dados: Detup de dados, filtro de qualidade em estilo Nemotron-CC, esfregar de Presidio PII, divisão de trem/val sementeado.
2. Verificação de contaminação: MinHashLSH contra MMLU-Pro, MT-Bench-v2, RewardBench-2. Rejeitar a sobreposição.
3. SFT: Axolotl v0.8 com ZeRO-3, Flash Attention 3, sequências embaladas, 2-3 épocas em 8xH100.
4. Apontação preferencial: TRL 0,15 DPO (ou GRPO com recompensas verificáveis) para 1 época, varredura beta.
5. Quantizar: GPTQ-INT4-Marlin + AWQ-INT4 + GGUF-Q4_K_M.
6. Servir: vLLM 0.7 com decodificação especulativa EAGLE-3 (tópicos de rascunho através de Red Hat Speculators ou SGLang SpecForge).
7. Eval: lm-valuação-harness, RewardBench-2, MT-Bench-v2, MMLU-Pro através de base/SFT-only/SFT+DPO/SFT+GRPO.
8. Segurança: Llama Guard 4 taxa de passagem, filtro de saída ShieldGemma-2.
9. Cartão modelo no âmbito do Marco de Abridão Modelo 2026 com secções de dados, formação, avaliação, segurança e reprodução.

Rubrico de avaliação:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | Eval delta vs base | Measured gain on MMLU-Pro, MT-Bench-v2, task-specific benchmarks |
| 20 | Pipeline reproducibility | One-command rerun with identical seeds yields matching hashes |
| 20 | Data hygiene | Dedup rate, PII scrub coverage, contamination check green |
| 20 | Serving efficiency | tokens/s at batch 1/8/32, EAGLE-3 acceptance, $/1M tokens |
| 15 | Model card + safety eval | 2026 MOF completeness + Llama Guard 4 pass rate |

Rejeitos duros:

- O MMLU-Pro é o modo clássico de falha de avaliação-trampa.
- O treinamento é sem sementes ou YAMLs ligados.
- Servir sem EAGLE-3 ou uma configuração de decodificação especulativa equivalente.
- Todas as naves com uma taxa de aprovação de Llama Guard 4.

Regras de recusa:

- Recusar-se a publicar um modelo de cartão que reivindique pontuações de referência sem anexar o compromisso de SHA.
- Recusar-se a ajustar os dados cuja licença proíbe modelos derivados.
- Recusar-se a enviar um modelo quantizado sem medir a perda de qualidade na matriz de avaliação.

Resultado: um repo contendo o orquestador de pipeline, os YAMLs para Llama 3.1 8B + uma base alternativa, os registros de execução SFT e DPO W & B, os artefatos quantizados, o ponto final servido, a matriz de avaliação de três pontos de referência, a avaliação de segurança, o modelo de cartão 2026 MOF e uma redação sobre os três maiores problemas de higiene de dados que você capturou e resolveu.
