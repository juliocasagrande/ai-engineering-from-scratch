---
name: managed-platform-picker
description: Pick a managed LLM platform (Bedrock, Azure OpenAI, Vertex AI) and a second for redundancy, given workload, SLA, and compliance requirements — then produce a FinOps instrumentation plan.
version: 1.0.0
phase: 17
lesson: 01
tags: [bedrock, azure-openai, vertex-ai, ptu, finops, managed-platforms]
---

Dado um perfil de carga de trabalho (modelos necessários, tokens mensais, TTFT SLA em P50/P99, restrições de conformidade, pegada existente na nuvem), produzir uma recomendação de plataforma.

Produzir:

1. Plataforma primária. Nomear a plataforma, os modelos específicos que abrange, e se unidades de transferência sob demanda ou fornecidas (PTUs) / transferência fornecida é apropriado dada utilização. Cite a matemática de equilíbrio (PTU em aproximadamente 40-60% de utilização sustentada).
2. Plataforma secundária. Nomear o retorno mínimo de dois provedores. Justificar o acoplamento  redundância deve cobrir a sobreposição do modelo (Claude em Bedrock + GPT em Azure OpenAI é o par comum) e a sobreposição da região.
3. Instrumentamento FinOps. Especifique o que é habilitado no primeiro dia: Perfis de Inferência de Aplicação Bedrock, escopo de Azure + reservas de PTU como objetos de custo, Vertex projeto por equipe + BigQuery Billing Export. Nomear as dimensões de atribuição  por usuário, por tarefa, por inquilino.
4. Verifique o SLA. Compare o TTFT P99 de destino com os benchmarks publicados (Azure OpenAI PTU ≈ 50 ms P50; Bedrock on-demand ≈ 75 ms P50).
5. Verificação de conformidade. Verifique BAA, SOC 2 Tipo II, HIPAA, residência de dados da UE conforme necessário. Observe que todos os três cumprem a linha de base, mas as políticas de retenção e a exclusão de monitorização de abusos são diferentes.
6. Caminho de migração. Nomear um passo reversível que a equipe pode tomar esta semana (por exemplo, implementar através de um fornecedor de abstracção de gateway de IA; cabeçalhos de atribuição de instrumentos) e um passo a longo prazo (compromiso PTU; falha transregional).

Rejeitos duros:
- Recomendo uma única plataforma sem um retrocesso nomeado.
- Recuperação de PTU sem estimativa de utilização.
- Ignorar perfis de inferência de aplicação de Bedrock quando a atribuição é listada como um requisito  são a superfície nativa mais limpa.

Regras de recusa:
- Se a carga de trabalho requer Claude, Gemini e GPT todos como P0, nome a realidade de três plataformas (Bedrock + Vertex + Azure OpenAI atrás de um gateway) em vez de fingir que uma plataforma pode servir a todas as três.
- Se o SLA for TTFT P99 < 100 ms e o orçamento previsto não puder apoiar a PTU, recusar-se a prometer ao SLA  explicar o limite máximo de variação sob demanda.
- Se o cliente pedir "utilizar o fornecedor mais barato", o preço de rejeição  é multidimensional (taxa de tokens + capacidade dedicada + custos gerais de atribuição + custo de bloqueio).

Resultado: uma decisão de uma página com plataforma primária, plataforma secundária, PTU vs on-demand, lista de instrumentos, verificação de SLA/conformidade e duas etapas de migração.
