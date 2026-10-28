---
name: compliance-matrix
description: Produzir a matriz de quadro necessário para um LLM SaaS dada a geografia do cliente, segmento e escopo do contrato. Controle de mapas em SOC 2, HIPAA, GDPR, PCI-DSS, EU AI Act, Colorado AI Act, ISO 42001.
version: 1.0.0
phase: 17
lesson: 26
tags: [compliance, soc2, hipaa, gdpr, pci-dss, eu-ai-act, colorado-ai-act, iso-42001, iso-27001]
---

Dada a geografia do cliente (EU/UE/Globais, ou estados específicos dos EUA), segmento (SaaS / saúde / fintech), âmbito do contrato (empresa vs PME) e estado de conformidade atual, produz a matriz de quadro exigida.

Produzir:

1. Estruturas necessárias: lista cada estrutura que deve ser alcançada com raciocínio (geografia, segmento, perfil do cliente).
2. Para cada quadro, indique o estado atual (não / Tipo I / em auditoria / Tipo II).
3. Mapeamento de controles transframework. Para cada quadro necessário, identifique controles que satisfaçam múltiplos (registro de acesso, criptografia, registro de auditoria, mudança mgmt).
4. A posição da Lei de IA da UE. Classificar o nível de risco do produto (inaceitável / alto / limitado / mínimo).
5. Manutenção de PII / PHI. Confirme a redação em tempo real da camada de inferência (Fase 17 · 25)  Pós-processamento não é defendível pelo GDPR. Confirme BAAs para todos os fornecedores de IA que tocam PHI.
6. Instrumentos de auditoria. Drata / Vanta / Secureframe para automação transframework. Vale o custo em âmbito multi-framework.

Rejeitos duros:
- A reivindicação de SOC 2 Tipo I é "SOC 2 compatível" para contratos empresariais.
- Enviar PHI para um provedor sem BAA. Recusar violação da HIPAA.
- A limpeza de PII pós-processamento como postura do GDPR.

Regras de recusa:
- Se o produto servir os utilizadores da UE sem registos do artigo 30.o do RGPD, recusar-se a enviar aos clientes da UE até que sejam estabelecidos registos.
- Se o produto servir os residentes do Colorado em crédito/emprego/habitação/educação/serviços essenciais, exigir provas de uma avaliação de impacto concluída até 30 de junho de 2026 (data de entrada em vigor da Lei de IA do Colorado sob SB24-205 alterada por SB25B-004) antes do lançamento.
- Se o produto for de alto risco nos termos da Lei da UE sobre IA e a equipe não tiver um plano de avaliação da conformidade, recusar-se a prometer a preparação em agosto de 2026 sem um parceiro de implementação designado.

Resultados: uma matriz de uma página com os quadros necessários, estado actual, lacunas, cronograma, controles transversais, nível da Lei de IA da UE, postura de PII, ferramentas.
