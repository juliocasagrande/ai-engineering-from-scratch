---
name: obs-platform-wiring
description: Pick an observability platform (Langfuse, Phoenix, Opik, Datadog) and wire traces + evals + prompt versions into an existing agent.
version: 1.0.0
phase: 14
lesson: 24
tags: [observability, langfuse, phoenix, opik, datadog, tracing]
---

Dado o tempo de execução do agente e os requisitos do produto, escolha uma plataforma de observabilidade e acopla o cabo.

Decisão:

1. Precisa de gerenciamento rápido + repetição de sessão em um só lugar -> **Langfuse**- Não .
2. Precisa de relevância profunda do RAG + detecção de deriva/anomalia -> **Phoenix**- Não .
3. Precisa de otimização automática de prompt + proteção de PII -> **Opik**- Não .
4. Já executa o Datadog -> **Datadog LLM Observability**(mapas GenAI nativo de v1.37+).
5. Preciso de licença ELv2 livre -> **Langfuse**(MIT) ou **Opik**(Apache 2.0); evitar Phoenix para distribuição pura de OSS.

Produzir:

1. Instrumentos OTel GenAI (Lessão 23)  este é o substrato comum.
2. Configuração de SDK ou OTel para exportadores específicos da plataforma.
3. Rubrico de juiz de LLM para o seu domínio (correção factual, alcance, tom, qualidade de recusa).
4. A versão rápida ligada a traços (Langfuse) ou a configuração de clustering de traços (Phoenix) ou definições de experimentos (Opik).
5. Proteção de conteúdo registrado: redacção de PII, limpeza secreta.
6. Painéis de controlo: saúde da sessão, taxonomia das falhas, distribuição de latência, custo por sessão.

Rejeitos duros:

- O transporte sem avaliações, o rastreamento é caro.
- Utilização de um juiz de LLM autografado sem verificação externa. padrão CRITICO (Lessão 05): os juízes precisam de ferramentas externas para a base factual.
- Armazenamento de PII em corpos de extensão.

Regras de recusa:

- Se o utilizador pedir "uma plataforma para tudo", recusar e oferecer a decisão acima.
- Se o produto não tiver critérios de aceitação para cada tarefa de agente, recuse-se a enviar avaliações.
- Se o utilizador quiser "sem amostragem, capture tudo", rejeite.

Output: `instrumentation.py`- Não .`judge.py`- Não .`dashboards.md`- Não .`README.md`A descrição da estratégia de amostragem e resposta a incidentes, que explica a escolha da plataforma, a rubrica e o que deve ser feito.
