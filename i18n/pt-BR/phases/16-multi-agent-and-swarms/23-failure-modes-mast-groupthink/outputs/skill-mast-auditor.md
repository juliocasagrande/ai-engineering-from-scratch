---
name: mast-auditor
description: Run a MAST-style failure-mode audit on a multi-agent system. Categorize execution-trace failures into Specification / Coordination / Verification and the Groupthink families; rank mitigations by expected failure reduction.
version: 1.0.0
phase: 16
lesson: 23
tags: [multi-agent, failure-modes, MAST, groupthink, circuit-breaker, audit]
---

Dado um sistema multi-agente e traços de execução de amostras, executar uma auditoria de modo falha.

Produzir:

1. **Sample construction.**Pelo menos 200 traços da produção, amostragem uniformemente em todos os tipos de tarefas e janelas de tempo.
2. **Classification pass.**Para cada traço, marca`success | failure`Para falhas, atribuir uma categoria MAST (espec / coord / verifique) e, se for caso disso, uma ou mais etiquetas da família Groupthink (monocultura / conformidade / tom / motivo misto / cascata).
3. **Distribution table.**Contas e porcentagens por categoria MAST e tag Groupthink. Comparar com a distribuição de referência de Cemri 2025 (41.77 / 36.94 / 21.30).
4. **Top failure patterns.**Identificar os 3 padrões específicos mais frequentes (por exemplo, "dois agentes revisam ambos").
5. **Mitigation ranking.**Para cada padrão superior, propor uma mitigação da biblioteca padrão: contratos de papel explícitos, estado compartilhado de versões, verificador independente, interruptor de circuito, trio de detecção-diagnóstico-validação (STRATUS).
6. **Risk of silent failures.**Quantas falhas produzem resultados plausíveis mas errados versus erros altos?
7. **Slow-failure proxies.**Recomenda-se 2-3 métricas ao vivo que surgirão antes que se torne um erro alto: taxa de acordo, taxa de retestamento, distribuição de comprimento de saída, distância de edição entre agentes.

Rejeitos duros:

- Auditoria sem amostra aleatória ou estratificada.
- Recomendações de mitigação sem uma medição de linha de base. "Adicionar um verificador" não significa nada, a menos que se conheça a taxa de falha atual.
- Ignorar os incidentes MAST-ignósitos. Se um rastro não se encaixa numa categoria, a taxonomia é incompleta; propor uma extensão em vez de forçar uma categoria.
- A reivindicação de uma auditoria trimestral é suficiente sem o controlo operacional de falhas lentas.

Regras de recusa:

- Se os dados não tiverem atribuição por agente (quem escreveu o que, quem leu o que), a auditoria não pode distinguir as falhas de coordenação dos conflitos de funções.
- Se o sistema tiver menos de 50 traços de falhas no total, a amostra é pequena demais para produzir estimativas de distribuição.
- Se os vestígios contêm PII, mascarar antes da análise.

Resultado: um relatório de três páginas. Comece com um resumo de uma frase ("41% falhas de especificação, 12% de coordenação, 39% de falhas de verificação, 8% desconhecidas; padrão superior é conflito de revisores duplos; mitigação de ROI mais alta é contratos de papel explícito. "), em seguida, as sete seções acima. Conclui com uma lista de ações prioritárias: três mitigações com custo de implementação estimado e redução esperada da taxa de falha.
