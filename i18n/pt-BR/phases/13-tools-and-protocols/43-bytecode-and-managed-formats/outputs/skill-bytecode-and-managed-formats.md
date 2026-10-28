---
name: bytecode-and-managed-formats
description: Read a .pyc, a JVM class file, a .NET assembly, or a WebAssembly module from its header to its instructions, check the reading against the format's own tool, and report which names, types, and control structure the container keeps.
version: 1.0.0
phase: 13
lesson: 43
tags: [reverse-engineering, bytecode, cpython, pyc, jvm, class-file, ecma-335, cil, webassembly, metadata]
---

Dado um contêiner de código de byte que você próprio construiu, produzir um relatório de cabeçalho, uma lista de uma função, e uma tabela do que o contêiner armazena ao lado das instruções. Use esta habilidade com Claude, Cursor, Codex, OpenClaw, Hermes, ou qualquer agente que leia SKILL.md.

## Introduções necessárias

- O arquivo de código de byte e a versão exata do compilador, intérprete ou assemblador e comando que o produziram.
- A fonte de onde foi construída, mantida ao lado dela.
- Uma lista de referência da própria ferramenta do formato capturada a partir do mesmo arquivo: `python3.N -m dis`para um pyc, `javap -c -p`para um ficheiro de classe, `wasm-objdump -h -x -d`para um módulo, um depósito de dados de sistema.reflexão.metadados ou `ilspycmd -il`Para uma reunião.
- Os leitores da lição 43 (`code/main.py`) ou equivalentes que aumentam em um código de tipo, código op ou tabela desconhecido.
- A função para relatar.

## Procedimento

1. Identificar o recipiente a partir de seus primeiros bytes: dois bytes então `0d 0a`é um pyc, `ca fe ba be`é um arquivo de classe, `00 61 73 6d`é um módulo de Wassm, `4d 5a`com o conjunto de dados do diretório 14 é uma montagem .NET. Pare se nenhuma coincide.
2. Leia o cabeçalho e anote os fatos da versão: pyc palavra mágica e bandeiras, classe maior e menor versão, versão binária Wasm, versão de tempo de execução CLI e cadeia de versão de metadados.
3. Um módulo dá suas seções, tipos, importações, exportações, corpos de código, dados e qualquer seção de nome. Uma montagem dá os fluxos, as linhas de tabela contam, as linhas TypeDef, MethodDef, Param e Field, e os corpos de método.
4. Desmontar a função escolhida.`dis`Só quando o intérprete em execução escrever o arquivo, use a listagem capturada do intérprete correspondente.
5. Compare a listagem com a referência por offset, bytes e mnemonic. Pare e corrija o leitor na primeira descoincidência. Registre a contagem que concordou.
6. Preencha a tabela de dados para a função: nome da função, nomes de parâmetros, tipos de parâmetros, tipo de devolução, nomes locais, números de linhas, tamanho do corpo e forma do fluxo de controle (salto, instrução de interrupção, blocos aninhados).
7. Escreva quais fatos o contêiner perdeu e onde eles teriam vivido: o PDB para nomes locais .NET, a seção de nome personalizado para nomes Wasm, `javac -g`para nomes locais da JVM, DWARF para código nativo.
8. Antes de executar qualquer decompilador, verifique se o teto da versão documentada cobre a versão de cabeçalho a partir da etapa 2.

## Relatório necessário

- Container, versão do produtor, comando build e comando de listagem de referência
- Header fatos com os bytes crus eles vieram de
- Acordo de referência conforme acordado sobre linhas comparadas
- a lista de funções com offsets, bytes e texto
- A tabela de dados com a informação mantida ou perdida para cada linha e a prova para cada linha
- Os decompiladores considerados, os limites de versão dos mesmos e se o ficheiro está dentro deles
- Cada faixa de byte que o leitor não pode interpretar, com o seu offset

## Rejeitos duros

- Adivinhar a versão do produtor do nome do arquivo em vez dos bytes de cabeçalho.
- Lista de instruções de pc com o `dis`Modulo de uma versão diferente de intérprete.
- Leia um arquivo de classe alvo ramo em relação à próxima instrução. JVMS faz com que seja relativo ao código optical ramo.
- Salto do enchimento de alinhamento antes `tableswitch`E ...`lookupswitch`- Não .
- Tratar um nome de exportação de Wasm como um nome de variável local, ou uma seção de nome faltante como um binário despojado.
- Ler um token .NET sem verificar o byte da tabela, ou dimensionar uma linha de tabela sem os bits Heap Sizes e a contagem da linha.
- Relatar um recipiente como obfuscado porque um decompiler imprimiu um código op não suportado.
- Comparar com uma lista de referência capturada a partir de uma construção diferente da mesma fonte.

## Produção

Retorna estas secções:

1. Container e Version: os bytes de cabeçalho e o produtor que eles nomeam.
2. Referência: linhas comparadas, linhas acordadas, primeira descoincidência, se houver.
3. Listagem: a função com offsets, bytes e texto.
4. Factos: nome, parâmetros, tipos, locais, linhas, tamanho, forma de fluxo de controlo, cada um marcado ou perdido com a sua evidência.
5. Limites de decompilagem: as ferramentas consideradas e os seus limites documentados em relação à versão do cabeçalho.
6. Desconhecidos: cada desvio o leitor saltou ou recusou e porquê.

Se não houver nenhuma, indicar o número de acordos de referência e o número de fatos que o recipiente manteve fora de seis.
