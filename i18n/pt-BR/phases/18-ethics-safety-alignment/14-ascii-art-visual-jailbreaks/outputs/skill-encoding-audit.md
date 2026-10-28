---
name: encoding-audit
description: Auditar um relatório de defesa contra a fuga de prisão em ataques de família de codificação.
version: 1.0.0
phase: 18
lesson: 14
tags: [artprompt, ascii-art, encoding-attack, utes, structural-sleight]
---

Dado um relatório de defesa contra jailbreak, enumere os ataques de família de codificação cobertos e a camada de defesa que apanha cada um.

Produzir:

1. Encodificação de cobertura. Lista de cada família de ataque avaliada: arte ASCII (ArtPrompt), base64, leet-speak, homoglifos UTF-8, JSON / YAML / CSV, árvore / gráfico UTES, modalidade de imagem. Famílias de bandeiras faltam.
2. Mapeamento de camadas de defesa. Para cada família, identifique qual camada de defesa (filtro de palavras-chave, filtro de perplexidade, parafrase, retokenization, classificador de saída, moderador multimodal) a pega e qual não.
3. Per Jiang et al. 2024, PPL e Retokenization falham contra ArtPrompt porque o reconhecimento acontece no nível visual.
4. O teste de generalização. UTES (StructuralSleight) generaliza para estruturas raras arbitrárias.
5. Compromiso de capacidade e segurança. Um modelo com maior capacidade visual-textual (alta pontuação ViTC) é mais vulnerável ao ArtPrompt. Observe a pontuação ViTC do modelo se relatada; solicite-a se não.

Rejeitos duros:
- Qualquer alegação de defesa baseada unicamente na filtragem de substring/palavras-chave.
- Qualquer afirmação de defesa que cobre uma família de codificação e extrapola a "ataques de codificação".
- Qualquer reivindicação de defesa sem uma taxa de sucesso de ataque por família.

Regras de recusa:
- Se o usuário perguntar se o ArtPrompt está "parado", recusar e explicar a lacuna de reconhecimento e defesa de texto.
- Se o usuário pedir uma defesa recomendada para todos os codificadores, recuse uma única recomendação.

Resultado: uma auditoria de uma página que preenche as cinco seções acima, sinaliza a lacuna de codificação primária e nomeia a camada de defesa mais urgente a ser adicionada. Cite Jiang et al. (arXiv:2402.11753) e StructuralSleight uma vez cada.
