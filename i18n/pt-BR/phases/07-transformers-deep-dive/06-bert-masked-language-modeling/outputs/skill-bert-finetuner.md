---
name: bert-finetuner
description: Capacitar um ajuste fino do BERT para uma nova tarefa de classificação, extração ou recuperação.
version: 1.0.0
phase: 7
lesson: 6
tags: [bert, fine-tuning, nlp]
---

Dada uma tarefa a seguir (classificação / NER / recuperação / re-ranqueamento / NLI), tamanho dos dados rotulados e restrições de implantação (latencia, dispositivo), a saída:

1. Seleção de espinha dorsal. Nome do modelo (ModernBERT-base / grande, DeBERTa-v3, multilingue-e5, etc.) com uma razão de uma frase. Preferir ModernBERT para tarefas em inglês que exigem contexto ≤8K.
2. Especificações de cabeças: `[CLS]` → drop-out → linear(num_classes). NER: linear por token + CRF opcional. Retorno: mean-pool + contraste de perda.
3. Recepta de formação: Otimizador (AdamW, lr 2e-5 típico), aquecimento % (610%), épocas (35), tamanho do lote, fp16/bf16.
4. Plano de avaliação. métricas adequadas às tarefas (acurateza + F1 para classificação, nível de entidade F1 para NER, MRR/NDCG para recuperação). tamanho de divisão mantido.
5. Verificação de modo de falha. Um risco chamado: vazamento de rótulos, desequilíbrio de classes, truncamento de contexto, desajuste de tokenizer entre pré-estrato e corpos de sintonia.

Recusar-se a ajustar um BERT em saída gerativa (geração de texto)  recomendar um decodificador apenas em vez disso. Recusar-se a enviar um ajuste fino sem avaliação estratificada por classe quando a classe minoritária é inferior a 10%. Marque qualquer ajuste fino que descongelar a espinha dorsal completa com <1,000 exemplos rotulados como provável sobre-ajustado.
