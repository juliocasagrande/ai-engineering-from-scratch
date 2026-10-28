---
name: calling-conventions-and-stack-frames
description: Recover the calling convention and the stack frame of a function from its disassembly, name the ABI rule behind every inference, and check each one against the source signature and the compiler's own unwind data.
version: 1.0.0
phase: 13
lesson: 38
tags: [reverse-engineering, calling-conventions, abi, stack-frames, system-v, microsoft-x64, aapcs64, prologue, unwind]
---

Dado um arquivo de objeto que você construiu, é`llvm-objdump -d -r`A listagem, e as assinaturas C de suas funções, produzem os locais de parâmetros, o layout do quadro, o registro de retorno e uma verificação de cada inferência contra a regra ABI que se baseia.

## Introduções necessárias

- O arquivo objeto, o comando exato do compilador e a versão do compilador.
- A lista de `llvm-objdump -d -r`do objeto, armazenado ao lado dele.
- A assinatura C de cada função em estudo, com o tamanho de byte de cada tipo de estruturas.
- O ABI para o qual o objeto foi construído.`e_machine`62 é o Sistema V AMD64 psABI, máquina COFF 0x8664 é Microsoft x64, ELF `e_machine`183 é AAPCS64, Mach-O `cputype`0x0100000c é o Apple arm64.
- O analista da lição 38 (`code/main.py`) ou um equivalente que separa as leituras de dados das leituras de endereços.
- Opcional: o objeto construído sem `-fno-asynchronous-unwind-tables`, para`.eh_frame`ou `.pdata`E ...`.xdata`- Não .

## Procedimento

1. Identifique o ABI do cabeçalho do objeto e anote qual livro de regras se aplica antes de ler qualquer instrução.
2. Leia o prólogo: em x86-64 os empurrões, o opcional `mov %rsp, %rbp`, e o `sub $N, %rsp`; no Arquivo 64 o`sub sp`, o `stp`E ...`str`de x19 a x30 com sp como base, e o `mov x29, sp`ou `add x29, sp, #k`. Registrar cada registro salvo com a sua deslocação do ponteiro de pilha na entrada e o tamanho do quadro como o ponteiro de pilha mais profundo que o prólogo atinge.
3. Caminhe pela corporação uma vez e registre todos os registros de classe de argumento que são lidos antes de serem escritos.`lea`Tratar o destino de`mov`- Não .`lea`- Não .`cvtsi2sd`, e o idioma zero .`xor r, r`Após uma chamada, marque o conjunto volátil como escrito.
4. Registre cada carga a partir de cima do ponteiro de pilha de entrada como um espaço de argumento de pilha: 8(%rsp) e até ao Sistema V, 40(%rsp) e até ao Microsoft x64 acima do armazém de sombra de 32 bytes, 0(sp) e até ao AAPCS64. Convert `rbp`E ...`x29`O que é que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é o que é?
5. Encontre o registo de devolução: o registo de resultados cujo último acesso antes da saída é um escrito. Uma leitura como operação de dados mata o candidato; uma leitura como base de endereços não. Um indicador de resultados oculto é o primeiro registo de argumentos que é armazenado através e copiado para `rax`, ou `x8`No AArch64.
6. Aplique as regras ABI à assinatura C: o sistema V classifica cada oitobytes INTEGER, SSE ou MEMORY e toma registros de duas listas independentes; a Microsoft x64 atribui o slot k para RCX/RDX/R8/R9 ou XMM0 para XMM3 e passa estruturas que não são 1, 2, 4 ou 8 bytes por referência; AAPCS64 atribui x[NGRN] e v[NSRN] e usa x8 para resultados maiores que 16 bytes. Comparar os locais esperados com os observados e registar acordo por regra.
7. Verifique as regras do quadro: os registros salvos de chamadas devem aparecer no conjunto salvos; `(rsp + 8) % 16 == 0`ou `sp % 16 == 0`em cada chamada; pelo menos 32 bytes abaixo do endereço de devolução em cada chamada Microsoft x64; nenhum acesso abaixo do ponteiro de pilha sob Microsoft x64 ou AAPCS64, no máximo 128 bytes sob o Sistema V; o epílogo restaura o que o prólogo salvou e o ponteiro de pilha está de volta ao seu valor de entrada.
8. Quando os dados de desvio existem, decodifique-os e compare: `UWOP_PUSH_NONVOL`E ...`UWOP_ALLOC_*`Códigos contra os empurrões e a atribuição, `DW_CFA_offset`Regras contra as compensações de registos guardados, a compensação mais profunda de CFA contra o indicador de pilha mais profundo.
9. Quando outra ferramenta estiver disponível, capture seu protótipo ou lista de argumentos para a mesma função com o comando exato, e registre onde concorda e onde não concorda com a fonte e com os bytes.

## Relatório necessário

Para cada função, informe:

- Nome do objeto, formato, máquina, ABI, compilador, comando de construção, caminho de listagem
- Bytes de prólogo e texto, registros salvos com offsets de entrada, bytes de quadro, offsets de indicador de quadro ou nenhum
- Registros de argumentos leídos antes de serem escritos, resenhas de argumentos em pilha, registros de argumentos com resenhas derramadas, lojas domésticas sob Microsoft x64
- Registo de devolução ou ponteiro oculto, com a instrução que o define
- Profundidades de chamada, bytes de sombra, bytes usados abaixo do ponteiro de pilha
- Cada controlo, como regra, esperado, observado, concordar
- Deslizar o controlo cruzado por função, quando disponível
- Output de outras ferramentas com o comando, e cada desacordo como uma conclusão

## Rejeitos duros

- Lendo um objeto x86-64 como Sistema V porque é x86-64. COFF significa Microsoft x64.
- Contando o destino de `cvtsi2sd`ou `xor r, r`como uma leitura, que inventa um argumento de ponto flutuante ou inteiro.
- Deixar um registo que é lido apenas como um `lea`base ou índice, que perde um argumento.
- Tratar um registo que é escrito e depois consumido como um registo de devolução.
- Tratamento`push rbp`Como prova de um indicador de quadro.`mov %rsp, %rbp`Depois de fazer um.
- Relatório de um argumento de pilha de um `lea`- O que é ?`lea`Computa um endereço e não carrega nada.
- Meter a utilização da zona vermelha a partir do ponteiro de entrada em vez do ponteiro atual.
- Comparar o CFA mais profundo com o quadro do prólogo quando o corpo empurra argumentos de saída.
- Aceitar o protótipo de uma ferramenta sem a assinatura fonte ou os bytes para verificá-la.
- Analisar um programa que não construiu ou não tem permissão para estudar.

## Produção

Retorna estas secções:

1. ABI: formato, máquina, livro de regras, com os bytes de cabeçalho que decidiram.
2. Prólogo e quadro: bytes, registros salvos, tamanho do quadro, indicador do quadro, zona vermelha ou uso de sombras.
3. Parâmetros: registos e espaços de estaca observados, esperados da assinatura, acordo por regra.
4. Resultado: registo de devolução ou ponteiro oculto e a instrução que o define.
5. Sites de ligação: profundidade, alinhamento, bytes de sombra, registros e lojas de saída.
6. Deslizar Cross-Check: códigos de deslizar ou regras de CFI contra o prólogo de análise.
7. Outras Ferramentas: comando, saída e cada desacordo como descoberta.

Concluir com o primeiro desavenço.Se não houver nenhum, indicar o número de verificações acordadas e o número de funções cobertas.
