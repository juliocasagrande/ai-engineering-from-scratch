---
name: compiler-idioms-and-optimization
description: Reconheça idiomas de compilador em uma lista de desmontagem de um programa que você construiu, decode cada um de volta à sua construção fonte com uma derivação e verifique o resultado contra a fonte.
version: 1.0.0
phase: 13
lesson: 39
tags: [reverse-engineering, x86-64, arm64, compiler-idioms, division-by-constant, switch-lowering, vectorization, inlining, tail-calls]
---

Dado um `llvm-objdump -d -r` lista de um objeto que você compilou, o arquivo objeto e a fonte C, produzem uma lista de idiomas de compilador reconhecidos. Cada entrada nomeia o tipo, as instruções de evidência, o formulário fonte decodificado e se a fonte o confirma. Use esta habilidade com Claude, Cursor, Codex, OpenClaw, Hermes ou qualquer agente que leia SKILL.md.

## Introduções necessárias

- A fonte C e o compilador exato, o alvo, o nível de otimização e as bandeiras que produziram o objeto.
- O arquivo objeto e os seus `llvm-objdump -d -r` Lista de capturas desse objeto.
- O reconhecedor da lição 39 (`code/main.py`) ou um equivalente que relate os endereços de provas para cada alegação.
- Para comparação, a saída de pelo menos um decompilador no mesmo objeto, capturado com a sua versão.

## Procedimento

1. Partilhe a listagem em funções e instruções. Anexe cada linha de realocação à instrução anterior. Grave a arquitetura da linha de formato de arquivo.
2. Encontre divisões por uma constante. `imul` com um instantâneo de 32 bits ou um `mov $imm` alimentação `imul`, depois as mudanças e a fixação do sinal ou a fixação adicional. `mov` e `movk` construindo a constante, então `smull` ou `umull` Recuperar o divisor do multiplicador e a mudança total com o Granlund-Montgomery ligado, e aceitar apenas quando o algoritmo dá as mesmas constantes de volta.
3. Encontre modulos como um quociente reconhecido multiplicado de volta pelo divisor e subtraído, como `msub`Quando um quociente também alimenta outro uso, mantenha a divisão e o modulo.
4. Classificar cada interruptor por sua redução: tabela de salto (salto indirecto através de uma tabela de endereços, entradas de realocações ou bytes), tabela de busca (carga indexada de valores, entradas dos bytes no endereço realocado mais 4 para um campo relativo ao RIP), mapa linear (aritmética afina selecionada por uma comparação de limites), árvore de comparação (testes de igualdade divididos por comparações ordenadas), comparar cadeia (apenas testes de igualdade), ou selecionar cadeia. Leia as limitações de verificação para a contagem de entradas e compare entradas com os casos de origem, permitindo um fator constante o compilador dobrado.
5. Encontre os circuitos de ramos retroceder cujo alvo possa alcançá-los novamente. Um corpo de loop que usa registros SIMD é vectorizado: rotas de relatório, acumuladores, elementos por iteração, a máscara de contagem de trip, o guardador de viagem mínima, a redução e o loop restante escalar. Um corpo com N carrega em offsets consecutivos de uma base é desenrolado por N.
6. Encontrar chamadas de cauda (a) `jmp` ou `b` Transporte de uma realocação de chamada), chamadas de linha (chamadas de origem sem instrução de chamada e a forma do corpo da chamada presente no chamador), substituição de bibliotecas (`memset` e `memcpy` O sistema de transferência de dados é um sistema de transferência de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de dados de
7. Decodificar seleções sem ramificação avaliando o código de linha reta antes da `cmov`- Não . `setcc`- Não . `csel`- Não . `cneg`, ou `cset` com os nomes dos parâmetros da fonte.
8. Relacionar as formas de endurecimento separadamente: o protetor de pilha (carga de proteção, slot, comparação, `__stack_chk_fail`) e `endbr64`- Não .
9. Verifique cada idioma contra a fonte: o divisor aparece após `/` ou `%`, o interruptor existe e os casos coincidem, o loop existe, a chamada é chamada, o selecto existe. Marque cada idioma verificado ou não e enumere os não verificados primeiro.
10. Compare com a saída do decompilador: para cada idioma, indique se a ferramenta a dobrou, deixou-a como aritmética ou imprimiu algo mais, e cite o texto da ferramenta.

## Relatório necessário

Para o objeto, informe:

- Compilador, alvo, nível, bandeiras e versão da ferramenta de listagem
- por função, cada idioma com tipo, forma fonte decodificada, endereços de evidência e status de verificação
- para divisões, o multiplicador, a mudança total, o divisor, o erro, e se as constantes do compilador correspondem ao algoritmo
- Para os interruptores, o tipo de redução, o número de entradas, a localização da tabela, as entradas ou os objetivos e o tipo de evidência (realocação ou bytes)
- Para os circuitos, vias, acumuladores, elementos por iteração, circuito restante ou o fator de desrolho
- A matriz tipo por nível de otimização e se dois níveis produziram o mesmo código
- A comparação do decompilador com a saída citada e a versão da ferramenta
- Todas as palavras que a fonte não confirmou, com a razão

## Rejeitos duros

- Nomear um divisor do multiplicador sozinho sem a mudança.
- Reportou uma mesa de busca como uma mesa de salto ou uma mesa de salto como código morto.
- Lendo entradas de tabela a partir de bytes zero em um objeto realojável quando as entradas são realocações.
- Contando um ramo para trás para um bloco padrão compartilhado como um loop.
- Chamando uma cauda de biblioteca chamando um retorno da função.
- Tratamento `-O0` Divisão de hardware como prova de que não existe multiplicação mágica para esse compilador.
- A reivindicação de um decompiler dobrar um idioma sem citar sua saída neste objeto.
- Relatar um idioma que a fonte não contém sem marcar o idioma sem verificar.

## Produção

Retorna estas secções:

1. Construir: compilador, alvo, nível, bandeiras, ferramenta de listagem.
2. Idiomas: por função, tipo, forma de origem, evidência, verificada.
3. Divisões: a tabela mágica com divisor, multiplicador, deslocamento, erro, adição de forma e correspondência de algoritmo.
4. Interruptores: redução por função por nível com entradas e tipo de evidência.
5. Loops: vector e desdobrar fatos por loop.
6. Decompiladores: por idioma, dobrados ou não, com o texto e a versão citados.
7. Não verificado: todas as palavras não foram confirmadas pela fonte.

Se estiver vazio, indique o número de idiomas reconhecidos e o número de divisões cujas constantes correspondem ao algoritmo.
