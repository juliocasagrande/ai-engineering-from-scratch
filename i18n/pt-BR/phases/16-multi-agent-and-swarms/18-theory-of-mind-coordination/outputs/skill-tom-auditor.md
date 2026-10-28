---
name: tom-auditor
description: Audit a multi-agent system that claims "emergent coordination." Separates real ToM-enabled coordination from prompt-dressed illusion with control conditions, statistical tests, and complementarity measurement.
version: 1.0.0
phase: 16
lesson: 18
tags: [multi-agent, theory-of-mind, coordination, evaluation, emergence]
---

Dado um sistema multi-agente que reivindica coordenação emergente, auditoria se a coordenação é real ou um artefato de engenharia rápida.

Produzir:

1. **Claim extraction.**Que comportamento de coordenação é reivindicado? (divisão do trabalho, antecipação, ações complementares, alcançamento de consenso).
2. **Prompt inspection.**O sistema de qualquer agente de instrução instrui explicitamente a coordenação, a seleção de papéis ou a conscientização da equipe?
3. **Control condition.**Uma versão do sistema com linguagem de indução de coordenação desligada. Especifique exatamente quais são as alterações no texto.
4. **Metric.**Pelo menos uma das seguintes: diferenciação ligada à identidade, complementaridade orientada para os objetivos, sinergia de ordem superior (Riedl 2025).
5. **Statistical test.**Significância da métrica no sistema versus controlo.`p < 0.05`Se ...`n < 50`Os testes, a comunicação de poder explicitamente.
6. **Model-capacity check.**Repetir a comparação num modelo base menor. O efeito persiste ou desaparece?
7. **Failure-case review.**Quando o sistema falha, como é que a declaração de ToM (se houver) parece? confusão de identidade (relação entre agente de crença quebrada) ou alucinação de conteúdo (conteúdo de crença errada)?

Rejeitos duros:

- As reivindicações de emergência sem condição de controlo.
- Reclamações que desaparecem no controlo estatístico (efeito abaixo `p < 0.05`- Não .`n >= 50`Estas são ilusões de coordenação.
- Se uma linha de base mais pequena e forte também alcançar o efeito sem a solicitação do ToM, a coordenação não é orientada pelo ToM.
- "Os nossos agentes descobriram" como explicação do mecanismo.

Regras de recusa:

- Se o sistema não tiver registros de raciocínio por agente, a auditoria não pode distinguir a coordenação real da aleatoriedade.
- Se a tarefa tiver uma coordenação óptima computação do oráculo, compare com a óptima em vez de controle.
- Se a alegação for estreita ("coordenação sobre tarefa de um ciclo"), a auditoria pode ser uma verificação mais curta: medir a complementaridade no ciclo único, sem necessidade de análise de longo horizonte.

Resultado: uma auditoria de duas páginas. Comece com um veredicto de uma frase ("A reivindicação de coordenação é rápida: a remoção da linguagem de 'trabalho juntos' reduz a métrica de 0,82 para 0,31, controle-significante."), em seguida, as sete seções acima.
