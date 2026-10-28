---
name: skill-rag-pipeline
description: Build and debug RAG pipelines from first principles
version: 1.0.0
phase: 11
lesson: 6
tags: [rag, retrieval, embeddings, vector-search, llm-engineering]
---

# Padrão de oleoduto RAG

Todos os sistemas RAG seguem este padrão:

```
documents -> chunk -> embed -> store
query -> embed -> search(top_k) -> build_prompt -> generate
```

A indexação acontece uma vez por documento.

## Quando utilizar RAG

- O Mestrado em Direito Jurídico precisa de acesso a documentos privados ou recentes
- A ajuste é demasiado cara ou lenta para atualizar
- Precisas de citar fontes para respostas
- A base de conhecimentos muda frequentemente

## Quando não utilizar RAG

- A resposta é o conhecimento geral que o Mestrado já possui
- A tarefa é criativa (escritura, brainstorming) não factual
- Você precisa do modelo para adotar um estilo de raciocínio específico (utilizar ajuste fino)

## Lista de verificação da execução

1. Documentos fragmentados em 256-512 segmentos de tokens com 50 tokens sobrepostos
2. Embed cada pedaço usando um modelo de embebimento consistente
3. Armazenar embalagens em um banco de dados vetorial com o texto original
4. No momento da consulta, inserir a pergunta do usuário com o mesmo modelo
5. Retirar os pedaços mais semelhantes (5-10) através da semelhança cosínica
6. Crie um prompt: instrução do sistema + contexto recuperado + pergunta do usuário
7. Gerar a resposta, colocando-a no contexto recuperado
8. Retorna a resposta com referências à fonte

## Erros comuns

- Utilização de diferentes modelos de inserção para indexação e consulta (vectores são incompatíveis)
- Peças muito pequenas (perder contexto) ou muito grandes (diluir a relevância)
- Não incluindo a sobreposição entre os blocos (divisões de frases nas fronteiras)
- Esquecer-se de re-indexar quando os documentos mudam
- Retorno de pedaços recuperados para o usuário sem gerar uma resposta coerente
- Não configuração de temperatura=0 para consultas de RAG factuais (temperatura mais alta = mais alucinação)

## Descarga de erros de recuperação

Se não estiverem a ser retiradas as peças certas:
1. Imprimir a consulta de inserção e verificar que não é zero
2. Verifique as semelhanças cosinas manualmente para um pedaço conhecido-relevante
3. Tente reformula-lo para combinar o vocabulário do documento
4. Verificar a correspondência do modelo de incorporação entre o tempo de índice e consulta
5. Verificar se o conteúdo relevante foi perdido durante a fragmentação

## Parâmetros de produção

- Tamanho do pedaço: 256-512 tokens
- Superposição: 50 tokens (10-20% do tamanho da peça)
- Top-k: 5-10 para a maioria dos casos de utilização
- Temperatura: 0 para respostas factuais
- Modelo de incorporação: inserção de texto-3-minor (eficiente em termos de custo) ou inserção de texto-3-grande (mais precisão)
