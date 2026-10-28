---
name: linking-loading-and-stripped-binaries
description: Turn a program you built into its import list with providers, one call traced to the slot the loader fills, a record of what strip removed and what survived, and a scored recovery of function starts and names in a stripped build.
version: 1.0.0
phase: 13
lesson: 40
tags: [reverse-engineering, linking, elf, pe, coff, mach-o, plt, got, iat, chained-fixups, strip, function-identification, flirt]
---

Dada uma biblioteca executável ou compartilhada vinculada que você construiu, seu gêmeo não cortado, e os objetos de que foi vinculado, produzir um relatório que nomeia cada provedor de chamada externa, mostra uma chamada seguida do site de chamada para o slot escrito pelo carregador com a aritmética, diz o que `strip`O que é que é necessário para o carregador, e que marca cada função e assinatura contra a tabela de símbolos do gêmeo.

## Introduções necessárias

- O arquivo ligado, o comando de ligação exato e as versões da cadeia de ferramentas.
- O gêmeo não despojado, ou o ficheiro anterior.`strip`, como a verdade fundamental para os começos e nomes da função.
- Os objetos realocaveis dos quais o ficheiro foi vinculado, com os seus registos de realocação, para as assinaturas e o plano de ligação.
- Capturado texto da ferramenta dos mesmos arquivos: `llvm-objdump -h -p -T -R -d`ou `-h -t -r`para ELF e COFF, `llvm-objdump -p`para PE, e `otool -h -l -Iv`- Não .`dyld_info -fixups -fixup_chain_details -imports -exports -function_starts`, e `nm -m`Para Mach-O.
- Os leitores da lição 40 (`code/main.py`) ou equivalentes que rejeitam formatos desconhecidos em vez de adivinhar.

## Procedimento

1. Leia os cabeçalhos e nomeie o formato e o tipo.
2. Lista das importações com os seus fornecedores.`DT_NEEDED`e o indefinido.`.dynsym`- inscrições, com nomes de versões quando `.gnu.version_r`O PE: cada descriptor de importação com o seu DLL, tabela de busca, IAT e indicações/nome.`LC_LOAD_DYLIB`Ordem, ou o `nlist`Ordinários da biblioteca.
3. Siga uma chamada para o seu slot. Registre os bytes de chamada e endereço, o estúdio ou os bytes de entrada PLT com a aritmética de deslocamento, o endereço do slot, a palavra no arquivo e o que o carregador escreve. Para uma entrada PLT, gravar o `pushq`índice e o `DT_JMPREL`Para uma correção em cadeia, decodificar, ligar ou rebasear,`next`Para um espaço IAT, mostrar que a tabela de busca e o IAT são iguais antes de se ligar.
4. A partir dos objetos, planeje a ligação: para cada realocação, decida em local, direto, PLT e GOT slot, GOT slot apenas, ou uma realocação dinâmica, com a fórmula da tabela 4.9.`.rela.plt`tamanhos com o arquivo vinculado onde existe um.
5. Compare a tabela de símbolos antes e depois `strip`. Lista os nomes removidos, os nomes mantidos com a razão pela qual o carregador precisa de cada um, e as tabelas que sobreviveram: exportações, inicialização de função, deslizar tabelas, secções ou cabeçalhos de comando de carga.
6. No arquivo desligado, execute todos os buscadores que puder: tabela de inicialização do editor de links (`LC_FUNCTION_STARTS`- Não .`.pdata`- Não .`.eh_frame`), o prólogo escaneia com o padrão exato de byte ou máscara, e liga alvos mais o ponto de entrada.
7. Construa assinaturas dos objetos: os primeiros 32 bytes com bytes relocados marcados variante, o CRC16 dos bytes após 32 até o primeiro byte variante, o comprimento da função e os nomes referenciados. Compare-os nos arranques recuperados. Regista cada colisão e o byte de cauda ou nome referenciado que o dividem, ou que nada fez.
8. Escreva cada reivindicação com a linha de ferramenta capturada que o suporta e cada desajuste entre o leitor e a ferramenta como um desconhecido com o endereço.

## Relatório necessário

- arquivo, formato, tipo, bandeiras, comando link, versões da cadeia de ferramentas e os comandos de captura
- importações com fornecedor, ordinal ou versão, e o espaço que cada um liga
- a chamada rastreada: local da chamada, ponto ou entrada, espaço, palavra no arquivo, ação do carregador, com a aritmética mostrada
- O plano de ligação com os números por decisão e os tamanhos planejados, e os tamanhos medidos quando existe um arquivo vinculado
- Comparar as tiras: registos antes e depois, nomes removidos, nomes mantidos com razões, tabelas sobreviventes, saída de programas antes e depois
- pontuações de detecção: para cada método, encontrados, positivos verdadeiros, falsos positivos, perdidos, recall
- Assinaturas: todas `.pat`linha, cada nome atribuído, cada colisão com a sua resolução
- Desconhecidos: qualquer endereço em que o leitor e a ferramenta discordam ou em que nenhum método nomeou uma função

## Rejeitos duros

- Lendo um GOT, IAT, ou `__got`palavra do arquivo e chamá-lo de endereço sem decodificá-lo como o formato define.
- Informação sobre uma entrada PLT para uma chamada cujo símbolo é definido nas entradas.
- Tratamento`nm`saída em um arquivo desligado como a conta da função quando existe uma tabela de inicialização.
- A marcar um buscador sem o gémeo não despojado.
- Reclamar RELRO parcial ou completo sem leitura `PT_GNU_RELRO`E ...`DF_BIND_NOW`- Não .
- Comparar COFF `REL32`com ELF `PC32`sem contabilizar o adendo no registo do ELF.
- Nomear uma função a partir de uma assinatura que chocou com outra assinatura e não foi dividida por um byte de cauda ou um nome referenciado.
- Construir uma assinatura a partir de bytes sob uma realocação sem marcá-los variante.
- Citar um número de uma ferramenta executada em outra construção ou outra máquina.
- Descarregar uma biblioteca compartilhada abaixo do nível necessário ao carregador sem registar o que a tabela de exportação ainda transporta.

## Produção

Retorna estas secções:

1. Identidade: formato, tipo, bandeiras, máquina, cadeia de ferramentas, comandos.
2. Importações: fornecedor por nome, espaço de ligação de cada um e tempo de ligação (pânico, em carga ou sem).
3. Um chamado: o caminho rastreado com bytes e aritmética.
4. Plano de ligação: decisões, contagens, dimensões planejadas e medidas.
5. Strip: antes e depois, removido, mantido com razões, tabelas sobreviventes, saída de programa.
6. Os encontradores: pontuações por método com as falhas nomeadas.
7. As assinaturas: `.pat`Linhas, atribuições, colisões e resolução.
8. Desconhecidos: todos os desentendimentos e todos os começos não identificados.

Terminar com o primeiro desconhecido. Se não houver nenhum, indicar o número de fixups ou relocalizações que coincidem com o texto da ferramenta e o número de funções nomeadas.
