---
name: skill-tokenizer
description: Choosing and building tokenizers for LLM projects
version: 1.0.0
phase: 10
lesson: 1
tags: [tokenizer, bpe, wordpiece, sentencepiece, llm, nlp]
---

# Seleção e implementação de Tokenizer

Ao iniciar um projecto de Mestrado em Direito Jurídico, aplicar este quadro de decisão para a selecção de tokenizadores.

## Quando utilizar cada tokenizer

**Byte-level BPE (tiktoken):**Você está construindo ou ajustando modelos da família GPT. Você precisa de manuseio garantido de qualquer sequência de byte de entrada.

**WordPiece (Hugging Face):**Você está trabalhando com modelos da família BERT para classificação, NER ou tarefas de incorporação. Você precisa do prefixo de continuação "##" para tarefas a jusante que dependem de sinais de fronteira de palavras.

**SentencePiece (BPE or Unigram):**Você está treinando a partir do zero. Você precisa de tokenization linguística-agnóstica. Os seus dados incluem línguas CJK, tailandês ou outros scripts sem limites de palavras em espaço branco. LLaMA, T5, e a maioria dos modelos multilíngues usam isso.

## Orientações para o tamanho do vocabulário

- Tokens 32K: bom padrão para modelos monolingues, mantém a camada de incorporação pequena
- Tokens 50K-64K: melhores para modelos multilíngues ou com código pesado
- 100K + tokens: somente quando você tem dados de treinamento maciços e quer sequências curtas

O vocabulário maior significa sequências mais curtas (inferação mais barata) mas mais parâmetros na matriz de incorporação. Para um vocabulário de 100K com incorporações de 4096 dimensões, a camada de incorporação sozinha é de parâmetros 400M.

## Regras de pré-tokenization que importam

1. Divisão no espaço em branco antes do BPE para evitar fusões de palavras cruzadas
2. Separar dígitos individualmente se você quer que o modelo aprenda aritmética
3. Normalize Unicode (NFC) antes da tokenization para comportamento consistente
4. Adicionar tokens especiais para o seu caso de uso: `<pad>`- Não .`<eos>`- Não .`<bos>`- Não .`<unk>`, e quaisquer marcadores específicos de tarefa

## Banderas vermelhas no comportamento do tokenizer

- Fertilidade acima de 2,0 para a sua língua-alvo: o modelo desperdiça a janela de contexto
- Palavras comuns de domínio divididas em 3+ tokens: retrain com dados de domínio
- Tokenization inconsistente dos números: verifique as regras de divisão de dígitos
- Grande vocabulário com muitos tokens de uso único: reduzir o tamanho do vocabulário

## Construir um tokenizer personalizado - lista de verificação

1. Recolher dados representativos de formação (pelo menos 1 GB de texto no domínio-alvo)
2. Escolha algoritmo: BPE para uso geral, Unigram para multilingue
3. Defina o tamanho do vocabulário com base nas orientações acima
4. Configurar a pré-tokenization: divisão de espaço em branco, manipulação de dígitos, pontuação
5. Adicionar tokens especiais
6. Trem usando a biblioteca de tokenizers Hugging Face (backend de Rust, rápido)
7. Validação: verificação da fertilidade de textos em todas as línguas-alvo
8. Casos de borda de teste: cadeia vazia, entrada muito longa, dados binários, emoji, texto RTL
9. Salvar e versão do tokenizer ao lado de pontos de controle modelo
