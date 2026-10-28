---
name: binary-diffing-and-symbolic-execution
description: Match the functions of two builds you compiled with staged signatures and stated confidence, explain every unmatched or changed function, and solve for the inputs that reach a chosen path with a bounded search and a production solver.
version: 1.0.0
phase: 13
lesson: 44
tags: [reverse-engineering, binary-diffing, function-matching, relocations, symbolic-execution, constraint-solving, angr, z3, ghidra, radare2]
---

Dados dois objetos x86-64 relocáveis ou ligados que você construiu, suas listas de referência e uma função cujas entradas você quer, produzem uma diferença de nível de função cuja cada correspondência nomeia a assinatura que a produziu e um relatório de caminho cuja cada folha carrega uma entrada resolvida. Use essa habilidade com Claude, Cursor, Codex, OpenClaw, Hermes ou qualquer agente que leia SKILL.md.

## Introduções necessárias

- Dois objetos, o compilador e comando exatos para cada um, e o SHA-256 de cada um.
- Uma lista de referência de `llvm-objdump -d`para cada objeto, capturado a partir dos mesmos bytes.
- As tabelas de símbolos com tamanhos de função e o `.rela.*`Seções em que os objetos não estão ligados.
- A lição 44 é diferente (`code/main.py`) ou um equivalente que lê bytes, relocalizações, mnemônicos e blocos.
- Para a tarefa de resolução: o IR da função da lição 34 ou um elevador manual com um endereço de instrução por instrução, as largura dos parâmetros e as tabelas de concreto que a função lê.
- Opcionais: radiff2, Ghidra com localização de versão, angr e z3 para as verificações cruzadas.

## Procedimento

1. Verifique cada listagem contra o objeto byte por byte. Pare na primeira desajuste. Uma listagem obsoleta é uma fixação alterada.
2. Construir um registro por função: bytes, bytes com campos de realocação zerados, sequência mnemônica, blocos básicos acessíveis com bordas digitalizadas, alvos de tabela de salto de `.rela.rodata`, e a mesa a`lea`pontos de realocação quando existem uma verificação de limites e uma carga indexada.
3. Execute os estágios em ordem e registre o estágio que produziu cada partida: bytes exatos, bytes mascarados, mnemônicos, forma do gráfico de fluxo, nomes. Uma assinatura coincide apenas quando seu valor é único em ambos os lados.
4. Repete os estágios com nomes em segundo lugar quando existem símbolos. Compare os dois conjuntos de correspondências. Uma correspondência estrutural que a etapa de nome contradiz é uma correspondência falsa; relate-a com a forma que a causou.
5. Para cada coincidência, compare as tabelas referenciadas. O mesmo código com constantes diferentes é uma função modificada.
6. Repita a diferença nas imagens carregadas: estabeleça as secções atribuídas, aplique `S + A - P`para cada campo relativo ao PC e `S + A`Uma função que coincide em bytes exatos nos objetos e apenas em bytes mascarados nas imagens movidas em relação aos seus dados.
7. Calcule uma semelhança para cada par como `1 - levenshtein / max(len)`Quando comparado com o radiff2, indique se foram aplicadas mudanças, porque a impressão digital muda.
8. Para a função a resolver: enumerar caminhos sobre o IR, adicionar cada condição de ramo ao caminho e soltar um garfo que o resolvedor não pode satisfazer.
9. Resolva cada folha para as entradas que deseja: um valor de retorno, um bloco alcançado ou uma igualdade entre duas construções.
10. Quando um solvente de produção estiver disponível, execute as mesmas consultas através do angr ou z3 e compare os limites de classe, satisfação e os modelos. Avalie cada modelo com o avaliador de IR antes de relatá-lo.

## Output

Para a diferença, informe:

- nomes de objetos, compilador, comandos, hashes e arquivos de listagem
- Por função: tamanho, número de instruções, blocos, bordas, relocalizações e as cinco assinaturas
- Lista de jogos com estágio, qualidade, assinaturas de acordo, semelhança, acordo de nome e igualdade de tabela
- funções inigualáveis de cada lado com o candidato mais próximo e a sua semelhança
- Os resultados da visão de objeto e da visão de imagem lado a lado, com o layout da seção e a mudança de deslocamento
- a tabela de comparação de ferramentas: seu estágio, veredicto e proporção de radiff2, correlatores Ghidra que coincidem

Para a resolução, informe:

- O IR com um endereço de instrução por declaração e a verificação de que cobre a lista uma vez
- a lista de caminhos com rastreamento, condição, expressão de devolução e status (retornado ou truncado)
- por folha: contagem de entrada resolvida, mínimo, máximo, amostra e limite utilizado
- A resposta do solvente de produção à mesma pergunta e se as classes concordam
- O limite de loop ou o limite de passo e quantos caminhos ele corta

## Modos de falha

- Confidando um hash de byte em uma imagem carregada.
- Confiar em um hash mascarado em um objeto relocable. os campos já são zero, então mascarar nada muda e os registros de relocalização e as constantes referenciadas carregam a diferença.
- Aceitar uma correspondência de forma de fluxo sem uma segunda assinatura.
- Execução de estágios estruturais antes dos nomes em uma construção com símbolos e, em seguida, não verificar o resultado contra os nomes.
- Comparando uma relação de similaridade com a relação de uma ferramenta sem os mesmos bytes. radiff2 digita os blocos encontrados pela análise e a contagem muda quando se aplicam as mudanças.
- Relatório de um modelo de solvente como entrada. É um modelo; outro solvente retorna outro.
- A correr num ciclo simbólico sem limite ou chapéu e à espera.
- Relatar um resultado de pesquisa limitado como insatisfatível.
- Alegando acordo com uma ferramenta que não executou. Descreva ferramentas fechadas de sua documentação e diga isso.
