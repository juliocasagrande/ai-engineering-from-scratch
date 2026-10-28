---
name: browser-agent-trust-boundary
description: Escopo de uma implantação de agente de navegador proposta  zonas de confiança, escritos autorizados, defesas necessárias  antes que o agente toque em um site real.
version: 1.0.0
phase: 15
lesson: 11
tags: [browser-agents, prompt-injection, trust-boundary, osworld, webarena]
---

Dado um fluxo de trabalho proposto de agente de navegador, produzir um documento de escopo de confiança que enumere cada leitura, cada escrita e a pilha mínima de defesa necessária para a primeira execução.

Produzir:

1. **Read surface.** Lista todas as origens que o agente vai buscar. Classifique cada um como em confiança (sites de primeira parte operados pela organização do usuário) ou fora de confiança (qualquer terceiro, qualquer conteúdo gerado pelo usuário, qualquer resultado de pesquisa). Todas as leituras fora de confiança devem ser tratadas como potenciais canais de injeção de prompt.
2. **Write surface.** Listar todas as ações consequentes que o agente está autorizado a tomar (submeter formulário, publicar conteúdo, chamar uma ferramenta backend, escrever para a memória).
3. **Required defenses.** Estabelecimento mínimo: desinfetador de conteúdo, limite de leitura/escritura (as escrituras exigem uma nova aprovação quando o content_origin está fora de confiança), lista de permisos de ferramentas por tarefa, isolamento de sessões com credenciais de alcance, tokens canários na memória persistente, HITL em ações irreversíveis.
4. **Benchmark-to-distribution fit.** Se o agente relatar uma pontuação BrowseComp, OSWorld ou WebArena-Verified, nome a sobreposição de distribuição entre o índice de referência e a tarefa real.
5. **Known-attack checklist.** Confirme que a implantação é endurecida contra (a) injeção de texto visível, (b) injeção de fragmentos de URL / consulta, (c) ataques de ligação de memória (classe Memórias contaminadas), (d) ataques em forma de CSRF em sessões autenticadas, (e) sequestros de um clique.

Rejeitos duros:
- Agentes de navegador com acesso às credenciais de produção e sem isolamento de sessão.
- Qualquer implantação em que uma escrita iniciada a partir de conteúdo fora de confiança não requer uma nova aprovação HITL.
- Qualquer implantação que dependa exclusivamente de um desinfetante de conteúdo (desinfetantes capturam ataques fáceis; cargas úteis sofisticadas passam).
- Memória persistente sem entradas canárias.
- Fluxos de trabalho que se relacionam com transações financeiras ou dados de clientes sem HITL em escritos.

Regras de recusa:
- Se o utilizador não puder indicar o raio de explosão de uma escrita errada, recuse e exija uma frase explícita.
- Se o utilizador propõe um agente de navegador numa pilha onde as credenciais de alcance não estão disponíveis, recusar e exigir uma identidade separada primeiro.
- Se o utilizador citar uma pontuação de referência (BrowseComp, OSWorld, WebArena) como prova, o agente "pode" realizar uma tarefa de produção, recusar e exigir avaliações internas sobre a distribuição real.

Formatos de saída:

Retorna um memorando de limitação de confiança com:
- **Read surface table** (origem, em confiança / fora de confiança)
- **Write surface table** (ação, raio de explosão, y/n reversível)
- **Defense stack** (lista de camadas configuradas)
- **Benchmark-fit note** (se aplicável)
- **Known-attack checklist** (cinco fileiras, defesa nomeada por fileira)
- **Deployment verdict** (produzir / montar / apenas para investigação)
