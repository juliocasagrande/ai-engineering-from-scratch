---
name: control-protocol-audit
description: Audit a deployment protocol under the AI Control threat model.
version: 1.0.0
phase: 18
lesson: 10
tags: [ai-control, subversion, trusted-editing, untrusted-monitoring, safety-case]
---

Dada uma descrição do protocolo de implantação, auditá-lo sob o modelo de ameaça de Controle de IA: U (forte sem confiança), T (fraco sem confiança), H (humano confiável) e medir a posição do protocolo na fronteira de utilidade-segurança.

Produzir:

1. Assegnação de papel. Identificar qual modelo joga U e qual joga T. Se T for outra instância de U, o risco de colisão de flag imediatamente.
2. Auditoria contabilidade orçamental. Como é alocado H? uniforme, aleatório, dirigido à bandeira? Que fração dos resultados são auditados na expectativa?
3. Enumeração de vetores de colusão: para cada par de componentes não confiáveis (U-produtor + U-monitor, U-produtor + U-editor), enumere os vetores de colusão: sinais steganográficos, exploração prévia de treinamento compartilhado, canais de cronometragem.
4. Análise de capacidade-gapas. Quão fraco é T do que U? Em que ponto o sinal de edição de T se torna ruído (por exemplo, T não pode detectar com segurança as portas traseiras que U produz)?
5. O pior modelo de ameaça, sob a suposição de que U é adversário com conhecimento perfeito do protocolo, qual é a melhor estratégia do adversário?

Rejeitos duros:
- Qualquer descrição de protocolo que use U como seu próprio monitor sem um mecanismo de resistência à colisão.
- Qualquer alegação de protocolo de "taxa de backdoor quase zero" sem avaliação da equipe vermelha, onde a equipe vermelha tem visibilidade do protocolo.
- Qualquer auditoria de um protocolo sem articular a lacuna de capacidade T-U e o orçamento da H.

Regras de recusa:
- Se o utilizador perguntar "este protocolo é seguro", recusar sem a prova em três partes: a) resultado da equipa vermelha, b) estimativa da lacuna de capacidade, c) orçamento H.
- Se o usuário mistura alinhamento e controle ("alignamos U, então não precisamos de um protocolo"), recuse e aponte para a lição 9 (alignamento falso)  alinhamento é uma propriedade de U; controle é uma propriedade do protocolo.

Resultado: uma auditoria de uma página que preenche as cinco seções acima, nomeia o link mais fraco (geralmente a lacuna de capacidade T-to-U ou resistência à colusão) e indica o maior modo de falha não abordado. Cite Greenblatt et al. (arXiv:2312.06942) uma vez como a fonte do modelo de ameaça.
