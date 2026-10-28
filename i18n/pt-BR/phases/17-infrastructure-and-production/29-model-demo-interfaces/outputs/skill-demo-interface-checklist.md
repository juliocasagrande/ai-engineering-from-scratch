---
name: demo-interface-checklist
description: Revisar uma demonstração de modelo antes de seu link ser publicado, verificar o contrato, os comentários, os erros, os controles de links públicos e a privacidade do registro.
version: 1.0.0
phase: 17
lesson: 29
tags: [demo, interface, validation, streaming, rate-limit, privacy, gradio, streamlit]
---

Se tiver uma descrição de um modelo de demonstração ou seu código, revise a demonstração contra a lista de verificação abaixo. Marque cada item PASS, FAIL ou UNKNOWN. Indique evidências para cada marcação: um arquivo e linha, uma configuração ou uma citação da descrição.

Pergunte-lhes estes fatos quando eles estão faltando:

- A chamada de modelo: uma API do provedor ou um modelo local, a latência típica e o custo de uma chamada.
- O público: apenas a equipa, os revisores convidados, ou qualquer pessoa com o link.
- O tipo de entrada e a maior entrada que o modelo aceita.
- Como funciona a demonstração: o framework, o servidor e o host do link.

Lista de verificação:

Contrato

1. A entrada tem um tipo, um tamanho máximo e uma regra para os caracteres de controle.
2. O servidor verifica todos os limites novamente.
3. A demonstração tem pelo menos um exemplo para cada classe de saída.
4. A chamada modelo tem um timeout, e o erro de timeout tem uma dica para o usuário.

Feedback

5. O controlo de submissão é desativado enquanto um pedido é executado.
6. A página mostra que o modelo está a funcionar, com o tempo passado ou uma exibição de progresso.
7. Uma resposta de texto chega como um fluxo, e a página mostra a hora de primeiro token.
8. Uma falha após o início do fluxo chega ao usuário como um evento de erro.

Erros

9. Cada resposta de erro tem um código estável, uma mensagem com os números relevantes, uma sugestão com uma ação e um ID de solicitação.
10. Nenhuma resposta de erro contém um rastro de pilha, um caminho de arquivo ou um segredo.

Linha pública

11. O número de clientes que recebem um pedido rejeitado é de 429 e a taxa de `Retry-After` - O cabeçalho.
12. A chave limite de taxa é correta atrás de um proxy. Um cliente não pode escolher a sua própria chave.
13. Existe um limite de utilização ou um limite de gastos para toda a demonstração, para todos os clientes juntos.
14. O acesso precisa de um token, uma senha ou um login, a menos que o proprietário queira que a demonstração esteja aberta a qualquer pessoa.
15. O limite de taxa e o limite máximo também se aplicam aos endpoints de API criados pelo quadro.
16. A página escreve o modelo de saída como texto, nunca como HTML. `Content-Security-Policy` - O cabeçalho.

Privacidade

17. Os registos não guardam texto de entrada, nenhum URL completo com uma cadeia de consulta e nenhum endereço de cliente bruto.
18. Cada recurso que armazena entrada, como sinalização, histórico ou análise, está desligado, ou a página diz aos usuários sobre isso.
19. A página diz aos usuários o que o servidor guarda.

Sinais de produto

20. Relatar cada um destes sinais que esteja presente:
    - Pessoas fora da equipa usam a demonstração todas as semanas.
    - Alguém pede um alvo de tempo de funcionamento.
    - Os usuários pedem contas, resultados salvos ou histórico.
    - O custo do modelo é uma linha no orçamento.
    - A entrada inclui dados que um contrato ou uma lei abrange.

Produzir:

1. Uma tabela com o número do item, a marca e a prova.
2. Uma lista de correções para cada FAIL, em ordem de risco. Coloque primeiro os itens de ligação pública e privacidade, depois erros, depois contrato, depois feedback. Cada correção nomeia o arquivo, a configuração ou a mudança de código.
3. Uma lista dos sinais de produto que estão presentes. Se um ou mais sinais estiverem presentes, recomende uma mudança para uma pilha de produção.
4. Um veredicto em uma linha: pronto para compartilhar, pronto após as correções listadas, ou passar para a pilha de produção primeiro.

Não marque a demonstração pronta para compartilhar quando qualquer uma destas coisas é verdadeira:

- O servidor não verifica o tamanho da entrada.
- Um link que qualquer pessoa pode abrir não tem limite de taxa ou limite de uso.
- Os registos ou um recurso de framework armazenam o texto de entrada, e a página não diz aos usuários.

Regras de recusa:

- Se o público for desconhecido, trate o link como aberto a qualquer pessoa.
- Se o custo de uma chamada modelo for desconhecido, exigir um limite de utilização antes de uma ligação pública.
- Se a demonstração estiver em execução em uma estrutura, verifique suas definições padrão para sinalização, compartilhamento de links e endpoints automáticos da API. Não presuma que as definições padrão sejam seguras para uma ligação pública.
