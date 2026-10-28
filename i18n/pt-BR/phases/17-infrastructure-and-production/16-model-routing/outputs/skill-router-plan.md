---
name: router-plan
description: Desenhar um plano de roteamento de modelo de LLM  escolher padrão (pre-rumo, cascata, conjunto), sinais (tarefa, comprimento, incorporação, confiança) e portas de qualidade online.
version: 1.0.0
phase: 17
lesson: 16
tags: [routing, cascade, model-cascade, routellm, notdiamond, cost-reduction]
---

Dada a mistura de carga de trabalho (example de classificação de tarefas), nível de qualidade, tolerância à latência e gastos mensais atuais, produzir um plano de roteamento.

Produzir:

1. Padrão: pré-ruta (mais rápida, dependente do classificador), cascata (capa de melhor qualidade) ou conjunto (só amostra A/B).
2. Os sinais. escolha entre: classificação de tarefas, comprimento rápido, inserindo semelhança com conhecido-duro, autoconfiança. estado que combinam (geralmente 2-3) e a regra de composição.
3. Par barata/fronteira. Nomear os modelos específicos. Exemplo: Claude Haiku 3.5 + GPT-5. Justificar com curva de custo + capacidade.
4. Economia esperada. Calcule o custo combinado na divisão recomendada; estado esperado mensal em dólares versus corrente.
5. Portais de qualidade online. Especificar o juiz de tráfego em tempo real: 5% de amostragem por rota avaliada por um juiz de fronteira; alerta se a qualidade Δ > 2%.
6. Rollout. Shadow (route mas ignore; compare offline), canário 10% por coorte de usuários, expandir no portal de passagem.

Rejeitos duros:
- Roteamento sem portas de qualidade online.
- Usando apenas classificação de tarefas como sinal. Recusar  perde dificuldade dentro de tarefas.
- Rotear tarefas elegíveis para fronteiras (código, matemática, multi-passo) a barato sem um retrocesso em cascata.

Regras de recusa:
- Se a tolerância de qualidade for indicada como "regressão zero", recusar a rota prévia e propor uma cascata com alta taxa de escalada.
- Se o modelo barato for não-antropico/não-OpenAI/não-fronterizo e tiver padrões de recusa conhecidos (por exemplo, modelos não censurados para uso de ferramentas de agente), recusar o par  quebrará silenciosamente as chamadas de ferramentas.
- Se o roteamento for para um fornecedor diferente por preço barato (cascada de fornecedores cruzados), exigir a camada de gateway de IA (Fase 17 · 19) para unificar as APIs.

Resultado: padrão de nomeamento de um plano de uma página, sinais, par de modelos, economias esperadas, portas online, plano de implantação.
