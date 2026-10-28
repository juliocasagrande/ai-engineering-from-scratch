---
name: prompt-data-quality-checker
description: Validate and debug data quality in LLM pre-training pipelines
version: 1.0.0
phase: 10
lesson: 3
tags: [data-pipeline, deduplication, quality-filter, pre-training, llm, data-cleaning]
---

# Verificador de Qualidade dos Dados para o Pré-Formação do Mestrado em Direito

Ao construir ou auditar um pipeline de dados para a pré-formação do Mestrado em Direito Jurídico, utilize este quadro para detectar problemas antes que eles cheguem ao modelo.

## Bandeiras vermelhas na produção de oleodutos

**Deduplication removed less than 20% of web data.**O Common Crawl normalmente contém 30-40% de duplicados. Se o seu passo dedup remover menos de 20%, seus parâmetros MinHash são muito conservadores ou seu limiar é muito alto. Verifique: tamanho da baranda k, número de funções hash, número de bandas LSH, limiar Jaccard.

**Compression ratio below 2.0 chars/token.**Isso significa que o seu tokenizer está a dividir-se de forma muito agressiva. Ou reestrine com mais fusões, aumente o tamanho do vocabulário, ou verifique se a pré-tokenização não está fragmentando o texto desnecessariamente.

**Compression ratio above 6.0 chars/token.**O tokenizador aprendeu fusões muito específicas de domínio que podem não generalizar.

**Sequence utilization below 90%.**O seu documento é muito curto (filtra-o ou aumenta o comprimento mínimo do documento) ou a sua embalagem de sequência é ineficiente (transforma-se de embalagem ingênua para embalagem de documentos múltiplos).

**Vocab utilization below 50%.**Ou o vocabulário é grande demais para o seu domínio ou o tokenizer foi treinado em dados muito diferentes.

## Calibração de filtros de qualidade

Faça estas verificações numa amostra aleatória de 1.000 documentos em cada fase do gasoduto:

1. **Read 20 random documents after cleaning.**Os dados contêm HTML residual, JavaScript, texto de navegação ou placa de caldeira?

2. **Read 20 random documents that PASSED the quality filter.**Alguma delas é spam, lista de palavras-chave ou gerada por máquina?

3. **Read 20 random documents that FAILED the quality filter.**Se sim, o seu filtro é muito agressivo.

4. **Read 20 random near-duplicate pairs from dedup.**Se não, baixar o limiar Jaccard ou aumentar o número de funções hash.

## Relações de mistura de dados

Não existe uma fórmula universal. Comece com estas linhas de base e ajuste com base na avaliação:

| Category | Llama 3 Ratio | Starting Point |
|----------|--------------|----------------|
| Web text | 50% | 50% |
| Code | 25% | 15-25% |
| Books/academic | 13% | 10-15% |
| Math | 8% | 5-10% |
| Multilingual web | 4% | 5-10% |

Aumente a relação de código se o modelo for forte na programação. Aumente a relação de matemática se o raciocínio importa. Diminui a relação da web se você precisa de menos ruído. Avalie sempre em benchmarks após mudanças de proporções.

## Estimativas de escala

Para uma determinada contagem de tokens-alvo:

- Tokens 1T da web: esperem ~3-5TB de texto bruto, ~1,5-2TB após limpeza e dedup
- Rápido de tokenização (Rust): ~ 100 milhões de tokens/segundo por núcleo
- Velocidade de tokenização (Python): ~1-10M tokens/segundo por núcleo
- MinHash dedup em 128 hashes, 16 bandas: ~ 10K documentos/segundo por núcleo
- Pacotamento de sequência: I/O ligado, use arquivos mapeados em memória para corpora acima de 10 GB

Para tokens 15T (escala Llama 3), planeje ~ 30-50 TB de dados de entrada brutos, 1-2 semanas de pré-processamento em uma máquina de 64 núcleos e 100 TB+ de disco para arquivos intermediários.

## Lista de verificação antes da formação

1. Contagem total de tokens corresponde ao seu orçamento de computação (utilizar Chinchilla escala ou o Llama 3 sobre-trein ratio como guia)
2. Dedup removeram 30-40% dos dados da web
3. Filtro de qualidade removido 10-20% dos dados restantes
4. A relação de compressão é de 3-5 caracteres/token para o inglês
5. Utilização de sequência superior a 95%
6. Verificações aleatórias pontuais mostram texto limpo e coerente em cada fase do pipeline
7. As relações de mistura de dados foram validadas numa formação em pequena escala
8. A remoção de PII foi verificada numa amostra
9. Todos os formatos binários (sequências embaladas, matrizes de ID de token) passam em testes de codificação/descodificação de ida e volta
10. O pipeline é reprodutivel: a mesma entrada produz a mesma saída com sementes aleatórias fixas
