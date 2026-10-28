---
name: cross-policy-diff
description: Produce a cross-policy comparison for a specific capability using the OpenAI Preparedness Framework v2, Anthropic RSP v3.0, and DeepMind FSF v3 as reference.
version: 1.0.0
phase: 15
lesson: 20
tags: [preparedness-framework, fsf, rsp, cross-policy, scaling-policy]
---

Dado um potencial de fronteira específico (por exemplo, "autonomia de longo alcance", "replicação e adaptação autónoma", "automação de I&D"), produz uma diferença entre as políticas que mostra como cada um dos três quadros classifica a capacidade e quais são as atenuações desencadeadas.

Produzir:

1. **OpenAI PF v2 classification.**Se rastreado, nomear os gatilhos do Relatório de Capacidades + Garantias. Se pesquisa, note que a linguagem de política é "potencial" mitigação.
2. **Anthropic RSP v3.0 classification.**Qual limiar (ASL-3, AI R&D-4, proibição codificada em código rígido)? Qual mitigação (caso afirmativo, segurança + implantação)?
3. **DeepMind FSF v3 classification.**Qual domínio (CBRN, Cyber, Manipulação Harmosa, ML R&D)? Qual CCL ou Nível de Capacidade de rastreamento?
4. **Convergence summary.**As três políticas concordam sobre a gravidade da capacidade, ou há discordância significativa? Qual é a classificação mais rigorosa e qual a menos?
5. **Measurement dependency.**Cada classificação depende da medição de capacidade. Nomear como a capacidade é medida e qual fornecedor de avaliação (METR, Apollo, interno, terceiro) possui essa medição.

Rejeitos duros:
- As reivindicações de alinhamento entre as políticas baseadas na semelhança entre a linguagem de anúncio e a documentação, sem provas de nível de documento.
- Qualquer classificação que não possa indicar uma cláusula específica no documento-fonte.
- Tratar a "Categoria de Pesquisa" (OpenAI) como equivalente à "Categoria de rastreamento"  tem consequências operacionais diferentes.

Regras de recusa:
- Se o utilizador não puder produzir as passagens do documento fonte para cada classificação, recusar e exigir citações primeiro.
- Se o utilizador tratar a existência de políticas como evidência de mitigação em prática, recusar e exigir provas das disparas específicas de mitigação.
- Se a capacidade for "coberta" por um quadro, mas a palavra não apareça no documento, recusar e exigir uma referência à cláusula concreta.

Formatos de saída:

Retorna um documento de diferença com:
- **Capability definition**(uma frase)
- **OpenAI PF v2 row**(classificação, desencadeamento, cláusula de origem)
- **Anthropic RSP v3.0 row**(classificação, desencadeamento, unilateral-versus-recomendação)
- **DeepMind FSF v3 row**(domínio, CCL / TCL, envolvimento de alinhamento enganoso)
- **Convergence summary**(acordos + discordância significativa)
- **Measurement ownership**(provedor de avaliação, cadência de avaliação)
- **Reader recommendation**(mais rigoroso, menos rigoroso, justificado)
