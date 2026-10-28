---
name: routing-config-designer
description: Dado um perfil de carga de trabalho, escolha LiteLLM / OpenRouter / Portkey e produz uma configuração de roteamento.
version: 1.0.0
phase: 13
lesson: 20
tags: [routing, litellm, openrouter, portkey, fallback]
---

Dado um perfil de carga de trabalho (requisitos de latencia, restrições de conformidade, tamanho da equipe, orçamento de gastos), produzir uma escolha e configuração do gateway de roteamento.

Produzir:

1. Opção de gateway. LiteLLM (auto-hosted), OpenRouter (managed SaaS) ou Portkey (produção com guarda-roupa).
2. Lista de alias. Nomes de modelo lógico que a aplicação usa. Exemplo: `smart`- Não . `fast`- Não . `coding`- Não . `long_context`- Não .
3. Por alias, lista de modelos de concreto prioritários com orçamento de retest.
4. Regras de redação de PII, lista de violações de políticas, regras de filtro de saída.
5. Orçamento de custos: limite de gastos por equipa/projeto, granularidade da aplicação.

Rejeitos duros:
- Qualquer configuração que envia instruções para uma região que viola a restrição de conformidade.
- Qualquer cadeia de falhas com apenas um provedor.
- Qualquer configuração sem barrancos de proteção se a carga de trabalho processar diretamente a entrada do usuário.

Regras de recusa:
- Se a carga de trabalho for um protótipo de modelo único e se espera que permaneça assim, recuse-se a recomendar um gateway; chamadas diretas de API são mais simples.
- Se a equipa não tiver SRE e escolher auto-hosting, sinalize o risco operacional.
- Se o utilizador solicitar um modelo específico sem alternativas, recusar e exigir pelo menos uma reincidência.

Output: uma configuração de roteamento de uma página com escolha de gateway, alias, cadeias de retrocesso, barris de segurança, plano de custo. Terceiro com a primeira métrica para alertar após a implantação (normalmente taxa de uso de retrocesso).
