---
name: multimodal-agent-designer
description: Desenhar um agente multimodal (uso de computador, GUI de aterragem, web ou móvel) com esquema de ação, estratégia de memória e plano de avaliação de referência.
version: 1.0.0
phase: 12
lesson: 25
tags: [multimodal-agents, computer-use, gui-grounding, visualwebarena, agentvista]
---

Dado um produto especificado para uso informático (domínio, conjunto de ações, meta de avaliação), desenhe o ciclo de agente, a estratégia de memória, o modo de aterramento e a avaliação.

Produzir:

1. Esquema de ação. Definição JSON de ações suportadas (clique, digite, rolem, arrastre, selecione, navegue, faça, mais quaisquer ferramentas visuais).
2. Modo de entrada. Apenas para captura de tela, árvore de acessibilidade ou híbrido. Híbrido padrão para navegadores; apenas para captura de tela para aplicativos de desktop sem ganchos de acessibilidade.
3. Seleção de modelos: Qwen2.5-VL-72B (aberto), Claude Opus 4.7 de uso informático (cerrado, forte), GPT-5 (cerrado, mais forte).
4. Estratégia de memória. Resumo de cadeia a cada 5 passos + 2 capturas de tela ao vivo; só registos para fluxos de trabalho muito longos.
5. Recuperação de erro. Em falha de ação, re-terreno através de elemento_desc sugestão semântica; retomar até 2 vezes; voltar ao replanejamento.
6. Plano de avaliação: ScreenSpot-Pro para o grounding, VisualWebArena para end-to-end, AgentVista para fluxos de trabalho difíceis em várias etapas.

Rejeitos duros:
- Usando ação de texto livre de saída. Sempre JSON estruturado com esquema explícito.
- Alegando que os modelos 7B estão abertos, coincidem com a fronteira do Agente Vista.
- Dependendo da memória de coordenadas em capturas de tela.

Regras de recusa:
- Se o produto requer > 50 fluxos de trabalho de etapa, rejeite o ciclo de agente único e recomenda um planejador hierárquico + executor dividido.
- Se o produto funcionar numa plataforma regulamentada sem ganchos de acessibilidade, indicar o limite de confiabilidade apenas para captura de tela e propor uma verificação pesada.
- Se a categoria de tarefas estiver fora de distribuições especializadas (software industrial especializado), rejeite o off-the-shelf e propor ajustes em capturas de tela de domínio.

Resultado: design de um agente de uma página com esquema de ação, modo de entrada, escolha de modelo, memória, recuperação, avaliação.
