import time
import requests

cs = True
while cs:
    response = requests.get('http://127.0.0.1:5000/')
    print('\n\t\t\t\t\t\t\t\t\t\t######## ULTIMA ATUALIZAÇÃO DO CLIMA ########')
    print(f'#  {response.json()}  #')
    time.sleep(2)
    print('#' * 29)
    print('#\t1º) - BUSCAR POR ID   \t#')
    print('#\t2º) - BUSCAR POR DATA \t#')
    print('#\t3º) - BUSCAR TODOS    \t#')
    print('#\t4º) - CRIAR           \t#')
    print('#\t5º) - ATUALIZAR       \t#')
    print('#\t6º) - DELETAR         \t#')
    print('#\t7º) - SAIR            \t#')
    print('#' * 29)
    opt = int(input('Escolha uma das Opções: '))

    if opt == 1:
        print('\n\n\n\t\t#####################################################')
        print('\t\t#     Digite o ID do Clima que Deseja Buscar:       #')
        print('\t\t#####################################################')
        id = int(input('\t\tID: '))
        response = requests.get(f'http://127.0.0.1:5000/clima/{id}')
        if response.status_code == 200:
            print(f'\n\t\t# {response.json()} #\n\n')
            time.sleep(2)
        else:
            print('\n\t\t#######################')
            print('\t\t#  ID NÃO ENCONTRADO  #')
            print('\t\t#######################\n\n')
            time.sleep(2)

    if opt == 2:
        print('\n\n\n\t\t#######################################################')
        print('\t\t#     Digite a DATA do Clima que Deseja Buscar:       #')
        print('\t\t#######################################################')
        id = str(input('\t\DATA: '))
        response = requests.get(f'http://127.0.0.1:5000/clima/{id}')
        if response.status_code == 200:
            print(f'\n\t\t# {response.json()} #\n\n')
            time.sleep(2)
        else:
            print('\n\t\t#########################')
            print('\t\t#  DATA NÃO ENCONTRADO  #')
            print('\t\t#########################\n\n')
            time.sleep(2)

    elif opt == 3:
        response = requests.get('http://127.0.0.1:5000/clima/')
        print(f'\n\n\t\t{response.json()}\n\n')
        time.sleep(5)

    elif opt == 4:
        print('\n\n\t\tModelo para Criar')
        print('\t\t#########################')
        print('\t\t#Umidade:    00         #')
        print('\t\t#Chuva:      00         #')
        print('\t\t#Celsius:    00         #')
        print('\t\t#Fahrenheit: 00         #')
        print('\t\t#kelvin:     00         #')
        print('\t\t#Data:       0000-00-00 #')
        print('\t\t#Hora:       00:00:00   #')
        print('\t\t#########################\n')
        umidade = int(input('\t\tUmidade: '))
        chuva = int(input('\t\tChuva: '))
        celsius = int(input('\t\tCelsius: '))
        print(f'\t\tfahrenheit: {32 + (celsius * 1.8)}')
        print(f'\t\tkelvin: {celsius + 272}')
        data = input('\t\tData: ')
        hora = input('\t\tHora: ')
        print('\n\n')
        dados = {
            "umidade": umidade,
            "chuva": chuva,
            "celsius": celsius,
            "fahrenheit": 32 + (celsius * 1.8),
            "kelvin": celsius + 272,
            "data": data,
            "hora": hora
        }
        response = requests.post(f'http://127.0.0.1:5000/clima/', json=dados)
        if response.status_code == 200:
            print('\n\t\t#############################')
            print('\t\t#  CADASTRADO COM SUCESSO!  #')
            print('\t\t#############################\n\n')
            time.sleep(2)
        else:
            print('\n\t\t########################')
            print('\t\t#  FALHA AO CADASTRAR  #')
            print('\t\t########################\n\n')
            time.sleep(2)


    elif opt == 5:
        print('\t\tQual Clima Deseja Atualizar? Digite o ID')
        id = int(input("\t\tID: "))
        response = requests.get(f'http://127.0.0.1:5000/clima/{id}')
        if response.status_code == 200:
            print(f'\n\t\t# {response.json()} #')
            celsius = int(input('\t\tCelsius: '))
            chuva = int(input('\t\tChuva: '))
            data = input('\t\tData: ')
            print(f'\t\tfahrenheit: {32 + (celsius * 1.8)}')
            hora = input('\t\tHora: ')
            print(f'\t\tkelvin: {celsius + 272}')
            umidade = int(input('\t\tUmidade: '))
            print('\n\n')
            dados = {
                "umidade": umidade,
                "chuva": chuva,
                "celsius": celsius,
                "fahrenheit": 32 + (celsius * 1.8),
                "kelvin": celsius + 272,
                "data": data,
                "hora": hora
            }
            requests.put(f'http://127.0.0.1:5000/clima/{id}', json=dados)
            print('\n\t\t#################################')
            print('\t\t#  CLIMA ALTERADO COM SUCESSO!  #')
            print('\t\t#################################\n\n')
            time.sleep(2)
        else:
            print('\n\t\t#######################')
            print('\t\t#  ID NÃO ENCONTRADO  #')
            print('\t\t#######################\n\n')
            time.sleep(2)

    elif opt == 6:
        request_clima = requests.get('http://127.0.0.1:5000/clima/')
        print(f'\t\t# {request_clima.json()} #')
        print('\n\n\n\t\t#####################################################')
        print('\t\t#     Digite o ID do Clima que Deseja Excluir:      #')
        print('\t\t#####################################################')
        id = int(input('\t\tID: '))
        response = requests.get(f'http://127.0.0.1:5000/clima/{id}')
        if response.status_code == 200:
            print(f'\n\t\t# {response.json()} #')
            requests.delete(f'http://127.0.0.1:5000/clima/{id}')
            print('\n\t\t#######################################')
            print('\t\t#     CLIMA DELETADO COM SUCESSO!     #')
            print('\t\t#######################################\n\n')
            time.sleep(2)
        else:
            print('\n\t\t#######################')
            print('\t\t#  ID NÃO ENCONTRADO  #')
            print('\t\t#######################\n\n')
            time.sleep(2)

    elif opt == 7:
        print('ATÉ MAIS!')
        cs = False

    else:
        print('\n\t\t#######################')
        print('\t\t#   OPÇÃO INVALIDA!   #')
        print('\t\t#######################\n\n')
        time.sleep(2)
