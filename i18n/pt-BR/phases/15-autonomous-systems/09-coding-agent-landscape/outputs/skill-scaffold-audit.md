---
name: coding-scaffold-audit
description: Auditar um andamio de agentes de codificação proposto (retorno, ciclo de verificação, caixa de areia, ajuste de referência) antes de o adotar para alterações no código de produção.
version: 1.0.0
phase: 15
lesson: 9
tags: [coding-agent, scaffolding, swe-bench, codeact, openhands]
---

Dado um andamio de agentes de codificação proposto (SWE-agent, OpenHands, Aider, Cline, Devin, Claude Code ou uma construção interna), pontua-o em quatro eixos e bandeira onde os números de referência exagerarão a qualidade da produção.

Produzir:

1. **Retrieval.** Descreva como o andaime seleciona quais arquivos o agente lê antes de agir. `grep` A qualidade da recuperação é o fator de confiabilidade dominante silencioso.
2. **Verifier loop.** O andaime executa testes, lê o rastro da pilha e a falha de alimentação volta para a próxima curva?
3. **Sandbox and blast radius.** Onde as ações são executadas? Sistema de arquivos local, contêiner efêmero, VM gerenciado. Para andares de estilo CodeAct, confirme que a caixa de areia está endurecida (sem saída, sem montagem de host, limite de tempo). Para andares de ferramentas de chamadas JSON, confirme que os validadores de ferramentas rejeitam todos os efeitos colaterais não intencionais.
4. **Benchmark fit.** Qual a distribuição que o número relatado cobre (por exemplo, "80,9% no banco SWE-Verified")? Conta a fração do índice de referência composto por 12 tarefas de linha; compare a pontuação relatada com o banco SWE-Pro (10+ tarefas de linha) para o mesmo modelo. Um andaime cujo número de cabeçalho é impulsionado pela cauda fácil não é um sinal de produção.

Rejeitos duros:
- Qualquer andaime sem um ciclo de verificação utilizado para tarefas acima de complexidade trivial.
- Echafões CodeAct sem isolamento de caixa de areia (sem Docker, sem recipiente sem raiz, sem VM) apontando para repositórios reais.
- As alegações de referência que não divulgam a distribuição (fração de cauda fácil, pontuação pro-equivalente).
- Ecafadores de chamada de ferramentas onde uma única ferramenta pode tocar caminhos arbitrários sem validador (por exemplo, um cru `shell_exec` ferramenta exposta ao modelo).

Regras de recusa:
- Se o utilizador não puder produzir a taxa de aprovação do banco de testes num sistema interno representativo, recuse-se e exige primeiro uma medição de pequena amostra.
- Se o andaime proposto correr contra um repositório de produção sem um sequestro de fase, recusar e exigir a faseção primeiro. Agentes de codificação reescrevem arquivos; agentes de codificação com má recuperação reescrevem os arquivos errados.
- Se o utilizador pretende utilizar apenas as pontuações de referência (sem as suas próprias avaliações) para tomar uma decisão de não-venda, recusar e exigir dados de avaliação interna.

Formatos de saída:

Retorna um memorando com:
- **Retrieval score** (05 com mecanismo descrito)
- **Verifier loop score** (05 com formato de feedback)
- **Sandbox score** (05 com mecanismo de isolamento)
- **Benchmark fit score** (05 com delta de distribuição interna)
- **Deployment recommendation** (só produção / colocação em cena / investigação)
- **One-line risk summary** (a primeira falha de produção mais provável)
