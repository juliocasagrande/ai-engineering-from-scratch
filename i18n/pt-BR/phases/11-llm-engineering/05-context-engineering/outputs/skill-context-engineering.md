---
name: skill-context-engineering
description: Quadro de decisão para a concepção de canais de montagem de contexto com base no tipo de tarefa, no tamanho da janela e no orçamento de latência
version: 1.0.0
phase: 11
lesson: 05
tags: [context-engineering, context-window, rag, memory, tool-selection, lost-in-the-middle]
---

# Engenharia de contexto

Ao criar uma aplicação de LLM, aplicar esta estrutura para projetar o conjunto de contextos.

## Princípios fundamentais

1. **Context is scarce.** Uma janela de 128K soa grande, mas enche-se rapidamente.
2. **Attention is uneven.** Os modelos atendem mais ao início e ao fim, colocam informações críticas lá.
3. **Dynamic beats static.** Diferentes consultas precisam de contextos diferentes.
4. **Less is more.** Um contexto de 10K selecionado supera um contexto de 100K descarregado.
5. **Measure everything.** Não se pode otimizar o que não se mede, contar tokens por componente em cada pedido.

## Orientações orçamentais contextuais

| Component | Typical Range | Priority | Compression Strategy |
|-----------|-------------|----------|---------------------|
| System prompt | 200-1,000 tokens | Fixed, high | Write tight, remove redundancy |
| Tool definitions | 500-3,000 tokens | Dynamic, medium | Prune by query intent |
| Retrieved context | 1,000-5,000 tokens | Dynamic, high | Rerank + threshold + deduplicate |
| Conversation history | 500-5,000 tokens | Dynamic, medium | Summarize old turns |
| Few-shot examples | 500-2,000 tokens | Dynamic, high | Select by task similarity |
| User query | 50-500 tokens | Fixed, highest | N/A |
| Generation reserve | 2,000-8,000 tokens | Fixed | Adjust by expected output length |

## Quando utilizar cada tipo de memória

**Short-term (conversation history):** A sessão atual. Gerido por resumo. Compressão voltas mais antigas do que 5-10 trocas. Mantém as últimas 3-4 voltas literal.

**Long-term (facts database):** Preferências e fatos do projeto que persistem em todas as sessões. Retirada no início da sessão. Exemplos: "o usuário prefere Python", "o projeto usa PostgreSQL", "a equipe segue o desenvolvimento baseado em tronco". Armazenar em CLAUDE.md, um banco de dados ou um sistema de memória estruturado.

**Episodic (past interactions):** Conversas anteriores específicas relevantes para a tarefa atual. Armazenar como embutidos, recuperar por semelhança. "Na semana passada, desbastamos um problema similar de autor" é memória episódica.

## Estratégia de selecção de ferramentas

Não inclua todas as ferramentas em cada pedido.

1. Classificar a intenção da consulta (código, e-mail, calendário, pesquisa, dados)
2. Intenções de mapeamento para categorias de ferramentas
3. Incluir apenas ferramentas correspondentes
4. Se a intenção for ambígua, inclua ferramentas das duas principais categorias
5. Sempre incluir uma ferramenta "general" (como pesquisa na web) como retrocesso

Economia esperada: 60-80% dos tokens de definição de ferramenta em consultas com intenção clara.

## Melhores práticas de recuperação

- **Rerank after retrieval.** A semelhança vectorial é um filtro grosseiro. Um reencoderador (cross-encoder ou LLM-based) melhora significativamente a precisão.
- **Set a relevance threshold.** Não incluam pedaços abaixo de 0,3 cosina de semelhança.
- **Deduplicate.** Se dois blocos compartilharem mais de 80% de conteúdo, mantenha apenas o mais alto.
- **Apply lost-in-the-middle ordering.** Coloque os pedaços mais relevantes em primeiro lugar e em último lugar.
- **Limit total retrieval tokens.** 3-5 pedaços altamente relevantes vencem 15 pedaços mediocres.

## Gestão de história

- Manter as últimas 3-4 curvas literalmente (o modelo precisa de contexto recente)
- Resumir as versões mais antigas em um digest ("Discutimos X, decidimos Y e bloqueamos em Z")
- Desligação de viradas geradas pelo sistema que não adicionam informações (invocações de ferramentas sem conteúdo orientado para o usuário)
- Compressão de desencadeamento quando o histórico exceda 30% do orçamento disponível

## Banderas vermelhas

- Sistema de prompt excede 2.000 tokens: provavelmente inclui informações que devem ser dinâmicas
- Todas as ferramentas incluídas em cada pedido: implementar a seleção baseada em intenções
- Não há filtragem de relevância na recuperação: você está a descarregar ruído na janela
- A história cresce sem limites: a resumida não é implementada
- Sem reserva de geração: o modelo truncado suas respostas
- A mesma informação em 3 lugares (promete do sistema, documento recuperado, histórico): deduplicar
- Utilização do contexto superior a 60%: deixam muito pouco espaço para o modelo "pensar"
