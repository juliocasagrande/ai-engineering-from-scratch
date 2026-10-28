# Quadro de tarefas: evitar endereços de e-mail duplicados durante o registro

Status: Pronto

## Factos de repositório
- Conta escreve uso AccountStore (`app/accounts.py:18`)
- Erros duplicados de utilização status 409 (`tests/test_accounts.py:44`)

## Caminhos permitidos
- `app/accounts.py`
- `tests/test_accounts.py`

## Caminhos proibidos
- `migrations/**`
- `deploy/**`

## Evidências de aceitação
- `python3 -m unittest tests.test_accounts`

## Desconhecidos
- Se a comparação de e-mail é insensivel ao caso
