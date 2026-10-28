---
name: sampling-tuner
description: Escolha estratégia de decodificação (com ganância / temperatura / top-k / top-p / min-p / especulativa) para uma determinada tarefa de geração.
version: 1.0.0
phase: 7
lesson: 7
tags: [gpt, sampling, decoding, inference]
---

Dado um trabalho de geração (código, escrita criativa, raciocínio, diálogo, saída estruturada) e um objetivo de latência/qualidade, saída:

1. Método de amostragem, uma de: gananciosa, apenas de temperatura, top-k, top-p, min-p, beam-k, especulativa.
2. Valores de parâmetro: temperatura, top-k, top-p, min-p, penalidade de repetição  números concretos ligados ao tipo de tarefa. (por exemplo, temperatura 0,2 + top-p 1,0 para código; min-p 0,1 + temperatura 0,7 para chat.)
3. Parar as condições. `max_new_tokens`, lista de tokens de parada, parada baseada em padrões (por exemplo, fechamento) `</tool_call>`)).
4. Determinismo de alternância: semente fixa para reprodução; sinalização de se o caso de utilização (evental, legal) o requer.
5. Verificação da qualidade: teste de uma linha contra o objetivo da tarefa (testes de unidade de compilação/apresentação, factualidade, validade do formato, etc.).

Recusar recomendar temperatura > 1,0 para saída estruturada ou conclusão de código  Risco de alucinação aumenta drasticamente. Recusar recomendar ganância pura para diálogo aberto  o modelo será loop. Recusar enviar uma configuração de amostragem sem uma lista de tokens de parada especificada quando o modelo pode gerar modelos/ferramentas.
