---
name: eval-suite
description: Build a three-layer eval suite (static benchmarks, custom offline, online production) with evaluator-optimizer loop and CI gates.
version: 1.0.0
phase: 14
lesson: 30
tags: [evaluation, ci, regression, benchmarks, llm-judge]
---

Dado um produto agente, construir uma suite de avaliação de três camadas conectada à CI.

Produzir:

1. **Static benchmark layer** pelo menos um indicador de referência relevante (SWE-bench Verified para código, BFCL V4 para uso de ferramentas, WebArena para web, OSWorld para desktop, GAIA para generalista).
2. **Custom offline layer** pelo menos uma rubrica de juiz de LLM marcada em dimensões específicas de domínio (factual, tom, alcance, qualidade de recusa). pelo menos um caso baseado em execução que analisa o estado real após o agente executar. pelo menos um caso baseado em trajetória com um caminho de ouro.
3. **Online eval layer** Repetições de sessões, alertas activadas por barril de segurança, rastreamento de custos/latencia por etapa através dos períodos OTel GenAI (Lessão 23).
4. **Evaluator-optimizer runner** envolver o agente em proposição / juízo / refinamento com um tapete redondo.
5. **CI gate** falhar na construção em >=5% regressão versus linha de base.
6. **Case mapping** cada guarda e cada regra aprendida das lições da Fase 14 tem pelo menos um caso.

Rejeitos duros:

- Não se pode detectar regressão sem referência.
- O processo de avaliação da qualidade de vida dos estudantes é um processo de avaliação da qualidade de vida dos estudantes.
- Casos sem sem sementes empilhadas ou estado de instantâneo.

Regras de recusa:

- Se o usuário quer "apenas o caminho feliz", recuse.
- Se o utilizador quiser "sem portal de informação", recuse-se a produtos que atingam utilizadores pagantes.
- Se o utilizador quiser "todos os juízes de LLM", recuse-se em tarefas factuais e de conformidade.

Output: `cases/benchmarks/`- Não .`cases/custom/`- Não .`cases/online/`- Não .`runner.py`- Não .`ci_gate.py`- Não .`README.md`Explicando rubricas, linhas de base e a tabela de mapeamento da Fase 14. Conclui com "o que ler a seguir" apontando para a lição 24 (observabilidade), lição 26 (modos de falha) ou lição 23 (OTel) para o substrato.
