---
name: mcp-auth-wiring
description: Design MCP 2026-07-28 authorization with issuer-bound enrollment, CIMD, protected-resource metadata, JWKS refresh, audience pinning, and per-request validation.
version: 2.0.0
phase: 13
lesson: 18
tags: [mcp, oauth, cimd, dcr, jwks, rfc8414, rfc7591, rfc8707, rfc7636, rfc9728, rfc9207]
---

Dada uma configuração do servidor MCP e um conjunto de capacidades IdP, emitir as regras de superfície de aut e recusa que constituem uma camada de autorização de produção MCP.

- Input:

- `mcp_resource_url` URL de recurso canônico (identificador mais específico; manter um caminho apenas quando distingue servidores co-hospedados), usado como `aud`e como os metadados de recursos protegidos `resource`- O valor.
- `idp_metadata_url` o IDP `/.well-known/oauth-authorization-server`(ou OpenID Connect Discovery) URL.
- `idp_capabilities`: valores observados para `issuer`- Não .`code_challenge_methods_supported`- Não .`grant_types_supported`- Não .`client_id_metadata_document_supported`, depreciado .`registration_endpoint`- Não .`response_types_supported`, e `authorization_response_iss_parameter_supported`- Não .
- `pre_registered_client_ids`O sistema de identificação de emissores é um sistema de identificação de emissores que é facultativo, fornecido por operadores de servidores de autorização.
- `application_type`- Não .`native`ou `web`, exigido quando a compatibilidade com DCR desatualizada é selecionada.
- `credential_store`: ID de cliente e credenciais de registo teclados pelo emissor do servidor de autorização, com tokens de acesso teclados por `(issuer, mcp_resource_url)`- Não .
- `tools`: a lista de ferramentas de MCP com o âmbito de aplicação requerido por cada uma.

Produzir:

1. **Refusal gate.**Recusar o acoplamento e parar se qualquer condição difícil falhar:
   - `S256`Está faltando de `code_challenge_methods_supported`(PKCE não tem modo degradado).
   - `authorization_code`Está faltando de `grant_types_supported`- Não .
   - `response_types_supported`É qualquer coisa além de exatamente.`["code"]`- Não .
   - Não existe caminho de inscrição: nenhum de pré-registados `client_id`- Não .`client_id_metadata_document_supported: true`, ou um ponto final de compatibilidade DCR desatualizado está disponível.
   - O CIMD é selecionado, mas o seu `client_id`Não é o URL absoluto do documento HTTPS com um caminho, não corresponde ao URL do documento ou o documento não tem um não vazio `client_name`ou `redirect_uris`Array.`application_type`é opcional para a CIMD.
   - Um RFC 9207 devolvido `iss`Diferença do emitente registrado antes da redirecção ou é omitido quando o servidor o anunciou como suportado.
   - Falta DCR depreciado `application_type`, ou a sua política de redirecção de URI entra em conflito com `native`ou `web`- Não .

2. **Protected-resource metadata document**(RFC 9728) para o servidor MCP. Para um recurso com um caminho, insira o segmento conhecido antes desse caminho: `https://host/team/mcp`mapas para `https://host/.well-known/oauth-protected-resource/team/mcp`Incluir`resource`- Não .`authorization_servers`(lista de autorização do emitente), `scopes_supported`, e `bearer_methods_supported: ["header"]`- Não .

3. **HTTP endpoints.**
   - `GET /.well-known/oauth-protected-resource` Retorna o documento a partir de (2).
   - `POST /mcp`(transporte de MCP sem Estado): valida o token do portador para este pedido antes de qualquer remessa de ferramentas.
   - Apenas compatibilidade com DCR: `POST /register`, com antecedência de um controlo do tipo de pedido e de um controlo do limite de taxa.

4. **Background job + routines.**
   - Um atualização programada da JWKS que retorna .`jwks_uri`no cache .`{keys, fetched_at}`- Idempotent; nunca coleta chaves. O AS gira; o servidor de recursos apenas atualiza.`0 */6 * * *`· Apertar para `*/15 * * * *`para IPI de alta rotação.
   - A.`validate`- verificação de rotina`iss`lista de permitimentos, assinatura contra JWKS em cache, `aud == mcp_resource_url`- Não .`exp`, o âmbito necessário.
   - Um caminho de emissão intensivo  somente se a lista de ferramentas contém operações bloqueadas por um âmbito que o utilizador não concede inicialmente.

5. **Cache plan.**Uma entrada por emissor aceito , selecionada por `issuer`, de detenção`{keys, fetched_at}`. Documente o padrão de leitura: o validador lê o cache e volta a uma única atualização sincrônica em `kid`miss (re-receber, não girar  re-receber é idempotente e não pode ser transformado em um DoS de criação de chaves).

6. **Scope mapping.**Mapear cada ferramenta para o escopo que ela requer.
   `| tool | required_scope | rationale |`- Agrupar as ferramentas destrutivas sob o seu próprio âmbito de aplicação; nunca reutilizar um âmbito de leitura para uma ferramenta de escrita.

7. **Refusal rules at runtime**(o validador deve codificar estes elementos):
   - Rejeitar quando`aud != mcp_resource_url`→ 401 `Bearer error="invalid_token", error_description="audience mismatch", resource_metadata="<prm_url>"`- Não .
   - Rejeitar quando`iss not in authorization_servers`- Não .
   - Rejeitar quando`kid`Não em JWKS em cache após uma única re-recorrida.
   - Rejeitar quando o âmbito requerido estiver ausente → 403 `Bearer error="insufficient_scope", scope="<required>", resource_metadata="<prm_url>"`- Não .
   - Rejeitar qualquer pedido de autorização sem um S256 `code_challenge`, e rejeitar qualquer pedido simbólico cujo`code_verifier`, cliente, redirecionamento URI, ou `resource`Não corresponde ao registro de código de autorização única.
   - Rejeitar qualquer credencial ou token cujo emissor não corresponda à sua chave de loja de credenciais.

Rejeitos duros (nunca enviar nenhum destes  recusar o pedido e documentar o porquê):

- Armazenamento`client_secret`Em texto simples.`token_endpoint_auth_method: none`; clientes confidenciais utilizam `private_key_jwt`Não há segredos compartilhados em texto claro em repouso ou nos registos de resposta ao registo.
- Salto o `aud`Verifique o validador. A vinculação ao público (restrição de privilégios de acesso a tokens) é a razão completa para RFC 8707 + RFC 9728.
- A transferência do JWKS para um "rotate-and-mint" em vez de um "re-fetch".`kid`E deixa o atacante controlado .`kid`O retorno deve ser o refresco idempotente.
- Permitir solicitações de código de autorização de PKCE-less. OAuth 2.1 proíbe isso; o validador deve rejeitar qualquer `/token`A taxa de câmbio de código de autorização não é de`code_challenge`- Não .
- Cachar JWKS sem um trabalho de atualização.
- Confiando no`iss`Qualquer validador que aceite um token de qualquer`iss`Deixa um atacante criar o seu próprio IDP e falsificar tokens.
- Enviar o token MCP entrante para uma API upstream (passthrough token). Se o servidor MCP chamar APIs upstream, ele DEVE obter seu próprio token separado; passthrough cria o problema de confusão-deputado.
- Armazenamento`registration_access_token`Hash-at-rest; exigir texto claro em cada atualização.
- Tratar os metadados de solicitação MCP ou uma sessão de protocolo removido como estado de autorização. O transporte 2026-07-28 é estatal; autenticar e autorizar cada solicitação.

Resultado: um plano de uma página com o documento de recurso protegido, layout de inscrição de chave do emissor, layout de token de emissor e recurso, caminho de inscrição escolhido, endpoints HTTP, trabalho de atualização JWKS, mapeamento de alcance e regras de recusa de tempo de execução. Termina com o primeiro portal de implantação não atendido encontrado nos metadados reais do servidor de autorização.
