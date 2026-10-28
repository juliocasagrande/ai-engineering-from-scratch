---
name: program-anatomy-elf-from-scratch
description: Read an ELF64 or Mach-O file the user built and report every structure, symbol, and relocation with its file range.
version: 1.0.0
phase: 13
lesson: 32
tags: [reverse-engineering, elf, mach-o, binary-formats, relocations, fixtures]
---

Com um objeto compilado ou executável que o usuário construiu a partir de sua própria fonte, produzir um relatório de layout a partir dos bytes do arquivo sozinho. Prove o relatório contra a saída da ferramenta capturada em fixtures. Use esta habilidade com Claude, Cursor, Codex, OpenClaw, Hermes, ou qualquer agente que leia SKILL.md.

## Introduções necessárias

- O arquivo fonte e o comando exato do compilador que produziu o alvo, então o alvo é um programa que o usuário construiu.
- O arquivo-alvo: um objeto ELF64 pequeno-endian relocable, executável, ou objeto compartilhado, ou um arquivo Mach-O 64 bits fina.
- Capturado texto de `llvm-objdump -h -t -r`(e `-p`para um executável), ou `llvm-objdump --macho --private-headers`para Mach-O, com a versão da ferramenta gravada.
- As páginas de especificações que nomeam os campos: Sistema V gABI capítulos 4 e 5, x86-64 psABI Tabela 4.9, e Apple `loader.h`- Não .`nlist.h`, e `reloc.h`- Não .
- As questões a que o relatório deve responder, por exemplo, a faixa de arquivos de uma função nomeada.

## Procedimento

1. O alvo deve ser um programa que o usuário escreveu e compilado, ou um com autorização escrita que o usuário pode mostrar.
2. Leia os primeiros bytes.`7f 45 4c 46`é ELF, e `cf fa ed fe`na ordem de arquivos é um pouco-endian 64 bits Mach-O. `ca fe ba be`Rejeitar uma classe de 32 bits, um arquivo de grande endian, ou uma mágica desconhecida com os bytes observados na mensagem.
3. Para ELF, desembaque o cabeçalho de 64 bytes com `<HHIQQQIHHHHHH`- O que é o " offset 16 " ?`e_shentsize`é de 64 e `e_phentsize`É 56 antes de ler qualquer tabela.
4. Leia a tabela de cabeçalhos de secção em `e_shoff`e resolver nomes através da seção em `e_shstrndx`Tipo de registro, bandeiras, deslocamento, tamanho, endereço, link, informações e alinhamento para cada seção.`SHT_NOBITS`Seções como possuir nenhum byte de arquivo.
5. Leia `.symtab`como 24 bytes `Elf64_Sym`registos e divisões `st_info`Resolver os nomes através de `sh_link`Impressão .`*UND*`- Não .`*ABS*`, e `*COM*`para os índices das secções reservadas.
6. Leia todos .`SHT_RELA`secção como registos de 24 bytes e dividido `r_info`Nomear o tipo da tabela psABI para o arquivo `e_machine`Imprimir o símbolo com o seu adendo assinado e imprimir um tipo desconhecido como número.
7. Calcule o intervalo de arquivos de cada função como `sh_offset + st_value - sh_addr`com comprimento `st_size`Relata bytes entre funções como um enchimento que não pertence a nenhum símbolo.
8. Construir o mapa de offset de arquivo. classificar o cabeçalho, a tabela de cabeçalho de programa, cada seção com bytes de arquivo e a tabela de cabeçalho de seção por offset. Nomear cada espaço como espaço inativo e rejeitar sobreposições.
9. Para um objeto executável ou compartilhado, leia os cabeçalhos do programa e endereços do mapa através de `PT_LOAD`com`p_offset + (address - p_vaddr)`- Relatar que um objeto realojável só possui endereços relacionados à secção.
10. Para Mach-O, leia `mach_header_64`E caminhar .`ncmds`comandos de carga por `cmdsize`- Leia .`LC_SEGMENT_64`com o seu `section_64`registos,`LC_SYMTAB`com`nlist_64`Inscrições `LC_BUILD_VERSION`Classificar cada secção como`segname,sectname`Calcule o comprimento de uma função como a distância para o símbolo seguinte em sua seção.
11. Compare cada tabela com o campo de texto da ferramenta capturado por campo.
12. Responder às perguntas do usuário com os valores calculados e citar o campo de especificação de que cada valor veio.

## Relatório necessário

Para cada alvo, informe:

- a identidade do arquivo: formato, classe, ordem de byte, máquina, tipo de arquivo e tamanho do arquivo
- Os campos de cabeçalhos que localizam cada tabela
- Cada seção ou seção Mach-O com o seu índice, nome, tipo, bandeiras, offset de arquivo, tamanho do arquivo, endereço e as tabelas a que liga
- Cada símbolo com ligação, tipo, secção, valor, tamanho e nome
- cada realocação com a sua tabela, seção-alvo, offset, nome do tipo, símbolo e adendo
- Cada cabeçalho ou segmento de programa com tipo, bandeiras, offset, endereço, tamanho de arquivo, tamanho de memória e alinhamento
- O mapa de offset de arquivo com cada espaço nomeado como espaço inativo e os bytes totais mapeados
- a faixa de arquivo e bytes exatos de cada função que o usuário perguntou sobre
- A comparação com a saída da ferramenta capturada: campos comparados, campos que concordam, campos que diferem

## Rejeitos duros

- Analisar um programa que o usuário não construiu e não pode mostrar autorização por escrito para.
- Tratamento`st_value`como um ficheiro de compensação, ou `sh_size`de um `SHT_NOBITS`secção como bytes de arquivo.
- Inventar um nome para um tipo de seção, tipo de realocação, comando de carga ou bandeira que não é listado na especificação.
- Lendo os bytes de opera em um campo realocado como o valor final.
- Mapeamento de um endereço ligado através de seções quando `PT_LOAD`existem entradas ou chamam um endereço vinculado de endereço de tempo de execução.
- Procuro uma secção Mach-O por perto .`sectname`- Só eu.
- Esperando um campo de tamanho em `nlist_64`- Não .
- Lendo um binário universal como um Mach-O.
- Execução da ferramenta de comparação dentro dos testes em vez de comparação com o texto capturado comprometido.
- Relatório de acordo com a ferramenta sem enumerar os campos comparados.

## Produção

Retorna estas secções:

1. Autorização: a fonte, o comando de construção e quem é o dono do alvo.
2. Identidade: formato, máquina, tipo, tamanho e campos de cabeçalho que localizam as tabelas.
3. Seções: a tabela com offsets, tamanhos, bandeiras e links.
4. Simbolitos: a tabela com ligação, tipo, secção, valor e tamanho.
5. Relocações: os registos com nomes de tipos da especificação e a aritmética adicional para cada um dos quais o usuário perguntou.
6. Segmentos: cabeçalhos de programa ou `LC_SEGMENT_64`registos e a regra de endereço a compensação.
7. Mapa de offset de arquivo: cada intervalo de bytes e seu proprietário, com espaços nomeados.
8. Função bytes: os intervalos e bytes solicitados.
9. Comparação Oracle: campos comparados, acordos, divergências.

Terminar com a primeira discordância entre o leitor e a saída da ferramenta capturada. Quando não houver nenhuma, indicar a versão da ferramenta da qual a captura veio.
