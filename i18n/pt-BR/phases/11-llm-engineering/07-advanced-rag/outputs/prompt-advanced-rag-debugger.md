---
name: prompt-advanced-rag-debugger
description: Diagnóstico e resolução de problemas de qualidade de RAG em todas as áreas de recuperação, geração e avaliação
phase: 11
lesson: 7
---

Se tivermos uma descrição de falhas ou má qualidade, diagnosticemos a causa e prescrevemos correções específicas.

Reúna estes diagnósticos:

1. **Sample failing query**A pergunta que deu um mau resultado .
2. **Retrieved chunks**: o que foi realmente recuperado (resultados top-k com pontuações)
3. **Generated answer**O que o MLL produziu
4. **Expected answer**O que é que a resposta correta deveria ter sido:
5. **Retrieval method**: apenas vetor, apenas BM25, ou híbrido
6. **Chunk size and overlap**: configuração corrente

Diagnóstico com esta árvore de decisão:

**Is the correct chunk in the vector store at all?**
- Não: o documento não foi indexado, ou foi dividido de uma forma que dividiu a resposta em limites de fragmentos.
- Sim: prossegue para o próximo cheque.

**Is the correct chunk in the top-50 retrieval results?**
- Não: inserção de desajuste. A consulta e o documento usam vocabulário diferente. Corrigir:
  - Adicionar busca híbrida (BM25 capta correspondências exatas de termos)
  - Tente HyDE para preencher a lacuna entre consulta e documento
  - Reformula a consulta usando um LLM antes de pesquisar
- Sim: prossegue para o próximo cheque.

**Is the correct chunk in the top-k (final results)?**
- Não, mas está no top 50, o pedaço está a ser recuperado mas classificado muito baixo.
  - Adicionar um re-ranqueador (cross-encoder) para re-pontuação do top-50
  - Aumentar k para incluir mais candidatos
  - Peso de fusão de Tune RRF
- Sim: prossegue para o próximo cheque.

**Is the LLM ignoring the retrieved context?**
- Sim: o modelo de solicitação é fraco.
  - Adicionar instruções explícitas: "Resposta SÓ baseado no contexto fornecido"
  - Colocar a temperatura em 0
  - Colocar o contexto recuperado antes da pergunta (efeito de primate)
  - Adicione "Se o contexto não contém a resposta, diga-o"
- Não: prossegue para o próximo cheque.

**Is the LLM hallucinating facts not in the context?**
- Sim, falha de fidelidade.
  - Temperatura mais baixa
  - Abreviar o contexto (contexto muito irrelevante confunde o modelo)
  - Adicionar um controlo de fidelidade: solicitar uma segunda chamada de LLM para verificar as reivindicações
  - Use a cadeia de pensamentos: "Primeiro, identifique a passagem relevante e depois responda".

**Common failure patterns and fixes:**

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Wrong source retrieved | Vocabulary mismatch | Add BM25, try HyDE |
| Right source, low rank | Imprecise embeddings | Add reranker |
| Answer contradicts context | Hallucination | Lower temp, add faithfulness check |
| Answer too vague | Context too broad | Smaller chunks, parent-child strategy |
| Misses multi-part questions | Single retrieval pass | Decompose query into sub-queries |
| Stale information returned | Index not updated | Re-index changed documents |
| Same chunk retrieved for everything | Chunk too generic | Improve chunking, add metadata filters |

Para cada diagnóstico, forneça:
- A causa raiz específica
- A correcção recomendada com detalhes de execução
- Como verificar a correção funcionou (um teste a executar)
