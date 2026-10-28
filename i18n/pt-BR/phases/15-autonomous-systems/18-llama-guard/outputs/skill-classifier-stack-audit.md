---
name: classifier-stack-audit
description: Audit a deployment's input/output classifier stack (model, taxonomy, input rails, output rails, dialog rails) and flag adversarial-attack gaps.
version: 1.0.0
phase: 15
lesson: 18
tags: [llama-guard, nemo-guardrails, input-rails, output-rails, colang, adversarial-attacks]
---

Dada a pilha de classificadores de uma implantação (versão Llama Guard, configuração NeMo Guardrails, classificadores personalizados, etapas de normalização), auditá-la contra a superfície de referência e ataque de bandeira de 2026 que a pilha não cobre.

Produzir:

1. **Model inventory.**Lista dos classificadores em uso. Llama Guard 3 (8B / 1B-INT4) vs Llama Guard 4 (multimodal, S1S14). NeMo Guardrails versão. Qualquer classificadores personalizados. Se a implantação aceita imagens, confirme que o classificador é multimodal.
2. **Taxonomy mapping.**O mapa declara categorias de negócios na taxonomia do classificador. Cada categoria que o operador se importa deve ser mapeada para uma categoria do classificador; categorias não mapeadas não são guardadas.
3. **Rail coverage.**As vias de entrada são confirmadas antes da rotação do modelo e as vias de saída são iniciadas antes dos navios de resposta. As vias de diálogo (Colang em NeMo) impõem restrições de rotação transversal.
4. **Normalization.**As entradas de confirmação são normalizadas em NFKC, mapeadas em homoglífico e têm caracteres de selector de largura zero / variação despojados antes da classificação.
5. **Attack-corpus coverage.**Para cada ataque documentado (contrabando de emoji, homoglifos, redireção no contexto, parafrase semântica), nome a defesa específica na pilha.

Rejeitos duros:
- Deploições que utilizam um classificador de texto apenas em entradas multimodal.
- Desdobramentos sem etapa de normalização.
- Deploições com apenas trilhas de entrada (sem trilhas de saída em saídas de categoria sensível).
- A pilha que trata o classificador como a camada de segurança única.
- A ASR alega que o operador não pode reproduzir na sua própria distribuição.

Regras de recusa:
- Se as categorias declaradas pelo usuário não se inserem na taxonomia do classificador, recusar e exigir primeiro um mapeamento.
- Se a implantação citar números Llama Guard 3 ASR numa superfície de entrada multimodal, rejeite e precise de Llama Guard 4 ou um classificador multimodal.
- Se o utilizador considerar que a camada de classificação é suficiente em um ambiente de alto risco, recusar.

Formatos de saída:

Retorno de uma auditoria do classificador com:
- **Model inventory**(nome, versão, modalidade)
- **Taxonomy mapping**(categoria de operador → categoria de classificador)
- **Rail coverage**(entrada / saída / diálogo; disparo antes/após modelo)
- **Normalization note**(NFKC y/n, homoglífico y/n, faixa de largura zero y/n)
- **Attack-corpus coverage**(ataque → defesa)
- **Layer completeness**(classificador + constituição + tempo de execução; três necessários)
- **Readiness**(produzir / montar / apenas para investigação)
