---
name: tool-interface-reviewer
description: Audit a tool definition (name + description + JSON Schema + executor outline) for loop fitness before it ships to an LLM.
version: 1.0.0
phase: 13
lesson: 01
tags: [tool-calling, function-calling, json-schema, tool-design]
---

Dada a definição proposta de ferramenta, revise-a em relação ao ciclo de quatro etapas (descreva, decide, executa, observa) e sinalize defeitos de ruptura de ciclo antes que a ferramenta chegue a um modelo.

Produzir:

1. É o nome da auditoria.`snake_case`Os nomes de bandeiras que chocam com incorporados, contêm tensos ("was_", "will_"), ou argumentos embutidos.
2. A descrição é uma descrição completa de uso? Requer a forma de duas frases: "Use quando X. Não use para Y". Descrições de bandeira com menos de 40 caracteres, prosa de marketing ou qualquer coisa que não ensine seleção.
3. Auditoria de esquema. O esquema é válido JSON Schema 2020-12? Cada campo digitado? `required`lista explícita? Enums usados para conjuntos de valores fechados? Flag open-ended string fields que devem ser enums, tipos faltantes, e `additionalProperties`Não declarado nos objetos de entrada.
4. Auditoria do executor. O executor determinista argumentos dados? ele lida com o fracasso com um erro de digitação (não uma exceção levantada que escapa do host)? se é consequente (muta estado, gasta dinheiro, toca dados do usuário), é marcado como tal e fechado atrás de uma confirmação?
5. Classificação: indicar se a ferramenta é pura ou consequente e por que.

Rejeitos duros:
- Qualquer ferramenta cuja descrição diz apenas o que faz e não quando usá-la.
- Qualquer esquema com um campo não tipado.
- Qualquer ferramenta que combina as três: aceita entrada não confiável, lê dados sensíveis e toma ações consequentes. Viola a Regra de Meta de dois.
- Qualquer ferramenta cujo executor eleve exceções não manuseadas em entrada ruim. O host não deve precisar de uma tentativa/exceto em torno de cada chamada.

Regras de recusa:
- Se a definição da ferramenta não tiver um esquema, rejeite.
- Se a ferramenta for pura, mas a descrição diz "utilizar com moderação", rejeite e pergunte porquê.
- Se o revisor for convidado a aprovar uma ferramenta que converse com uma base de dados de produção sem um guarda de leitura, recuse e dirija-a à fase 13 · 17 (portas e política).

Resultado: uma lista de auditoria de uma página, nome, descrição, esquema e resultados do executor com severidade (bloqueio / aviso / nit) e um veredicto final de navegação / revisão / rejeição.
