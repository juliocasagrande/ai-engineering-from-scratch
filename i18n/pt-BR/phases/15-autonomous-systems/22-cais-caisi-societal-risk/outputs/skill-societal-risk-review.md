---
name: societal-risk-review
description: Revisar uma implementação para a postura de risco em escala social, utilizando o quadro de quatro riscos do CAIS e o contexto regulamentar do CAISI/SB-53.
version: 1.0.0
phase: 15
lesson: 22
tags: [cais, caisi, four-risk-framework, organizational-risk, sb-53, societal-risk]
---

Dado uma implantação de IA proposta ou operacional, produzir uma revisão de risco em escala social que marque a implantação contra o quadro de quatro riscos do CAIS, inventarize sub-leveres de risco organizacional e nomeie a superfície regulatória.

Produzir:

1. **Four-risk tagging.** Para cada uma das quatro categorias (uso malicioso, corridas de IA, riscos organizacionais, IA desonestas), indique se a implantação a toca e como. Uma implantação pode tocar em várias categorias; "não se aplica" deve ser justificada em uma frase.
2. **Organizational-risk inventory.** A pontuação da implantação é feita em relação aos quatro sub-levers: cultura da segurança, rigor de auditoria, defesas de várias camadas, segurança da informação.
3. **Regulatory surface.** Nomear os quadros regulamentares aplicáveis: Lei da UE sobre IA (se na UE ou servindo os utilizadores da UE), SB-53 da Califórnia (se assinado e aplicável), acordos voluntários CAISI (se o laboratório assinou um).
4. **External-evaluation posture.** Nomear as avaliações externas que a implantação ou o modelo base tiver submetido (METR, CAISI, Apollo, Gray Swan, etc.).
5. **Structural-force exposure.** Estimar a quantidade de pressão competitiva que a organização está sob e como isso opera contra as alavancas de risco organizacional.

Rejeitos duros:
- Desdobramentos que afectam categorias de capacidade nociva sem uma camada de proibição de código rígido (Lessão 17).
- Deploições em condições de concorrência sem auditoria independente.
- As instalações autónomas de longo prazo sem avaliação de capacidade externa.
- Desplojamento da UE sem o artigo 14.o da HITL (Lessão 15).
- Envio de californianos sem processo de relatar incidentes se o SB-53 for assinado.

Regras de recusa:
- Se o utilizador não puder nomear o avaliador externo para o modelo base, recusar e exigir a identificação primeiro.
- Se o usuário tratar "temos uma política de escalagem" como conformidade com a regulamentação de risco de catástrofe, recusar e exigir mapeamento de superfície regulatório específico.
- Se o utilizador propõe a implantação sob pressão de corrida sem auditoria, recusar e nomear a constatação do CAIS sobre o risco organizacional.

Formatos de saída:

Retorno de uma revisão dos riscos sociais com:
- **Four-risk row table** (categoria, afetada, natureza)
- **Organizational-risk scorecard** (cultura de segurança / auditoria / defesas / infosec)
- **Regulatory surface** (quadros aplicáveis com status de conformidade)
- **External-evaluation posture** (avaliação, alcance, cadência)
- **Structural-force exposure** (baixo / médio / alto com justificação)
- **Deployment readiness** (produzir / montar / apenas para investigação)
