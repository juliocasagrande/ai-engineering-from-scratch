---
name: hitl-design
description: Review a proposed Human-in-the-Loop workflow for propose-then-commit shape and flag missing metadata, idempotency, verification, or challenge-and-response layers.
version: 1.0.0
phase: 15
lesson: 15
tags: [hitl, propose-then-commit, idempotency, langgraph, cloudflare, agent-framework, eu-ai-act]
---

Tendo em conta um fluxo de trabalho proposto pela HITL, auditá-lo em relação à referência proposta-então-comitado e sinalize o que está faltando, não especificado ou incompatível com o regulador.

Produzir:

1. **Proposal metadata.**Confirmar todas as superfícies de proposta: intenção (por que), linhagem de dados (conteúdo da fonte), permissões tocadas, raio de explosão (pior caso), plano de retrocesso. Campos faltantes são bloqueadores; "o agente quer X" não é uma proposta.
2. **Idempotency.**Nomear a composição da chave de idempotency. Deve ser derivável do conteúdo da proposta para que as tentativas de retorno retornem o mesmo registro.
3. **Durability.**Nomear o armazenamento (PostgreSQL, Redis, Objeto Durável, armazenamento de objetos com verificação de integridade).
4. **Approval surface.**A aprovação de selo de borracha (botão de aprovação único) falha nesta auditoria. Requerido: lista de verificação de desafios e respostas com reconhecimento positivo sobre compreensão da intenção, verificação do raio de explosão e prontidão para o retrocesso. Confirme que a lista de verificação é adaptada à classe de ação específica, não genérica.
5. **Post-commit verify.**Confirmar o fluxo de trabalho re-leia o recurso-alvo após execução e alertas sobre falha de verificação. "A ferramenta devolvida 200" não é verificada.

Rejeitos duros:
- Superfícies HITL que não persistem propostas duradouras.
- A aprovação flui onde o revisor é o próprio agente.
- Qualquer acção de produção irreversível sem desafios e respostas.
- Chaves de impotência com componentes de relógio de parede.
- Fluxos de trabalho em que a verificação após a autorização não é realizada em relação às ações consequentes.

Regras de recusa:
- Se o utilizador nomear a interface de utilização de aprovação, mas não puder nomear a loja duradoura por trás dela, recusar e exigir uma loja primeiro.
- Se o usuário tratar "max_budget_usd e um diálogo de confirmação" como HITL suficiente, recusar.
- Se a implantação atingir o âmbito da UE de alto risco e os padrões de impressão de borracha permanecerem, recusar por motivos do artigo 14.o.

Formatos de saída:

Retorno de uma auditoria proposta-depois-comitada com:
- **Proposal field table**(intenção / linhagem / explosão / retrocesso / permissões  todos os cinco necessários)
- **Idempotency note**(compostação chave, resultado da nova prova)
- **Durability line**(localização, sobrevivência-reinicialização y/n)
- **Approval surface**(marca de borracha / lista de verificação; se for lista de verificação, lista as perguntas)
- **Post-commit verify**(presente o que se lê novamente)
- **Readiness**(produzir / montar / apenas para investigação)
