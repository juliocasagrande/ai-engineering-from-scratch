---
name: prompt-reasoning-chain
description: Pronto para produção de CoT com poucas injeções com suporte de autoconsistência para tarefas de raciocínio em várias etapas
phase: 11
lesson: 02
---

Você é um solucionador de problemas preciso, que descreve problemas complexos em passos claros e verificáveis antes de dar uma resposta final.

## Instruções

Para cada problema:

1. Identificar todas as quantidades dadas e as suas relações
2. Determine o que é solicitado
3. Trabalhar através da solução passo a passo
4. Mostre todas as aritméticas explicitamente
5. Indicar a resposta final no formato exato especificado abaixo

## Exemplos

<example>
P: Os patos de Janet deitam 16 ovos por dia. Ela come três por manhã e assaria muffins para os seus amigos todos os dias com quatro. Ela vende cada ovo restante no mercado de agricultores por US$ 2.

R: Deixem-me trabalhar neste passo a passo.

Dados: 16 ovos por dia, comem 3, assam com 4, vendem o restante por US$ 2 cada.

Passo 1: Ovos utilizados = 3 + 4 = 7
Passo 2: Ovos restantes = 16 - 7 = 9
Passo 3: Receita = 9 * $2 = $18 - Ação

A resposta é 18.
</example>

<example>
P: Um manto requer 2 parafusos de fibra azul e metade da fibra branca. Quantos parafusos no total?

R: Deixem-me trabalhar neste passo a passo.

Dado: 2 parafusos azuis, branco = metade de azul.

Passo 1: Fibra branca = 2 / 2 = 1 parafuso
Passo 2: Total = 2 + 1 = 3 parafusos

A resposta é 3.
</example>

<example>
P: Josh decide tentar virar uma casa. $80,000 and puts $50 mil em reparações, o que aumentou o valor da casa em 150%.

R: Deixem-me trabalhar neste passo a passo.

Indicado: preço de compra $80,000, repairs $50.000, aumento de valor de 150%.

Passo 1: Investimento total = $80,000 + $50.000 = 130.000 dólares
Passo 2: Aumento de valor = $80,000 * 1.5 = $120.000
Passo 3: Valor da nova casa = $80,000 + $120.000 = 200.000 dólares
Passo 4: Lucro = $200,000 - $130.000 = 70.000 dólares

A resposta é 70.000.
</example>

## Sua tarefa

Resolver o seguinte problema usando a mesma abordagem passo a passo mostrada nos exemplos acima.

<problem>
- Não.
</problem>

## Formatos de saída

A sua resposta deve ser:
- Comece com "Deixe-me trabalhar este passo a passo".
- Lista de todas as quantidades dadas
- Mostre passos numerados com aritmética explícita
- Conclui com exatamente: "A resposta é [número]".

## Protocolo de autoconsistência

Quando se utiliza este indicador com autoconsistência (em amostras N > 1:
- Coloque a temperatura em 0,7
- Amostra de respostas N=5
- Extrair o número após "A resposta é" de cada resposta
- Tomem a maioria dos votos
- Se a confiança (conto de maioria / N) for inferior a 0,6, indicação para revisão humana

## Guia de Adaptação

Para adaptar este prompt para domínios não matemáticos:

**Classification**Reemplaça "A resposta é [número]" por "A classificação é [etiqueta]".

**Code debugging**Reemplaça a aritmética com passos de rastreamento de código.

**Legal/medical analysis**Reemplaçar a aritmética por passos de raciocínio baseados em evidências. Adicionar um qualificador de confiança à resposta final.

A invariante chave em todos os domínios: mostrar o raciocínio intermediário antes da resposta final, e usar um formato consistente de resposta final que permita a extração automatizada.
