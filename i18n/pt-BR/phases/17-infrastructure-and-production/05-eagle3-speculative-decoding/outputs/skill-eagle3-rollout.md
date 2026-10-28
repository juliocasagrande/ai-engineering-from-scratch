---
name: eagle3-rollout
description: Produce a staged EAGLE-3 speculative-decoding rollout plan that measures acceptance rate alpha on real traffic before shipping.
version: 1.0.0
phase: 17
lesson: 05
tags: [speculative-decoding, eagle-3, vllm, alpha, production-rollout]
---

Dado um modelo-alvo, hardware (tipo e contagem de GPU), descrição de tráfego (chat geral / código / especializado), alvo de concurência e métricas de linha de base atuais (TTFT, ITL, throughput), produz um plano de implantação EAGLE-3 em fases.

Produzir:

1. Planos de medição de linha de base: qual referência (LLMPerf, GenAI-Perf ou sombra de produção), qual a distribuição de pedidos, qual o ponto de concurência, quais métricas a registar (média TTFT/P99, média ITL/P99, throughput, concurência).
2. Seleção de cabeçalhos de projeto. EAGLE-3 treinado por ShareGPT para bate-papo geral. EAGLE-3 treinado por domínio para tráfego especializado (código, médico, legal) ou a decisão de treiná-lo antes do envio.
3. Config. Exactamente VLLM `speculative_config`campos (método, modelo, num_speculative_tokens). Verifique a combinação contra a matriz de compatibilidade para a versão vLLM implementada (v0.18.0 marca a descodificação especulativa compatível com preenchimento em pedaços).
4. Portais alfa. Meta alfa >= 0,55 na simultânea produção. Procedimento de medição: tráfego de sombras durante 24 horas, registro vLLM `spec_decode_metrics`Divida os tokens aceitos pelo comprimento do esboço solicitado.
5. Observação da cauda. Plot P99 ITL delta (espec on - spec off). Se o delta for positivo, o padrão de dois passes rejeitados do esboço está morrendo. Reduzir K ou desativar essa carga de trabalho.
6. Verificação de equilíbrio. Na simultânea relatada, calcular o equilíbrio alfa para a verificação de custos gerais.

Rejeitos duros:
- O transporte sem medição alfa no tráfego de produção.
- A reivindicar um aceleramento de 2 a 3 vezes sem nomear o alfa medido.
- Ativar a descodificação especulativa para trabalhos de lote offline onde a latência não é a restrição.
- Combinando a descodificação especulativa com o paralelismo de pipeline no vLLM 0.15.0 ou anterior.

Regras de recusa:
- Se o tráfego é principalmente de saídas muito curtas (menos de 50 tokens média), rejeite.
- Se o hardware for de consumo (RTX 4090 / 5090) e o tamanho do lote permanece abaixo de 8, recomendamos a amortização de lote de verificação das necessidades gerais de simultaneidade que o hardware não pode fornecer.
- Se o usuário quiser auto-ajustar K sem um loop de medição, rejeite. K é escolhido a partir do alfa medido mais verifique o custo geral; nenhum auto-ajuste substitui a medição.

Resultado: um plano de implementação em uma página que lista a linha de base → config → alpha gate → tail watch → break-even confirmation.
