---
name: provenance-audit
description: Auditar a cadeia de proveniência de uma implantação de conteúdo através de metadados de marcas de água e C2PA.
version: 1.0.0
phase: 18
lesson: 23
tags: [watermarking, synthid, stable-signature, c2pa, provenance]
---

Dado o desdobramento de conteúdos com uma alegação de proveniência, auditem a cadeia de proveniência.

Produzir:

1. Inventário de marcas de água. Enumera todas as modalidades (texto, imagem, áudio, vídeo) e a marca de água aplicada em cada uma.
2. Robustez da marca de água. Para cada marca de água, nome a classe adversária que sobrevive (compressão, corte, parafrase, afinidade). Limitações de bandeira por Kirchenbauer 2023 Seção 6 (parafrase) e "Signatura estável é instável" 2024 ( afinidade).
3. Cobertura C2PA. Os metadados C2PA estão anexados? A cadeia de assinatura é de uma identidade confiável? Os metadados podem ser despojados; a presença não é suficiente.
4. Detector transmodal. Existe um detector unificado em todas as modalidades (SynthID 2025) ou apenas específico de modalidade?
5. Alinhamento regulamentar. A implantação cumpre as obrigações de transparência previstas no artigo 50.o da Lei da UE relativa à IA (de agosto de 2026)?

Rejeitos duros:
- Qualquer alegação de "marca de água" sem um mecanismo e detector designados.
- Qualquer alegação de "autenticidade" baseada apenas na ausência de marca de água (modelo não marcado com marca de água ≠ autêntica).
- Qualquer alegação de origem de imagem sem uma avaliação do ataque de remoção de Fernandez 2024.

Regras de recusa:
- Se o usuário perguntar "isso irá detectar todo o conteúdo da IA", recusar a alegação binária; a marcação de água é específica do modelo.
- Se o utilizador solicitar uma solução de proveniência universal, recusar e apontar para a abordagem em camadas de marca de água + C2PA.

Resultado: uma auditoria de uma página preenchendo as cinco seções, sinalizando as lacunas de robustez por modalidade e nomeando o único controle adicional de maior valor. Cite SynthID (Google DeepMind), STABLE SIGNATURE (Fernandez et al. 2023), e C2PA uma vez cada.
