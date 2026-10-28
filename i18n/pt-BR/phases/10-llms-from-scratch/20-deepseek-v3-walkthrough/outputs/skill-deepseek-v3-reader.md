---
name: deepseek-v3-reader
description: Read a DeepSeek-family config and produce a component-by-component architecture analysis.
version: 1.0.0
phase: 10
lesson: 20
tags: [deepseek-v3, deepseek-r1, mla, moe, mtp, dualpipe, architecture]
---

Dado um modelo da família DeepSeek (V3, R1 ou qualquer derivado) e sua configuração (size oculto, camadas, num_experts, kv_lora_rank, etc.), produz uma análise de arquitetura que descompõe o modelo por componente e identifica quais inovações específicas do DeepSeek usam.

Produzir:

1. Configuração de campo por campo. Para cada campo, nomear o componente que mapeia e contar o parâmetro que contribui. Formatos: `field_name: value → interpretation → parameter contribution`- Não .
2. Parâmetro de desagregação. Parâmetros totais, parâmetros ativos, relação ativa. Dividido por embutidação, atenção por camada, MLP por camada (denso versus especialista), roteador, módulo MTP, cabeça LM, RMSNorm total.
3. Cache de KV no contexto-alvo. Relatar valores BF16 e FP8. Incluir uma comparação com uma linha de base GQA (8/128) estilo Llama-3 no mesmo contexto e tamanho oculto.
4. Lista de verificação da inovação: para cada um dos MLA, MTP, roteamento sem perda, DualPipe, identifique se o modelo o usa e onde no documento de configuração/papel isso é visível.
5. Verificação de sanidade. Calcule o orçamento de memória de inferência do modelo (pesos + cache KV + ativações) em um objetivo de implantação específico (H100 80GB, H200 141GB, MI300X 192GB, único nó versus multi-nodo). Relate se ele se encaixa e qual quantização seria necessária.

Rejeitos duros:
- Qualquer análise que confunda DeepSeek-V3 com modelos densos da classe GPT.
- A afirmação de MLA é mais rápida do que a GQA sem especificar o comprimento do contexto.
- Interpretar o MTP como um substituto da descodificação especulativa. É um objetivo pré-treinamento que também se duplica como um esboço.

Regras de recusa:
- Se a configuração fornecida estiver ausente `kv_lora_rank`- Não .`num_experts`, ou `first_k_dense_layers`Não é um modelo da família DeepSeek.
- Se o utilizador solicitar a correspondência exata da contagem de parâmetros publicada (até os 100M mais próximos), recuse e explique que o número publicado inclui parâmetros estruturais específicos de implementação que uma calculadora simplificada não reproduz exatamente.
- Se o objetivo de implantação for uma GPU de consumo (24GB ou menos), recuse e recomenda um derivado da família DeepSeek destilado em quantizado.

Resultado: uma análise de arquitetura de uma página listando campos, desagregação de parâmetros, cache KV, lista de verificação de inovação e ajuste de implantação.
