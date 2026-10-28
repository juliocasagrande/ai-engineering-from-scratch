---
name: skill-prompt-injection-detector
description: Layered detector pipeline that returns a category and confidence for any prompt, with measurable precision and recall
version: 1.0.0
phase: 19
lesson: 83
tags: [safety, detector, prompt-injection]
---

# Detector de injecção rápida

Um detetor aqui é uma função de prompt para veredicto. Um veredicto carrega uma categoria da leção 82 taxonomia e uma confiança em [0, 1].

## Pipeline

1. Normalize - desprenda caracteres de largura zero, desfaça homoglifos, decode base64/hex, dobra dígitos de leet-speak, tente corromper13 com uma verificação de sanidade de palavras comuns.
2. Regras de substring - agulhas escritas à mão como `ignore previous`- Não .`from now on you are`- Não .`decode this base64`- Não .
3. Regex regras - padrões de nível de token , tais como `\bignor\w*\s+(all|prior|previous|earlier)\b`- Não .

A agregação mantém a pontuação máxima por categoria e retorna a categoria com a pontuação mais alta, ou `benign`Se nada disparar.

## Adição de uma regra

Edit `code/rules.py`Uma regra é um dicionário com`name`- Não .`category`(uma das seis categorias de taxonomia), `score`(flotante 0 a 1), e uma das `substring`ou `regex`- Re-exercício .`main.py`Para ver o impacto na precisão e na retirada por categoria.

## Artifacto

`outputs/detector_report.json`A porta de fim para fim na lição 87 lê-a para o limiar de confiança.
