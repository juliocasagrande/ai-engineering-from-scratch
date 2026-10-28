---
name: dynamic-analysis-of-your-own-program
description: Drive lldb ou gdb em modo batch sobre um programa que você compilar, registar registros e memória em cada parada, e classificar cada reivindicação estática como confirmado, refutado, ou não observado para essa execução.
version: 1.0.0
phase: 13
lesson: 42
tags: [reverse-engineering, dynamic-analysis, lldb, gdb, breakpoints, watchpoints, core-dumps, evidence]
---

Dado um programa que você escreveu e compilado com informações de depuração, uma lista de desmontagem dessa construção e uma lista de reivindicações estáticas de análises anteriores, produzem uma execução de depuração cuja transcrição é salvada e um registro de evidências por reivindicação por parada. Use esta habilidade com Claude, Cursor, Codex, OpenClaw, Hermes ou qualquer agente que leia SKILL.md.

## Introduções necessárias

- A fonte, o comando exato do compilador e o binário que produz.
- Uma lista de `llvm-objdump -d` ou `objdump -d` de que binário, então os endereços de ponto de ruptura vêm da lista e não da memória.
- O depósito DWARF dos tipos de estruturas mencionados nas alegações ou `ctypes` O layout, como fonte de compensações de campo.
- As reivindicações de teste, cada uma como uma frase com a função, o registo ou endereço, o valor esperado ou a borda, e a lição ou documento de que veio.
- Um depurador: lldb a partir das ferramentas de linha de comando ou Xcode no macOS, lldb ou gdb no Linux. Gravar a cadeia de versões.

## Procedimento

1. Leia a listagem. Para cada função nas reivindicações, registre seu endereço de início e fim. Para cada ramo condicional em uma função com uma reivindicação de borda, registre o endereço da filial, seu alvo e seu endereço de queda.
2. Escreva os comandos debugger para um arquivo antes de executar qualquer coisa: um `breakpoint set -n` por função, um `breakpoint set -a ADDR -s MODULE` por sucessor de ramo, um gancho de parada que lê os registros de argumentos, a memória por trás do primeiro argumento, e as variáveis de quadro, então `run`, o ponto de observação que você quer, um orçamento fixo de `continue`, e `breakpoint list` Mais `watchpoint list -v` No final.
3. Execute o depurador em modo batch com `settings set interpreter.stop-command-source-on-error false` Então um comando que falha após o processo sair não termina a sessão. Salve a saída completa como a transcrição com a linha de comando e a versão debugger em um cabeçalho.
4. Parse a transcrição em paradas. Cada parada tem um contador de programa, uma função, uma razão de parada, os registros e memória do gancho impresso, e as variáveis do quadro.
5. Classifique cada reivindicação em cada parada que possa testá-la. Uma alegação de registro compara o registro com a variável quadro. Uma reivindicação de campo de compensação decodifica as palavras de memória através dos offsets DWARF e as compara com os campos variáveis do quadro. Uma reivindicação de borda lê o valor comparado na entrada da função e verifica que a próxima parada é o sucessor da condição levantada prevê. Uma reclamação de call-edge conta as paradas de entrada após o processo ter saído.
6. Escreva `confirmed` Quando a observação for de acordo, `refuted` quando não estiver de acordo, e `not-observed` Quando não houver parada, pode-se verificar a alegação.
7. Repita uma construção otimizada da mesma fonte. Espera pontos de ruptura resolvidos com contagem de hits 0 onde o compilador alinhou a função, e mantenha essas reivindicações `not-observed` A menos que a alegação tenha sido relativa à própria vantagem da chamada, o que é refutado pela execução completa.
8. Se a execução não puder começar, registre o erro exato. `attach failed ((os/kern) invalid address)`E um alvo endurecido sem `com.apple.security.get-task-allow` Não há provas do programa.

## Relatório necessário

- compiler, versão debugger, sistema operacional e as bandeiras de construção de cada binário usado
- Os nomes dos arquivos transcritos e o comando que produziu cada um
- as paradas em ordem com o contador do programa, função, razão e os registros
- Cada reivindicação com o seu veredicto, os índices de parada que produziram o veredicto, e o texto de observação
- Contas de pontos de intervalo e de pontos de observação desde o final da corrida
- O estado de saída do processo e a sua saída padrão
- As reivindicações que permaneceram `not-observed` e a razão de cada

## Rejeitos duros

- Tratar um ponto de ruptura resolvido como prova de que o código está em execução.
- Tratar um número de hits de zero como prova de que uma função é código morto.
- Lendo um estruto através de um ponteiro sem os deslocamentos de campo a partir do DWARF ou das regras ABI.
- Comparar um registo de argumentos em uma parada que não seja a entrada de função, onde o registo pode ter um valor restante.
- Classificação de uma reivindicação de vantagem a partir da instrução da filial sozinha em vez da parada no sucessor.
- Colocar um ponto de vigilância em um local que vive em um registo em uma construção otimizada e relatar o silêncio como prova.
- A execução do depurador contra um binário que não construiu, ou a ligação a um processo que não possui.
- A transcrição é a prova, os veredictos são derivados dela.
- Relatar uma corrida em uma entrada como uma declaração sobre cada entrada.

## Produção

Retorna estas secções:

1. Construir: compilador, bandeiras, depurador e os arquivos listados e DWARF usados.
2. Plano: o arquivo de comando conforme escrito, com o endereço de cada ponto de ruptura e de onde veio.
3. Paradas: linha do tempo, uma linha por parada.
4. Veredictos: uma linha por reivindicação com contagens confirmadas, refutadas e não observadas e o veredicto final.
5. Não observado: cada uma afirma não parar de testar, com a razão.
6. Factos ambientais: assinatura de bandeiras do binário, contagem de pontos de vigilância de hardware e qualquer erro de lançamento.

Se não houver nenhuma, indicar o número de paradas e o número de reivindicações confirmadas por elas.
