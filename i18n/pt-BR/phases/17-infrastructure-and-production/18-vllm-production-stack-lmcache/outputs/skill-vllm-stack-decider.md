---
name: vllm-stack-decider
description: Decidir o layout de implantação do vLLM  gráfico de capacetes de produção, descarga de KV (CPU nativa ou LMCache), integração de roteador/observabilidade  dada a carga de trabalho e o tamanho da frota.
version: 1.0.0
phase: 17
lesson: 18
tags: [vllm, production-stack, lmcache, kv-offload, connector-api]
---

Dada a carga de trabalho (forma de urgência, concurência, padrão de reutilização de prefixos), frota (motores, tipo de GPU) e contexto operacional (Kubernetes-nativo, multi-arrendante, orçamento), produzir um plano de pilha vLLM.

Produzir:

1. Estaca. Utilize o gráfico de capacetes de produção vLLM (recomendado para novas implantações) ou rolem a sua própria.
2. Descarga de KV.
   - Nenhum (interrupções curtas, baixa concurência  custos gerais excederem o benefício).
   - Descarga de CPU vLLM nativa (pressão HBM de motor único, simples).
   - Conector LMCache (reutilização de préfixos multi-motor, preposição pesada ou solicitações compartilhadas para vários inquilinos).
3. Monitoramento da utilização de HBMs. `--gpu-memory-utilization` com espaço de cabeça; alerta de 92%+ sustentada como sinal de pré-preempção.
4. Integração do roteador. Roteador consciente de cache (Fase 17 · 11).
5. Observabilidade: Prometheus scrape por motor, ATEL GenAI atributos (fase 17 · 13), modelo de painel de instrumentos Grafana da pilha de produção.
6. Impacto esperado. Quantificar o ganho esperado de capacidade versus corrente  referir a forma de referência 16x H100 (LMCache ajuda quando a pegada de KV excede o HBM).

Rejeitos duros:
- Implementação de LMCache sem prefixos ou preempção compartilhados.
- A execução de VLLM sem monitoramento de pressão HBM.
- - a produção de pilhas de rolos manuais quando o gráfico do capacete cobre o caso de utilização.

Regras de recusa:
- Se a frota tiver < 2 motores, rejeite LMCache  reutilização transversal de motores é o ponto; uso único de motores nativos.
- Se a carga de trabalho tiver indicadores < 1K tokens e < 100 simultaneidades, rejeite qualquer tipo de descarga  O espaço de comando HBM é suficiente.
- Se a equipe não tem capacidade para K8, recuse a produção de pilhas  comece com um vLLM de motor único + proxy simples.

Resultado: um plano de uma página de nomeação de pilha, opção de descarga KV, monitoramento HBM, integração do roteador, observabilidade, impacto esperado.
