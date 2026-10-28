---
name: topology-picker
description: Pick a multi-agent debate topology (star / chain / tree / graph), an N of agents, a heterogeneity profile, and a round bound for a given task.
version: 1.0.0
phase: 16
lesson: 15
tags: [multi-agent, debate, topology, voting, self-consistency]
---

Dada a descrição da tarefa, recomendamos uma topologia e um dimensionamento multi-agente.

Produzir:

1. **Task fingerprint.**Pesquisa (horizonte longo, aberto), factual rápida (resposta fechada), refinamento gradual (tubulação em fase) ou opinião (sem verdade básica).
2. **Topology.**Estrela, cadeia, árvore ou gráfico.
   - Pesquisa → gráfico (criticismo de qualquer tipo)
   - → estrela de facto rápido (agregados de hub)
   - Refinamento gradual → cadeia (ou árvore se divide-e-conquista)
   - opinião → nenhuma das referidas; recomendação de agente único + decisão humana
3. **N of agents.**3 é o conjunto mais barato útil; 5 é o ponto de adoçante comum; 7+ é especialidade.
4. **Heterogeneity profile.**Pelo menos um agente deve ser proveniente de uma família de modelos base diferente se a monocultura é importante (pesquisa, raciocínio).
5. **Round bound.**1 ronda = voto. 2 rondas = um refinamento. 3 rondas = máximo antes da conformidade dominar. Nunca ilimitado.
6. **Aggregation.**Pluralidade (barata), ponderada pela confiança (CP-WBFT da lição 14), mediana geométrica (DecentLLMs) ou pontuação do juiz.
7. **Escalation.**Consenso abaixo do limiar → escala onde? humano, outro conjunto com diferentes modelos base, ou abstenção?

Rejeitos duros:

- Qualquer recomendação de 10+ agentes sobre topologia gráfica.
- A topologia das estrelas para perguntas de pesquisa abertas, a Star perde o benefício de qualquer crítica.
- Qualquer recomendação que execute o mesmo modelo base N vezes e chama-o multi-agente.
- Os resultados são bem-sucedidos, mas o debate é mais longo, e os agentes mais concordam com a pressão do que com a lógica.

Regras de recusa:

- Se a tarefa não tiver verdade básica (opinião, síntese, criatividade), indicar que o voto é consultivo. Recomendar um agente único + decisão humana.
- Se o utilizador não tiver acesso a vários modelos base, marque o teto da monocultura e recomenda a autoconsistência com variação de temperatura como um retrocesso.
- Se a tarefa for simples (busca de fatos única, < 100 tokens de raciocínio), recomendamos um único agente com autoconsistência N=5.

Resultado: um resumo de uma página. Comece com uma recomendação de uma frase ("Topologia gráfica, N = 5 agentes de 3 modelos base diferentes, 2 rodadas, agregação ponderada pela confiança, escala para humano em menos de um limiar. "), em seguida, as sete seções acima. Termine com uma estimativa orçamental: tokens esperados por consulta e latência esperada em segundos.
