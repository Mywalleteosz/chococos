from eospy import eosapi, keys

# Конфигурация узла EOS
eosapi.set_nodes(['http://api.eosnewyork.io'])

# Приватный ключ аккаунта, который отправляет транзакцию
sender_private_key = '5Jq88WjnJTjP4ZuuujAiXapbxs8Jj1XH1CdSBtYWvkBQuQK6sbn'

# Публичный ключ аккаунта, которому предоставляются полномочия
receiver_public_key = 'EOS6AZJomGL88BoXtWFQfcQswVenHso2pvAj5cr3T5mHCBSuHKHno'

# Имя контракта для управления полномочиями (например, eosio)
contract_account = 'eosio'

# Имя аккаунта, которому предоставляются полномочия
receiver_account = 'mywalleteosx'

# Создание объекта транзакции
transaction = eosapi.gen_transaction()

# Добавление действия для объявления полномочий
action = {
    'account': contract_account,
    'name': 'delegatebw',
    'authorization': [{
        'actor': 'mywalleteosx',
        'permission': 'active',
    }],
    'data': {
        'from': 'mywalleteosx',
        'receiver': receiver_account,
        'stake_net_quantity': '1.0000 EOS',  # количество EOS для стейкинга сети
        'stake_cpu_quantity': '1.0000 EOS',  # количество EOS для стейкинга CPU
        'transfer': 0,  # флаг, указывающий, что нет необходимости переводить токены
    }
}

# Добавление действия к транзакции
eosapi.add_action(transaction, action)

# Подготовка транзакции (с подписью)
eosapi.prepare_transaction(transaction)

# Получение подписи для транзакции
signature = eosapi.sign_transaction(transaction, sender_private_key)

# Добавление подписи к транзакции
eosapi.add_signature(transaction, signature, 'mywalleteosx')

# Отправка транзакции
response = eosapi.push_transaction(transaction)

print(response)
