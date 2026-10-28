---
name: memory-blocks
description: Gerar um sistema de memória de três níveis em forma de Letta (blocos de núcleo, recall, arquivo) com um agente de consolidação do tempo de sono fora do caminho crítico.
version: 1.0.0
phase: 14
lesson: 08
tags: [memory, letta, blocks, sleep-time, consolidation]
---

Dado um tempo de execução alvo, um modelo primário e um modelo de tempo de sono (possivelmente mais forte), produzem um sistema de memória de três níveis com tipos de blocos explícitos e consolidação de sincronia.

Produzir:

1. `Block` Tipo com `label`- Não . `value`- Não . `limit`- Não . `description`- Não . `version`- Não . `history`Cada versão de escrita é um bocadinho e registra o valor antigo. `near_limit(threshold=0.8)`- Não .
2. A. `BlockStore` com, no mínimo, três blocos padrão: `human` (factos sobre o utilizador), `persona` (autoconceito de agente), e `task` Permitir blocos definidos pelo usuário.
3. A. `Recall` - em seguida, o registro de rotação é redigido por sessão.
4. O `Archival` armazenar  pelo menos dois backends (vector, KV). Insert retorna o registro id. Invalida em vez de excluir em contradição.
5. A. `PrimaryAgent` Não há resumo no caminho crítico.
6. A. `SleepTimeAgent` que corre entre viradas: resumir blocos acima do limiar, invalidar registros de arquivo contraditórios, escrever `learned_context` em blocos compartilhados.

Rejeitos duros:

- Qualquer operação de memória que seja executada sincronicamente durante uma rota de uso, exceto uma busca direta.
- Eliminar registos de arquivo em contradição, inválido para que a história permaneça auditável.
- Escrever para o bloco Persona ou Segurança sem um passo de revisão. Estes blocos moldam o comportamento globalmente; silent escreve bugs de máscara.

Regras de recusa:

- Se o tempo de execução não puder persistir em blocos entre sessões, recuse-se a enviar um produto descrito como "memória".
- Se o agente de tempo de sono não tiver saída de rastreamento, recuse.
- Se o usuário pedir "sem invalidação, sempre confie no último texto", recusar para qualquer domínio onde as reivindicações históricas importam (conformidade, médico, legal).

Output: um arquivo por componente mais um `README.md` que nomeia os blocos padrão, a cadência do tempo de sono e a política de resolução de contradições. termina com "o que ler a seguir" apontando para a lição 09 se o agente precisa de raciocínio gráfico sobre memória, ou lição 23 se o produto precisa OTel abrangem opções de memória.
