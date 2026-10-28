---
name: mt-evaluator
description: Evaluate a machine translation output for shipping.
version: 1.0.0
phase: 5
lesson: 11
tags: [nlp, translation, evaluation]
---

Dados os textos de origem e a tradução candidata, a saída:

1. Estimativa automática de pontuação.
2. Lista de verificação de cinco pontos por humanos: preservação do conteúdo (sem alucinações), linguagem-alvo correta, correspondência de registro/formalidade, consistência da terminologia com o glossário, se for fornecido, sem truncamento ou explosão de comprimento.
3. Um problema específico para o domínio a investigar. Legal: entidades nomeadas, citações estatutárias. Médico: nomes de medicamentos, dosagens. UI: variáveis de posicionamento como `{name}`- Não .
4. "Navio com revisão" / "Não enviem".

Recusar-se a enviar sem uma verificação de identificação de idioma na saída. Recusar-se a avaliar sem referência a menos que o usuário opte explícitamente pela pontuação sem referência (COMET-QE, BLEURT-QE). Marcar qualquer conteúdo acima de 1000 tokens como provavelmente necessitando de tradução em pedaços.
