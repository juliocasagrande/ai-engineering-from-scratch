---
name: mcp-contract-reviewer
description: Review MCP tool descriptors, results, pagination, completions, and parameter-header policy before exposing tools to a model.
version: 1.0.0
phase: 13
lesson: 28
tags: [mcp, tools, json-schema, pagination, completion, security]
---

Revisar a superfície da ferramenta MCP fornecida em relação à versão do protocolo `2026-07-28`- Não .

Pergunte se estão ausentes:

1. O completo`tools/list`páginas de descrição, incluindo todas `nextCursor`campo.
2. Pelo menos um resultado bem sucedido e um resultado falhado por ferramenta.
3. O mapeamento de cabeçalho de parâmetro HTTP Streamable, se usado.
4. Referências de conclusão, aulas de chamadores e sugestões de exemplo.
5. O contexto de autorização que pode alterar o conjunto de ferramentas visíveis.

Produza um relatório compacto com estas secções.

## Admissão de descriptores

Para cada instrumento:

- Verificar um nome estável não vazio;
- exigir um objeto `inputSchema`O artigo 2.o
- Identificar o dialeto JSON Schema, que é padrão para 2020-12 quando omitido;
- validar `outputSchema`quando estiver presente;
- Lista as anotações como indicações não confiáveis, e não como política;
- Retorno`ADMIT`- Não .`REJECT`, ou `CONDITIONAL`com uma razão precisa.

Rejeitar um descritivo mal formado sem rejeitar ferramentas válidas não relacionadas.

## Contrato de resultados

Para cada resultado completo, incluindo um com `isError: true`- Não .

- exigir`resultType: complete`O artigo 2.o
- validar cada bloco de conteúdo por tipo;
- Tratamento`structuredContent`como qualquer valor JSON, não apenas para objeto;
- exigir`structuredContent`e conformidade com `outputSchema`quando existe;
- Requer um bloco de texto de compatibilidade para resultados estruturados;
- distinguir os links de recursos dos recursos incorporados;
- limites de tamanho do estado e tipo de mídia.

Classificar solicitações mal formadas como erros JSON-RPC. Classificar execução acionável
falhas como resultados completos com `isError: true`, sem contornar o
contrato de produção publicado.

## Tópicos de parâmetros

Por cada um .`x-mcp-header`- Não .

- Requer um token de nome de campo HTTP válido e não vazio;
- exigir uma singularidade insensible ao caso;
- Requerem string, inteiro ou tipo booleano;
- atravessar todo o esquema de entrada, incluindo propriedades aninhadas, combinadores,
  elementos do conjunto e definições utilizadas por `$ref`O artigo 2.o
- permitir a anotação apenas em um directo `inputSchema.properties`membro e
  rejeitar todas as anotações encontradas em outros lugares ou em`outputSchema`O artigo 2.o
- rejeitar`number`e valores inteiros fora `-9007199254740991`através
  `9007199254740991`O artigo 2.o
- Rejeitar os campos de credenciais, tokens, segredos, senhas, autorizações e PII por política de implantação;
- Transmitir um valor claramente apenas quando não é um ASCII visível em branco e
  Não começa com `=?base64?`O artigo 2.o
- emite exactamente`=?base64?{Base64UTF8}?=`sem corte ou
  Normalização do valor original;
- codificar Unicode, vazio, espaço branco, controle, CR ou LF, enchido, e
  As cadeias de sentinela e os booleanos como texto minúsculo;
- na fronteira HTTP, decodificação reconhecida `Mcp-Param-*`valores, cabeçalho de comparação
  Nomear valores insensivelmente para casos e decodificar exactamente com o corpo JSON, e
  rejeitar uma cópia que falte, seja duplicada, seja inesperada, seja malformada ou seja incompatível com a
  HTTP `400`+ JSON-RPC `-32020`O artigo 2.o
- Registre o nome final do cabeçalho e a categoria de rejeição, nunca o valor do argumento
  ou carga útil codificada.

## Paginação

Rastrear todas as solicitações de lista. Continuar sempre que`nextCursor`Não é presente e não é nula, inclusive quando é uma cadeia vazia. Nunca decodifique, modifique, incremente, ordene ou derive significado de um cursor. Relate ferramentas duplicadas, páginas faltantes e ordenação instável.

## Completamento

Para cada referência de recurso ou de resposta:

- validar a referência e o argumento;
- Filtrar as sugestões através da autorização do telefonista;
- O limite do resultado é de 100 valores;
- Definir limites de devolução do cliente e de taxa de servidor;
- Teste que os nomes ocultos dos inquilinos, recursos e ambientes não se filtrem.

## Matriz de verificação

Retorna pelo menos estes cheques:

| Check | Fixture | Expected result |
|------|---------|-----------------|
| Non-object structured output | Valid array, scalar, or null schema | Accepted when conforming |
| Output mismatch | Wrong JSON type or missing property | Rejected before model use |
| Error output mismatch | `isError: true` with missing or invalid structured content | Rejected before model use |
| Empty cursor | `nextCursor: ""` | Follow-up request sends the exact cursor |
| Unsafe header | Token or invalid field name | Descriptor rejected |
| Nested header annotation | `oneOf`, `items`, nested object, or `$ref` definition | Descriptor rejected during full-tree admission |
| Encoded header values | Unicode, newline, padding, or sentinel-looking text | Exact base64 UTF-8 sentinel round-trips the original value |
| Integer header values | Both safe bounds and one value beyond each bound | Safe bounds pass; unsafe values are rejected |
| Header and body parity | Case variant, missing copy, and decoded mismatch | Case variant passes; missing or mismatch returns HTTP 400 and JSON-RPC -32020 |
| Mixed content | Text, media, link, embedded resource | Each block validated independently |
| Completion isolation | Low-privilege caller | No privileged suggestion returned |
| Error layering | Unknown tool and business failure | JSON-RPC error and `isError: true` remain distinct |

Recusar aprovação quando a evidência inclui apenas uma chamada de ferramenta bem-sucedida. Requer páginas de descoberta, decisões de admissão e fixações de resultados validadas.
