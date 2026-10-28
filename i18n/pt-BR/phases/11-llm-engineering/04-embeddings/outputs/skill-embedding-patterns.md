---
name: skill-embedding-patterns
description: Production patterns for embeddings, vector search, and similarity
version: 1.0.0
phase: 11
lesson: 4
tags: [embeddings, vectors, similarity, search, chunking, quantization]
---

# Introdução de padrões

Cada fluxo de trabalho de incorporação segue este contrato:

```
text -> embed(text) -> vector (float array)
similarity(vector_a, vector_b) -> score (float)
```

O modelo de incorporação e a métrica de semelhança são as únicas duas decisões que importam.

## Quando utilizar as incorporações

- Pesquisa semântica em documentos (encontrar significado, não palavras-chave)
- Clustering of similar items (tickets de suporte, avaliações de produtos, relatórios de bugs)
- Classificação por vizinhos mais próximos (etiquetar novos itens por semelhança com os exemplos etiquetados)
- Sistemas de recomendação (encontrar elementos semelhantes aos que o utilizador gostou)
- Deduplicação (encontrar conteúdo quase duplicado usando um limiar de semelhança)

## Quando não utilizar embutidos

- Correspondência de palavras-chave exata (utilizar pesquisa de texto completo)
- Consultas estruturadas (uso de SQL, filtros)
- Pequenas datasets em que a rotulagem manual é mais rápida (< 100 itens)
- Funções em que a explicabilidade é mais importante do que a precisão (as incorporações são opacas)

## Seleção de modelos

Escolha com base nas suas restrições:

- **Need an API, best value**: OpenAI embutida em texto 3 - pequeno (1536d, tokens de $ 0,02 / 1M)
- **Need maximum accuracy**Voyage-3 (1024d, tokens de 0,06 $ / 1M, MTEB mais alto)
- **Need local/private**: BGE-M3 (1024d, livre, multilingue, GPU recomendado)
- **Need fast local prototyping**: todo MiniLM-L6-v2 (384d, gratuito, funciona com CPU)
- **Need multilingual**: Cohere embed-v3 (1024d) ou BGE-M3 (ambos fortemente multilíngues)

Regra: nunca misture modelos de inserção entre indexação e consulta.

## Regras de fragmentação

1. Objetivo 256-512 tokens por peça com 50 tokens sobrepostos
2. Nunca se dividam no meio da frase se conseguem evitar isso.
3. Incluir metadados (arquivo fonte, título da seção, posição) com cada peça
4. Para documentos estruturados (Markdown, HTML), dividido em primeiro lugar nos limites das cabeçalhas
5. Teste a qualidade da peça procurando respostas conhecidas e verificando a recuperação

## Seleção de métricas de semelhança

- **Cosine similarity**: opção padrão, manipula texto de comprimento variável, normalizado
- **Dot product**: quando os vetores já estão normalizados por unidade (modelos OpenAI são), um pouco mais rápido
- **Euclidean distance**: utilização para agrupamento, quando a posição absoluta é importante

Os três dão a mesma classificação quando os vetores são normalizados.

## Optimização de armazenamento

Três níveis de compressão empilaveis:

1. **Matryoshka truncation**: dimen­tões reduzidas (1536 -> 256 = poupança de 6x, perda de precisão de 3-5%)
2. **Float16 quantization**: armazenamento pela metade por dimensão (2x de poupança, < 1% de perda de precisão)
3. **Binary quantization**: 1 bit por dimensão (32x de poupança, perda de precisão de 5 a 10%, utilização com rescoring)

Padrão de produção: busca binária sobre o corpo completo, rescore top-1000 com vetores float32.

## Retriever-then-ranger

Em dois estágios, para melhor precisão:

1. Bi-encoder recupera os 100 candidatos principais (rápido, usa embalagens pré-computadas)
2. Cross-encoder reranks para top-10 (lento, processando cada par de consulta-doc)

Isto supera a recuperação em uma única etapa em 10-15% em métricas de precisão.

## Erros comuns

- Utilização de diferentes modelos de inserção para indexação e consulta
- Embedagem de documentos inteiros em vez de pedaços (embedagem torna-se média de tudo)
- Não normalizar vetores antes da semelhança cosínica (a maioria dos modelos pre-normalizar, mas verificar)
- Ignorar a sobreposição de pedaços (as frases divididas em limites perdem contexto)
- Armazenar apenas vetores sem o texto original (você precisa de ambos para a recuperação)
- Não re-embedagem quando o modelo muda (vectores antigos são incompatíveis)
- Escolha das dimensões com base apenas na precisão (escala de armazenamento e latência linearmente com as dimensões)

## Debug embutidos

Se os resultados da pesquisa forem pobres:

1. Verifique se a incorporação da consulta não é zero (entrada em espaço vazio ou em espaço branco produz vetores zero)
2. Verifique manualmente a pontuação de semelhança de um documento conhecido e relevante
3. Tente reformula-lo para combinar o vocabulário do documento
4. Inscrever os limites dos pedaços para garantir que o conteúdo relevante não seja dividido em pedaços
5. Compare os resultados de top-k em métricas (cosino, ponto, euclidiano) para detectar problemas de normalização
6. Teste com uma consulta trivialmente correspondente (copiar uma frase de um documento) para confirmar o funcionamento do pipeline

## Parâmetros de produção

- Tamanho do pedaço: 256-512 tokens
- Superposição de pedaços: 50 tokens (10-20% do tamanho do pedaço)
- Recuperação de ponta: 5-10 para utilização direta, 50-100 para re-ranqueamento
- Prazo de semelhança: 0,7+ para coseno (em relação a este, os resultados são geralmente irrelevantes)
- Embedagem em lote: processar 100-500 textos por chamada de API para o rendimento
- Reconstrução do índice: reincorporado quando o modelo muda ou os documentos são atualizados significativamente
