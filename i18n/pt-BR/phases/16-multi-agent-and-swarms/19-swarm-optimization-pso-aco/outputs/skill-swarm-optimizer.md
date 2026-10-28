---
name: swarm-optimizer
description: Escolha entre PSO, ACO, algoritmos genéticos e optimizadores baseados em gradientes para um determinado problema de otimização de LLM ou agente. Os algoritmos de enxame bio-inspirados são livres de gradientes e se adaptam às cargas de trabalho da era LLM onde o espaço de pesquisa é discreto ou a função de fitness é caixa preta.
version: 1.0.0
phase: 16
lesson: 19
tags: [multi-agent, swarm-optimization, PSO, ACO, prompt-optimization, routing]
---

Dado um problema de otimização de LLM ou agente, escolha otimizador certo.

Produzir:

1. **Problem fingerprint.** Espaço de pesquisa (número contínuo, string de instrução, pesos de modelo, gráfico de roteamento), sinal de fitness (teste automático, juiz de LLM, avaliador humano, KPI de negócios), tempo a valor (minutos, horas, dias).
2. **Optimizer choice.** PSO, ACO, algoritmo genético, DPO/RL, sintonização manual.
   - Numérico contínuo num espaço limitado → PSO
   - seleção de rota ou de caminho → ACO
   - Discreto simbólico / programas → algoritmos genéticos
   - remuneração diferenciável → DPO/RL
   - Pesquisa de baixa dimensão, rápida e avaliada → busca em rede/random
3. **Population sizing.** 10-30 para PSO/GA, tamanho da matriz feromônica para ACO. Calculo orçamental: N × T × custo por média. Não executar enxames que custem mais do que o valor que produzem.
4. **Fitness + quality gate.** Para roteamento ACO, qual limiar de qualidade desencadeia o depósito de feromônios?
5. **Convergence monitoring.** Registro de estabilidade g_best ou feromônio por iteração. Alerta sobre divergência (drift catastrófico) e sobre convergência prematura (ótimo local).
6. **Decay / exploration tuning.** Inercia do PSO e pesos cognitivos/sociais; taxa de decadência e quantidade de depósito da feromona ACO. Comércio: baixa decadência → apertado no ganhador inicial; alta decadência → nenhuma memória.
7. **Reset conditions.** Quando a distribuição de eval muda ou o padrão de implantação muda, restabeleça temporariamente g_best ou zero feromonas.

Rejeitos duros:

- Otimizadores de massa em tarefas onde a aptidão precisa de revisão humana.
- Dimensões populacionais > 50 sem uma clara justificação orçamental.
- Feromonas sem um portal de qualidade, agentes rápidos, mas errados.
- PSO em espaços de pesquisa discretos que não têm uma incorporação contínua natural.

Regras de recusa:

- Se o usuário está tentando otimizar algo sem uma função de fitness clara, recomende definir a condição física primeiro.
- Se o orçamento do usuário for inferior a 100 dólares, recomende ajuste manual + armazenamento em cache em vez de enxames.
- Se a distribuição mudar diariamente, recomende aprendizado on-line ou bandidos, não optimizadores de enxame.

Resultado: um resumo de uma página. Comece com uma recomendação de uma frase ("Use ACO com depósitos de feromônios de qualidade-gated em um problema de roteamento tipo 3 agente × 4 tarefas. Decadência 0.05, limiar 0.6, 200 tarefas de aquecimento."), em seguida, as sete seções acima. Conclui com uma estimativa orçamental e um plano de implantação de 1 semana.
