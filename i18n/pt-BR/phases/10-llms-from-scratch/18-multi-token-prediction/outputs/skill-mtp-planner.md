---
name: mtp-planner
description: Planejar uma integração de previsão de vários tokens para uma nova corrida pré-treinamento.
version: 1.0.0
phase: 10
lesson: 18
tags: [mtp, multi-token-prediction, deepseek-v3, pre-training, speculative-decoding]
---

Dada uma especificação de execução pré-treinamento (escala de modelo, tamanho oculto, camadas, orçamento de tokens de dados, topologia da GPU, implantação de alvos) e um objetivo declarado (sinal de treinamento mais denso vs. projeto de decodificação especulativa vs. ambos), produzir um plano de integração MTP.

Produzir:

1. Profundidade D. Selecionar 1 ou 2. DeepSeek-V3 usa D=1 e relata a primeira aceitação de descodificação especulativa de profundidade em 80%+. D=2 é território diminuindo-retorna para a maioria das corridas. Justificar a escolha contra o orçamento de computação  cada profundidade extra adiciona aproximadamente um bloco transformador de computação por etapa de treinamento.
2. Programação Lambda. Default: 0,3 para os primeiros 10% do treino, 0,1 depois. Ajuste até 0,5 cedo para modelos pequenos (menos de 7B) onde o sinal mais denso importa mais; ajuste para baixo se observar a perda de MTP dominando a perda principal.
3. Orçamento de parâmetros. Conto de parâmetros por módulo em relação ao modelo principal.
4. Quantificar as FLOPs adicionais de passagem avançada por passo (aproximadamente `D * transformer_block_cost`), memória de passagem para trás extra (memória de ativação para módulos D) e VRAM extra pico (embedagem compartilhada e cabeça não contam, projecção e bloco transformador não contam).
5. Descreva como consumir o módulo MTP como um rascunho de descodificação especulativa na inferência. Nomeie o caminho de integração da regra Leviathan e a contabilidade de rollback KV. Confirme a compatibilidade com a pilha de inferência alvo (vLLM, SGLang, TensorRT-LLM).

Rejeitos duros:
- Adição de MTP a um modelo denso pré-treinado sem ele. Não pode ser retrofitado  os módulos MTP não são treinados.
- D > 2 para uma primeira integração. O ganho sobre D = 1 é pequeno; a complexidade cresce rapidamente.
- MTP num modelo com parâmetros ativos 1B. O sinal é mais fraco do que o custo geral nessa escala.
- Usando cabeças paralelas (estilo de Gloeckle) quando o objetivo é a descodificação especulativa.

Regras de recusa:
- Se os dados pré-treinamento forem dominados por sequências curtas (menos de 2k), rejeite.
- Se a pilha de inferência-alvo não suportar a descodificação especulativa, note que o MTP ainda compra o sinal de treinamento mais denso e prossegue, mas marque a descoincidência.
- Se o utilizador continuar a fazer o pré-treino num ponto de controlo denso existente sem MTP, recusar e recomendar a adição de MTP somente no início de uma corrida de treinamento limpa ou numa redefinição limpa das fronteiras de dados.

Output: um plano de integração de uma página que enumera D, cronograma lambda, custos gerais de parâmetros (absoluto e percentual), custos gerais de cálculo (percentual por etapa de formação) e o plano de descodificação especulativa de tempo de inferência. Terminar com um parágrafo "critério de sucesso" que nomeie a métrica medida que justifica a manutenção do MTP: a taxa de aceitação na profundidade 1 após 50B tokens de treinamento deve ser superior a 70%, caso contrário, a arquitetura deve ser revertida.
