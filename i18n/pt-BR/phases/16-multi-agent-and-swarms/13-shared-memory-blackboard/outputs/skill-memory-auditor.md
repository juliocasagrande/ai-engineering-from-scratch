---
name: memory-auditor
description: Auditar o projeto de memória compartilhada de um sistema multi-agente para proveniência, versão, separação do verificador e esquema de projeção.
version: 1.0.0
phase: 16
lesson: 13
tags: [multi-agent, shared-state, blackboard, memory-poisoning, provenance]
---

Dado um código base ou documento de arquitetura multi-agente, auditem o projeto de memória compartilhada e a exposição de bandeira ao envenenamento de memória.

Produzir:

1. **Topology.** Completo conjunto de mensagens, tabela negra dividida em tópicos, visão projetada por agente ou híbrido? Nomear a estrutura de dados (lista, dit, quadro de pandas, armazenamento de vetores, tabela SQL).
2. **Provenance fields.** Em cada escrita, a entrada registra: identificação do escritor, timestamp, hash ou texto prompt, rastreamento de chamada de ferramenta, URI de fonte ou nome da ferramenta?
3. **Update model.** O log apêndice apenas, ou os escritores mutam no lugar? Se mutação, qual é o mecanismo de controle de concurência (bloqueio, versão otimista, nenhuma)?
4. **Verifier separation.** Existe um agente de leitura apenas com acesso independente à fonte? Pode escrever para o pool principal (não deve)? Onde vai sua saída?
5. **Projection schema.** Se o projeto usa projeções (redutores de LangGraph, tópicos de tabela negra, visões de escala de papel), o esquema está documentado? Como os novos agentes declaram a projeção que consumem?
6. **Poisoning risk score.** Pontuação 1-5 em cada eixo: [completude de origem], [supersessão sobre mutação], [independência do verificador], [claridade do esquema de projeção]. Um sistema que pontua abaixo de 3 em qualquer eixo é sinalizado.

Rejeitos duros:

- Qualquer auditoria que não marque um verificador faltante. Um verificador não escritível com acesso independente à fonte é a mitigação da carga; qualquer outra mitigação é decorativa sem ela.
- Auditores que recomendam " acrescentar mais testes". Os testes não detectam envenenamento da memória porque o envenenamento produz resultados plausíveis que passam os testes.
- Auditoria que recomenda hashing do conteúdo como a única proveniência. Um hash diz-lhe * o que * foi escrito, não * quem * ou * de onde *.

Regras de recusa:

- Se a base de código oculta o estado compartilhado num serviço externo (Redis, Postgres, vector DB) sem ferramentas de inspeção, indicar que a auditoria não pode ser concluída sem acesso à leitura da produção.
- Se o sistema tiver menos de três agentes, note que o risco de intoxicação da memória é baixo, mas a proveniência ainda é seguro barato.
- Se o sistema utilizar um quadro com gestão de estado integrada (ponte de controlo LangGraph, grupo AutoGen), auditá-los em vez de os redirecionar.

Resultado: um relatório de duas páginas. Comece com um resumo de uma frase ("Estado compartilhado é um conjunto completo de mensagens sem origem e sem verificador  alto risco de intoxicação. "), em seguida, as seis seções acima. Terceira com uma lista de ações prioritárias: três alterações, cada uma rotulada [crítico] [deve] ou [próprio para ter], com tempo estimado para implementação.
