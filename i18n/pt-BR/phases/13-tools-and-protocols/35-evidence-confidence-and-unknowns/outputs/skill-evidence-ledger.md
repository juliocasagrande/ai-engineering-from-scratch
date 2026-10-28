---
name: evidence-ledger
description: Registrar as conclusões da análise binária como observadas, evidências derivadas ou inferidas com ids de conteúdo hash, e recusar-se a declarar um resultado sem uma corrida observada.
version: 1.0.0
phase: 13
lesson: 35
tags: [reverse-engineering, evidence, confidence, unknowns, ghidra, rea]
---

Considerando um programa que você compilou e um conjunto de perguntas sobre ele, mantenha um livro de registros de evidências e uma lista de desconhecidos residuais.

## Introduções necessárias

- O ficheiro-alvo, o SHA-256, o formato e a arquitetura.
- O fornecedor de cada observação: nome e versão da ferramenta, ou o analista.
- O perfil de análise de cada fornecedor executado, incluindo cada cadeia de versões de contrato.
- As perguntas a responder, cada uma com autoridade e confiança que a resolverão.
- Um compilador host e um programa de teste quando as perguntas são sobre comportamento.
- Analisar apenas programas que você possui ou tem permissão por escrito para analisar.

## Procedimento

1. Marque o alvo, coloque o digest, formato e arquitetura em cada assunto, mantenha o nome e o caminho fora da identidade.
2. Dê a cada disco uma confiança. `observed` significa leitura a partir de bytes ou de uma corrida. `derived` significa calculado a partir de registos observados. `inferred` significa uma expectativa.
3. Dê a cada registro uma autoridade. `shipped-artifact` significa uma leitura do processo. `controlled-replay` Significa uma corrida que controlaste. `analyst-inference` significa o seu próprio julgamento.
4. Computação `evidence_id` como `ev_` mais SHA-256 sobre o JSON canônico (RFC 8785) do registro. Deixe fora o id, o nome e o caminho.
5. Limitações de fornecedor de registro, literalmente. Adicione sua própria limitação quando uma execução usa uma construção diferente do arquivo em análise.
6. Ligue todos os registros derivados e inferidos aos registros em que se baseia através `evidence_links`- Não .
7. Abra uma desconhecida por pergunta, guarda a pergunta, o escopo, a gravidade, a confiança necessária, a autoridade necessária e uma sonda recomendada.
8. Faça todas as alterações em uma revisão desconhecida uma nova revisão que nomeie o digest da revisão anterior.
9. Verifique uma alegação de comportamento apenas contra registros de execução observados que nomeam a mesma função e argumentos. Conte as entradas que têm uma execução.
10. Relatório `pass` Quando cada entrada tiver uma corrida de acordo. `fail` Quando qualquer jogador discorda. `unknown` Quando algumas entradas não têm execução. `unsupported` Quando nenhum o faz.
11. Resolva um desconhecido apenas com identidades de evidências que tenham a confiança e autoridade necessárias.
12. O provedor de cache responde sob uma chave que cobre o alvo, o provedor, o digest de perfil, a operação e os parâmetros.

## Registro de contabilidade necessário

Para cada reivindicação, informe:

- Texto da reivindicação e a função e os argumentos que abrange
- O registro de previsão id e os registos derivados que ele se baseia
- Introduções com corridas observadas, das entradas cobertas pela alegação
- Identificação de provas de apoio e contradição
- limitações efectuadas a partir dos registos de apoio
- Estatuto: `pass`- Não . `fail`- Não . `unknown`, ou `unsupported`
- O ID desconhecido, o seu estado atual e a sua revisão

Para cada desconhecido, informe a pergunta, a gravidade, a autoridade requerida, o estado atual e a contagem de revisões.

## Rejeitos duros

- Um resultado declarado a partir de pseudocódio ou de uma lista de desmontagem sem execução observada.
- A. `pass` Para uma reivindicação cujos insumos são apenas parcialmente cobertos por corridas.
- A. `fail` ou a `pass` Uma lista vazia é `unknown`- Não .
- Uma identificação de evidência calculada sobre o caminho local ou o nome do arquivo.
- Um registo cujo perfil de análise nomeia um fornecedor diferente do registo.
- Um desconhecido resolvido com evidências derivadas ou inferidas, ou sem identificação de evidências.
- Um desconhecido mudou sem o número de revisão atual.
- Um instantâneo reproduzido após uma série de versões de contrato mudar.
- Um registo que elimina a limitação de fornecedores.
- Um registro de execução que oculta o facto de ter executado uma construção diferente da mesma fonte.
- Uma alegação que chama a análise estática de observação da execução.

## Produção

Retorna estas secções:

1. Alvo: digest, formato, arquitetura, comando de construção e autorização.
2. Evidência: todo registro com identidade, confiança, autoridade, operação e limitações.
3. Reclamações: o livro-razão exigido acima, uma linha por reclamação.
4. Desconhecidos: abertos, investigados, bloqueados, contraditórios e resolvidos, cada um com sua cadeia de revisão.
5. Cache: os campos de chave instantânea, as entradas reutilizadas e cada importação recusada com a sua razão.
6. Conclusão: `ecl_` Identificação, contagem por status e aprovação de cada pedido.

Acaba com o primeiro desconhecido que ainda bloqueia uma resposta completa, e a sonda que o fecharia.
