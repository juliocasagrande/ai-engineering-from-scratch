---
name: computer-use-safety
description: Construir um classificador de segurança por etapa + porta de confirmação para um agente de uso informático, com navegação de lista de autorização e filtragem de marcadores de injecção.
version: 1.0.0
phase: 14
lesson: 21
tags: [computer-use, safety, claude, openai-cua, gemini]
---

Dado um agente de uso de computador e uma lista de aplicativos alvo, produzir uma camada de segurança que classifica cada ação antes da execução.

Produzir:

1. `SafetyClassifier.assess(action, screen) -> SafetyVerdict` com campos `allow`- Não . `reason`- Não . `needs_confirmation`- Não .
2. Lista de rótulos de elementos que o agente pode clicar; recusa em contrário.
3. Lista de URLs permitidas para os agentes navegarem; recusa em redirecionamentos fora da lista.
4. Filtro de marcador de injeção no texto DOM, conteúdo recuperado e texto digitado. Qualquer correspondência bloqueia a ação.
5. Porta de confirmação para ações sensíveis (login, compra, exclusão, publicação).
6. Emite de rastreamento: cada decisão registada (ação, veredicto, razão).

Rejeitos duros:

- Classificador de segurança que só funciona na primeira ação.
- Lista de forma `*`Um autor que permite tudo não é um autor.
- Salto confirmação porque o modelo "parece confiante".

Regras de recusa:

- Se o agente tiver acesso a um computador sem segurança por passo, recuse-se a enviar.
- Se o agente pode navegar para URLs arbitrárias, recuse. Requer lista de permisos ou lista de bloqueio.
- Se as ações sensíveis ignorarem o portal de confirmação em qualquer modo, recusar.

Output: `classifier.py`- Não . `allowlist.py`- Não . `confirmation.py`- Não . `trace.py`- Não . `README.md` A conclusão é a seguinte: "O que ler a seguir" com referência à lição 27 (injecção imediata) e à lição 23 (atribuição de tempo de utilização OTel para decisões de segurança).
