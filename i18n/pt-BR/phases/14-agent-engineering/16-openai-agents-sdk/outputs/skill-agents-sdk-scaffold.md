---
name: agents-sdk-scaffold
description: Scaffold an OpenAI Agents SDK app with a triage agent, handoffs, input/output/tool guardrails, session store, and a trace processor.
version: 1.0.0
phase: 14
lesson: 16
tags: [openai, agents-sdk, handoffs, guardrails, tracing, session]
---

Dado um domínio de produto e uma lista de agentes especializados, estabeleça um aplicativo OpenAI Agents SDK.

Produzir:

1. `Agent`por especialista mais um `triage`Agente que só tem transferências (sem ferramentas de domínio).
2. `FunctionTool`por ferramenta de domínio com esquema de entrada digitado, descrição clara (indica ao modelo quando usá-lo) e caixa de arame de execução.
3. `Handoff`A selecção de ferramentas é feita por um grupo de especialistas.`transfer_to_<agent>`Convenção.
4. `InputGuardrail`Para PII, política, escopo. Default para modo paralelo, a menos que o guardrail LLM seja grande em relação ao modelo principal  então use bloqueio.
5. `OutputGuardrail`Sempre bloqueando o prod para resultados críticos à segurança.
6. Os dispositivos de proteção por ferramenta são utilizados para as ferramentas de função que tocam a rede ou o sistema de arquivos.
7. `Session`armazenamento (SQLite por defeito; Redis para prod).
8. `add_trace_processor`O cabo vai para o seu backend ao lado da interface de rastreamento da OpenAI.

Rejeitos duros:

- Agentes de triagem com ferramentas de domínio. Triagem apenas entregues; mistura diluir a decisão do roteador.
- Os guardrails que mutam a entrada/saída. Os guardrails aprovam ou rejeitam  não reescrevem.
- Loops de transferência silenciosos.

Regras de recusa:

- Se o usuário quer "sem barris, apenas se move rápido", recuse qualquer produto que atinja usuários pagantes ou PII.
- Se o produto tiver apenas 2 especialistas, sugira- se o encaminhamento através de `Agents`Com um classificador direto (Lessão 12) em vez de triagem+caso de subsídios  menor custo simbólico.
- Se o rastreamento estiver desativado, recuse-se a enviar.

Output: `agents.py`- Não .`tools.py`- Não .`guardrails.py`- Não .`app.py`- Não .`README.md`com a raciocínio do agente de triagem, modos de guarda-panela, processador de rastreamento e backend da sessão. terminar com "o que ler a seguir" apontando para a lição 23 (OTel GenAI), lição 24 (backends de observabilidade), ou lição 17 para Claude Agent SDK tradução.
