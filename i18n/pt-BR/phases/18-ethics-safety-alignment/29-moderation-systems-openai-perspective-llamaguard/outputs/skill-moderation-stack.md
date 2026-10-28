---
name: moderation-stack
description: Recomendar uma configuração de pilha de moderação para uma implantação de produção.
version: 1.0.0
phase: 18
lesson: 29
tags: [openai-moderation, perspective, llama-guard, layered-moderation, azure-content-safety]
---

Considerando a implantação de produção, recomendamos uma configuração de pilha de moderação nas três camadas.

Produzir:

1. Classificador de entrada. Escolha OpenAI Moderation, Llama Guard 3/4, ou Perspective API. Correspondem à taxonomia de política. Para implantações multimodal, Llama Guard 4 ou OpenAI omni-moderation.
2. Classificador de saída. O mesmo ou diferente do classificador de entrada.
3. Regras de domínio personalizadas: enumere as regras específicas de domínio que os classificadores gerais não captarão: isenções de aconselhamento financeiro, recusa de aconselhamento médico, padrões de isenção legal.
4. Juzgar casos de extremo. Especificar o caminho de escalada humana. Rejeitamentos duros são finais; casos ambíguos vão para revisão humana dentro do SLA.
5. Se o Moderador de Conteúdo do Azure estiver na pilha, planeje a migração para a Segurança de Conteúdo do Azure AI antes da aposentadoria em fevereiro de 2027.

Rejeitos duros:
- Qualquer implantação sem moderação de saída (a entrada sozinha não é suficiente).
- Qualquer implantação sem regras de domínio personalizadas em superfícies regulamentadas (financeiras, saúde, legais).
- Qualquer implantação baseada exclusivamente em classificadores da era pré-LLM (Perspective) para aplicações de chat modernas.

Regras de recusa:
- Se o utilizador solicitar o melhor classificador único, recusar a escolha do classificador  é específica da política.
- Se o utilizador solicitar prazos, recusar números únicos  Os prazos dependem da tolerância ao risco e do efeito descendente.

Resultado: uma recomendação de uma página preenchendo as cinco seções, nomeando o classificador em cada camada e sinalizando as obrigações de migração. Cite os documentos de Moderação OpenAI e as referências Llama Guard 3/4 uma vez cada.
