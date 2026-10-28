---
name: prompt-tokenizer-builder
description: Build and debug production-quality tokenizers for LLM projects
version: 1.0.0
phase: 10
lesson: 2
tags: [tokenizer, bpe, byte-level, special-tokens, chat-template, multilingual]
---

# Construção de Tokenizer de Produção

Ao construir ou depurar um tokenizer para um projeto de LLM, siga este quadro.

## Lista de verificação de oleodutos

Cada tokenizer de produção precisa destas cinco etapas. Se faltar uma, você vai atingir casos de borda na produção.

1. **Normalize**Aplicar normalização de Unicode NFKC. Isso desintegra ligaturas ("fi" -> "fi"), normaliza caracteres de largura completa e padroniza o espaço branco. Esqueça isso e a mesma palavra recebe diferentes IDs de token dependendo de como foi digitada.

2. **Pre-Tokenize**-- Divide o texto em pedaços antes do BPE. Use o padrão regex do GPT-2 para modelos centrados no inglês. Use a abordagem de byte bruto do SentencePiece para modelos multilíngües. A escolha determina se o BPE pode se fundir através de limites de palavras.

3. **BPE Merge**Aplicar a tabela de fusão aprendida para sequências de byte dentro de cada peça. a tabela de fusão é o conhecimento aprendido do tokenizer. tudo o resto é plumbing.

4. **Special Token Injection**- Correspondem a tokens especiais exatamente antes da execução do BPE. [BOS], [EOS], [PAD], marcadores de modelos de bate-papo recebem identidades fixas.

5. **ID Mapping**- Converte cadeias de tokens para números inteiros. O modelo vê apenas números inteiros.

## Problemas de Desembaraço de Tokenizer

**Symptom: model produces garbage on chat input**
- Verifique o modelo de chat. Cada modelo tem um formato diferente.`<|start_header_id|>`Marcadores.`<|im_start|>`Uma modelo errada coloca entrada fora da distribuição de treinamento.

**Symptom: non-English text uses too many tokens**
- Verifique a fertilidade (tokens por palavra). acima de 2.0 significa que o tokenizer desperdiça a janela de contexto nessa língua. Soluções: retrain com dados mais multilíngues, aumentar o tamanho do vocabulário ou usar SentencePiece com Unigram.

**Symptom: numbers and arithmetic fail**
- Verifique como os dígitos são tokenizados. "1234" como um token significa que o modelo não pode fazer operações de nível de dígitos. Divide dígitos individualmente durante a pré-tokenization.

**Symptom: code tokens are inefficient**
- Verifique como a indentation é manuseada. O tokenizer do GPT-2 desperdiça tokens em espaços. Codex e StarCoder usam tokens especiais de indentation (4 espaços = 1 token).

## Decidência sobre o tamanho do vocabulário

- Tokens 32K: monolingue, modelo pequeno, computação limitada.
- 50K-64K: multilíngue ou com código pesado.
- 100K+ (GPT-4, Llama 3): apenas com dados de treinamento massivos. Sequências mais curtas mas parâmetros de incorporação de 100K * d_modelo.

Para um modelo 4096 dimensões: 32K vocab = 131M parâmetros de incorporação. 128K vocab = 524M parâmetros de incorporação. Isso é parâmetros 400M apenas na camada de incorporação.

## Requisitos de velocidade

- Formação para tokenização de dados: use bibliotecas com Rust (tiktoken, huggingface tokenizer). Python puro é 10-100 vezes mais lento.
- Tokenization de inferência: a latência importa menos (seqüência única), mas ainda usa implementações compiladas.
- Benchmark: tokenize 1GB de texto e medir o tempo do relógio de parede. Se demorar mais de 60 segundos, passe para um backend Rust.

## Validação de Modelo de Chat

Antes de implementar qualquer modelo de chat, verifique o modelo:

1. Encode uma conversa conhecida com o tokenizer
2. Descifrá-lo de volta para texto
3. Compare caracteres por caracteres com o formato esperado da documentação do modelo
4. Preste atenção a: novas linhas após os tokens de cabeçalho, espaços antes do conteúdo, marcadores de final de turno
5. Casos de borda de teste: mensagem de sistema vazia, mensagem de usuário muito longa, várias voltas de assistente

O erro no modelo de bate-papo é a fonte mais comum de desempenho degradado do modelo de bate-papo.
