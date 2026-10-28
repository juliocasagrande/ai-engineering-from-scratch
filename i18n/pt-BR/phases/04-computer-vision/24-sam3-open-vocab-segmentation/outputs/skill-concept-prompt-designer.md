---
name: skill-concept-prompt-designer
description: Turn user utterances into well-formed SAM 3 concept prompts with splitting, disambiguation, and fallbacks
version: 1.0.0
phase: 4
lesson: 24
tags: [sam3, open-vocab, prompt-engineering, segmentation]
---

# Conceito de Projeto de Pronto

A precisão do SAM 3 depende fortemente da forma como o prompt conceitual é formulado. Esta habilidade normaliza as declarações do usuário em forma livre em instruções que o SAM 3 lida bem.

## Quando utilizar

- Construir uma interface de interface que aceita consultas de objetos em linguagem natural.
- Expondo SAM 3 através de uma API onde os chamadores de montante enviam frases.
- Debugging SAM 3 péssimas combinações  muitas vezes o prompt é malformado, não o modelo.

## Input

- `utterance`: sequência de usuários brutos.
- `context`: indicação de domínio opcional (por exemplo, "vigilância", "médica", "retail").
- `max_concepts`: conceitos máximos a extrair por expressão; padrão 5.

## Regras que a SAM 3 prefere

- **Short noun phrases, not sentences.** `"cat"`ganha .`"there is a cat"`- Não .
- **Concrete nouns.** `"skateboard"`ganha .`"thing to ride on"`- Não .
- **Modifiers immediately before the noun.** `"red car"`ganha .`"car that is red"`- Não .
- **Lowercase.**SAM 3 é robusto, mas empiricamente um pouco melhor em insumos minúsculos.
- **Singular or plural.**Ambos funcionam; o plural ajuda quando se esperam múltiplas instâncias.

## Passo

1. **Tokenise by common separators** virgem, semicolon, "e", "ou", "&".
2. **Drop filler prefixes**"Encontrar", "mostrar-me", "segmento", "detectar", "localizar", "a", "um", "o".
3. **Keep prepositional modifiers**Só se forem visíveis  `"striped red umbrella"`Sim, sim.`"umbrella from yesterday"`Não (o `"from yesterday"`Não é na imagem).
4. **Disambiguate collisions**usando o opcional `context`- Não .
   - `"window"`no contexto da vigilância -> `"building window"`- Não .
   - `"window"`no contexto médico -> frequentemente erro; sugere que o utilizador esclareça.
5. **Fallback**Se a divisão produz zero conceitos *e* a expressão contém pelo menos um substantivo concreto. Se nenhum substantivo concreto pode ser extraído, não emitir um conceito  retornar apenas avisos e pedir ao usuário para esclarecer (ver Regras).
6. **Cap at `max_concepts`.**Se foram extraídos mais conceitos do que o solicitado, mantenha o primeiro.`max_concepts`em ordem de expressão e emitir o resto sob`dropped`com razão .`"exceeded max_concepts"`Isto mantém a latência limitada quando um usuário pega uma longa enumeração.

## Formatos de saída

```
[designed prompts]
  utterance:    <original>
  concepts:     ["concept_1", "concept_2", ...]
  dropped:      ["filler_1", ...]
  warnings:     ["concept too abstract", "may match many classes", ...]

[sam3 calls]
  For each concept run: sam3.detect(image, concept)
  Merge outputs with distinct concept tags per detection.
```

## Exemplos

```
in:  "can you find me a cat or two dogs?"
out: ["cat", "dogs"]
dropped: ["can you find me", "a", "or two", "?"]
note: "dogs" kept plural because the utterance says "two dogs" — plural hint preserved.

in:  "segment the big red truck and the blue sedan"
out: ["big red truck", "blue sedan"]
dropped: ["segment", "the", "and"]

in:  "thing near the door"
out: ["door"]
warnings: ["'thing' is too abstract for SAM 3; fell back to 'door'"]

in:  "striped red umbrella, green hat, pink balloon"
out: ["striped red umbrella", "green hat", "pink balloon"]
```

## Regras

- Nunca passe frases de mais de 8 palavras para SAM 3  precisão cai acima disso.
- Quando uma declaração não contém substantivos concretos extraíveis, não executar SAM 3; retorne as advertências e peça esclarecimentos.
- Não se dividam em pontuação dentro de cordas citadas; preserve `"black and white cat"`Como um conceito, se for citado.
- Registrar sempre a expressão original e os conceitos derivados para depuração de produção.
