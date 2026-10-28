---
name: skill-bpe-vs-wordpiece
description: Escolha o algoritmo de tokenização, o tamanho do vocabulário, a biblioteca para um determinado corpo e o alvo de implantação.
version: 1.0.0
phase: 5
lesson: 19
tags: [nlp, tokenization]
---

Dado um corpus (dimenção, linguagem, domínio) e um objetivo de implantação (formação a partir do zero / ajuste fino / inferência compatível com a API), a saída:

1. Algoritmo, BPE, Unigram ou WordPiece, razão de uma frase.
2. Biblioteca, SentencePiece, HF Tokenizers, ou tiktoken.
3. Dimensão de vocabulário, arredondada para o mais próximo de 1k. Razão ligada ao tamanho do modelo e à cobertura linguística.
4. Configurações de cobertura. `character_coverage`- Não . `byte_fallback`, lista de tokens especiais.
5. Plano de validação: token-es-médio por palavra no conjunto de retenção, taxa de OOV, relação de compressão, igualdade de decodificação de ida e volta.

Recusar a formação de um tokenizer de cobertura de caracteres < 0,995 em corpora com conteúdo de manuscritos raros. Recusar a envio de um vocabulário sem um congelado `tokenizer.json` Marque qualquer tokenizer monolingüe com menos de 16k de vocabulário como provavelmente subespecificado.
