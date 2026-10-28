---
name: rebuild-and-prove-equal
description: Prove uma função reconstruída igual à original com uma grade diferencial, uma comparação de byte consciente de realocação e um registro de prova apoiado por evidências.
version: 1.0.0
phase: 13
lesson: 36
tags: [reverse-engineering, differential-testing, elf, relocations, mcp, evidence]
---

Dado um arquivo objeto original que possui, evidência de função de um fornecedor de análise, e um candidato reconstruir em C, produzir uma prova de duas pernas e um registro de prova que nomeia cada identificação de evidência que se baseia. Use esta habilidade com Claude, Cursor, Codex, OpenClaw, Hermes, ou qualquer agente que leia SKILL.md.

## Introduções necessárias

- O objeto original ou executável, o SHA-256, e prova de que o escreviamos e compilamos.
- O compilador exato, versão, alvo e bandeiras que construíram o original.
- A lista de instruções e pseudocódio de cada função-alvo, com os seus identificadores de evidência.
- A candidata reconstruir, uma função por arquivo, com os mesmos nomes de função que o original.
- O ancho inteiro e a assinatura de cada operando, leído na lista.
- A arquitetura em que a prova se baseia e se o objeto original pode ser ligado a ela.
- Para cada realocação dentro de uma função: offset, tipo, largura, seção-alvo e forma dos dados a que aponta.

## Procedimento

1. Leia a lista antes do pseudocódio. Escreva a reconstrução das operações que a lista mostra.
2. Regista a identificação de todos os registos de onde veio a reconstrução.
3. Construir uma grade de entrada com uma classe por perigo: zero de proteção, negativo, arredondamento, sobreflow, armadilha e cada limite de ramo.
4. Adicionar as entradas que fazem cada envoltura intermediária na largura utilizada na listagem.
5. Compile o original, o candidato renomeado e um driver em um programa.
6. Instalar um `SIGFPE` O motorista tem um controlador no motorista, de modo que uma armadilha divide se torna um resultado gravado.
7. Execute a grade, grava cada célula com entradas, saída original, saída candidata e classe.
8. Verifique a coluna original contra um modelo da semântica do alvo.
9. Recompõe o candidato com as bandeiras originais exatas.
10. Leia ambos os objetos: símbolo de compensação e tamanho, bytes de função, e o `.rela` registos dentro da função.
11. Mascarar todos os campos de realocação, depois comparar tamanhos e bytes.
12. Compare registros de realocação por secção de offset, tipo e objetivo.
13. Leia as constantes em cada ponto de realocação e compare-as entrada por entrada.
14. Escreva uma reivindicação por perna por função com status `pass`- Não . `fail`, ou `unknown`- Não .
15. A primeira falha do agregado, depois desconhecido. `pass` para uma reclamação que não foi executada.
16. Tenta o registo de prova com `predicate_type`- Não . `operation`- Não . `confidence`- Não . `authority`Marque-o para a identificação.

## Matriz necessária

Para cada função, informe:

- Nome da função, offset original e tamanho em bytes
- Identidades de prova dos registos de listagem e pseudocódio
- tamanho da grade e contagem por classe
- Número e resultado dos testes ingênuos
- desajustes de rede com as três primeiras células em pleno
- Arquitetura host e se o original foi o objeto fixado ou uma construção nativa da sua fonte
- Desacordos do modelo com o original observado
- Dimensões de candidato, intervalos mascarados, compensações diferentes
- Registros de realocação em ambos os lados, com a secção-alvo e o anexo
- constantes referenciadas em ambos os lados
- Estatutos dos créditos e estatuto agregado
- ID de registro de prova

## Rejeitos duros

- Chamar uma reconstrução igual porque os testes manuscritos passaram.
- Uma grade sem entradas de sobreposição para cada multiplicação, adição ou subtração na função.
- Uma grade que salta a célula de armadilha dependente da arquitetura sem dizer.
- Comparar bytes sem mascarar campos de realocação.
- Mascarar campos de realocação sem comparar as constantes que apontam.
- Relatório de igualdade de byte entre compiladores, versões ou bandeiras diferentes.
- Tratar a igualdade de tamanho como aceitação.
- Ler a saída de um modelo como observação.
- Uma reivindicação com status `pass` E sem provas de identificação.
- Um agregado `pass` enquanto qualquer reivindicação é `unknown`- Não .
- Um registro comprovado cuja identidade não se recalcula do seu conteúdo.
- Qualquer análise de um programa para o qual não possamos ou não temos autorização por escrito.

## Produção

Retorna estas secções:

1. Evidência: os registos da reconstrução vieram, por id, com as suas limitações.
2. Candidato: o texto C e as operações de listagem a que se refere.
3. 1a etapa: design de grade, contagem por classe, resultado ingênuo, desajustes, verificação do modelo, hospedeiro e tipo original.
4. 2o Leg: tamanhos, intervalos mascarados, resultado de byte, registos de realocação, constantes referenciadas.
5. Reclamações: uma linha por reclamação com identificação de status e de provas.
6. Registo de prova: o registo JSON e os seus `ev_` - O que é?
7. Desconhecidos: todas as classes de entrada, arquitetura ou compilador não foram cobertos pela prova.

Se cada pedido for aprovado, indique a grade, as bandeiras e a arquitetura que a passagem cobre.
