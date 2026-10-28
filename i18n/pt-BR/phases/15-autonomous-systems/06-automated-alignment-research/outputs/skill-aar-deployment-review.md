---
name: aar-deployment-review
description: Pre-deployment review of an automated-alignment-research pipeline, including sandbox isolation and log integrity.
version: 1.0.0
phase: 15
lesson: 6
tags: [aar, alignment-research, sandbox, log-integrity, rsp]
---

Tendo em conta a implantação proposta de Pesquisa de Alineação Automática (modelo, caixa de areia, fila de tarefas, fórum), produzir uma revisão pré-implementação que uma equipa de segurança do laboratório de fronteira concordaria.

Produzir:

1. **Sandbox isolation.**Verifique os limites de arquivos, rede e processo para cada instância de AAR. Confirme que nenhum AAR pode ler ou modificar a caixa de areia de outro AAR. Confirme que nenhum AAR pode chegar ao endpoint de escrita do armazenamento do fórum diretamente (todas as postagens passam por um serviço separado).
2. **Forum log integrity.**O fórum deve ser apenas apêndice e evidente de adulteração. Especifique o armazenamento (por exemplo, S3 com bloqueio de objeto, livro imutável, WAL apenas apêndice). Especifique o intervalo de verificação e a resposta se a adulteração for detectada.
3. **Task allocation policy.**Estabelecer como as tarefas são atribuídas: quem as escreve, quem as aprova, se os AAR podem propor suas próprias tarefas de acompanhamento e em que condições. A descomponência livre ganha o desempenho; o fluxo de trabalho prescrito ganha a auditabilidade. Documentar explicitamente a compensação.
4. **Human review gate.**Antes de qualquer saída de AAR influenciar a direção real da pesquisa, dados de treinamento ou trabalho publicado, um revisor humano nomeado deve assinar. Especificar a lista de verificação da revisão: reproducibilidade do experimento, integridade do registro, mapeamento de reivindicações para evidências.
5. **Threshold monitoring.**Seguir sinais de que o sistema AAR se aproxima do território RSP v3.0 AI R&D-4: delta de complexidade de tarefas, reprodução autónoma de subtarefas, transferência de informações entre tarefas. Defina limites que exigem revisão elevada.

Rejeitos duros:
- Qualquer implantação de AAR sem registos de manipulação evidentes.
- Qualquer canalização em que as saídas dos AARs se alimentem diretamente de dados de formação ou de políticas de produção sem uma revisão humana designada.
- Qualquer canalização em que uma única ARA tenha credenciais suficientes para influenciar vários sistemas a jusante.

Regras de recusa:
- Se o isolamento da caixa de areia não for especificado ou se basear numa única camada (apenas Docker, sem seccomp/gVisor), rejeite e precise de defesa em profundidade.
- Se o armazenamento do registro for editável por qualquer pessoa (mesmo por operadores), recusar e exigir mídia de escrita única.
- Se o objetivo da implantação for automatizar uma parte do pipeline de capacidades  não apenas a investigação de alinhamento  recusar e escalar para revisão do RSP.

Formatos de saída:

Retorna um memorando de revisão com:
- **Pipeline summary**(um parágrafo)
- **Isolation score**(per-dimensão: fs, net, proc, peer)
- **Log integrity score**(com plano de verificação)
- **Task allocation decision**(fixado / livre / híbrido, com justificação)
- **Human review gate**(nome do revisor, lista de verificação)
- **Threshold monitors**(lista de sinais, limiares, resposta)
- **Deployment verdict**(Via / espera / não vai)
