while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-*/): ')
    numeros_validos = None #flag para determinar uma condição ao longo do código
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Erro! Digite apenas números!")
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Erro!Escolha apenas entre os quatro operadores mencionados')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if operador == '+':
        print(f'O resultado é: {num_1_float + num_2_float}')
    elif operador == '-':
        print(f'O resultado é: {num_1_float - num_2_float}')
    elif operador == '*':
        print(f'O resultado é: {num_1_float * num_2_float}')
    elif operador == '/':
        print(f'O resultado é: {num_1_float / num_2_float}')
    else:
        print('Nunca deveria chegar até aqui')

    sair = input('Deseja sair agora? Pressione [s] para Sim ').lower().startswith('s') #você pode incluir vários métodos dentro de uma variável ao mesmo tempo.

    if sair is True:
        print('Usuário saiu')
        break