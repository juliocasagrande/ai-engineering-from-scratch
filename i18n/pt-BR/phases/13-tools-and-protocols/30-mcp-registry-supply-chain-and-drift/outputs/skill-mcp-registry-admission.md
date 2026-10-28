---
name: mcp-registry-admission
description: Admit, pin, monitor, quarantine, and roll back an MCP Registry release with supply chain evidence.
version: 1.0.0
phase: 13
lesson: 30
tags: [mcp, registry, provenance, admission, drift, rollback]
---

Dado uma resposta do Registro MCP, uma identidade verificada do editor, evidências de artefatos, uma observação ao vivo do servidor e uma política local, produzem uma decisão de admissão e um pacote de evidências.

## Introduções necessárias

- Fonte de registo, registro do servidor, metadados gerenciados pelo Registo e tempo de recuperação.
- Espaço de nomes verificado e o método de autenticação que o estabeleceu.
- Registro de embalagens, identificador, versão exacta, resultado de propriedade e digestão calculada de artefatos.
- Viva .`server/discover`Resultados, versões de protocolo, capacidades, informações do servidor de diagnóstico e descriptórios completos de ferramentas.
- Capacidades exigidas, propriedades proibidas de ferramentas, revisores, retenção de evidências e política de retrocesso.
- Pins admitidos anteriormente, rotas atuais, quarentena e observações recentes de saúde.

## Procedimento

1. Validar a forma do registro Registry. Requer um nome, versão, descrição não vazio e pelo menos um pacote ou remoto. Trata a versão do esquema do Registro e a versão do protocolo MCP ao vivo como valores independentes.
2. Leia o status gerenciado pelo Registo a partir do nível de resposta `_meta["io.modelcontextprotocol.registry/official"].status`Não de forma direta .`_meta.status`Rejeitar a admissão automática, a menos que o status seja`active`- Não .
3. Compare o namespace exatamente com o namespace estabelecido por autenticação confiável. Rejeita prefixos looklikes e slugs vazios.
4. Junte-se a uma fonte de execução declarada para evidências verificadas. Para um pacote, correspondência do tipo de registro, identificador, versão exata e transporte. Para um registro remoto apenas, correspondência URL e transporte para evidências de endpoint verificadas de forma independente. Requer um digestão de evidências SHA-256 confiável para qualquer fonte.
5. Hash o registro canônico do Registro. Hash um objeto de origem que se une à fonte do Registro, nome do servidor, versão do Registro, digest de registro, fonte selecionada e digest de evidências de fonte.
6. Observe o endpoint ao vivo. Requer uma versão de protocolo aceita, recursos necessários e descriptórios completos de ferramentas. Preserva o resultado `_meta["io.modelcontextprotocol/serverInfo"]`Apenas para exibição, registos e depuração. Nunca use auto-relatado `serverInfo`, incluindo um alias direto apenas, como autoridade de admissão ou de segurança.
7. Normalize apenas coleções semânticamente não ordenadas. Hash a superfície completa do descrito normalizado para que um nome, descrição, esquema, anotação ou mudança de conjunto de ferramentas crie deriva.
8. Aplique autorização local, dados, rede e política de revisão.
9. Após aprovação, armazenar um pin imutável contendo registros, fonte de execução, proveniência e digestões de conjunto de ferramentas.
10. Adicionar a decisão, razões, referências de evidências, hash do livro de contabilidade anterior e hash da entrada atual ao livro de contabilidade de admissão.
11. Reconciliar o status do Registro e os descritores ao vivo em um cronograma e antes da ativação. Quarantena e desativa um pin quando o status se torna depreciado ou excluído, sua evidência fonte muda ou seu comportamento ao vivo difere. Um pin em quarentena nunca é um alvo de retrocesso.
12. Registrar a restauração da rota como um novo evento. Nunca reescrever uma publicação antiga ou decisão de admissão.

## Rejeitos duros

- Confiança derivada apenas de um nome familiar ou presença do Registo.
- `startswith`Verificações de espaço de nomes ou um espaço de nomes reivindicado apenas pelo registro apresentado.
- `latest`, variedades de versões, ou coordenadas de pacotes sem digestão de artefatos.
- Os campos de editor que imitam o status ou a verificação gerenciados pelo Registo.
- Falta ou falha de protocolo, capacidade ou evidência descritiva.
- Tratamento de auto-relatores `serverInfo`como espaço de nome, proveniência, ponto de destino ou autoridade de admissão.
- Atualizações do pin de descriptório silencioso após a deriva.
- Ativação de versões ultrapassadas, excluídas, desconhecidas ou em quarentena.
- Voltar para um alvo sem provas completas de admissão.
- Evidências do livro-razão contendo tokens de portador, cookies, credenciais de pacote ou argumentos de ferramentas desnecessários.

## Produção

Retorna estas secções:

1. Decisão: `approve`- Não .`reject`, ou `quarantine`, com códigos de razão estáveis.
2. Proof of namespace: espaço de nomes verificado, fonte de autenticação e comparação de nomes exatos.
3. Pin de publicação: fonte de registro, nome do servidor, versão exata, status, versão de esquema e digestão de registro.
4. Pin de fonte: coordenada do pacote e transporte ou URL remoto e transporte, referência de resultados de propriedade e digestão de evidências da fonte.
5. Pin de execução: versão de protocolo aceita, recursos necessários, digestão de conjunto de ferramentas e diagnóstico opcional `serverInfo`- Não .
6. Provenance Join: os campos canônicos e a proveniência resultante.
7. Resultados da política: cada controlo aprovado, falhado e não aplicável.
8. Evento do Ledger: sequência, tempo, evento, resultado, códigos de razão, referências de evidências, hash anterior e hash de entrada.
9. Plano de Reconciliação: próximo estado, artefato, descoberta, descriptório e verificações de saúde.
10. Planos de reestruturação: pin prévio elegível, etapas de validação, alteração de rota, janela de saúde e evidências para reter.

Se não faltarem os fatos necessários, indicar o próximo teste de deriva programado.
