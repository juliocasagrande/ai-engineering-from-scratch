---
name: economy-designer
description: Design a minimal agent economy — identity, credit attribution, payment mechanism, reputation. Picks the smallest stack that solves the user's multi-agent incentive problem.
version: 1.0.0
phase: 16
lesson: 21
tags: [multi-agent, economy, Shapley, auctions, reputation, DePIN]
---

Dado um cenário multi-agente que requer alinhamento de incentivos (rede aberta, operadores heterogêneos, recompensas tokenizadas ou roteamento baseado em reputação), desenhe a camada econômica.

Produzir:

1. **Identity layer.**DIDs W3C para identidade portátil ou IDs internos da plataforma se o sistema estiver fechado.
2. **Credit attribution.**Divisão igual, último contribuinte-tomou-todo, contribuição ponderada, Shapley (exacto ou amostragado), ou nenhum (pagamento por chamada). Recomendação de amostragem Shapley quando coalizões importam; divisão igual para simples pagamentos por chamada.
3. **Payment mechanism.**O segundo preço do leilão para atribuição de tarefas (verdadeiro sob agregação monótona), o primeiro preço da velocidade, o preço publicado pela simplicidade.
4. **Reputation rule.**A reputação lê barato (O(1) para roteamento) e escreve após a verificação.
5. **Verification.**Quem verifica a qualidade da contribuição? Um agente separado, revisão humana, oráculos na cadeia, atestamento entre agentes? Sem verificação, a atribuição de crédito é uma conjectura.
6. **Sybil mitigation.**O que impede um operador de fazer N agentes falsos?
7. **Legal and jurisdictional check.**Os pagamentos denominados em tokens têm um impacto na regulamentação financeira na maioria das jurisdições.

Rejeitos duros:

- Qualquer projeto sem verificação da qualidade da contribuição.
- Repútua sem decadência, repútua estável recompensa agentes que fizeram um bom trabalho anos atrás, mas agora estão quebrados.
- Calculação exata de Shapley para N > 6. O tempo de cálculo aumenta como N!; mostra em vez disso.
- Os leilões de segundo preço em que a função de agregação não é monótona.
- Distribuição de tokens sem verificação regulatória. Muitas jurisdições tratam isso como atividade de valores mobiliários.

Regras de recusa:

- Se o sistema for totalmente interno (uma empresa, um operador), recomendemos uma alocação mais simples (o gerente atribui, as métricas são internas).
- Se não houver forma de verificar a qualidade da contribuição, recomenda-se adicionar a verificação antes do projeto económico.
- Se o usuário quiser um sistema tokenizado, mas não tiver uma equipe legal, marque o risco e recomenda começar com reputação (não-token).

Resultado: um resumo de duas páginas. Comece com um resumo de uma frase ("Sistema de Reputasão Somente com DIDs, crédito Shapley-sampled em oleodutos de 3 agentes, leilão de segundo preço para atribuição de slots, corte em falha de verificação. "), então as sete seções acima. Termina com um plano piloto de 30 dias: fase de aquecimento, configuração de pipeline de verificação, implantação ponderada pela reputação, cronograma de auditoria.
