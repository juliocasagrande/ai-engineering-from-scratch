---
name: parallel-inference-router
description: Route a reasoning workload between voting, tree-of-thought, multi-agent, Hogwild!, and speculative decoding strategies.
version: 1.0.0
phase: 10
lesson: 22
tags: [parallel-inference, hogwild, speculative-decoding, tree-of-thought, multi-agent, reasoning]
---

Tendo em conta um perfil de carga de trabalho raciocínico (orçamento de tokens por tarefa, características de paralelismo de tarefa, família de modelos, objetivo de implantação, orçamento de latência), recomendamos uma estratégia de inferência paralela ou uma combinação.

Produzir:

1. Classificação de tarefas. Raciocínio longo (5k + tokens), cadeia de pensamento média (1k-5k), chat curto (menos de 1k) ou classificação.
2. O sistema de decodificação de sequências internos (descódigo especulativo) versus transversal (voting, Hogwild!, multi-agent).
3. Recomendação de estratégia. Escolha entre: apenas descodificação especulativa (default segura para qualquer carga de trabalho acima de 100 tokens), especulativa + Hogwild! (razão longa com estrutura paralelavel), árvore de pensamento (problemas explícitos de ramificação e poda), multi-agente (problemas de especialização de papéis), conjunto de votação (classificação de alto risco).
4. Para descodificação especulativa: família de projetos (default EAGLE-3) e `N`(Fase 10 · 15 habilidade) Para Hogwild!: número de trabalhadores N (2 a 4, raramente mais), modelo de resposta de coordenação, confirmação de implantação de um único nó.
5. Estimativa combinada de aceleração: se combinar a descodificação especulativa com Hogwild!, informe a aceleração multiplicativa (intervalo típico: 3x especificação * 1,5-2x Hogwild! = 4,5-6x).

Rejeitos duros:
- Hogwild! para qualquer carga de trabalho inferior a 2000 tokens.
- Hogwild! sobre modelos não racionais (sem coordenação emergente).
- Quadro multi-agente para problemas que não têm uma decomposição natural de papel.
- Árvore de pensamento sem lógica explícita de ramificação e poda (a estratégia se reduz a CoT linear, caso contrário).
- Execução Hogwild! através de nós (sincronização de cache de nós cruzados é muito lenta).

Regras de recusa:
- Se a carga de trabalho é pesquisa experimental, recomende Hogwild! como uma experiência em vez de uma aposta de produção. Os speedups são dependentes da tarefa e a implantação no mundo real é rara a partir de abril de 2026.
- Se o usuário pedir uma aceleração garantida, recuse e explique que apenas a descodificação especulativa tem a propriedade de forte garantia (distribuição de saída preservada).
- Se o usuário tiver VRAM limitado, recuse Hogwild! N>2  cada trabalhador precisa de sua própria memória de ativação, mesmo que o cache seja compartilhado.

Resultado: uma recomendação de uma página listando classificação de tarefas, eixo de paralelismo, estratégia, parâmetros e estimativa combinada de aceleração.
