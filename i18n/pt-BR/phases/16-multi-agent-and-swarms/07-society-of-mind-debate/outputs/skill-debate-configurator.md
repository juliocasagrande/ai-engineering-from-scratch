---
name: debate-configurator
description: Configure a multi-agent debate for a given task, estimating quality gain and token cost before running.
version: 1.0.0
phase: 16
lesson: 07
tags: [multi-agent, debate, society-of-mind, consensus]
---

Dado uma pergunta ou tarefa, produzir uma configuração de debate pronta para ser executada em qualquer framework de agentes (LangGraph, AutoGen, loop personalizado).

Produzir:

1. **Task-fit check.**O debate ajuda o raciocínio, a factualidade e a decomposição; não ajuda tarefas que já são deterministas (aritmética, compilação de código) ou puramente gerativas (escritura criativa).
2. **Agent count.**3, 4 ou 5. Default 3; 4+ apenas se não for sensível aos custos e a tarefa necessitar de visões mais diversas.
3. **Round count.**2 ou 3. padrão 3; raramente mais.
4. **Heterogeneity.**O mesmo modelo base (erros mais simples, mais baratos e mais correlacionados) ou família mista (Llama + Claude + GPT; descorrela; mais caro, precisa de uma camada de roteamento).
5. **Role assignment.**Simétrico (todos os agentes têm o mesmo papel) versus oponente (um agente instruído a discordar).
6. **Aggregation method.**Voto majoritário (respostas discretas), média ponderada (número) ou síntese de juízes LLM (aberto).
7. **Cost estimate.**N agentes × R rodadas × tokens médianos por turno. Indique a estimativa em dólares dada a fixação de preços atual do fornecedor.

Rejeitos duros:

- Qualquer config com mais de 5 agentes ou mais de 3 tiros sem justificação concreta dos custos.
- Debates apenas simétricos sobre tarefas com risco conhecido de sícofancia.
- Usando debate para tarefas que têm um verificador determinista (compilação, teste, matemática exata)  executar o verificador em vez disso.

Regras de recusa:

- Se a tarefa for uma simples pesquisa factual, recuse e recomenda um único agente com aumento de recuperação.
- Se a tarefa for generativa (escrever um poema), recusar o debate arrasta as saídas para a média.
- Se o utilizador não tiver definido um orçamento de tokens/dolar, recuse-se e peça um.

Resultado: um resumo de configuração de uma página. Comece com a verificação de ajuste de tarefa, encerra com a estimativa total de custos.
