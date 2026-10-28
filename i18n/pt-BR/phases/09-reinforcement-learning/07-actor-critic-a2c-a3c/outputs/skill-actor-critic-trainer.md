---
name: actor-critic-trainer
description: Produce an A2C / A3C / GAE configuration for a given environment, with advantage estimation and loss weights specified.
version: 1.0.0
phase: 9
lesson: 7
tags: [rl, actor-critic, gae]
---

Dados os orçamentos ambientais e de computação, a produção:

1. Paralelamente, A2C (GPU em lote) versus A3C (CPU async) e o número de trabalhadores.
2. Duração de implantação T. Pasos por env por atualização.
3. Estimador de vantagem. n-passo ou GAE(λ); especifique λ.
4. Perder peso.`c_v`(valor), `c_e`(entropia), clip de gradiente.
5. Taxas de aprendizagem: ator e crítico (separados se estiverem a utilizar).

Recusar a A2C de trabalho individual em ambientes com horizonte > 1000 (demasiado em política, muito lento). Recusar a expedição sem normalização de vantagem.`c_e = 0`e entropia observada < 0,1 como entropia- colapsada.
