---
name: the-reverse-engineering-landscape
description: Execute vários desmontagens e decompiladores em um objeto que você construiu, normalize seus endereços e informe onde eles concordam e onde cada um inventa ou perde código.
version: 1.0.0
phase: 13
lesson: 37
tags: [reverse-engineering, tool-comparison, disassembly, control-flow-graph, intermediate-representation, ghidra, radare2, rizin, angr]
---

Dado um objeto relocable ou vinculado que você construiu, o comando do compilador que o produziu, e duas ou mais ferramentas de análise, produzem uma comparação que diz, para cada função, quais ferramentas concordam em inicialização de instrução, blocos e bordas, e que bytes cada ferramenta decodifica que os outros não fazem. Use esta habilidade com Claude, Cursor, Codex, OpenClaw, Hermes, ou qualquer agente que leia SKILL.md.

## Introduções necessárias

- O arquivo objeto e o compilador exato e o comando que o produziram.
- A tabela de símbolos do objeto (nome de função, offsets, tamanhos) é lida a partir do próprio arquivo.
- Para cada ferramenta: a cadeia de versões, o comando exato sem cabeça e a saída bruta capturada em um arquivo ao lado do objeto.
- O endereço que cada ferramenta deu à `.text` Seção, para que cada endereço possa ser reduzido a uma secção de compensação.
- A lição 37 (`code/main.py`) ou um equivalente que lê capta e nunca confia em um instrumento como o oráculo.

## Procedimento

1. Capture first, compare second.`llvm-objdump -d -r`- Não . `r2 -qc`- Não . `rizin -qc`, um guião de Angr, `analyzeHeadless -postScript`), armazenar a saída, e gravar o comando e versão em um manifesto. Nunca compare a saída ao vivo que você não pode ler novamente.
2. Leia os símbolos da função da tabela de símbolos ELF. Eles são a única verdade de terra compartilhada.
3. Normalizar cada endereço para um `.text` Compare que uma função conhecida atinge o mesmo deslocamento em cada ferramenta antes de comparar qualquer outra coisa.
4. Para cada extensão da função, coletar o conjunto de instruções inicia por ferramenta. Pegue a maioria definida sobre os construtores de gráficos e relatar, por ferramenta, os iniciais que adiciona e os iniciais que faltam.
5. Reúna os blocos de iniciação e as bordas por ferramenta como pares de offset. Relate as contagens e se os conjuntos coincidem. Quando as contagens diferem, lista as bordas que cada ferramenta carece em relação à união e leia as próprias notas da ferramenta (resolução do interruptor, salto computado, alvo não resolvedor) antes de julgar.
6. Para cada ferramenta, registar bytes de código dentro de símbolos, bytes de enchimento reclamados e bytes de símbolo deixados não reclamados. Nomear os bytes uma ferramenta afirma que a maioria não é como código inventado, e os bytes que deixa que a maioria decodifica como código perdido.
7. Compare a saída do decompilador em uma pequena função com um idioma conhecido (uma divisão por uma constante, um interruptor).
8. Para as ferramentas que não tiverem sido executadas, diga-as no relatório e descreva-as apenas a partir da sua documentação.

## Output

Para o objeto, informe:

- Compilador, comando, nome do objeto e manifesto das versões e comandos da ferramenta
- A base de cada ferramenta utilizada e o controlo de compensação de uma função
- por função: acordo de inicialização de instrução, inicialização extra e falta de cada ferramenta, contagem de blocos, contagem de bordas, conjuntos de bordas faltantes por ferramenta
- por ferramenta: bytes de código dentro de símbolos, bytes de enchimento reclamados, bytes de símbolos não reclamados, intervalos inventados, intervalos perdidos
- Os dados variam dentro de símbolos que nenhum criador de gráficos decodifica
- As funções que uma ferramenta inventa sem símbolo e as funções que ela perde
- saída de decompilador para uma função por ferramenta com o idioma chamado
- A lista das ferramentas descritas apenas a partir da documentação

## Modos de falha

- Comparar endereços antes de subtrair a base de cada ferramenta, o que faz com que cada ferramenta pareça errada.
- Tratar uma ferramenta como o oráculo.
- Uma divisão de rótulos ou uma heurística de enchimento muda a contagem sem mudar o código.
- Deixar as notas próprias de uma ferramenta (resolução de interruptor, salto não resolutivo) do relatório, que oculta por que as contagens de borda diferem.
- As capturas com comandos gravados e versões são o que torna um desacordo reprodutivo.
- Descrição de uma ferramenta que não foi executada como se a tivesse executado.
- Comparar captações feitas a partir de diferentes objetos ou versões de compilador diferentes.
