---
name: mcp-conformance-release-gate
description: Construir uma matriz de conformidade com o MCP e tomar uma decisão de promoção, suspensão ou rebote baseada em evidências.
version: 1.0.0
phase: 13
lesson: 31
tags: [mcp, conformance, versioning, transcripts, proxy, operations]
---

Dado um cliente, servidor, gateway, SDK ou mudança de transporte do MCP, produzir um conjunto de conformidade de nível de fio e uma decisão de liberação com evidências editadas.

## Introduções necessárias

- Apoiava versões de protocolo modernas e antigas e a política para cada alvo de implantação.
- Pontos de captura de solicitações e respostas brutos antes da decodificação do SDK.
- cabeçalhos HTTP espelhados, corpos JSON-RPC, status, tipos de conteúdo e topologia intermediária.
- Capacidades de cliente, servidor e extensão publicitadas.
- Nomes, versões, valores normalizados e exceções do SDK.
- Os limites de saúde, a janela de canários, o número mínimo de amostras e as medições de referência.
- Versão de reabastecimento exata, digestão de provas de admissão, artefatos e pinos de descrição SHA-256, estado do Registo, estado atual, sinais de liberação confiáveis e uma certificação sobre a carga útil completa de reabastecimento.
- Política de redacção, retenção e acesso à evidência.

## Procedimento

1. Defina eras de protocolo explícito. `io.modelcontextprotocol/protocolVersion` e `io.modelcontextprotocol/clientCapabilities` Coloque o comportamento da era da inicialização através de `2025-11-25` num adaptador antigo separado.
2. Escolha uma política de retrocesso rigorosa ou limitada por alvo. `server/discover` O resultado é um erro moderno reconhecido que prova o ramo moderno. Uma resposta de tempo ou vazia não prova nada. Permitir uma sonda legada apenas para um endpoint configurado ou permitido, então selecionar legado apenas após validar um positivo `initialize` resultado para a revisão de legado fixado. Nunca rebaixar após `-32020`- Não . `-32021`, ou `-32022`- Não .
3. Crie transcrições douradas para pedidos aceitos, resultados válidos específicos de método, resultados de extensão anunciados, comportamento selecionado e a invariante de notificação sem resposta.
4. Crie transcrições negativas para envelopes mal formados, versão de resposta ou não-conformidade de ID, exclusividade de resultado e erro, erros mal formados, mapeamento HTTP incorreto, falta de metadados, falta de encaixe e corpos, falta de resposta de erro de servidor, versão não suportada, falta de modernos `resultType`, cargas úteis de métodos mal formados, tipos de resultados desconhecidos ou não publicitados e respostas de notificação proibidas. `HeaderMismatch`, exigir e validar estruturalmente o HTTP 400 JSON-RPC real `-32020` A única exceção local nunca passa por esse caso.
5. Validar os tipos de metadados JSON-RPC primeiro. Combine os nomes de cabeçalhos HTTP de forma insensible a casos, rejeite duplicados conflitantes, decode o sentinela Base64 exato para inseguro `Mcp-Name` valores, em seguida, comparar `MCP-Protocol-Version`- Não . `Mcp-Method`, e aplicável `Mcp-Name` Tratar o espaço branco anterior ou posterior como inseguro e rejeitá-lo quando enviado crudo, mesmo que seja igual ao valor do corpo.
6. Aceitar conhecido moderno `complete` e `input_required` Resultados. Aceitar um discriminador de extensão apenas quando a sua capacidade foi anunciada. Rejeitar todos os desconhecidos ou não anunciados `resultType`.Em seguida, valida a carga útil do método, incluindo descrições completas de ferramentas para `tools/list`, campos de ciclo de vida necessários para um resultado de tarefa, e um objeto de conclusão de valores de cadeia de limites para `completion/complete`- Não .
7. Preservar o resultado do aditivo bruto e `_meta` Decidir explicitamente se cada componente pode ignorá-los ou deve encaminhá-los.
8. Execute todas as transcrições de alto risco através de cada SDK enviado. Compare a semântica de fio bruto com o valor de retorno normalizado e informe todos os campos sintetizados, levantados, despojados ou alterados.
9. Execute o conjunto diretamente e através de todos os intermediários de produção. Capture redactado entrada, origem e evidências de saída. Detectar colapso de status, JSON-RPC reescrever corpo, encaminhamento de cabeçalho desajuste, tampão e mudanças de negociação de conteúdo.
10. Aplique a redação antes da serialização, hashing, registro ou upload. Case-fold campos e nomes de cabeçalhos e remova os separadores para camelCase, variantes com fitas, sublinhados e pontilhados compartilhar a denilista, em seguida, remova credenciais como `Authorization`- Não . `Set-Cookie`- Não . `X-Api-Key`- Não . `accessToken`- Não . `clientSecret`, e `registrationAccessToken` - E há argumentos sensíveis específicos de métodos.
11. Avalie o candidato em relação a transcrição determinista não vazia, diferencial SDK e evidência de proxy, além de uma janela de saúde pré-declarada com uma contagem mínima de amostras positiva. Requer digestões de evidências válidas de todas as fontes. Um limite omitido é um gate falhado, não uma lista vazia passando.
12. Verifique um alvo de retrocesso exato admitido, fixado, ativo e saudável antes da promoção. Validear os tipos exatos de campos e digestões SHA-256, em seguida, verifique criptograficamente sua certificação contra uma identidade de controle de liberação confiável. Promover apenas quando a prova de conformidade, SDK, proxy, saúde e prontidão de retrocesso passar. Em caso de fracasso do candidato, volte apenas para esse alvo verificado. Caso contrário, mantenha.

## Matriz necessária

Para cada caso, informe:

- Nome do caso estável e invariante normativo
- Era do protocolo e evidências de seleção
- cliente, servidor, SDK, proxy e versões de construção
- estado esperado, forma da resposta, tipo de resultado ou código de erro
- Digestões de evidências de entrada, origem e saída observadas
- Diferenças de normalização do KSD
- passar ou falhar em cada limite
- versão da política de redação
- Código de razão final

Incluir, como mínimo, os seguintes casos:

- Descoberta moderna ou chamada de método
- Resultado completo conhecido de ouro com um campo aditivo
- O legado dourado desapareceu. `resultType` na era do legado selecionado
- resultado de extensão anunciado em ouro
- Valido em ouro `completion/complete` Resultado
- notificação de ouro sem resposta JSON-RPC
- Descoincidência negativa entre cabeçalho e corpo
- Capacidades negativas faltantes
- versão correspondente não suportada negativa
- Negativo falta moderno `resultType`
- Negativo desconhecido ou não anunciado `resultType`
- status de proxy negativo ou transformação corporal
- Perda de campo semântico SDK negativo
- Negativo deformado `completion/complete` Resultado

## Rejeitos duros

- A reivindicação de conformidade dos valores de devolução do SDK sem provas de fio bruto.
- Um parser que aceita silenciosamente formas modernas e antigas.
- Retorno herdado após um erro moderno reconhecido.
- O retorno baseado apenas em um timeout, silêncio, fechamento da ligação ou uma resposta não reconhecida.
- Passar um caso de solicitação negativa sem capturar e validar a resposta de erro do servidor.
- Fazer HTTP 400 JSON-RPC `-32020` prova opcional após local `HeaderMismatch` detecção.
- Inferir completo para um desaparecido `resultType` antes de escolher uma era legada.
- Tratar um discriminador desconhecido como completo.
- Rejeitar todos os campos aditivos desconhecidos sem razão de campo reservado.
- Envio de qualquer resposta JSON-RPC a uma notificação.
- Aceitar um conhecido `resultType` sem validar a carga útil específica do método.
- Autorizar cabeçalhos espelhados sem verificar a igualdade com o corpo.
- Tratar nomes de campos HTTP como sensíveis a casos ou comparar um código `Mcp-Name` Sem a descodificação exacta do Sentinela.
- Aceitar um produto bruto `Mcp-Name` com espaço branco anterior ou posterior, em vez de exigir codificação sentinela.
- Aceitar um resultado de conclusão sem um objeto de conclusão de valores de cadeia de limites válido.
- Tratar um 500 gerado por proxy como equivalente a um erro de protocolo de origem.
- Escrever tokens, cookies, segredos ou argumentos sensíveis como evidências.
- Usando a normalização de redação que permite que camelCase ou variantes separadoras contornem o denilista de credenciais canônicos.
- Declarando um canário com zero amostras saudável.
- Tratar transcrição vazia, SDK ou provas de proxy como um limite de passagem.
- Tratar as cordas verdadeiras ou um dicionário de reversão não autenticado como evidência verificada.
- Voltar para uma versão sem admissão exata, pin, status e evidências de saúde.
- Promover um candidato à produção antes de provar um objetivo de retrocesso saudável.

## Produção

Retorna estas secções:

1. Política da Era: provas modernas, alvos rigorosos, gatilhos limitados de retrocesso e sinais proibidos de rebaixamento.
2. Matriz de transcrição: casos de ouro e negativos com resultados esperados.
3. Compatibilidade dos resultados: discriminadores principais, extensões publicitárias, política de campo aditivo e limite de inferência legado.
4. Diferencial SDK: digestões crudas e normalizadas mais campos levantados, despojados, sintetizados e alterados.
5. Evidências de proxy: entrada, origem e saída de resultados com o salto exato falhado.
6. Relatório de redação: versão de política, removidas classes de campo e digestão de evidências editada.
7. Figura de saúde: amostras, taxa de erro, latência, saturação, duração, limiares e comparação de linha de base.
8. Proof of rollback: destino exato, digestão de admissão, pinos, estado do Registo, saúde, identidade do signatário, atestado verificado e plano de restauração da rota.
9. Decisão: `promote`- Não . `hold`, ou `rollback`, com códigos de razão estáveis e a digestão completa das provas.

Se todos os limites forem superados, indicar a condição de conclusão do canário que autoriza a promoção total.
