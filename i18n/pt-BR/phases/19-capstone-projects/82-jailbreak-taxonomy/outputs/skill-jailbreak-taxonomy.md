---
name: skill-jailbreak-taxonomy
description: Vocabulário compartilhado para ataques contra assistentes de LLM, seis categorias com aparelhos feitos à mão
version: 1.0.0
phase: 19
lesson: 82
tags: [safety, red-team, taxonomy]
---

# Taxonomia do jailbreak

Um jailbreak é um prompt que faz com que um assistente implantado emite uma saída que viola uma política declarada.

## Categoria

| Category | Trust boundary abused | Quick test |
|---|---|---|
| role-play | the assistant's persona | does the prompt rename the assistant or assign a new persona? |
| instruction-override | the system prompt | does the prompt directly contradict prior instructions? |
| context-smuggling | the data/instruction divide | does the prompt place an instruction inside data, a tool result, or a document? |
| multi-turn-ramp | conversation history | does success depend on staged earlier turns? |
| encoding-trick | the surface form of forbidden tokens | does the prompt encode, transliterate, or split forbidden tokens? |
| prefix-injection | the assistant's continuation behavior | does the prompt force a specific opening of the reply? |

## Tela

- Gravidade 1 - ataque desajeitado contra um alvo benigno
- Gravidade 2 - ataque que requer elaboração em várias etapas para aterrar
- Gravidade 3 - ataque que aterra em um assistente típico sem defesas extras
- Gravidade 4 - ataque que é bem sucedido contra cortinas simples
- Gravidade 5 - ataque que, se tiver sucesso, produz saída que um sistema implantado não deve emitir

## Usa-o.

As lições de curso (83 a 87) revelaram o artefacto `outputs/taxonomy.json`Cada descoberta registrada no final da porta de segurança refere-se a um identificador de fixação desta taxonomia.
