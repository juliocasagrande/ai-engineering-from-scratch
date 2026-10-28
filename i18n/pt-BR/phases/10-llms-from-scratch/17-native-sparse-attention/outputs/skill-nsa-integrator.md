---
name: nsa-integrator
description: Plano de integração para a Atenção Nativa Sparse numa fase de pré-formação de longo prazo.
version: 1.0.0
phase: 10
lesson: 17
tags: [nsa, sparse-attention, long-context, pre-training, kernel-aligned, deepseek]
---

Dado um contexto longo de especificação de execução pré-treinamento (contexto-alvo, arquitetura base, tokens de treinamento disponíveis, topologia GPU, alvo de implantação), produzir um plano de integração NSA.

Produzir:

1. Tamanho do bloco de compressão `l`Escolha 32, 64 ou 128. `l = 32` para 16k-32k, `l = 64` para 64k-128k, `l = 128` Para mais de 256k. `l` significa menos teclas comprimidas mas um sinal de encaminhamento mais grosseiro.
2. A lista de seleção de top-k. Escolha entre 8 e 32. O padrão do artigo é 16. `k` As tarefas pesadas de recuperação funcionam em níveis mais baixos `k`- Não .
3. Janela deslizante `W`- Selecionar 256, 512, ou 1024. Default 512. Mais curto para conteúdo fortemente estruturado (código) quando o contexto local é suficiente; mais longo para prosa.
4. MLP de porta. Especifique largura e inicialização. `hidden` até 3, com `sigmoid` ou `softplus` Ativar se os pesos da porta desmoronarem em favor de um ramo `l`- Não . `k`, ou `W` - Não é um bom acorde.
5. Seleção do núcleo. Confirme a disponibilidade do núcleo Triton ou CUDA para o acelerador-alvo. Rejeite a queda para a atenção densa na inferência (o objetivo da NSA é salvar a computação de decodificação). Se apenas existem núcleos avançados e não para trás, rejeite o treinamento prévio e recomende treinamento contínuo em pontos de controle densos existentes.

Rejeitos duros:
- A NSA num modelo pré-treinado com atenção intensa sem continuar o pré-treinamento.
- Contexto alvo abaixo de 16 mil.
- Deploições de apenas inferência em pilhas sem suporte do kernel da NSA. Recomenda atenção MLA ou janela deslizante em vez disso.

Regras de recusa:
- Se não estiverem disponíveis dados de avaliação de longo contexto (RULER, LongBench, Needle-in-haystack), recusar e solicitar primeiro dados de calibração.
- Se a distribuição de conteúdo de dados de formação for dominada por sequências curtas, recusar e recomendar o reponte dos dados antes de integrar a NSA.
- Se o acelerador for mais velho do que o A100, rejeite  As vantagens do kernel da NSA assumem hierarquias de memória H100/H200/MI300.

Resultado: lista de um plano de integração de uma página `l`- Não . `k`- Não . `W`, configuração de gate, caminho do kernel e economia esperada de computação no contexto-alvo. Terceiro com um parágrafo "critério de sucesso": o número específico RULER ou LongBench (pontos percentuais versus uma linha de base de atenção densa correspondente) que justifica a manutenção da NSA. Incluir um gatilho de retorno  o limiar métrico abaixo do qual a arquitetura deve ser revertida para MLA ou GQA densa.
