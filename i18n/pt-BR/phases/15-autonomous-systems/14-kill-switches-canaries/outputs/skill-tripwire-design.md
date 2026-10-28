---
name: tripwire-design
description: Revisar a pilha de detectores de agentes proposta (interruptor de morte, interruptores de circuito, tokens canários) e sinalizar os fios triplo faltantes antes da primeira execução autônoma.
version: 1.0.0
phase: 15
lesson: 14
tags: [kill-switch, circuit-breaker, canary, honeytoken, detection-and-response]
---

Dado um conjunto de detectores proposto para a implantação de um agente, auditá-lo contra a referência de três detectores (interruptor de morte, interruptor de circuito, canário) e sinalize o que está faltando, mal sintonizado ou exposto ao agente.

Produzir:

1. **Kill-switch audit.** Confirme que as credenciais do agente não podem ativá-lo. Confirme que todas as ações consequentes verificam o interruptor, não apenas a inicialização. Confirme que a reatividade é uma ação humana explícita.
2. **Circuit-breaker inventory.** Lista todos os padrões que um relógio de interrupção observa (repetição, falhas consecutivas, taxa, ferramenta específica após leitura fora de confiança).
3. **Canary design.** Lista todos os tokens canários no ambiente. Para cada um: o que é (créditais falsos, registro DB falso, arquivo falso, entrada de memória falsa), onde vive, que acesso desencadeia o alarme, quem é paged. Confirme que nenhum canário tem uma razão legítima para ser tocado.
4. **Statistical + hard layering.** Confirme que a pilha utiliza pelo menos um limite de duração (estilo constitucional da lição 17) além de quaisquer detectores estatísticos (EWMA, pontuação z).
5. **Quarantine path.** O que acontece quando um detector dispara? parada completa de agente, pausa específica de caminho, redirecionamento de tráfego (eBPF / Cilium honeypot), apenas alerta. Confirme que o caminho foi testado de ponta a ponta pelo menos uma vez.

Rejeitos duros:
- Qualquer implantação sem um interruptor externo de eliminação.
- Tokens Canários armazenados em sistemas aos quais o agente tem acesso por escrito.
- Detecção apenas estatística, sem limites rígidos.
- Interruptores de circuito com descolerações que se reativam automaticamente sem revisão humana.
- Corridas sem supervisão onde o interruptor de execução é verificado apenas no início, não por ação.

Regras de recusa:
- Se o usuário não puder nomear os sistemas específicos fora das credenciais do agente que hospedam o switch de eliminação, recuse. "Usamos um arquivo de configuração que o agente lê" não é um switch de eliminação se o agente pode escrever arquivos de configuração.
- Se o utilizador tratar o classificador de modo automático (Lessão 10) como um substituto dos tripwires, rejeite.
- Se os canários propostos estiverem em sistemas, o agente tem motivos legítimos para ler, recusar e exigir um redesenho.

Formatos de saída:

Retorna uma auditoria de tripwire com:
- **Kill-switch line** (localização, cadência de verificação, procedimento de reativação)
- **Circuit-breaker table** (patrão, limiar, resfriamento)
- **Canary table** (token, localização, alarme, proprietário)
- **Layering note** (statísticas + limites de duração presentes y/n)
- **Quarantine flow** (o que incende, o que acontece, testado y/n)
- **Readiness** (produzir / montar / apenas para investigação)
