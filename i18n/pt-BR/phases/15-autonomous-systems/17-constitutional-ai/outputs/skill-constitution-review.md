---
name: constitution-review
description: Auditar a camada constitucional de uma implementação  proibições codificadas com código rígido, padrões codificados com código macio, limites ajustáveis pelo operador e resolução de hierarquia de quatro níveis.
version: 1.0.0
phase: 15
lesson: 17
tags: [constitutional-ai, rule-override, hierarchy, cai, rlaif, hardcoded-prohibition]
---

Dada a camada constitucional de uma implantação (promulgação do sistema, configuração do operador, princípios declarados), auditá-la contra a referência da Constituição Claude e sinalizar falta de proibições codificadas, princípios ambíguos ou níveis mal ordenados.

Produzir:

1. **Hardcoded prohibition inventory.** Lista todas as proibições que não devem dobrar independentemente da instrução do operador ou do usuário. piso mínimo: armas biológicas / CBRN elevação, CSAM, planejamento de ataque de infraestrutura crítica, identidade falsa-quando solicitado. Adições são específicas de implantação (por exemplo, serviços financeiros adiciona proibições específicas de fraude).
2. **Soft-coded defaults.** Lista todos os comportamentos que o operador pode ajustar. Para cada um, especifique o limite declarado. Uma configuração "ajustável" sem limite é um sobrepassamento de porta traseira.
3. **Tier ordering.** Confirmar a ordem de resolução é: segurança > ética > orientações > utilidade. Se a utilidade alguma vez vencer a ética no resolutor implementado, marque como uma pausa de implantação.
4. **Principle ambiguity flags.** Identificar qualquer princípio cujo texto deixa espaço para interpretações materialmente diferentes.
5. **Layer completeness.** Confirmar os controles de camada de execução (Lessões 10, 13, 14) estão presentes além da camada constitucional.

Rejeitos duros:
- Deploições sem qualquer camada de proibição codificada.
- Configuração do operador que alega anular uma proibição codificada em código rígido (mesmo por renomear).
- Ordens de nível que colocam a ajuda acima da ética.
- O texto de princípio é tão geral que não pode ser avaliado ("ser bom").
- Tratar a IA constitucional como um substituto para os controles de tempo de execução.

Regras de recusa:
- Se o utilizador nomear uma proibição codificada em código rígido, mas não puder apontar para uma plataforma de segurança de camada de execução, marque a implantação como de camada única e rejeite a produção.
- Se a configuração do operador incluir uma configuração de "segurança" ajustável sem limite declarado, rejeitar.
- Se o usuário tratar as conclusões da constituição participativa de 2023 como acionáveis na implementação atual, verifique: a Constituição de 2026 não as incorporou, então "herda democraticamente" é uma alegação que a implementação não pode dar suporte.

Formatos de saída:

Retorna uma auditoria constitucional com:
- **Hardcoded floor** (proibições, camada de aplicação: pesos / inferência / ambos)
- **Soft-coded defaults** (conjunto, operador ligado, visível para o utilizador y/n)
- **Tier order** (lista; segurança confirmada > ética > orientações > utilidade)
- **Ambiguity flags** (Princípio, ambiguidade específica, reforço proposto)
- **Layer completeness** (constitucional y/n, controles de tempo de execução y/n, ambos obrigatórios)
- **Readiness** (produzir / montar / apenas para investigação)
