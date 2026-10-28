---
name: prompt-api-troubleshooter
description: Diagnose and fix common AI API errors (auth, rate limits, timeouts)
phase: 0
lesson: 4
---

Quando alguém compartilha um erro, identifica a causa e dá a correção.

Erros e correções comuns:

- **401 Unauthorized**: A chave API está errada ou faltando. Verifique se a variável ambiente está definida e a chave é válida.
- **403 Forbidden**A chave API não tem permissão para este endpoint ou modelo.
- **429 Too Many Requests**Esperar e tentar novamente, ou reduzir a frequência de solicitação.
- **400 Bad Request**Corpo de pedido está malformado. Verifique os campos necessários, ortografia do nome do modelo, formato da mensagem.
- **500/502/503**Um problema do lado do servidor.
- **Timeout**Requerem muito tempo. Reduzir max_tokens ou usar streaming.
- **Connection refused**: URL base errada ou problema de rede. Verifique o endpoint URL.

Pasos de diagnóstico:
1. A chave da API está definida?`echo $ANTHROPIC_API_KEY | head -c 10`
2. A chave é válida?
3. O formato da solicitação é correto?
4. Há algum problema de rede?`curl -I https://api.anthropic.com`
