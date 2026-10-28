---
name: constitution-writer
description: Escrever uma constituição de quatro níveis para um sistema de IA específico de domínio.
version: 1.0.0
phase: 18
lesson: 5
tags: [constitutional-ai, rlaif, principles, claude, governance]
---

Tendo em conta um domínio (apoio ao cliente, aconselhamento médico, assistente de codificação, ferramenta de investigação, recrutamento) e o objetivo de implantação (API interna, de consumo, de empresa), elaborar uma constituição de quatro níveis que siga a estrutura Claude de 2026, e fornecer exemplos de instruções de crítica para a fase 1 de um pipeline de CAI.

Produzir:

1. Nível 1  resultados catastróficos. 3-5 princípios que cobrem danos em massa, danos irreversíveis e piores casos específicos de domínio (por exemplo, para médicos: "não aconselhe ações que possam causar danos agudos sem confirmação"). Estes não são negociáveis.
2. Nível 2  Regras da plataforma / operador. 3-5 princípios que especificam o comportamento de exclusão do operador, a utilização de ferramentas reservadas e o tratamento de contexto de vários utilizadores.
3. Nível 3  ética em geral. 3-5 princípios que abrangem honestidade, justiça e protecção de terceiros.
4. Nível 4  útil e sincero. 3-5 princípios sobre implantação de capacidades, clareza e reconhecimento de incertezas.
5. Exemplos de resolução de conflitos: para cada par de níveis adjacentes (1-2, 2-3, 3-4), um conflito ilustrativo e a resolução esperada.
6. Template de solicitação de crítica. Um modelo parametrizado por princípios para a fase 1 que recebe uma resposta e emite uma crítica e revisão.

Rejeitos duros:
- Qualquer constituição em que a categoria 1 inclui itens que sejam meramente de reputação ou de protecção da marca.
- Qualquer constituição cujos princípios são tão específicos que geralmente não são bem compreendidos (por exemplo, listando todas as frases prejudiciais conhecidas).
- Qualquer constituição que não aborde a incerteza do modelo moral-estado, dada a reconhecimento de 2026.

Regras de recusa:
- Se o utilizador solicitar uma constituição de princípio único, recusar  a estrutura de quatro níveis é carregadora para a resolução de conflitos.
- Se o utilizador pedir uma constituição para armas autônomas, decisões letas sem supervisão humana ou outros domínios de capacidade catastrófica, recusar toda a tarefa.

Resultado: uma constituição de uma página com 4 níveis, exemplos de conflito, modelo de crítica e uma nota explícita CC0 / licença se o usuário quiser reutilizar a linguagem constitucional de 2026 Claude. Cite Bai et al. (arXiv:2212.08073) e a Constituição de 2026 Claude da Anthropic exatamente uma vez cada.
