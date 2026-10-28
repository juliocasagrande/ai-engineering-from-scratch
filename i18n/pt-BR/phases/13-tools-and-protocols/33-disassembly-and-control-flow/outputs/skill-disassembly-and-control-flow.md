---
name: disassembly-and-control-flow
description: Transforme um arquivo de objeto e um nome de função em uma listagem verificada, blocos básicos, bordas digitalizadas, dominadores e um registro de cada transferência não resolvida.
version: 1.0.0
phase: 13
lesson: 33
tags: [reverse-engineering, x86-64, disassembly, control-flow-graph, dominators, jump-tables, relocations]
---

Dado um objeto x86-64 relocable ou ligado que você construiu e uma função nele, produzir um desmonte cujas fronteiras de instruções são verificadas, um gráfico de fluxo de controle cujas bordas carregam suas evidências, e uma lista do que permaneceu desconhecido.

## Introduções necessárias

- O arquivo objeto e o compilador exato e o comando que o produziram.
- Uma lista de referência de `llvm-objdump -d` Capturado do mesmo objeto e armazenado ao lado dele.
- O nome da função ou endereço de entrada, e a seção que contém o código.
- A tabela de símbolos com tamanhos de função e a `.rela.*` Seções em que o objeto não está ligado.
- O decodificador da lição 33 (`code/main.py`) ou um equivalente que se eleva num código op desconhecido.

## Procedimento

1. Execute o decodificador como uma varredura linear em toda a seção de código e compare cada instrução com a lista de referência por endereço, bytes e texto. Pare e corrija o decodificador na primeira descoincidência. Registre a contagem de instruções que concordou.
2. Execute descida recursiva da entrada da função com a extensão da função como limite. Registre a ordem de visitas, os conflitos e cada salto indireto ou chamada não resolvido com seu endereço.
3. Para cada salto indireto não resolvido, corresponder ao idioma da mesa: o registo o salto lê, o `add` que o produziu, a carga indexada, a relação entre o período de inquérito e o período de inquérito `lea`- E as fronteiras verificam. `lea` através da sua realocação com `S + A + (end - P)`Leia as entradas . `.rela.rodata` Quando o objeto é realocavel, ou dos bytes quando está ligado.
4. Repete a descida com as tabelas recuperadas e construa blocos básicos: líderes são a entrada, cada alvo direto ou de mesa e cada instrução após uma transferência. `fallthrough`- Não . `taken`- Não . `jump`, ou `table`- Não .
5. Compute dominadores imediatos com o algoritmo iterativo na ordem posterior inversa. Enumere as bordas traseiras como loops.
6. Classificar o segundo grupo como padding ou dados e o terceiro como inacessível ou faltante.
7. Procure cargas através de um RIP-relativo `lea` A taxa de variação de carga é a taxa de variação de carga, que não alimenta um salto.
8. Escreva cada transferência indireta, conflito e byte não codificável restante como desconhecido com seu endereço e os bytes que viu.

## Relatório necessário

Para a função, informe:

- nome do objeto, compilador, comando de construção e caminho de listagem de referência
- acordo do oráculo conforme acordado sobre instruções comparadas
- Conta de instruções sob o varredor, a descida plana e a descida com tabelas
- Lista de blocos com início, fim e contagem de instruções
- Lista de bordas com tipo e, para `table` em bordas, a realocação ou o offset em bytes que produziram o alvo
- Dominar imediatamente de cada bloco e das bordas traseiras
- Contabilidade de bytes: código reclamado, enchimento reclamado pela varredura, bytes de dados, bytes nunca alcançados
- Cada tabela com secção, compensação, tamanho da entrada, contagem, entradas e tipo de evidência
- Todos os desconhecidos com endereço, bytes e a razão pela qual a análise parou

## Rejeitos duros

- Confiar numa lista porque cada byte foi decodificado.
- Tratamento de acordo com `llvm-objdump` O oráculo é um varredão linear.
- Imagino um código optico que o decodificador não sabe, em vez de levantar.
- Lendo mais de 15 bytes para uma instrução ou lendo além da parte final.
- Resolver um operando relativo ao RIP sem adicionar a distância do campo de realocação ao final da instrução.
- Lendo uma tabela de salto a partir de bytes zero em um objeto realojável em vez de de suas realocações.
- Relatar uma tabela de valores como uma tabela de salto, ou uma tabela de salto como código morto.
- A retirada de uma transferência indireta não resolvida do relatório.
- Contando o enchimento após a última volta como código de função.
- Computação dominadores sobre blocos que a entrada não pode alcançar.
- Capturar o oráculo a partir de um compilador ou objeto diferente do que o analisado.

## Produção

Retorna estas secções:

1. Oracle: instruções comparadas, instruções acordadas, primeiro desajuste, se houver.
2. Métodos: instrução e byte contam para varrer, descer e descer com tabelas.
3. Blocks and Edges: o gráfico digitado com a evidência de cada borda da mesa.
4. Dominatores e Loops: a mesa do dominador imediato e as bordas traseiras.
5. Tabelas: tabelas de salto e tabelas de valores com entradas e tipo de evidência.
6. Contabilidade de bytes: reivindicados, enchidos, dados, não alcançados, com intervalos de endereços.
7. Desconhecidos: cada endereço onde a análise parou e porquê.

Se não houver nenhum, indique o número de acordo do oráculo e o número de alvos da mesa comprovados pela realocação.
