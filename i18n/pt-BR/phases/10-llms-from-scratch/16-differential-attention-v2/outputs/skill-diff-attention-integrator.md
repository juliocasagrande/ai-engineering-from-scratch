---
name: diff-attention-integrator
description: Integration plan for adding Differential Attention V2 to a new pre-training run or LoRA fine-tune.
version: 1.0.0
phase: 10
lesson: 16
tags: [differential-attention, diff-transformer, long-context, flash-attention, pre-training, lora]
---

Dada uma arquitetura de modelo (oculto, cabeças, cabeças de KV, camadas, d_head), um comprimento de contexto-alvo, uma alucinação ou um perfil de contexto-longo (modos de falha em suas avaliações existentes) e um orçamento de treinamento (tokens disponíveis, horas de GPU), produzir um plano de integração para DIFF V2.

Produzir:

1. Modo de integração: pré-treino do zero, troca de arquitetura no meio do treino ou ajuste fino do LoRA nas projeções Q. Justifique a escolha em relação ao orçamento de treinamento e aos pesos disponíveis.
2. Arquitetura diferente. Lista de mudanças de campo por campo em concreto: quais projeções crescem, que permanecem as mesmas, qual número de parâmetros você está adicionando e onde a subtração é colocada no bloco de atenção. Incluir `lambda_init`Programa por profundidade de camada (`0.8 - 0.6 * exp(-0.3 * (depth - 1))`é a padrão do papel; ajuste por profundidade se a telemetria em camadas mostrar instabilidade).
3. Opção de núcleo. Confirme o suporte FlashAttention 2 ou 3 dado o número de pessoas duplicando V2. Rejeitar o caminho do núcleo personalizado de V1 a menos que o usuário precise explicitamente para a reprodução.
4. Prestação de memória. O cache KV permanece na linha de base (cabeças KV inalteradas). Computa delta de memória por token de ativação (cabeças Q extras, computação extra). Relata números absolutos no contexto de destino.
5. Plano de estabilidade do treino.`lambda`A diferença de variação de gradientes nas projeções Q. Nomear a métrica específica que deve desencadear um retorno à atenção de linha de base se a telemetria indicar divergência.

Rejeitos duros:
- Adicionar atenção DIFF a um modelo pré-treinado sem continuar com o pré-treinamento.
- DIFF V1 para qualquer nova corrida após abril de 2026.
- A integração do DIFF sem permitir também dados de formação de longo contexto.
- Mudanças`lambda_init`O valor negativo inicial subtrai mais do que o nível de ruído e desmorona o treinamento.

Regras de recusa:
- Se o contexto-alvo for inferior a 16k, recuse a integração e recomenda atenção padrão.
- Se o utilizador não puder fornecer dados de avaliação de longo contexto (RULER, agulha em manto de feno, MultiNeedle), recuse-se e solicite primeiro dados de calibração.
- Se o usuário estiver em uma pilha pré-FlashAttention-2, recuse e recomenda atualizar a pilha antes de tentar a integração.

Resultado: um modo de listagem de plano de integração de uma página, delta de contagem de parâmetros, impacto no cache KV, confirmação FlashAttention, `lambda`O programa de avaliação de um determinado número de avaliação de longo contexto (punto percentual delta no RULER 64k ou equivalente) que justifique manter o DIFF V2 na arquitetura em vez de reverter.
