---
name: skill-cmer-monitor
description: Instrumentos de produção VLM ponto final com monitoramento de taxa de erro transmodal, painéis de controle e alertas
version: 1.0.0
phase: 4
lesson: 25
tags: [vlm, production, monitoring, hallucination]
---

# Monitor CMER

Tratar o alinhamento trans-modal como um KPI de produção de primeira classe.

## Quando utilizar

- Deploição de qualquer ponto final de VLM que produz texto baseado em imagens.
- Investigar relatórios de respostas alucinadas.
- Seguimento de se uma mudança de distribuição de entrada degrada a fixação do modelo.

## Input

- `vlm_output`: texto gerado.
- `text_confidence`: probabilidade média por token após softmax, em `[0, 1]`- Calcule como `exp(mean(log_probs))`Não passe em logits brutos; logits brutos são ilimitados e `conf_threshold` - Supõe uma probabilidade.
- `image_embedding`: Embedamento da imagem na família CLIP (DINOv3, SigLIP, CLIP).
- `text_embedding`: Embedamento de texto gerado na família CLIP.
- Opcional `prompt_type`: etiqueta para agrupamento (vqa / ocr / subtítulos / agente).

## Calculação por pedido

```python
import torch

def cmer_flag(image_emb, text_emb, text_conf, sim_thr=0.25, conf_thr=0.8):
    if image_emb.shape != text_emb.shape:
        raise ValueError(f"emb shape mismatch: {image_emb.shape} vs {text_emb.shape}")
    image_emb = image_emb / (image_emb.norm() + 1e-8)
    text_emb = text_emb / (text_emb.norm() + 1e-8)
    sim = float((image_emb * text_emb).sum())
    flagged = (text_conf > conf_thr) and (sim < sim_thr)
    return {"sim": sim, "flagged": flagged}
```

Os incorporados são tensores PyTorch 1-D (`torch.float32`Se você usar matrizes NumPy, trocar `.norm()` para `np.linalg.norm(...)` E lançar a saída em conformidade.

Loja `sim`- Não . `text_conf`- Não . `flagged`- Não . `prompt_type`- Não . `timestamp`- Não . `model_version`- Não . `request_id` O seu canal de monitoramento (Prometheus, DataDog, OpenTelemetry).

## Metrica agregada

```
CMER = (flagged requests in window) / (total requests in window)
```

Relatório por ponto final, por tipo de prompt, por versão de modelo.

## Limite de alarme

- CMER de base: estabelecer um período normal de tráfego superior a 7 dias.
- Aviso: CMER >= 1,5x do valor de base durante 1 hora.
- Critical: CMER >= 2x linha de base durante 30 minutos ou > 15% absoluta para qualquer janela.

## Painéis de painel

1. CMER ao longo do tempo (5 minutos de espera, 7 dias de espera).
2. CMER por tipo prompt_type (barra empilhada).
3. Distribuição de `sim` por hora (histograma).
4. Resultados de alucinação superiores (prova de 20 respostas marcadas por dia para revisão humana).

## Ações quando o CMER aumenta

1. Amostra das solicitações marcadas.
2. Verificar que a versão do modelo não tenha sido alterada inadvertidamente.
3. Verifique a distribuição de entrada (novos formatos de arquivo? nova fonte de imagem? comprimido de forma diferente?).
4. Envia o tráfego afetado para revisão humana até que o pico se resolva.
5. Se o ponto for persistente, ajuste o modelo ou substitua-o; não suprima o alerta.

## Regras

- Nunca compute CMER usando as próprias incorporações do VLM; use um codificador independente (DINOv3, SigLIP ou CLIP-L/14). Caso contrário, você está medindo a autoconsistência do modelo, não o alinhamento.
- Sempre registar o crudo `sim` O valor, não só o `flagged` Bit; as mudanças de distribuição aparecem no quartilo inferior antes das alterações na taxa de bandeira.
- Não enviar um ponto final VLM sem monitoramento CMER; as alucinações são o modo dominante de falha de produção e silenciosas sem esta métrica.
- Para domínios sensíveis (médicos, jurídicos, financeiros), aumentar `sim_threshold` para 0,35 ou mais; a condição de bandeira é `sim < sim_threshold`, de modo que um limiar mais elevado capta mais saídas como potencialmente sem fundamento  o padrão certo para o uso de riscos elevados.
