---
name: skill-llm-evaluation
description: Decision framework for choosing the right LLM evaluation strategy based on task type, budget, and requirements
version: 1.0.0
phase: 10
lesson: 10
tags: [evaluation, evals, benchmarks, llm-as-judge, elo, metrics]
---

# Estratégia de avaliação do MLL

Ao avaliar um sistema de Mestrado em Direito Jurídico, aplique este quadro de decisão para escolher a abordagem correta.

## Quando utilizar cada tipo de avaliação

**Benchmarks (MMLU, HumanEval, SWE-bench):**Você está fazendo a seleção inicial de modelos. Você precisa restringir 10 modelos candidatos para 3. Os índices de referência fornecem classificação aproximada a custo zero. Não use os índices de referência como sua avaliação final.

**Custom evals:**Você está construindo para produção. Você tem uma tarefa específica com modos de falha específicos. Avaliações personalizadas são a única avaliação que prevê o desempenho no mundo real. Mínimo 50 casos de teste para protótipo, 200+ para produção.

**LLM-as-judge:**A sua tarefa é aberta (resumo, escrita, conversa). Metricas de coincidência exatas e de sobreposição de tokens são muito rígidas. LLM como juiz custa ~ $ 0,01 por julgamento e concorda com os seres humanos ~ 80% do tempo.

**Human evals:**As apostas são altas e as métricas automatizadas discordam.$0.10-$Reserva para casos ambíguos e calibração periódica de métricas automatizadas.

**ELO from pairwise comparisons:**O Pairwise é mais confiável do que a pontuação absoluta porque os humanos (e os juízes de LLM) são melhores em julgamentos relativos.

## Seleção de função de pontuação

- **Exact match**: classificação, extracção de entidades, saídas estruturadas com respostas conhecidas
- **Token F1**: tarefas de extracção em caso de crédito parcial
- **ROUGE-L**: resumo, tradução
- **BLEU**: tradução automática
- **LLM-as-judge**: geração aberta, qualidade das conversas, utilidade
- **Execution-based**: geração de código (exercer o código, verificar se os testes são aprovados)
- **Schema compliance**: saídas estruturadas (o JSON corresponde ao esquema?)

## Bandeiras vermelhas no projeto de avaliação

- Eval Set menor que 50 casos: os resultados não têm significado estatístico
- Não há casos de borda: você está a medir o desempenho do caminho feliz, que é sempre superior ao mundo real
- Metrica única: métricas diferentes contam histórias diferentes, usem pelo menos duas
- Não há versão: não pode acompanhar a melhoria sem conjuntos de avaliação versão
- Contaminação do conjunto de Eval: nunca incluir exemplos de eval em dados de ajuste fino ou em pedidos de poucas fotos
- Testar apenas um modelo: é necessário uma linha de base (mesmo uma simples heurística) para comparação

## Lista de verificação do gasoduto Eval

1. Defina a tarefa com precisão (não "responder perguntas" mas "clasificar os bilhetes de apoio em 5 categorias")
2. Criar casos de teste em todo caminho feliz, casos de borda e regressões conhecidas
3. Selecionar as funções de pontuação 2-3 adequadas para o tipo de tarefa
4. Limitações de aprovação/falha definidas com base nos requisitos de produção
5. Execução automática: um comando executa o conjunto completo
6. Versão de tudo: casos de teste, funções de pontuação, instruções, versões de modelo
7. Execute todas as alterações: atualizações rápidas, troca de modelos, implementações de código
8. Tendências de pista: uma única pontuação é ruído, uma linha de tendência é sinal
9. Calibração contra o julgamento humano trimestral
10. Adicionar casos de regressão sempre que uma falha de produção for descoberta
