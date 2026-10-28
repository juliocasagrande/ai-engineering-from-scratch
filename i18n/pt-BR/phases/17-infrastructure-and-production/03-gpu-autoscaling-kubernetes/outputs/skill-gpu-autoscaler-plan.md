---
name: gpu-autoscaler-plan
description: Desenhar um plano de autoescalação de GPU de três camadas (Karpenter + KAI Scheduler + sinais de aplicação) para um cluster de servidores LLM baseado em Kubernetes. Diagnose as armadilhas DCGM_FI_DEV_GPU_UTIL e falhas de alocação parcial.
version: 1.0.0
phase: 17
lesson: 03
tags: [kubernetes, gpu, autoscaling, karpenter, kai-scheduler, hpa, dynamo-planner, llm-d]
---

Dada a topologia do cluster (nodos, tipos de GPU, domínios NVLink), forma da carga de trabalho (configuração TP/PP, concurência média, fator de explosão) e SLO (TTFT P99, goodput), produz um plano de autoescalação de três camadas.

Produzir:

1. Layer 1  Carpenter NodePool. Especificar `instance-type`- Não . `capacity-type` (a pedido / local / reservado), `consolidationPolicy` (deve ser) `WhenEmpty` com `consolidateAfter: 1h` para pools de GPU), manchas que excluem cargas de trabalho não GPU, e rótulos para a selecção do programador KAI.
2. Layer 2  Política de agendamento de KAI. Indique se é necessário agendar grupos (sim para TP/PP > 1). Define restrição de topologia (domínio NVLink, rack, zona). Especifique hierarquia de fila e regras de pré-empenho para os inquilinos de produção versus treinamento.
3. Layer 3  Aplicação automática. Escolha o sinal: profundidade de fila para cargas de trabalho pre-enchidas, utilização de cache KV para decodificação, goodput composto para misturado. Proibido `DCGM_FI_DEV_GPU_UTIL` e explicar o porquê.
4. Se utilizar a fase 17 · 17 preenchimento/decodificação desagregada, especifique HPAs separados  sinal de profundidade de fila para o pool de preenchimento, sinal de utilização KV para o pool de decodificação.
5. Dimensão de piscina quente: réplicas mínimas prontas para os caminhos críticos SLO, com base na restrição P99 TTFT e no tempo de arranque a frio observado (provimento do nó + carga do modelo).
6. Monitoramento. Metricas para painel: profundidade de fila por réplica, utilização de KV por réplica, tempo de espera de fornecimento de nós, contagem de adiamento de agendamento de gang, eventos de consolidação Karpenter.

Rejeitos duros:
- Recomendação de HPA sobre `DCGM_FI_DEV_GPU_UTIL`- Recusar e nomear a profundidade da fila + utilização de KV como os sinais corretos.
- Deixando `consolidationPolicy: WhenEmptyOrUnderutilized` Recusar e citar o risco de expulsão de empregos.
- Ignorar a programação de gangs para uma carga de trabalho TP/PP.

Regras de recusa:
- Se o cluster tiver apenas um tipo de GPU e um nó, recusar a proposta de Karpenter  o cliente precisa de um servidor administrado sem servidor (Fase 17 · 02) primeiro.
- Se o operador pedir "escalada na memória da GPU", rejeitar  vLLM pré-aloca para `--gpu-memory-utilization`A memória permanece próxima de 90% mesmo com uma única solicitação.
- Se a programação de gangue for rejeitada para uma carga de trabalho TP-8 citando complexidade, recusar a certificação do plano  colocação de um único pod em 8 GPUs espalhados falha atomicamente.

Resultado: um plano de uma página com um snippet Karpenter YAML, um snippet de configuração KAI Scheduler, uma escolha de sinal HPA / autoescalador personalizado, um número de piscina de calor e cinco métricas do painel de controle.
