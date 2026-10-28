---
name: compliance-gap
description: Avalia se um relatório de segurança pode detectar a falsificação do alinhamento, através da lacuna de conformidade monitorada/sem monitoramento.
version: 1.0.0
phase: 18
lesson: 9
tags: [alignment-faking, compliance-gap, anthropic, safety-evaluation]
---

Tendo em conta um relatório de avaliação da segurança, avaliar se pode distinguir a falsificação de alinhamento da conformidade real utilizando o quadro de lacunas de conformidade de Greenblatt et al. 2024.

Produzir:

1. A avaliação é realizada tanto em condições monitoradas (relevantes ao treinamento) quanto em condições não monitoradas (não treinadas)?
2. Medida da diferença de conformidade. Relatar a diferença como taxa de conformidade (monitorada - não monitoreada). Interpretar sinal e magnitude: diferença positiva = comportamento em forma de falsificação; diferença negativa = recusa excessiva quando observada.
3. Verificação de rastreamento verbal vs comportamento. A avaliação depende do raciocínio do scratchpad do modelo, ou da ação em si?
4. Auditoria de operacionalização. A condição de monitoramento é criada através do sistema de ponta, sintética de ajuste fino ou contexto de implantação natural?
5. Verificação de incentivos residuais: Após qualquer mitigação aplicada, a estrutura de incentivo ainda está presente (o modelo ainda se beneficiaria da falsificação se assim o quisesse)?

Rejeitos duros:
- Qualquer alegação de "falsação de não alinhamento" baseada apenas em avaliação não controlada.
- Qualquer alegação de que "o raciocínio de scratchpad não mais verbalisa a falsificação" implica que o comportamento cesse.
- Qualquer alegação de que os modelos treinados com HHH não falsificam o alinhamento  Greenblatt et al. 2024 estabelece que o treinamento com HHH é a condição necessária, não uma defesa suficiente.

Regras de recusa:
- Se o usuário perguntar "faz o meu modelo alinhamento falso", recusar a resposta binária sem os dados de conformidade-gapas.
- Se o utilizador solicitar uma remediação que exerça apenas contra um rastro visível (respostas de perguntas, raciocínio com scratchpad sinalizado), explique o aviso do seguimento de 2025 de que tal treinamento pode ensinar o modelo a esconder o rastro.

Output: uma avaliação de uma página que relata a conformidade em ambas as condições, a lacuna, a separação verbal-trace-vs-behavior e a força de operacionalização.
