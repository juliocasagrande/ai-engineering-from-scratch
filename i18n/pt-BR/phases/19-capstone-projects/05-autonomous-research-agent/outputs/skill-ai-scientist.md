---
name: ai-scientist
description: Build an autonomous research agent that runs experiment tree search, writes LaTeX papers with vision critique, and passes a sandbox-escape red team.
version: 1.0.0
phase: 19
lesson: 05
tags: [capstone, autonomous-agent, ai-scientist, sakana, langgraph, sandbox, research]
---

Dado uma ideia de semente, um domínio estreito e um orçamento de computação de $ 30, construir um agente que execute uma pesquisa de árvore experimental, escreve um artigo LaTeX revisable, e emite um pacote de reprodução.

Construir um plano:

1. Passagem de literatura: API de gráfico de estudiosos semânticos + OpenAlex; resumos do cache em FAISS; gerar um digest de domínio de 1 página.
2. Busca de árvore: implementar melhor-primeira expansão sobre nós experimentais com `expand(node) -> children`(uma edição de configuração por filho) e `score(node) = novelty*0.4 + quality*0.5 + budget*0.1`- Não .
3. Sandbox por nó: cada experimento é executado`docker run --network=none --memory=8g --cpus=2 --pids-limit=256 --read-only`ou equivalente E2B; sementes deterministas; limite de recursos aplicado.
4. Plan-execute-verifique: verifique as verificações de passo que a perda convergiu, as linhas de base foram executadas, as ablações isolam a reivindicação.
5. Escrever: gerar LaTeX, compilar para PDF, alimentar PDF para modo de visão Claude Opus 4.7 para crítica no layout e alinhamento de reivindicação-evidência, iterar até 3 vezes.
6. Ensemble de revisores: cinco juízes (Opus 4.7, GPT-5.4, Gemini 3 Pro, DeepSeek R1, Qwen3-Max) pontuação na rubrica NeurIPS (novidade, rigor, clareza, reprodução, impacto); média < 4.0 retorna ao escritor.
7. Equipe vermelha: integra tarefas adversárias (bomba de garfo, fuga do sistema de arquivos, chamada de rede escrita pelo LLM).`red_team.md`- Não .
8. Pacote de reprodução: paper.pdf + review.md + tree-search trace JSON + sementes + W&B run links + sandbox config + comando de re-run de uma linha.

Rubrico de avaliação:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | Paper quality | Blind rubric review against published workshop papers on the same seed topic |
| 20 | Experimental rigor | Baselines, seeds, ablations; every claim backed by a cell in the results table |
| 20 | Cost and compute discipline | $30 ceiling per paper enforced, Langfuse-traced |
| 20 | Safety | Sandbox red team passes; network policy and kill-switch verified with logged attempts |
| 15 | Reproducibility | One-command rerun reproduces the paper with identical seeds |

Rejeitos duros:

- A tese da pedra final é que a execução está contida.
- Passo de escrita que não relee o PDF compilado (a crítica visual é carregadora).
- Papéis sem linhas de base, sementes ou secção de ablação.
- Os orçamentos de custos só foram aplicados como avisos pós-hoc, não como limites rígidos.

Regras de recusa:

- Recusar a publicação de um artigo com média de revisores abaixo de 4,0/5 sem uma autorização humana explícita.
- Recusar-se a executar uma ideia semente que requer acesso à rede a partir do interior da caixa de areia. Adicionar um volume de conjunto de dados separado apenas para leitura em vez disso.
- Recusar-se a reproduzir um jornal cuja equipa vermelha não tenha sido executada e registada.

Resultado: um repo contendo o motor de pesquisa de árvores, a política de caixa de areia, o ciclo de escritor/revisor, três exemplos de corridas com pacotes de reprodução, um relatório da equipe vermelha, um csv do livro de custos e um registro de nomeação de quais dos modos de falha Sakana v2 você reproduzido e como a mitigação funcionou.
