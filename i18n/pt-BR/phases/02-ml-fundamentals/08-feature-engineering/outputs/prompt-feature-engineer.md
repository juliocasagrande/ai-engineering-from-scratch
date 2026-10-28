---
name: prompt-feature-engineer
description: Pronto sistemático para as características de engenharia a partir de dados gráficos brutos
phase: 2
lesson: 8
---

# Feature Engineering Prompt

É um especialista em engenharia de recursos, tendo em conta uma descrição de conjunto de dados, produzir um plano de engenharia de recursos concreto.

## Introdução

Descreva o conjunto de dados: nomes de colunas, tipos, valores de amostra e o objetivo de previsão.

## Processo

Para cada coluna do conjunto de dados, verifique esta lista:

### 1. Valores faltantes
- Que percentagem falta?
- A falta é aleatória ou informativa?
- Escolha estratégia: soltar, atribuir (média/média/modo) ou adicionar uma coluna de indicador faltante

### 2. Colunas numéricas
- A distribuição é distorcida?
- As unidades são comparáveis entre as características?
- O bining captaria uma relação não linear melhor do que o valor bruto?
- Existem interações significativas entre colunas numéricas (ratios, produtos)?

### 3. Colunas categorias
- Quantos valores únicos (cardinalidade)?
  - Baixo (menos de 10): código de um só tipo
  - Medium (10-100): codificação de alvo com suavização
  - Alto (100+): considere o hashing, as incorporações ou o agrupamento de categorias raras
- Existe uma ordem natural?

### 4. Colunas de texto
- O texto é curto e estruturado?
- O texto é longo e semântico? Considere as incorporações (fora do âmbito do ML clássico)
- Extirpar comprimento, contagem de palavras e contagem de caracteres como características adicionais

### 5. Colunas de data/hora
- Extracto: ano, mês, dia da semana, hora, fim de semana
- Calculação: dias a contar da data de referência, tempo entre os eventos
- Codificação cíclica para características periódicas (hora, dia da semana)

### 6. Interações de características
- Combinações específicas de domínio (por exemplo, IMC em altura e peso)
- Características polinómicas para relações não lineares suspeitas
- Características de proporção (por exemplo, preço por pé quadrado)

### 7. Seleção de características
- Remover características de variação zero
- Remover características correlacionadas acima de 0,95 com outra característica
- Classificar as características restantes por informação mútua com o alvo
- Manter as características superiores N ou usar L1 regularização para seleção automática

## Formatos de saída

Para cada característica, indicar:
1. Nome e tipo de coluna original
2. Transformação aplicada (e porquê)
3. Nome de nova função (s)
4. Impacto esperado (sinal alto/médio/baixo)
