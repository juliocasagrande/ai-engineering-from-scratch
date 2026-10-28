---
name: scaling-policy-review
description: Review a frontier-lab scaling policy (Anthropic RSP, OpenAI Preparedness, DeepMind FSF, internal) against the RSP v3.0 reference shape.
version: 1.0.0
phase: 15
lesson: 19
tags: [rsp, scaling-policy, ai-rd-4, pause-commitment, saferai, governance]
---

Tendo em conta uma política de escalada publicada ou proposta, produzir uma revisão estruturada comparando-a com a forma de referência RSP v3.0 (AI R&D-4, caso afirmativo, mitigação de dois níveis, Roteiro de segurança de fronteiras, Relatório de riscos, revisão independente).

Produzir:

1. **Two-tier inventory.**Os compromissos no nível de recomendação são de defesa, não promessas.
2. **Thresholds.**Nomear todos os limites de capacidade e a mitigação que desencadeia. Os limites de qualidade onde v2 tinha quantitativo. Os limites de capacidade faltantes para as capacidades que a política afirma cobrir.
3. **Pause commitment.**Confirme que as políticas nomeiam uma cláusula de pausa (pausas de treinamento, pausas de implantação ou similares) em limiares específicos. V3.0 removido isso; políticas que seguem o exemplo herdar a regressão.
4. **Standing artifacts.**Confirmar os mandatos de política que constam dos documentos do Mapa de Rodas de Segurança Fronteira e do Relatório de Riscos com cadência declarada.
5. **Independent review.**A revisão interna (um "Grupo Consultivo de Segurança" composto por funcionários do laboratório) não é considerada supervisão independente.

Rejeitos duros:
- Políticas sem limite de capacidade designado.
- Políticas cujas medidas de mitigação estão todas no nível de recomendação da indústria.
- Políticas sem roteiro permanente / relatórios de risco.
- Políticas sem mecanismo de revisão independente.
- Políticas que afirmam "aprender da experiência do mundo real" sem indicar como o texto da política é atualizado e em que cadência.

Regras de recusa:
- Se o documento de política é de comercialização em vez de governança (sem compromissos específicos, sem limiares, sem cadência), recusa-se a classificá-lo como uma política de escala.
- Se o utilizador tratar a existência de uma política como equivalente ao cumprimento, recusar.
- Se o usuário citar uma versão anterior da política (por exemplo, 2023 Anthropic RSP) como atual, recusar e exigir a versão atual.

Formatos de saída:

Retorno de uma revisão da política com:
- **Two-tier ratio**(unilateral / recomendação / contagem total)
- **Threshold table**(nome, tipo: quantitativo / qualitativo, desencadeador, mitigação)
- **Pause commitment**(presente y/n, cláusula específica)
- **Standing artifacts**(Cadência do mapa de estrada, cadência do relatório de risco)
- **Independent review**(mecanismo, identidade do revisor, frequência)
- **Summary rating**(forte / moderada / fraca, justificada)
