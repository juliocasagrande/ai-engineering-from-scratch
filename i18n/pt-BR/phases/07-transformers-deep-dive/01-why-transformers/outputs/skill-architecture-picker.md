---
name: sequence-architecture-picker
description: Arquitetura de sequência de escolha (RNN, transformador, SSM, híbrido) dada comprimento, capacidade de produção e orçamento de treinamento.
version: 1.0.0
phase: 7
lesson: 1
tags: [transformers, architecture, rnn, ssm]
---

Dados os problemas de sequência (longoura máxima, forma de lote, tokens de treinamento orçados, meta de latência de inferência, classe de dispositivo), saída:

1. Arquitetura primária. Uma das seguintes: transformador, modelo de estado-espaço (Mamba/RWKV), SSM+atensão híbrida, RNN. Razão de uma frase ligada à restrição dominante.
2. Estratégia de comprimento de contexto. Se transformador: corte de atenção total, tamanho da janela deslizante, factor de escalagem RoPE. Se SSM: tamanho da peça de varredura. Se RNN: largura oculta.
3. Formação de perfil FLOP. FLOP por token de arquitetura + contexto; observe se a especificação se encaixa no orçamento de computação.
4. Profil de memória de inferência. Caché KV para transformadores, tamanho de estado para SSMs, memória por token para RNNs. Bandeira se o dispositivo alvo pode conter um único lote de 1.
5. Nota de risco: um modo de falha específico que esta escolha é conhecida por ter na escala da especificação (por exemplo, transformador OOM em contexto de 64K em uma GPU de 24 GB sem atenção flash).

Recusar-se a recomendar um RNN puro para qualquer treinamento executado acima dos tokens 1B sem indicar explicitamente as sanções de fluxo de gradiente e paralelo. `O(N^2)` Recusa-se a recomendar uma arquitetura totalmente nova (publicada há < 12 meses) para produção sem um retrocesso designado.
