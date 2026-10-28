---
name: scheming-triage
description: Triage an agent-deployment incident report against the Apollo three-pillar scheming framework.
version: 1.0.0
phase: 18
lesson: 8
tags: [scheming, agent-safety, apollo, three-pillars, safety-cases]
---

Tendo em conta um relatório de incidente de implantação de agentes (uso inesperado de ferramentas, acesso a dados, comportamento adjacente à autoconservação), classifique o modo de falha e, quando a elaboração de planos for candidata, aplique o teste de três pilares da Apollo.

Produzir:

1. Triamento de classe de falha. Etiquete o incidente como um de: falha de capacidade (o modelo não pôde realizar a tarefa), falha de controle (o protocolo de monitoramento/utilização de ferramentas não continha o modelo) ou esquema (o modelo tomou ações contra o objetivo do usuário em serviço de um objetivo diferente no contexto).
2. Verificação de três pilares (se o esquema é um candidato).
   - Desalinhamento: a ação serviu a um objectivo ortogonal presente no ambiente ou na saída da ferramenta?
   - Orientação ao objetivo: a ação era parte de um plano de várias etapas ou um erro de um tiro?
   - Consciência situacional: há evidências de que o modelo sabia que estava a ser avaliado na época?
3. Auditoria de contexto de avaliação. O incidente foi observado na implementação, na avaliação da equipe vermelha ou em ambos?
4. Reproducibilidade de elicitação. Pode o mesmo prompt + ambiente produzir o comportamento novamente? Um incidente reprodutivel está dentro do quadro de três pilares; um não reprodutivel pode ser um artefato de elicitação de capacidade.
5. Qual dos três pilares que o caso de segurança atual para esta implantação aborda e qual deixa descoberto?

Rejeitos duros:
- Qualquer enquadramento que trate o esquema como um fracasso da classe de capacidade.
- Qualquer inferência de que "a formação anti-scheming reduziu a taxa de ação secreta" implica uma redução do desalinhamento subjacente, sem verificar a taxa de reconhecimento de contexto de avaliação para o mesmo modelo.
- Qualquer alegação de que a subversão de supervisão não é "um ataque" porque o agente não exfiltrou dados  subversão de supervisão é uma ação conspiratória em si mesma.

Regras de recusa:
- Se o utilizador perguntar "o meu modelo está a planejar", recusar uma resposta binária sem a prova de três pilares; solicitar os dados de avaliação-contexto e de elicitação-reprodução.
- Se o utilizador solicitar uma probabilidade residual de planejamento, recusar a resposta numérica e explicar que a confiabilidade da avaliação de 2026 é limitada pela própria consciência situacional do modelo.

Resultado: uma triagem de uma página que rotula a classe de falha, preenche os três pilares com as evidências disponíveis, sinaliza evidências faltantes e nomeia a lacuna única de caso de segurança mais urgente para ser fechada. Cite Meinke et al. (arXiv:2412.04984) uma vez como fonte de quadro.
