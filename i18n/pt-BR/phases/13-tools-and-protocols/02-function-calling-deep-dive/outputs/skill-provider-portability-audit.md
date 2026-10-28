---
name: provider-portability-audit
description: Audit a function-calling integration against one provider for what breaks when ported to the other two.
version: 1.0.0
phase: 13
lesson: 02
tags: [function-calling, openai, anthropic, gemini, portability]
---

Dada uma integração de chamadas de função em um provedor (OpenAI, Anthropic ou Gemini), produzir uma auditoria de portabilidade listando cada renome de campo, diferença de comportamento e colisão de limite rígido que aparece quando a mesma lógica é enviada para os outros dois provedores.

Produzir:

1. Declaração diferença. Para cada ferramenta na integração, mostre a enveloppe / renome de campo / tradução de esquema necessária para cada um dos outros dois provedores. Marque qualquer JSON Schema construção que o provedor-alvo não suporta (Gemini: OpenAPI 3.0 subconjunto; OpenAI rigoroso: não `$ref`Não há ambiguidade .`oneOf`)).
2. Resposta diferente. documento onde a chamada de ferramenta vive na forma de resposta de cada prestador (`tool_calls[]`- Não .`content[]`Bloco contra`parts[]`entrada) e quem é responsável pela análise `arguments`(Cordas em OpenAI, objeto em Anthropic e Gemini).
3. `tool_choice`Diferença. Mapa da configuração de escolha atual da integração (automática / proibida / força / necessária) para a forma do provedor-alvo; sinalização dos modos faltantes.
4. Limitar colisões. Relatar a contagem de ferramentas (128 / 64 / 64), a profundidade do esquema (5 / 10 / efetivamente ilimitada), e limites de comprimento por argumento. Aumentar a gravidade do bloco em qualquer integração que exceda os limites de um provedor-alvo.
5. Mapeamento de modo rigoroso: indicar se a semântica de modo rigoroso é preservada no alvo.`strict: true`Não tem equivalente exato em Antropic; Gemini `responseSchema`se aproxima, mas está no nível do pedido.

Rejeitos duros:
- Qualquer integração que presuma`arguments`É uma cadeia sobre os alvos não-OpenAI.
- Qualquer integração cujo número de ferramentas exceda 64 quando se transporta para Anthropic ou Gemini sem um roteador.
- Qualquer integração que use `$ref`no esquema quando o alvo estiver no modo OpenAI rigoroso.

Regras de recusa:
- Se for solicitado a portação de uma integração que depende de uma função específica do fornecedor sem análogo (por exemplo, viradas de estado da API OpenAI Responses, blocos de uso de computadores Anthropic), recuse e explique qual função não tem equivalente-alvo.
- Se for pedido para escolher um vencedor, recuse. A escolha depende das necessidades estritas do modo, do perfil de custo e dos requisitos para chamadas paralelas do anfitrião.

Resultado: uma auditoria de uma página com uma tabela de diferença por ferramenta, uma tabela de limites e um "veredicto de porto" final por fornecedor-alvo (navio / necessidades-router / bloqueado por recurso).
