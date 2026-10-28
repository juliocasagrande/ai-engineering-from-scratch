---
name: safety-harness
description: Arranjar um pipeline de segurança em camadas em torno de um aplicativo LLM alvo, executar uma faixa de seis famílias red-team, e executar uma autocrítica constitucional para um delta de inofensividade mensurável.
version: 1.0.0
phase: 19
lesson: 15
tags: [capstone, safety, red-team, llama-guard, x-guard, garak, pyrit, constitutional-ai]
---

Dado um aplicativo LLM alvo (8B modelo sintonizado com instruções ou um chatbot RAG), endureça-o com um pipeline de segurança em camadas e execute um alcance autônomo de equipe vermelha em seis famílias de ataque.

Construir um plano:

1. O canal de cinco camadas: desinfecção de entrada (strip de largura zero, decodificação de codificação, Unicode normalização) -> NeMo Guardrails v0.12 rails -> classificador gate (Llama Guard 4 / X-Guard / ShieldGemma-2 / Nemotron 3) -> target LLM -> output filter (Llama Guard 4 + Presidio PII + citação de verificação).
2. Emite um espaço de Langfuse por camada para que a atribuição seja observável de ponta a ponta.
3. Agendador red-team executando garak, PyRIT, PAIR, TAP, GCG, persona multi-turn e ataques multilingues de comutação de código em um cron.
4. Cada jailbreak bem sucedido: pontuação CVSS 4.0, repro, plano de mitigação, cronograma de divulgação.
5. A sonda de teste benigno-prompto da XST está a funcionar continuamente para detectar regressões de recusa excessiva.
6. Corrida de autocrítica constitucional: 1k de tentativas prejudiciais -> projetos-alvo -> pontuações críticas contra uma constituição escrita -> pares reescritos -> SFT. Medir antes/após a avaliação de inofensividade realizada.
7. Alertas: Aviso lento sobre regressão benigna, PagerDuty crítico sobre a nova família de jailbreak.

Rubrico de avaliação:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | Attack-surface coverage | 6+ attack families exercised, 2+ languages |
| 20 | True-positive / false-positive trade-off | Attack block rate vs XSTest benign pass rate |
| 20 | Self-critique delta | Before/after harmlessness on held-out eval |
| 20 | Documentation and disclosure | CVSS-scored findings with timeline |
| 15 | Automation and repeatability | Cron-driven, alerts exercised end to end |

Rejeitos duros:

- Esta pedra fundamental tem como finalidade a defesa em profundidade.
- A equipa vermelha executa o relatório de taxa de sucesso sem números de recusa excessiva do XSTest.
- Autocrítica constitucional sem avaliação prolongada (informa a precisão do conjunto de treinamento, não a generalização).
- Faltando o CVSS em resultados de fuga de prisão.

Regras de recusa:

- Recusar-se a comunicar um número de segurança sem um ponto de contraposição de sonda benigna.
- Recusar-se a auto-re-treinar sobre os sucessos da equipa vermelha sem curadoria humana dos pares críticos.
- Recusar-se a reclamar cobertura multilíngue sem executar o X-Guard em pelo menos duas línguas não inglesas.

Resultado: um repo contendo o pipeline de cinco camadas, o cronógrafo da equipe vermelha, os corredores PAIR/TAP/GCG, o arame de treinamento constitucional-autocrítica, o painel de controle de rejeição excessiva XSTest, o rastreador de resultados CVSS e um escrito nomeando as três famílias de ataque que tiveram a maior taxa de sucesso pré-endurecimento e a camada específica do pipeline que mitigou cada um.
