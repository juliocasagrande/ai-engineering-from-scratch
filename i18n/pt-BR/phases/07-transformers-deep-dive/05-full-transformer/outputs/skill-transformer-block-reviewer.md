---
name: transformer-block-reviewer
description: Revisar a implementação de blocos de transformadores em relação a erros de 2026 e à deriva de bandeira.
version: 1.0.0
phase: 7
lesson: 5
tags: [transformers, architecture, review]
---

Dada a fonte de bloco do transformador (PyTorch / JAX / numpy / pseudocode) e o seu papel pretendido (encodor / decodor / encodor-decodor), saída:

1. Verificação de cabos. pré-norma ou pós-norma. Conexões residuais em torno de cada subcamada. Bandeira pós-norma como não padrão para 2026, a menos que o autor indique o porquê.
2. Normalização. LayerNorm vs RMSNorm. RMSNorm preferido. Flag se termos de viés estão presentes em projeções Q / K / V / O  a maioria dos modelos 2026 os deixam cair.
3. Forma da atenção. MHA / GQA / MQA / MLA. Para blocos de decodificador: confirmação de que a máscara causal é aplicada. Para a atenção cruzada: confirmação de Q do decodificador, K/V do encodificador.
4. FFN. Ativação (ReLU / GELU / SwiGLU / GeGLU). Ratio de expansão. SwiGLU com ~ 2,67 × é padrão moderno; 4 × ReLU / GELU é clássico.
5. O sinal de posição: confirmação de que a RoPE/ALiBi/absoluto é aplicada quando esperado (normalmente projeções Q,K para a RoPE).

Recusar a assinatura em um bloco que apile mais de 12 camadas com pós-norma e nenhum cronograma de aquecimento  treinamento vai divergir. Recusar um bloco de decodificador sem enmascaramento causal. Marcar qualquer bloco cuja expansão FFN cai abaixo de 2x como provavelmente de capacidade. Avise se o bloco codificar-se com código rígido `d_model` sem um campo de configuração para dimensionamento de troca.
