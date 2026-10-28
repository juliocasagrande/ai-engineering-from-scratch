---
name: recovering-data-and-types
description: Transforme uma lista de desmontagem e uma construção opcional debug em um layout de estruturas com evidências por campo, um passo com suas fontes, uma comparação com o DWARF e uma lista de que permaneceu desconhecido.
version: 1.0.0
phase: 13
lesson: 41
tags: [reverse-engineering, x86-64, types, structs, dwarf, system-v-abi, itanium-abi, vtables]
---

Dado um objeto x86-64 que você construiu por si mesmo, seu `llvm-objdump -d -r` A listagem, e as funções que recebem um indicador para o tipo em estudo, produzem o layout de campo as instruções provam, o passo os loops provam, a comparação com o layout DWARF quando um `-g` Use esta habilidade com Claude, Cursor, Codex, OpenClaw, Hermes, ou qualquer agente que leia SKILL.md.

## Introduções necessárias

- O arquivo objeto, o compilador exato e o comando que o produziram, e o `llvm-objdump -d -r` texto capturado a partir do mesmo objeto.
- Os nomes das funções cujo primeiro parâmetro aponta para o tipo, ou os locais de chamada que passam um objeto para eles.
- Quando disponível, a `-g` construção da mesma fonte e `llvm-dwarfdump --debug-info` - Não.
- Para um objeto C++, a tabela de símbolos e os registros de realocação do `.data.rel.ro.*` Seções que contêm os vtais.
- O passe e o leitor da lição 41 (`code/main.py`) ou um equivalente que registra a instrução por trás de cada campo.

## Procedimento

1. Partilhe a lista em funções. Anexe cada linha de realocação à instrução acima dela, para que as chamadas tenham o nome da chamada.
2. Execute o rastro para a frente sobre cada função com os registros de argumentos do sistema V semidos como puntuações. Registre cada operando de memória cuja base detém um puntuação como um acesso com raiz, offset, largura, tipo, signo e armazenar bandeira. Registre incrementos de 64 bits, ramos para trás como loops e os valores de argumento em cada chamada.
3. Para cada loop, agrupar acessos de largura igual através de um registo base. `d` separados e o passo do loop é `k * d` com `k` O valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de um valor de valor de valor de um valor de valor de valor de um valor de valor de valor de valor de valor de um valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor de valor `unrolled`Não confies em nenhum deslocamento antes deste passo.
4. Recolha evidências de passos de todos os tipos: escalas de índice de mudanças e multiplicadores, passos de loop, delta de compensação e offsets de elementos de call-site. O passos é o maior divisor comum de todos eles. Nomear o tipo de cada valor.
5. Construir os campos. Combinar acessos em um offset e largura. Marcar um campo como um ponteiro apenas quando um valor carregado a partir dele foi posteriormente usado como base ou avançado com `lea`Registrar os acessos sobrepostos de largura diferente como conflitos.
6. Se um `-g` construção existe, leia o seu DWARF 5 através da tabela de abreviação e o `.debug_str_offsets` e `.debug_addr` Verifique o cabeçalho da unidade, os membros de compensação e o tamanho de byte contra `llvm-dwarfdump`Compare campo por campo e etiquete cada linha `match`- Não . `no-evidence`- Não . `size-mismatch`- Não . `pointer-unproven`- Não . `kind-mismatch`, ou `unexpected`- Não .
7. Verifique o layout recuperado contra as regras do Sistema V: cada campo em um múltiplo de seu próprio tamanho, tamanho de um múltiplo do alinhamento mais rigoroso, lacunas onde as regras exigem empolgação. Uma violação significa um estruto embalado, um campo de bits ou um campo errado.
8. Para um objeto C ++, leia cada `_ZTV` símbolo de suas mudanças: offset para cima, typeinfo, em seguida, slots do ponto de endereço 16 bytes. `_ZTI` por sua espécie, cadeia de nomes e base. `call *disp(%reg)` cujo registo foi carregado a partir do deslocamento 0 de um objeto para `disp / 8` e listar as funções candidatas por classe. `_Z` nome e controlo contra `llvm-cxxfilt --no-strip-underscore`- Não .
9. Escreva todos os nomes, qualificadores, tipos de ponta e suposições como desconhecidos ou inferidos.

## Relatório necessário

Para o tipo, relatório:

- nome do objeto, compilador, comando de construção e caminho de listagem
- funções de testemunha e a evidência de que compartilham um tipo (sitos de ligação ou afirmação de analista)
- Tabela de campo com deslocamento, tamanho, tipo, sinal, número de acesso e endereço de cada acesso
- Probações de apontamento com a instrução de desreferência
- Tabela de passos com todos os valores e tipos, os loops dobrados e o passo e tamanho resultantes
- Linhas de comparação com DWARF quando um `-g` construção existe, e os valores de cabeçalho de unidade que foram verificados
- Verificação de alinhamento com as regras do Sistema V
- Para C++: vtables com slots e símbolos, tipo e base de tipo de informação, chamadas virtuais com slots e candidatos, nomes desfigurados
- Todos os desconhecidos: membros sem provas, indicadores não comprovados, nomes, qualificadores, tipos de ponta

## Rejeitos duros

- Relatar um deslocamento passado do passo sem verificar o ciclo para desdobrar.
- Tomando um único incremento de ciclo como o tamanho do elemento.
- Chamando um campo de 8 bytes um ponteiro sem desreferência.
- Chamando um 1 byte comparar um cartão assinado ou não assinado.
- A fusão dos acessos de várias funções num único estruto sem provas de local de chamada ou uma afirmação gravada.
- Leitura `.debug_str` por índice bruto, ou `.debug_addr` sem as suas realocações, num objeto realocavel.
- Partilhar um cabeçalho DWARF 4 com o layout DWARF 5.
- A leitura de espaços de vtable do símbolo começa em vez do ponto de endereço.
- Tratar um vtable faltante em um objeto como prova de que a classe não tem nenhum.
- Copia do nome do tipo do decompiler no relatório como prova.
- Inventar um nome de membro.

## Produção

Retorna estas secções:

1. Testemunhas: as funções, as raízes e as provas de alias.
2. Acesso: a tabela de acesso completa com endereços.
3. Layout: campos, provas de ponteiros, conflitos, lacunas e verificação de alinhamento.
4. Passo: cada valor com o seu tipo, as dobras aplicadas, o passo e o tamanho.
5. DWARF: a verificação de cabeçalho da unidade e as linhas de comparação, ou a declaração de que não existe nenhuma construção de depuração.
6. C++: vtables, typeinfo, chamadas virtuais e nomes desfigurados, ou a declaração de que o objeto não tem nenhum.
7. Desconhecidos: cada membro, tipo, nome e qualificação a evidência não alcança.

Se não houver nenhum, indique o número de membros correspondentes contra o DWARF e o número de fontes de passos que concordaram.
