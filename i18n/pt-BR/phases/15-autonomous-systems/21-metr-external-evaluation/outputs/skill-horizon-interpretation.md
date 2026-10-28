---
name: horizon-interpretation
description: Review a vendor's time-horizon claim and produce a gap analysis between benchmark claim and deployment reality.
version: 1.0.0
phase: 15
lesson: 21
tags: [metr, time-horizon, hcast, re-bench, eval-vs-deploy, external-evaluation]
---

Dado o pedido de um fornecedor publicado sobre o horizonte temporal (por exemplo, "o nosso modelo completa tarefas de 14 horas com uma confiabilidade de 50%"), produz uma análise de lacunas que quantifica o delta de implementação-realidade e sinaliza quaisquer fraquezas metodológicas.

Produzir:

1. **Methodology audit.**Identificar o conjunto de tarefas (HCAST, RE-Bench, SWAA ou proprietário). Confirmar que a adequação logística é divulgada (inclinação, tamanho da amostra, intervalo de confiança). Um horizonte sem divulgação de metodologia é uma alegação de marketing.
2. **Task distribution fit.**Mapa da distribuição de tarefas de referência do fornecedor para a distribuição de tarefas de produção do usuário. Se elas divergem materialmente (o fornecedor mede tarefas SWE, a produção é fluxos de suporte ao cliente), o número não se transfere.
3. **Eval-context gap.**Aplicar uma lacuna de 1040% entre o horizonte de referência e a realidade da implantação. Cite o estudo de alinhamento de 2024 da Anthropic e o Relatório Internacional de Segurança de IA de 2026 sobre jogos de conteúdo de avaliação. A lacuna real depende do protocolo de avaliação; os jogos são maiores em tarefas não estruturadas.
4. **Tooling gap.**As ferramentas de referência são limpas e bem equipadas. As ferramentas de produção são mais complexas. Estima-se um desconto adicional de fiabilidade de 530%.
5. **Human-in-the-loop assumption.**Os indicadores de referência não assumem HITL. Agentes de produção com HITL executam com maior confiabilidade mas menor autonomia. Ajuste a interpretação do horizonte em conformidade.

Rejeitos duros:
- As alegações do Horizon sem metodologia de origem ou tamanho da amostra.
- A Comissão considera que o mercado de trabalho é um mercado de trabalho.
- Os fornecedores citando um número de horizonte de 2025 ou anterior como atual (o tempo de duplicação é de ~ 7 meses; os números de 2025 são obsoletos dentro de um ano).
- Tratar um horizonte de 50% como "funcionará na maior parte do tempo"  50% de confiabilidade é um desvio de moeda.

Regras de recusa:
- Se o fornecedor não divulgar a metodologia, recusar e exigir o documento de origem ou a publicação no blog.
- Se a distribuição de referência não se sobrepõer à distribuição da produção, é recusada e requer uma avaliação interna.
- Se o fornecedor citar horizontes sem uma auditoria de jogos em seu pipeline de avaliação específico, recusar citar o número como uma previsão de confiabilidade.

Formatos de saída:

Retorna um memorando de interpretação do horizonte com:
- **Source methodology**(companhia, método de adaptação, tamanho da amostra, CI)
- **Distribution overlap**(marca de referência vs produção; mapeamento em %)
- **Eval-context gap estimate**(baixo / médio / alto com raciocínio)
- **Tooling gap estimate**(baixo / médio / alto)
- **HITL assumption**(autônomo de modelo de referência versus HITL de produção)
- **Deploy-adjusted horizon**(horizão após validade e descontos em ferramentas)
- **Readiness verdict**(produzir / montar / apenas para investigação)
