---
name: virtual-memory
description: Scaffold a MemGPT-shaped two-tier memory system (main context + archival store + memory tools) for any target runtime with correct eviction, citation, and untrusted-input handling.
version: 1.0.0
phase: 14
lesson: 07
tags: [memory, memgpt, virtual-context, archival, citations]
---

Dado um tempo de execução alvo (Python, Node, Rust), um provedor de modelo (Anthropic, OpenAI, local) e um backend de armazenamento (in-memória, SQLite, vector DB, KV, gráfico), produz um sistema de memória em forma de MemGPT correto.

Produzir:

1. A.`MainContext`Tipo com um `core`O artigo 1.o, n.o 1, do Tratado CEE, estabelece um regime de controlo da segurança social.`messages`Lista (FIFO). Auto-expulso no limite de tamanho; viradas despeladas continuam a ser recuperadas até `conversation_search`- Não .
2. Um `ArchivalStore`Os registos devem ser transportados.`id`- Não .`text`- Não .`tags`- Não .`session_id`- Não .`turn_id`- Não .`created_at`Cada carta devolve a identificação armazenada para citação.
3. Cinco ferramentas de memória que correspondem à superfície MemGPT: `core_memory_append`- Não .`core_memory_replace`- Não .`archival_memory_insert`- Não .`archival_memory_search`- Não .`conversation_search`- Presente-os ao modelo com`description`texto que diga ao modelo quando usar cada um.
4. Um contrato de citação: cada recuperação de arquivo DEVE devolver ids de registro ao lado do texto, e o agente DEVE citá-los nas respostas finais.
5. Um gancho de consolidação (pode ser um no-op em v1) para que os agentes do tempo de sono da lição 08 possam ligar sem re-sanitário.`list_records_since(timestamp)`E ...`delete(id)`- Não .

Rejeitos duros:

- Buscar arquivo com pontuação LLM completa. Use um backend de recuperação adequado (BM25, semelhança vetorial).
- O contexto principal sem política de despejo, o contexto principal sem limites, cresce silenciosamente além da janela.
- Armazenar conteúdo recuperado como se fosse instruções do usuário. Todo o conteúdo do arquivo é texto não confiável (Lessão 27). Passe-o para o modelo como observação, não como um pedido de sistema.
- Escrever um`core_memory_clear`O núcleo é suportável, o despejo é uma arma de pé.`replace`Não .`clear`- Não .

Regras de recusa:

- Se o usuário pedir "sem citações, apenas respostas", recusar para qualquer domínio onde a atribuição de origem é importante (médica, legal, política, financeira). Oferecer um compromisso: citações rendered como notas de rodapé em vez de linhas.
- Se o usuário pedir "escrever todo o conteúdo recuperado de volta ao arquivo sem filtragem", rejeite e aponte para a lição 27.
- Se o tempo de execução não tiver camada de persistência, recuse-se a enviar um agente descrito como tendo "memória de longo prazo".

Output: um arquivo por componente (`main_context.*`- Não .`archival_store.*`- Não .`memory_tools.*`- Não .`agent.*`) mais um `README.md`Explicando a política de despejo, contrato de citação e onde ligar a lição 08 (consolidação do tempo de sono) e a lição 09 (fusão Mem0).
