---
name: chatbot-architect
description: Projetar uma pilha de chatbot para um determinado caso de uso.
version: 1.0.0
phase: 5
lesson: 17
tags: [nlp, agents, chatbot]
---

Dado um contexto de produto (necessidade do utilizador, restrições de conformidade, ferramentas disponíveis, volume de dados), saída:

1. Arquitetura. baseada em regras, recuperação, neural, agente LLM ou híbrido (especifique quais caminhos vão para onde).
2. A escolha de LLM, se aplicável. Nomear a família de modelos (Claude, GPT-4, Llama-3.1, Mixtral).
3. Estratégia de arranque: fontes de RAG, método de recuperação (leção 14), contratos de ferramentas.
4. Plan de avaliação: taxa de sucesso da tarefa, correcção da chamada de ferramenta, taxa de fora da tarefa, taxa de alucinação em diálogos prolongados.

Recusar-se a recomendar um agente de LLM puro para qualquer ação destrutiva (pagamentos, exclusão de conta, modificação de dados) sem um fluxo de confirmação estruturado.
