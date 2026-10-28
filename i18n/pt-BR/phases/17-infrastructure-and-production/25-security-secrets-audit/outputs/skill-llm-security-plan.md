---
name: llm-security-plan
description: Produce an LLM security plan covering secrets vault, PII scrubbing with consistent tokenization, network egress allowlist, audit log retention, and zero-trust posture.
version: 1.0.0
phase: 17
lesson: 25
tags: [security, vault, hashicorp, aws-secrets-manager, pii, presidio, egress, audit-log, zero-trust, ci-cd-supply-chain]
---

Dado o escopo regulamentar (SOC 2, HIPAA, GDPR), o estado atual da credencial e a postura de rede/entrada, produz um plano de segurança.

Produzir:

1. Migração de cofre. Cofre cofre (HashiCorp, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager). Padrão de gateway: aplicativos → gateway → cofre em tempo de execução. Deprecar env codificado e credenciais de arquivo de configuração.
2. Avaliar TruffleHog / GitGuardian / Gitleaks em cada compromisso.
3. Política de rotação. ≤ 90 dias. Automatizado sempre que possível. rotação dedicada para credenciais CI/CD (recomendável  30d mais curto).
4. PII scrubbing. reconhecimento de entidade (Presidio + regex). Tokenization consistente (seme valor → mesmo lugar) para preservar a semântica.
5. Egress Allowlist, Whitelist LLM Provider, vector DB, vault endpoints, DNS Allowlist resolver.
6. Registro de auditoria. Somente adicionado, imutável. Campos exigidos: usuário, inquilino, hash de resposta/pronto, tokens, custo, viagens de guarda-roupa. Retinhamento por framework (SOC 2 1y / HIPAA 6y).
7. A Comissão Europeia (UE) não pode permitir que a Comissão, em conformidade com o artigo 150.o, não tenha de fazer qualquer intervenção para a aplicação da legislação comunitária.

Rejeitos duros:
- Chaves estáticas em arquivos de configuração.
- Armazenamento de informações brutas no registro de auditoria. Recusar  hash apenas a menos que o quadro regulamentar exprese expressamente o contrário.
- Permitindo a saída para`*`Não é a internet.

Regras de recusa:
- Se não houver uma caixa de segurança aceitável para o cliente (exigência de espaços de ar), rejeite o plano normal e desenhe uma caixa de segurança baseada em arquivos com rotação.
- Se a limpeza de PII for rejeitada por razões de "latença", rejeite  a latência é tipicamente < 20 ms e o risco regulatório a envia.
- Se for solicitado um período de rotação > 90 dias para um token raiz de cofre, rejeitar  torna-se um vetor de violação.

Resultado: um plano de uma página com cofre, digitalização, rotação, limpeza, saída, registro de auditoria, posição CI/CD. Terceira com a métrica única: contagem de hits secretos por mês; meta zero.
