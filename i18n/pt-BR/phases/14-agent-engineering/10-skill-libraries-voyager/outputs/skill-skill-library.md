---
name: skill-library
description: Gerencie uma biblioteca de habilidades em forma de Voyager com registro, recuperação por semelhança, execução de composição e refinamento de falha.
version: 1.0.0
phase: 14
lesson: 10
tags: [voyager, skills, library, composition, refinement]
---

Dado um tempo de execução alvo e um domínio, produzir uma biblioteca de habilidades que suporta os três componentes da Voyager: gancho de currículo, armazenamento de habilidades recuperáveis, refinamento iterativo.

Produzir:

1. `Skill` Tipo com `name`- Não . `description`- Não . `code`- Não . `version`- Não . `tags`- Não . `depends_on`- Não . `history`Cada escrita registra o código anterior.
2. `SkillLibrary` com `register(skill, dedup=True)` (nova ou versão de embotamento), `search(query, top_k, tag_filter)`- Não . `get(name)`- Não . `topo_order(name)` (Resolução de profundidade), `execute(name, context)` (Rota topológica).
3. A recuperação deve usar a semelhança de incorporação ou BM25, não a pontuação de LLM sobre a biblioteca completa.
4. A execução DEVE capturar exceções por habilidade e superficá-las no rastro como feedback que o ciclo de refinamento pode consumir.
5. Um gancho de refinamento: após um falho `execute`, o runtime coleta (tarefa, skill_name, erro, env_state), passa-o para o modelo, e liga `register` A versão falha, a história conserva o código antigo.

Rejeitos duros:

- Uma biblioteca onde as habilidades são cordas de prosa, não código. `description`- Não .
- Composta sem classificação topológica, profundidade em primeiro lugar sem interrupções de detecção de ciclo em DAG de habilidade.
- A versão silenciosa se sobreescreve. `version` e empurrar o código antigo para `history` para auditoria.

Regras de recusa:

- Se o tempo de execução do objetivo não tiver caixa de areia para execução de habilidades, rejeite para domínios onde as habilidades tocam os sistemas de produção.
- Se o usuário pedir "retestar automaticamente em cada falha sem refinamento", recusar.
- Se a biblioteca exceder ~ 200 habilidades com recuperação plana, recuse-se a chamá-la de "pronta para produção". Adicione filtros de tags e espaços de nomes hierárquicos primeiro.

Output: `skill.py`- Não . `library.py`- Não . `execute.py`- Não . `refine.py`, e um `README.md` Explicando a regra de dedup, retorno de backend, requisito de refinamento e política de versão. Conclui com "o que ler a seguir" apontando para a lição 17 para a integração do Claude Agent SDK, lição 16 para a tradução de ferramentas do OpenAI Agents SDK ou lição 30 para avaliar a qualidade da biblioteca de habilidades.
