---
name: actor-critic-trainer
description: Produzir uma configuração A2C / A3C / GAE para um determinado ambiente, com estimativa de vantagem e pesos de perda especificados.
version: 1.0.0
phase: 9
lesson: 7
tags: [rl, actor-critic, gae]
---

Dados os orçamentos ambientais e de computação, a produção:

1. Paralelamente, A2C (GPU em lote) versus A3C (CPU async) e o número de trabalhadores.
2. Duração de implantação T. Pasos por env por atualização.
3. Estimador de vantagem. n-passo ou GAE(λ); especifique λ.
4. Perder peso. `c_v` (valor), `c_e` (entropia), clip de gradiente.
5. Taxas de aprendizagem: ator e crítico (separados se estiverem a utilizar).

Recusar a navegação sem normalização de vantagem. `c_e = 0` e entropia observada < 0,1 como entropia- colapsada.
