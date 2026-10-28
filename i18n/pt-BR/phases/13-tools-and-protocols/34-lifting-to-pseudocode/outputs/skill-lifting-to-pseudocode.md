---
name: lifting-to-pseudocode
description: Levante uma função compilada para pseudocode com uma derivação para cada linha, e depois conciliá-la com o texto do decompilador.
version: 1.0.0
phase: 13
lesson: 34
tags: [reverse-engineering, decompilation, ir, ssa, structuring, ghidra, rea]
---

Uma função em um arquivo objeto ou executável que você construiu ou está autorizado a analisar, produz duas coisas. Primeiro, pseudocode onde cada linha remonta às instruções. Segundo, uma tabela de diferença contra a saída do decompilador. Use essa habilidade com Claude, Cursor, Codex, OpenClaw, Hermes ou qualquer agente que leia SKILL.md.

## Introduções necessárias

- O ficheiro-alvo, o SHA-256, o compilador e as bandeiras que o produziram, e a autorização escrita para analisá-lo.
- O nome da função ou endereço de entrada e a seção que a mantém.
- Desmontagem de referência `llvm-objdump -d -r` ou a visão de instruções do decompilador.
- Registros de realocação aplicáveis ao organismo de função.
- A convenção de chamada do alvo (Sistema V AMD64 psABI secção 3.2.3 para objetos x86-64 Linux).
- O texto do decompilador para a mesma função, com o nome do fornecedor e a versão, por exemplo, Ghidra 12.1.4 a rea 6.5.0.
- A fonte da função quando o alvo é o seu próprio dispositivo, para a comparação de comportamento.

## Procedimento

1. Decodificar a função de seu primeiro byte para o próximo início da função. Compare cada instrução com a desmontagem de referência por endereço, bytes e texto. Pare com a primeira desacordo.
2. Divida as instruções em blocos básicos em alvos de salto e após cada salto ou retorno. Regista sucessores e antecessores.
3. Levante cada instrução para declarações IR. `flags` Mantém o ponteiro de pilha e o ponteiro de quadro fora do IR e torne os espaços de quadro em locais nomeados.
4. Resolver cada operando RIP-relativo através de sua realocação: alvo = símbolo + adição + a distância do campo de deslocamento até o final da instrução.
5. Tome parâmetros da convenção de chamada. Um registro na sequência de argumentos que é lido antes de qualquer escrita é um parâmetro. O mais alto de tal registro fixa a contagem. Nunca tome um registro salvado por chamada como um parâmetro.
6. Construir SSA: colocar as funções phi na fronteira de domínio iterada das definições de cada variável, então renomear com um andar de árvore dominadora.
7. Simplificar: codes de condição de dobra contra `cmp` e `test`, dobrar lançamentos, transformar cargas escaladas em acessos de elementos, e reconhecer o idioma de divisão multiplicar e deslocar apenas quando o multiplicador é igual ao teto de um poder de dois sobre o divisor e o limite de erro mantém.
8. Substitua um valor em seu único uso quando o uso está no mesmo bloco e nenhuma loja ou chamada fica entre eles. Substitua constantes em qualquer lugar, exceto em uma phi. Remova definições sem usos e sem efeitos colaterais. Repita até que nada mude.
9. Coalize cada phi com seus argumentos em uma variável. Dê nomes de variáveis que mostram o registro ou slot de que vieram. `int` ou `long` de largura e de tipo de ponteiro de utilização como base de carga escalada, e compartilhar o tipo ao longo de cópias.
10. Estrutura: utilizar o post-dominador imediato como a junção de um condicional. `if`- Não . `if` com `else`Detectar os circuitos dos arredores traseiros. `while` Quando o cabeçalho sai e `do while` Quando o bloqueio sair, informe um salto indireto como não resolvido, em vez de adivinhar alvos.
11. Compile o pseudocódio com o triple alvo e `-Wall -Werror`Quando a fonte estiver disponível, compilar a fonte e o pseudocódio em programas separados com um driver e comparar as suas saídas através de uma rede de entrada.
12. Coloque o texto do decompilador ao lado do pseudocód. Para cada linha que diferir, escreva a instrução que explica a diferença, ou escreva que a diferença é uma conjectura do decompilador sem instrução por trás.

## Matriz necessária

Para cada função, informe:

- Nome da função, intervalo de endereços, contagem de instruções, contagem de blocos e contagem de phi
- acordo de decodificação com a desmontagem de referência: cada instrução ou o primeiro endereço que seja diferente
- Cada parâmetro com o seu registo, largura e tipo de dedução
- Cada tabela lida com a sua realocação, o deslocamento de seções, a largura dos elementos e o limite que fixa o seu comprimento
- Cada idioma reconhecido, com a aritmética que o justifica
- cada estrutura emitida (se, se-else, retorno antecipado, enquanto, fazer enquanto, salto indireto não resolvido)
- Compile o resultado e o resultado de comparação de comportamento com a rede de entrada utilizada
- a tabela de diferença contra o decompilador: linha, nosso texto, seu texto, instrução ou adivinhação

## Rejeitos duros

- Confiar em uma assinatura do decompilador, tipo de devolução ou contagem de parâmetros sem verificar o registro lê e escreve atrás dele.
- Tomar um registro salvo de chamadas ou um registro escrito primeiro dentro da função como um parâmetro.
- Dobrar um multiplicador e deslocamento em divisão sem verificar o multiplicador e o limite de erro.
- Adivinhar os alvos de um salto indireto de código próximo.
- Leitura de uma tabela além do próximo endereço referenciado ou do final da seção.
- Substituição de um valor carregado em uma loja ou uma chamada.
- Emissão `goto` para uma forma que `if`- Não . `while`, ou `do while` - Os coberturas.
- A compilação prova a sintaxe, a comparação de comportamento prova a semântica.
- Aceitar a edição de um modelo de refinamento que substitua um desconhecido visível por um campo, tipo, chamada ou guarda inventado.
- Analisar software que não possui ou não está autorizado a analisar.

## Produção

Retorna estas secções:

1. Alvo: arquivo, SHA-256, compilador, bandeiras, autorização.
2. Acordo de decodificador: contagem de instruções e resultado de comparação de referência.
3. Gráfico: blocos, sucessores, dominadores imediatos, loops.
4. IR e SSA: as listas de declarações com versões e funções phi.
5. Pseudocódigo: o texto estruturado com as suas definições de dados.
6. Tipos: cada parâmetro, local e tipo de devolução com a evidência para cada um.
7. Comparação de decompiladores: a tabela de diferença com a instrução ou adivinhação para cada linha.
8. Prova: compilar o resultado e a comparação do comportamento sobre a rede de entrada.
9. Desconhecidos: saltos não resolvidos, realocações não aplicadas, tipos que o código da máquina não pode corrigir.

Terminar com a primeira linha do texto do decompilador que nenhuma instrução suporta. Se cada linha é suportada, indicar a grade de entrada que provou o comportamento igual.
