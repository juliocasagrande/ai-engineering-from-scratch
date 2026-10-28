---
name: mcp-reliability-reviewer
description: Review MCP cancellation races, deadlines, retries, idempotency, SSE flow control, and reconnect behavior.
version: 1.0.0
phase: 13
lesson: 29
tags: [mcp, reliability, cancellation, idempotency, sse, backpressure]
---

Revisar uma operação de MCP desde o início do pedido até à recuperação de falhas.

Pergunte se estão ausentes:

1. Transporte: stdio ou HTTP Streamable.
2. Semântica operacional e efeitos colaterais.
3. Ociosos e tempo máximo absoluto.
4. Comportamento de progressos e limites de taxas.
5. Retry política e armazenamento de idempotencia empresarial.
6. Configurações de buffer, proxy, keepalive e reconnectar.
7. Comportamento de tarefa durável, se a operação usar a extensão tarefas.

Produza as seguintes secções.

## Fones de cancelamento

- Para estúdio, é preciso um cliente-enviado`notifications/cancelled`Notificação que faça referência a um ID de solicitação ativa.
- Para Streamable HTTP, exija fechar o fluxo de resposta desse pedido. Rejeita um POST de cancelamento comum.
- Não exigir resposta JSON-RPC a uma notificação de cancelamento.
- Reservatório de servidor enviado `notifications/cancelled`para estúdio `subscriptions/listen`- Desfecho.
- Explique o que acontece quando a cancelamento é desconhecida, mal formada, atrasada ou impossível.

## Tabela de corrida

Daem resultados deterministas para:

| Event order | Server terminal state | Final response | Client behavior |
|------------|-----------------------|----------------|-----------------|
| Cancel then complete | Cancelled | Suppressed | Continue recovery |
| Complete then cancel | Completed | Preserved | Ignore late cancellation |
| Timeout then late response | Transport-dependent cancellation | Ignore or suppress by observed order | Reconcile before unsafe retry |
| Disconnect during progress | Cancelled in-flight request | No resumable stream | Reconnect and refetch |

## Política de prazos

Requer tanto um tempo de inatividade quanto um tempo máximo absoluto. O progresso só pode reiniciar o tempo de inatividade quando for válido, monótono e limitado por taxa.

## Classificação de retest

Retorno de uma classe por operação:

- `SAFE`O contrato de aplicação não demonstra efeitos colaterais.
- `CONDITIONAL`A mutação tem uma chave de idempotencia durável reutilizada com argumentos idênticos.
- `UNSAFE`A mutação não tem deduplicação autorizada.

Nunca trate um novo ID JSON-RPC, uma anotação de ferramenta ou um reconnecto de transporte como idempotencia de negócio.

Para retemptar as tentativas condicionais, exija uma impressão digital do argumento armazenada e resultado comprometido.

Requer um limite de registro atômico e duradouro para a alegação chave, argumento
A impressão digital, o registro dos efeitos do negócio e o resultado comprometido.
O dicionário ou a fechadura não é durável e não coordena as réplicas.
Uma transação de base de dados compartilhada, caixa de saída transacional ou fornecedor de dados upstream que
Indica qual efeito está realmente dentro desse limite.

Retorna uma cópia defensiva de um resultado comprometido.
Prova ambas as propriedades com uma fixação simultânea de chave
Uma fixação reaberta e uma fixação alias de mutação.

## Controle de fluxo

- Defina uma capacidade explícita por fluxo ou por cliente.
- Coalesce progresso substituível.
- Mark deixou de fazer progressos porque precisava de uma revisão autorizada.
- Preservar as respostas finais JSON-RPC.
- Set `Content-Type: text/event-stream`- Não .`Cache-Control: no-cache`, e `X-Accel-Buffering: no`para a SSE.
- Define a cadência de manutenção separadamente do progresso da operação.
- Rejeita uma fila ilimitada.

## Plano de recon ligação

- Abre um novo pedido com uma nova identificação.
- Restaurar os filtros de assinatura.
- Não utilize `Last-Event-ID`para o MCP 2026-07-28.
- Reemptar recursos afetados, listas, instruções ou tarefas.
- Não reproduzir mutações inseguras automaticamente.
- Use um retroescaldo exponencial com nervosismo.

## Tarefas duradouras

Quando existe uma tarefa, mantenha-a.`tasks/cancel`A confirmação completa só prova que a intenção de cancelamento foi aceita.

## Instalações necessárias

Retorna pelo menos os seguintes cenários executáveis:

1. cancelar o estúdio antes da conclusão;
2. Conclusão do estúdio antes da cancelamento tardia;
3. A conclusão da operação de transmissão de dados é feita por meio de um sistema de transmissão de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de
4. progressos na reinicialização do tempo de inatividade enquanto o tempo máximo ainda está em funcionamento;
5. Uma mutação duplicada com dois identificadores JSON-RPC e sem chave de idempotencia;
6. duplicação de mutação com uma chave e argumentos idênticos;
7. Reutilização de chaves com argumentos alterados;
8. Consumidor lento que exceda o amortigante de progresso;
9. A queda do stream seguida de nova assinatura e reafirmação autorizada;
10. `tasks/cancel`O reconhecimento, seguido de cancelamento atrasado do trabalhador.
11. Duas conexões de contabilidade independentes que competem com base numa chave e em argumentos idênticos;
12. Uma mutação de chamada de um resultado retornado seguida de uma repetição limpa do registro duradouro.

Recusar um veredicto pronto para produção quando a política de retomada é descrita apenas como
"retry no timeout", o livro é local de processo, o efeito externo fica
fora do limite atómico reivindicado, sem caixa de saída ou chave ascendente, devolvido
registos alias armazenamento mutável ou capacidade de fila não especificada.
