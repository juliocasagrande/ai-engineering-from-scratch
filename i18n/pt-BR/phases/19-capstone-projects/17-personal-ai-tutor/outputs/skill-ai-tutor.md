---
name: ai-tutor
description: Envie um tutor pessoal multimodal adaptativo para um assunto específico com rastreamento de conhecimento bayesiano, um gráfico do currículo, filtros de segurança e um estudo de eficácia medido de duas semanas.
version: 1.0.0
phase: 19
lesson: 17
tags: [capstone, tutor, adaptive, bkt, fsrs, livekit, multimodal, coppa]
---

Dado um assunto (algebra K-12 ou Python introdutório), construa um tutor pessoal com entrada de texto + voz + foto-matemática, modelo de aprendizagem de conhecimento de Bayesian, seleção de conceitos baseados em currículo-grafo, memória consciente da COPPA e filtros de segurança.

Construir um plano:

1. Gráfico do currículo em Neo4j: 50-150 nós conceituais com bordas pré-requisitas e conteúdo OER anexado (OpenStax, Open Textbook).
2. Modelo de aprendiz: conhecimento bayesiano com antecedentes para adivinhação/deslizamento/taxa de aprendizagem por conceito; estado persistente por aprendiz.
3. Política de tutor (LangGraph sobre Claude Sonnet 4.7 com cache rápido): read_signal -> select_concept (graph walk) -> andamento (Socratic) -> update_mastery.
4. Memória: armazenamento episódico + semântico persistente em estilo de agente memória; apagamento automático após 1 ano, conforme a COPPA; exclusão acessível aos pais.
5. Voz: Trabalhador do LiveKit Agents com Whisper-v3-turbo ASR e Cartesia Sonic-2 TTS; reutilizar pipeline capstone 03.
6. Matemática fotográfica: dots.ocr ou PaliGemma 2 para reconhecimento de equações; fornecer informações estruturadas ao tutor.
7. Segurança: entrada/saída de Llama Guard 4; filtro adequado à idade que bloqueia a auto-lesionamento/adulto/violência; isolamento de memória verificado pelo aprendiz.
8. Relatórios semanais de progresso PDF por aprendiz.
9. Estudo de eficácia: 10 alunos, pré-test (linha de base padronizada de 30 perguntas), 2 semanas de sessões (3/semana), pós-test; comparação com a coorte linear não adaptativa.

Rubrico de avaliação:

| Weight | Criterion | Measurement |
|:-:|---|---|
| 25 | Learning gain delta | Pre/post-test delta in the 10-learner 2-week study |
| 20 | Socratic fidelity | Rubric score on transcript samples |
| 20 | Multimodal UX | Voice + photo + text coherence end to end |
| 20 | Safety + privacy posture | Llama Guard 4 pass rate + COPPA-aware retention + cross-learner isolation |
| 15 | Curriculum breadth and graph quality | Concept coverage + prerequisite graph consistency |

Rejeitos duros:

- Políticas de tutor que respondem ao invés de fazerem a próxima pergunta.
- Modelos de aprendizagem que não atualizam por interação.
- Memória sem retenção consciente da COPPA, inaceitável para um público de K-12.
- Atividades de eficácia sem coorte de referência não adaptativa.

Regras de recusa:

- Recusar-se a implantar sem Llama Guard 4 tanto na entrada quanto na saída.
- Recusar a persistência dos dados do aprendiz sem uma superfície de exclusão acessível aos pais.
- Recusar-se a afirmar que é "adaptiva" sem executar a linha de base não adaptativa ao lado.

Resultado: um repo contendo o gráfico do currículo, o modelo de aprendiz BKT, a política de tutor LangGraph, os gestores de entrada multimodal, o pipeline de voz LiveKit, o pipeline de segurança, o painel de controle dos pais, o corredor de estudo de eficácia, o uso do teste pré/pós-exame e um texto documentando o delta de ganho de aprendizagem em relação à linha de base com intervalos de confiança.
