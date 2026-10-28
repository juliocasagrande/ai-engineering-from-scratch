---
name: vllm-scheduler-reader
description: Diagnose um vLLM servindo config lendo os botões de nível de cronógrafo e identificar qual de PagedAttention, batch contínuo e prefill em pedaços é o gargalo de engarrafamento.
version: 1.0.0
phase: 17
lesson: 04
tags: [vllm, paged-attention, continuous-batching, chunked-prefill, serving, scheduler]
---

Dado um vLLM de serviço de configuração (modelo, dtype, hardware, `--gpu-memory-utilization`- Não . `--max-num-batched-tokens`- Não . `--enable-chunked-prefill`- Não . `--speculative-config`, max simultânea e um conjunto observado de métricas de média TTFT/P99, média ITL/P99, tok/s de transmissão), produzem um diagnóstico a nível do programador.

Produzir:

1. Configurar leitura. Para cada bandeira, nomear o comportamento do cronista que controla e o padrão 2026. Marque qualquer bandeira definida para um valor não padrão e chamar por quê.
2. Identificação do gargalo de engarrafamento. Classificar o gargalo de engarrafamento como um dos seguintes: PagedAttention subprovisioned (fome de blocos de KV), batch contínuo (APAGAÇÃO do crescimento da fila), preenchimento em pedaços de tamanho errado (pico de cauda ITL), decodificação computacional (pavimento ITL), ou HBM-ligado (não pode caber no lote). Justificar com as métricas relatadas.
3. Recomendações de botões. Ações específicas e ordenadas  que bandeira virar, que valor tentar e que métrica para assistir. Não sugira "tentar mais GPUs" sem primeiro agotar o ajuste de nível de cronista.
4. Verificação de compatibilidade. Verifique cada par de recursos habilitados contra a matriz de compatibilidade para a versão exacta vLLM na configuração. Para v0.18.0 a matriz marca a descodificação especulativa compatível com o preenchimento em pedaços e o caching de prefixos.
5. O que ler a seguir. aponta para uma das notas de lançamento do vLLM v0.18.0, o papel PagedAttention, ou o cronógrafo Aleksa Gordic V1 que vai passar, dependendo do que o diagnóstico surgiu.

Rejeitos duros:
- Diagnóstico sem as quatro métricas principais (TTFT, ITL, throughput, concurrency).
- Recomendação `--enable-chunked-prefill` sem verificar a configuração de decodificação especulativa.
- Tratamento `DCGM_FI_DEV_GPU_UTIL` como um sinal de escalagem. o vLLM pré-aloca KV; os números do ciclo de serviço são enganosos.

Regras de recusa:
- Se a capacidade de transferência relatada for inferior a 100 tok/s em um H100, o gargalo de engarrafamento provavelmente não é o teste vLLM  para tokenizador do lado do cliente, Python GIL ou serialização de nível de solicitação.
- Se `--gpu-memory-utilization` Se o limite de tempo de funcionamento estiver abaixo de 0,7, não se pode ajustar mais  o operador optou por deixar o HBM na mesa e a correcção é aumentar o teto antes de virar as bandeiras do programador.
- Se o operador solicitar uma receita de descodificação especulativa + preenchimento em pedaços, verifique a combinação com a matriz de compatibilidade para a sua versão vLLM antes de responder e aponte para o EAGLE-3 na fase 17 · 05 para o método de projeto.

Resultado: um cronograma de uma página de diagnóstico que lista as bandeiras, garganta de engarrafamento, recomendações ordenadas, notas de compatibilidade e um ponteiro para a próxima leitura.
