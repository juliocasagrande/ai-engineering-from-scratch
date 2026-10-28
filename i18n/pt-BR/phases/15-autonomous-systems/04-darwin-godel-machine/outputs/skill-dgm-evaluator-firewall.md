---
name: dgm-evaluator-firewall
description: Especifique a separação do avaliador que um agente auto-modificador de ciclo de estilo Darwin-Godel-Machine precisa para evitar o hacking de recompensas documentado.
version: 1.0.0
phase: 15
lesson: 4
tags: [dgm, self-modification, reward-hacking, evaluator, sandbox]
---

Dado um ciclo de agente auto-modificador proposto (estafalamento de agente, pipeline de avaliador, alvo de implantação), produzir uma especificação de firewall que mantenha o avaliador fora do alcance do agente.

Produzir:

1. **File-system boundary.** Lista todos os arquivos que o agente pode editar. Lista todos os arquivos que o avaliador lê. A intersecção deve ser vazia. Se não for, especifique o movimento exato necessário para torná-la vazia.
2. **Process boundary.** O avaliador deve executar um processo que o agente não controla. Especifique o recipiente ou caixa de areia.
3. **Network and secret boundary.** O agente não deve ser capaz de editar os segredos da CI que trazem entradas de avaliadores ou pontuações de postagem.
4. **Score-ingress contract.** Os resultados retornam do avaliador para o arquivo do circuito, que é o único canal, e qualquer coisa que o agente escreva que influenciar a pontuação futura rompe o contrato.
5. **Mutation review list.** Lista as classes de edições de agente que exigem revisão manual antes da aceitação: novas dependências, edições para o código de pontuação adjacente, edições para a configuração de caixa de areia, edições para registro ou monitoramento.

Rejeitos duros:
- O avaliador no mesmo repositório que a fonte do agente.
- Evaluação que funciona como uma importação Python dentro do processo do agente.
- Qualquer ajuste de pontuação que seja aplicado no lado do agente da fronteira.
- Qualquer registro que o agente possa silenciar, editando o seu próprio código.

Regras de recusa:
- Se o usuário não puder nomear todos os arquivos, o agente pode editar, recusar e exigir uma auditoria de acesso de escrita em nível de arquivo primeiro.
- Se o avaliador não tiver insumos adiantados, recusar  esta é a auditoria da lição 3, uma condição prévia.
- Se a superfície de implantação incluir mutações no próprio avaliador (mesmo indiretamente através de uma atualização de dependência proposta), recusar e exigir uma fase manual de revisão do firewall.

Formatos de saída:

Retorna uma especificação de uma página com:
- **Agent write-surface** (caminhos, globos)
- **Evaluator read-surface** (Caminhos, pontos finais)
- **Intersection** (deve ser vazio; mostre a diferença)
- **Process model** (como o avaliador é isolado)
- **Secrets inventory** (onde e como montado)
- **Review-required mutation classes** - Não .
- **Sign-off line** (que é o proprietário da invariante do firewall)
