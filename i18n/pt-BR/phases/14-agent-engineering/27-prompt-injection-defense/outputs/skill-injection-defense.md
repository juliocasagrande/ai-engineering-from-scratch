---
name: injection-defense
description: Construir uma camada PVE (Prompt-Validator-Executor) com conteúdo etiquetado de origem, digitalização de marcador de injeção e navegação de lista de autorização para qualquer tempo de execução do agente.
version: 1.0.0
phase: 14
lesson: 27
tags: [security, prompt-injection, pve, greshake, source-tag]
---

Dado um agente com acesso e recuperação de ferramentas, produzir uma camada de defesa por injecção.

Produzir:

1. Tag de fonte em cada pedaço de conteúdo: `user_message`- Não . `tool_output`- Não . `retrieved_web`- Não . `retrieved_memory`- Não . `retrieved_file`Propagar tags através do histórico da mensagem.
2. `Validator.assess(tool_call, contents)`  recusa chamadas de ferramentas com args em forma de injecção ou conteúdo recuperado; permitido apenas quando as etiquetas de origem correspondem ao nível de confiança declarado.
3. Lista de permisos / lista de bloqueio para navegação: URLs, domínios, caminhos de arquivos que o agente pode tocar.
4. Proteção de memória-escritura: rejeita escreve que parecem directivas.
5. Disciplina de captura de conteúdo (Lessão 23): armazenar conteúdo recuperado externamente; os espaços contêm IDs de referência, não prosa.
6. Suíte de teste: as cinco classes de exploração Greshake como casos de equipe vermelha.

Rejeitos duros:

- Superfície de uso de ferramentas sem etiquetas de origem. Não pode distinguir níveis de permissão sem proveniência.
- Validador que é executado apenas na saída final. Validação tardia é irrelevante  o modelo já atuou.
- "Confie em mim, o sistema de urgência trata disso". A higiene de urgência do sistema não é um controle.

Regras de recusa:

- Se o agente tiver alguma capacidade de recuperação sem etiquetagem de fonte, recuse-se a enviar.
- Se as ferramentas sensíveis (enviar mensagem, executar shell, escrever arquivo em /) não tiverem confirmação humana no loop, recusar.
- Se as memórias não estiverem guardadas, recuse-se.

Output: `validator.py`- Não . `source_tag.py`- Não . `allowlist.py`- Não . `memory_guard.py`- Não . `red_team.py`- Não . `README.md` A conclusão é "o que ler a seguir" apontando para a lição 21 (segurança do uso do computador) e a lição 23 (contenido de captura através OTel).
