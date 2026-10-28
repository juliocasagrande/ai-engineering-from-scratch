---
name: reflexion-buffer
description: Maintain an episodic-memory buffer of reflections for verbal RL with TTL, dedup, and scoped scope.
version: 1.0.0
phase: 14
lesson: 03
tags: [reflexion, episodic-memory, self-healing, verbal-rl, sleep-time]
---

Dada uma classe de tarefas (repetindo o tipo de agente executado , por exemplo "refactor a função", "cobrir um ticket de suporte"), mantenha um buffer de memória episódica de reflexões. Cada reflexão registra um modo de falha e a visão corretória em linguagem natural. O buffer é prependido para a próxima prova da mesma classe de tarefas.

Produzir:

1. Captura de reflexão: após um ensaio terminar com uma pontuação do avaliador abaixo do limiar, emite uma reflexão de uma linha na forma "Eu não consegui fazer X porque Y; da próxima vez, Z. " Jogue reflexões sobre falhas externas (rede, 500s upstream) a menos que sejam reprodutíveis.
2. TTL e dedup. As reflexões expiram após os testes N por padrão (10 sugeridos). Duplicados exatos colapsam. Duplicados próximos (> 0,9 cosinus em um modelo de inserção pequena, ou substring compartilhada >= 80%) mantêm apenas os mais recentes.
3. Política de alcance. Três escopoes: classe de tarefas (por nome de tarefa), usuário (em todas as tarefas para o mesmo usuário), agente (em todos os usuários). Default é classe de tarefas. Escala para o alcance do usuário somente se a reflexão se refere às preferências específicas do usuário; nunca escalar para o alcance do agente automaticamente.
4. Compação: quando o buffer excede o orçamento, executar compação no tempo de sono: agrupamento quase duplicado, resumir, fundir. Compação corre fora do caminho quente  não atrasar a resposta do agente primário.
5. Integração rápida. Emite um bloco único intitulado "O que aprendi de testes anteriores" com uma lista com bolas. Cap em 6 itens no prompt; sobreflow vai para um item de resumo separado ("... e 4 reflexões antigas sobre tempos de espera").

Rejeitos duros:

- Escrever reflexões como "seja mais cuidadoso da próxima vez". Isso não é prático.
- Reflexões expirando com base no tempo do relógio de parede em vez de contar a prova.
- Armazenamento de reflexos que fazem referência a segredos (chaves API, tokens, PII). Rejeitar com um erro específico de classe "contece segredo" antes de se comprometer com o buffer.

Regras de recusa:

- Se não estiverem anexados avaliadores, recusar e recomendar a lição 05 (Auto-refinamento/Crítico)  A reflexão requer um sinal, não um sentimento intestinal.
- Se a classe de tarefas for de um só tiro (nunca se repete), recuse; memória episódica não faz nada para uma tarefa que nunca se repete.

A saída: um arquivo de tampão estruturado (JSON com objetos de reflexão: ID de ensaio, classe de tarefas, escopo, texto, created_at, ttl_remaining), um bloco de solicitação para o próximo ensaio e um relatório de "reflexões permanentes" listando entradas que expirarão em breve.

Terceira com uma nota "o que ler a seguir" apontando para a lição 06 (compressão de contexto) se o tampão continuar a bater no seu limite, ou lição 08 (computação do tempo de sono Letta) para mover a compactação do caminho quente.
