---
name: wmdp-eval
description: Auditar uma alegação de capacidade de duplo uso contra o WMDP, a avaliação do desaprendizagem e os estudos de elicitação.
version: 1.0.0
phase: 18
lesson: 17
tags: [wmdp, rmu, dual-use, biosecurity, cybersecurity, chemistry]
---

Tendo em conta uma alegação de capacidade de duplo uso ("o nosso modelo não ajuda significativamente com as armas biológicas / ataques cibernéticos / química"), auditem a avaliação de apoio.

Produzir:

1. Cobertura de índices de referência. Foi executado o WMDP (ou um índice de referência equivalente de zona amarela)? Relatório de pontuações por domínio (bio, ciber, química).
2. Se for aplicado o desaprendizagem (RMU ou alternativa), informe o delta de capacidade geral (MMLU, HELM, HumanEval).
3. O modelo de referência foi administrado através da conclusão em bruto ou através da pilha de segurança de produção?
4. Estudo de elicitação. A capacidade de escolha múltipla não é igual à capacidade de elicitação endurecida. São referenciados ensaios de aquisição de estilo antropólico, ou estudos equivalentes de novato no loop?
5. A divisão entre novato e especialista, a ascensão relativa aos novatos e a capacidade absoluta dos especialistas são quantidades diferentes.

Rejeitos duros:
- Qualquer alegação de segurança de duplo uso sem uma medição de capacidade equivalente à WMDP.
- Qualquer alegação de não aprendizagem sem delta de capacidade geral.
- Qualquer afirmação de "não ter um aumento significativo" sem estudo de novatos.

Regras de recusa:
- Se o utilizador perguntar se o seu modelo atravessa a ASL-3, recusar uma resposta direta; os limiares são específicos do laboratório (Lessão 18) e dependentes da elicitação.
- Se o usuário pedir um corte WMDP que seja "seguro", rejeite  o limite depende da resistência à elicitação, barreiras de conhecimento tácito e da superfície de implantação.

Resultado: uma auditoria de uma página que preenche as cinco seções acima, sinaliza as evidências mais importantes que faltam e identifica se a alegação é de nível WMDP ou de nível de implantação.
