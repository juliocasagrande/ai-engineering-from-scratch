# Fase 13: Ferramentas e Protocolos

> As interfaces entre IA e o mundo real.

Esta fase passa das chamadas de função e dos esquemas de ferramentas para a interoperabilidade
protocolos, habilidades de agentes, segurança e governança de produção.
As rotas focalizadas abaixo são a ordem de aprendizagem confiável.

## Comece esta fase no GitHub

**Prerequisites:** Phase 11 LLM completion APIs. For MCP or Agent Skills, use
a rota focada abaixo em vez de assumir a ordem numérica das lições.

**First full-phase lesson:** [The Tool Interface](01-the-tool-interface/)

Execute este comando a partir da raiz do repositório:

```bash
python3 phases/13-tools-and-protocols/01-the-tool-interface/code/main.py
```

Manter o comando, código de saída, descrever-decidir-executa-observar rastreio, rejeitado
- Uma frase que explica o limite de virada.

**Next action:** Continuem a [Function Calling Deep Dive](02-function-calling-deep-dive/)- Não .
ou escolher o modelo de protocolo de contexto (MCP) ou a rota de competências de agentes abaixo.

Explore o [full Phase 13 lesson list](../../README.md#phase-13) ou o
[cross-phase roadmap](../../ROADMAP.md)- Não .

## Modelo de caminho de protocolo de contexto (MCP)

A rota de MCP focada é de 17 lições e cerca de 23 horas e 15 minutos.
MCP `2026-07-28` de uma solicitação de JSON-RPC auto-descrição para uma operacional
Porta de conformidade.

| Stage | Lessons | What you prove | Time |
|---|---|---|---:|
| Core | [06](06-mcp-fundamentals/), [07](07-building-an-mcp-server/), [08](08-building-an-mcp-client/), [09](09-mcp-transports/), [10](10-mcp-resources-and-prompts/) | Envelopes, discovery, client and server behavior, transports, resources, and prompts. | 5 hr 50 min |
| Bidirectional | [11](11-mcp-sampling/), [12](12-mcp-roots-and-elicitation/), [13](13-mcp-async-tasks/), [14](14-mcp-apps/) | MRTR input, explicit scope, durable tasks, and app boundaries without server-initiated requests. | 5 hr |
| Secure | [15](15-mcp-security-tool-poisoning/), [16](16-mcp-security-oauth-2-1/), [18](18-mcp-auth-production/), [17](17-mcp-gateways-and-registries/) | Poisoning defenses, authorization, production tokens, gateway routing, and registry admission. | 5 hr 15 min |
| Advanced | [28](28-mcp-tool-contracts-and-content/), [29](29-mcp-reliability-cancellation-and-flow-control/), [30](30-mcp-registry-supply-chain-and-drift/), [31](31-mcp-conformance-versioning-and-operations/) | Contract fidelity, cancellation races, supply-chain drift, and release evidence. | 7 hr 10 min |

A ordem exacta é 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 18, 17, 28,
29, 30, 31. É definido em
[`learning-paths/model-context-protocol.json`](../../learning-paths/model-context-protocol.json)- Não .
O tutor cria `MCP-LEARNING.md`, ensina uma lição por
Invocação e registo de solicitação, resposta, comando, diretório de trabalho, saída
Código e provas de fronteira redigidas exigidas por cada ponto de controlo.

Comece com a invocação apoiada pelo seu anfitrião:

| Host | Invocation |
|---|---|
| Codex | `learn-mcp`, or choose it from `/skills` |
| Claude Code | `/learn-mcp` |
| Other compatible hosts | `Use learn-mcp to start or resume the Model Context Protocol (MCP) path.` |

### Os teus primeiros dez minutos

A partir da raiz do repositório, execute a transcrição sem estado da lição 06:

```bash
python3 phases/13-tools-and-protocols/06-mcp-fundamentals/code/main.py
```

Encontre quatro coisas na saída: pedidos repetidos metadados, um completo
`server/discover` Resultado, erro `-32022` para uma versão não suportada, e
Clusão de transporte que não crie ou encerre uma sessão de protocolo MCP.
Essa transcrição é o primeiro ponto de controlo, não apenas uma demonstração.

Se o repositório ou o Python 3 não estiver disponível, leia [Lesson 06](06-mcp-fundamentals/)
A Comissão de Controle de Pessoas e de Serviços de Informação
A Comissão deve apresentar uma proposta de decisão relativa à aplicação do artigo 107.o, n.o 1, do Regulamento (CE) n.o 1069/2009 do Parlamento Europeu e do Conselho.

Complete o ponto de controlo de segurança executável da lição 15 antes de qualquer não-loopback
O sistema de ligação, acesso compartilhado, ponto final hospedado ou publicação de registros.
Objetivo externo e autoridade requerida, em seguida, confirmar a ação de implantação
Um tutorial completado não concede autoridade de implantação.

Mais velhos `initialize`- Não . `Mcp-Session-Id`, SSE independente `GET`, sessão `DELETE`- Não .
e os fluxos de solicitações iniciados pelo servidor aparecem apenas nas notas de compatibilidade explícitas.
As solicitações modernas declaram a versão do protocolo e as capacidades do cliente em
`params._meta`, uso `server/discover`, e transportar informações suficientes para ser
A avaliação foi validada, autorizada, encaminhada e retestada de forma independente.

[Lesson 23](23-capstone-tool-ecosystem/) é a única rota opcional de MCP
Completar as 17 lições necessárias mais [Lesson 19](19-a2a-protocol/)
e [Lesson 20](20-opentelemetry-genai/) Antes de começar.

## O Agente Skills é um caminho rápido.

A rota focada é de cinco lições e cerca de 9 horas e 30 minutos:

| Step | Lesson | Outcome | Time |
|---:|---|---|---:|
| 1 | [22: Portable Contract and Runtime Boundary](22-skills-and-agent-sdks/) | Create, install, invoke, verify, and remove a complete skill bundle. | 90 min |
| 2 | [24: Discovery and Progressive Disclosure](24-skill-discovery-and-progressive-disclosure/) | Trace discovery, cataloging, activation, and resource loading. | 105 min |
| 3 | [25: Invocation and Routing](25-skill-invocation-and-routing/) | Control explicit, implicit, human, model, and abstention paths. | 105 min |
| 4 | [26: Permissions, Sandboxes, and Trust](26-skill-permissions-sandboxes-and-trust/) | Separate instructions, permissions, containment, and verification. | 120 min |
| 5 | [27: Evals, Packaging, and Portability](27-skill-evals-packaging-and-portability/) | Build a release gate and prove behavior in real hosts. | 150 min |

Comece com a invocação apoiada pelo seu anfitrião:

| Host | Invocation |
|---|---|
| Codex | `learn-agent-skills`, or choose it from `/skills` |
| Claude Code | `/learn-agent-skills` |
| Other compatible hosts | `Use learn-agent-skills to start or resume the Agent Skills Engineering path.` |

O tutor cria ou reinicia `AGENT-SKILLS-LEARNING.md`, ensina uma lição por
A rota é a seguinte:
definidas em
[`learning-paths/agent-skills.json`](../../learning-paths/agent-skills.json)- Não .

Se preferir ler primeiro, comece com [Lesson 22](22-skills-and-agent-sdks/)- Não .
O primeiro laboratório obtém uma habilidade para um verdadeiro anfitrião em cerca de dez minutos.

### Pré-requisito de via rápida

- Para os laboratórios reais, precisas de `node`- Não . `npx`- Não . `python3`, um selecionado
  O anfitrião com habilidade e o acesso escrito ao projeto escolhido ou à habilidade do utilizador
  Verifique os três comandos com `node --version`- Não . `npx --version`, e
  `python3 --version` antes da instalação.
- Se esse pré-vôo não estiver disponível, use o site ou leia cada um `docs/en.md`
  Pode concluir o trabalho conceitual, mas mantém a descoberta,
  Invocação, script, atualização e desinstalação de provas marcadas pendentes.
- Skim [Lesson 01](01-the-tool-interface/) e [Lesson 05](05-tool-schema-design/)
  Se os contratos de ferramentas são novos para si.
- Antes da lição 26, confirme que pode explicar o envenenamento de ferramentas e não confiar
  - Instruções. [Lesson 15](15-mcp-security-tool-poisoning/) é opcional
  A renovação para o voo, não uma sexta lição necessária nesta rota.
- [Lesson 23](23-capstone-tool-ecosystem/) é um sistema opcional,
  Não a próxima aula de habilidades de agente depois de 22.
  antes de o tomar.

## Percurso de engenharia inversa

Quatorze lições ensinam como ler um programa compilado que você construiu. Lições 32 a 36 construem o pipeline central: analisam o arquivo, decodificam as instruções, elevam-nas para pseudocód, gravam o que sabem como evidência e provam uma função reconstruída igual ao original. As lições 37 a 45 ensinam o campo em torno desse pipeline: sua história e ferramentas principais, convocando convenções, idiomas de compilador, vinculando e despojando binários, recuperação de tipos, depuração, formatos de código de bits, execução binária e simbólica, e análise assistida por IA. Cada lição usa as ferramentas reais nos mesmos aparelhos. O manual de acompanhamento, [Reverse Engineering 101](../../manuals/reverse-engineering-101/), corre no mesmo dispositivo através do rea 6.7.0 e Ghidra 12.1.4.

| Lesson | What you build | Time |
|---|---|---|
| [32](32-program-anatomy-elf-from-scratch/) | An ELF reader: headers, sections, symbols, relocations | 2 hr |
| [33](33-disassembly-and-control-flow/) | An x86-64 decoder, linear sweep, recursive descent, and a control-flow graph | 2 hr 30 min |
| [34](34-lifting-to-pseudocode/) | A lifter from instructions to structured pseudocode | 2 hr 30 min |
| [35](35-evidence-confidence-and-unknowns/) | An evidence ledger with confidence, limitations, and unknowns | 1 hr 45 min |
| [36](36-rebuild-and-prove-equal/) | A differential test harness and a byte comparison that masks relocations | 1 hr 50 min |
| [37](37-the-reverse-engineering-landscape/) | A comparison harness over five tools, with a history timeline and four IRs | 2 hr 30 min |
| [38](38-calling-conventions-and-stack-frames/) | A calling-convention analyzer for System V, Windows x64, and AArch64 | 2 hr 20 min |
| [39](39-compiler-idioms-and-optimization/) | An idiom recognizer that decodes division, switches, loops, and selects | 2 hr 30 min |
| [40](40-linking-loading-and-stripped-binaries/) | PE, Mach-O fixup, and ELF link readers, and a function finder for stripped builds | 2 hr 40 min |
| [41](41-recovering-data-and-types/) | A struct and C++ type recovery pass checked against a DWARF reader | 2 hr 20 min |
| [42](42-dynamic-analysis-of-your-own-program/) | An lldb harness that confirms or refutes static claims | 2 hr 10 min |
| [43](43-bytecode-and-managed-formats/) | Readers for .pyc, JVM class, .NET CIL, and WebAssembly | 2 hr 30 min |
| [44](44-binary-diffing-and-symbolic-execution/) | A function differ and a small symbolic executor | 2 hr 30 min |
| [45](45-ai-assisted-reverse-engineering/) | A ground-truth scorecard for AI reconstructions and analysis reports | 2 hr 20 min |

Cada alvo neste caminho é um programa que você escreveu e compilado. a lição 32 começa com a lei e as regras de autorização. para seguir o caminho com um tutor que registra o seu progresso, executar o `learn-reverse-engineering` A sua ordem e os seus pontos de controlo estão no [Reverse Engineering manifest](../../learning-paths/reverse-engineering.json)- Não .

## Fase completa

Veja [ROADMAP.md](../../ROADMAP.md) Para o plano completo da lição.
