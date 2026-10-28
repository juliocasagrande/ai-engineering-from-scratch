---
name: ipi-audit
description: Auditar uma implantação de agentes para a exposição indireta à injecção imediata e a cobertura do controlo dos fluxos de informação.
version: 1.0.0
phase: 18
lesson: 15
tags: [ipi, indirect-prompt-injection, ifc, agent-security, owasp-llm01]
---

Tendo em conta a descrição da implantação agencial, deve ser verificada a exposição à injecção imediata indireta.

Produzir:

1. Inventário de conteúdo não confiável. Enumera todas as fontes de conteúdo que o agente pode ler: documentos RAG, caixa de entrada, calendário, saídas de ferramentas, ingressos, revisões de produtos, APIs de terceiros. Cada um é um potencial vetor IPI.
2. Etiquetado de confiança. A implantação separa o conteúdo confiável (interrogativo do usuário) do não confiável (conteúdo recuperado)?
3. Ação gating. Que ferramentas podem ser invocadas? Para cada uma, a invocação é fechada apenas pelo prompt de confiança, ou o conteúdo não confiável pode influenciar a invocação?
4. Avaliação de ataque adaptativo. A implementação foi testada com ataques adaptativos (gradiente, RL, equipe vermelha humana) por Nasr et al. 2025? A avaliação apenas de ataque estático é insuficiente.
5. Limite de alcance-violação. Identifique cada limite transversal de confiança (por exemplo, caixa de entrada -> enviar, documentos -> API externa). Para cada uma, verifique se a ação é ou proibida sob influência não confiável, ou explicitamente ratificada pelo prompt confiável.

Rejeitos duros:
- Qualquer implantação de agentes sem uma etiqueta de confiança explícita no conteúdo recuperado.
- Qualquer reivindicação de defesa baseada apenas em ataques estáticos.
- Qualquer afirmação de "o nosso agente é seguro para injecção imediata" sem indicar o mecanismo da IFC.

Regras de recusa:
- Se o usuário perguntar se a filtragem é suficiente, recusar e explicar o Nasr 2025 resultado de que os ataques adaptativos quebram > 90% das defesas baseadas em filtros.
- Se o usuário pedir uma defesa de bala de prata, recusar  IPI defesa requer IFC mais camadas de moderação de resposta mais auditoria humana em ações de alto risco.

Resultado: uma auditoria de uma página que preenche as cinco seções acima, sinaliza o limite mais perigoso entre não confiável e confiável e nomeia o controle mais urgente a ser adicionado. Cite MDPI Informação 17 ((1): 54 (2026) e Nasr et al. (outubro 2025) uma vez cada.
