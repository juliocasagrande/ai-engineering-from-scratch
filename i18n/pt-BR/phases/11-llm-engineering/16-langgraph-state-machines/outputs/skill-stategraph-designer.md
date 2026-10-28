---
name: stategraph-designer
description: Transforme uma tarefa de agente em um StateGraph LangGraph com nós nomeados, estado digitado, redutores, checkpointer e interrupções humanas.
version: 1.0.0
phase: 11
lesson: 16
tags: [langgraph, stategraph, checkpointer, interrupt, time-travel, react-agent, human-in-the-loop]
---

Dado o trabalho do agente (objetivo para o utilizador, ferramentas disponíveis, contagem de voltas esperada, efeitos colaterais com raio de explosão de segurança, requisitos de durabilidade, orçamento de latência-alvo), saída:

1. Lista de nós. Nomear cada passo discreto: o pensador LLM, cada executor de ferramentas, cada passo de revisão humana, qualquer resumidor ou crítico, qualquer retriever. Rejeitar o projeto se qualquer nodo toca mais de uma preocupação; dividir.
2. Esquema de estado. TipedDict (ou Pydantic) campos com um redutor para cada lista. Sempre Anotado [lista, add_messages] no registro de mensagens. Levante qualquer lista específica de tarefa de mensagens (um plano, um contador de orçamento, uma lista de documentos recuperados) para que os redutores permaneçam corretos sob atualizações paralelas.
3. Mapa de bordas. bordas estáticas onde o próximo passo é determinista. bordas condicionais com uma função de roteador nomeado apenas onde o modelo escolhe o próximo passo. Rejeitar qualquer gráfico cuja função do roteador depende de uma chamada LLM recente que você não já fez em um nó anterior.
4. Interrupt_before em cada nó com um efeito colateral irreversível (escritos, apagamentos, pagamentos, chamadas externas de API com custo). interrupt_after no nó modelo quando a validação de saída é executada em um processo separado. Rejeitar interrupt_after em qualquer nó que efeta lateral; até então o efeito colateral já aconteceu.
5. Checkpointer. MemorySaver apenas para testes. Escolha entre PostgresSaver, SQLiteSaver, RedisSaver para qualquer ambiente que deva sobreviver a uma reinicialização. Confirme a estratégia thread_id (por usuário, por sessão, por conversa) e o ponto de verificação TTL.

Recusa-se a enviar um LangGraph sem um ponto de controlo. Sem ponto de controlo significa sem currículo, sem viagens no tempo, sem repetição humana no circuito. Recusar-se a enviar um campo de mensagens sem add_messages; a segunda escrita sobrepõe a primeira silenciosamente e metade da conversa desaparece. Rejeitar um gráfico cuja cada transição é uma borda condicional encaminhada por um planejador LLM; isto é, AutoGen com passos extras e queima tokens por turno.

Exemplo de entrada: "Agente de tratamento de reembolsos sobre o Anthropic Claude com três ferramentas (lookup_order, issue_refund, send_email), deve pausar para um ser humano antes de qualquer reembolso acima de 100 dólares, deve retomar após a reinicialização do servidor, p95 orçamento de latência 8 segundos".

Exemplo de saída:
- Nodos: agente (chamada de LLM), search_tool, refund_tool, email_tool, human_review.
- Estado: mensagens com add_messages, order_context (overwrite), refund_amount (overwrite), reviewer_decision (overwrite).
- Arredores: agente para deve_continue roteador com ramos lookup_tool, refund_tool, email_tool, human_review, END. Os nós da ferramenta voltam para agente.
- Interrupts: interrupt_before na ferramenta de reembolso quando o montante de reembolso > 100.
- Checkpointer: PostgresSaver com thread_id "user:{user_id}:case:{case_id}" e TTL de 30 dias.
