---
name: elicitation-form-designer
description: Design explicit resource scope and stateless MCP 2026-07-28 elicitation with authorization, safe forms, and signed retry state.
version: 2.0.0
phase: 13
lesson: 12
tags: [mcp, elicitation, mrtr, scope, authorization]
---

Projetar uma etapa de entrada do utilizador para uma operação MCP com foco na revisão do protocolo `2026-07-28`- Não .

Produzir:

1. Contrato de alcance. Coloque o espaço de trabalho, diretório ou URI de recurso em argumentos visíveis de ferramentas ou configuração de servidor.
2. Verificações de fronteiras. Defina a normalização URI, contenção de componentes de caminho, política de ligação simbólica e a caixa de areia do sistema operacional.
3. Condição do gatilho. Nomear a ambiguidade exata, confirmação ou interação externa que requer entrada do usuário.
4. Descoberta e porta de capacidade.`supportedVersions`, capacidades,`ttlMs`, e `cacheScope`de`server/discover`- se as ferramentas são publicitadas, incluir deterministas obrigatórios `tools/list`Descrição com um objeto válido `inputSchema`, metadados de identidade do servidor e sugestões de cache.`elicitation: {}`e explícito.`elicitation.form`rejeitar o suporte faltante ou apenas URL com `-32021`E ...`data.requiredCapabilities.elicitation.form`· utilização `-32022`com exato`supported`E ...`requested`dados para uma versão não suportada.
5. Resultado do MRTR.`resultType: "input_required"`com uma estaca`inputRequests`chave e `elicitation/create`- O pedido.
6. Design de interação. Para o modo de formulário, forneça uma mensagem simples e um esquema plano restrito. Para o modo URL, mostre o destino HTTPS e a regra de conclusão fora da banda.
7. Requer um novo ID JSON-RPC, método original e argumentos, atual `inputResponses`, por pedido `_meta`, e exato `requestState`- É o eco.
   Uma notificação sem id nunca recebe um resultado ou erro JSON-RPC; uma notificação HTTP Streamable aceita recebe `202`Sem corpo.
8. Manutenção de ramo.`accept`- Não .`decline`, e `cancel`para resultados seguros diferentes.
9. Proteção do Estado. Ligue HMAC ou criptografia autenticada ao principal autenticado, digestão de argumento original, conjunto candidato, fase de operação, expiração e não-caso. Consuma o não-caso atomicamente em um limite, TTL-cutado replay loja compartilhada por cada instância de processador.
10. Reverificar a autorização, o estado do registro ao vivo e a contenção imediatamente antes da mutação.

Rejeitos duros:

- Tratar as raízes desatualizadas como autorização, contenção ou sandboxing.
- Usando`roots/list`ou `notifications/roots/list_changed`em um novo projeto de 2026-07-28.
- Enviando um reverso .`elicitation/create`pedido em vez de devolvê-lo através do MRTR.
- Coleta de senhas, chaves de API, tokens de acesso ou credenciais de pagamento no modo formulário.
- Enviar um modo de elicitação ausente das capacidades atuais de solicitação.
- Tratamento`clientInfo`como identidade de utilizador autenticada.
- Realização de uma ação destrutiva antes de uma aceitação validada e de uma verificação final da autorização.
- Não assinado .`requestState`que contenha candidatos ou dados relevantes para a autorização.

Regras de recusa:

- Rejeitar repetidas instruções após um declínio explícito.
- Recusar a obtenção de um valor que o servidor possa derivar ou validar sem o utilizador.
- Recusar um URL que contenha credenciais, segredos de usuário ou um valor de portador pré-authenticado.
- Recusar um pedido que usa o estado de sessão de protocolo oculto,`initialize`, ou `Mcp-Session-Id`- Não .

Faça um desenho de uma página com escopo, autorização, contenção, modo de interação, esquema ou URL, forma de fio MRTR, campos de estado, ramos de resposta, política de repetição e lista de verificação final de revalidação.
