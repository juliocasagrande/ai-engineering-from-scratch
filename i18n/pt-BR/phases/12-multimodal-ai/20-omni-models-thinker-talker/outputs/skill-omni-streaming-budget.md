---
name: omni-streaming-budget
description: Dimensione um canal de voz de streaming Thinker-Talker (Qwen-Omni / Moshi / Mini-Omni) para um objetivo TTFAB e conjunto de recursos.
version: 1.0.0
phase: 12
lesson: 20
tags: [qwen-omni, moshi, mini-omni, streaming, ttfab, thinker-talker]
---

Dado um produto especificado por voz (target TTFAB, microfone sample rate, visão em sim/não, bilíngue, duplex completo) e uma restrição de computação (classe GPU, orçamento), dimensionar o Thinker-Talker pipeline.

Produzir:

1. Seleção de família de modelos: Moshi (melhor latência), Qwen2.5 Omni (melhor recurso aberto), Qwen3-Omni (qualidade de fronteira), Mini-Omni (mais simples).
2. Tamanhos de pensador e conversador. 7B Thinker + 200-300M Talker para < 400ms TTFAB. 70B+ Thinker para qualidade, aceitar TTFAB mais alto.
3. TTFAB desintegração. Estimação de latência componente por componente.
4. Modo duplex. Meio duplex com VAD de rotação como padrão; duplex completo se o produto requer backchannel.
5. Integração visual. TMRoPE com marcas de tempo absolutas para quadros de vídeo entrelaçados.
6. Forma de implantação: Single-GPU vs split (Thinker on A, Talker on B) com base nas necessidades de transferência.

Rejeitos duros:
- Proponho um 70B Talker, deve ser pequeno para acompanhar a taxa de sinalização de fala.
- Usando um decodificador de voz sem transmissão, o TTFAB explode.
- A reivindicação de duplex completo é plug-and-play.

Regras de recusa:
- Se atingir TTFAB < 200ms, recusar qualquer coisa maior que a classe Moshi (7B fusível) em um único A100.
- Se o produto requer geração de música em fluxo, rejeite essa arquitetura e recomenda um pipeline musical separado.
- Se a taxa de amostragem do microfone for de 48 kHz com qualidade rigorosa, sinalize a necessidade de um codificador de fala mais forte; não reduzir a amostragem cegamente.

Resultado: plano de streaming de uma página com escolha de modelo, tamanhos, desagregação TTFAB, modo duplex, estratégia de visão, implantação.
