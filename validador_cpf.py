#cpf = '746.824.890-70'
cpf = '298.051.180-37'
indice = 0
contagem = 10
numero_final = 0


###### SEPARANDO A STRING #######

nove_digitos = cpf[0:len(cpf)-3]
nove_digitos = nove_digitos.split('.')
nove_digitos = ''.join(nove_digitos)


###### CHECAGEM DE DADOS #######

if nove_digitos == cpf[0]*len(nove_digitos):
    print('CPF inválido! Os números são iguais')
else:
###### CALCULAR O PRIMEIRO DÍGITO #######
    for numeros in nove_digitos:
        numeros = int(numeros)
        numeros = numeros*contagem
        contagem -= 1
        numero_final += numeros

primeiro_digito = numero_final % 11

primeiro_digito = 0 if primeiro_digito < 2 else 11 - primeiro_digito

###### CALCULAR O SEGUNDO DÍGITO #######

primeiro_digito_str = str(primeiro_digito)
dez_digitos = nove_digitos + primeiro_digito_str

contagem = 11
numero_final_2 = 0

for numeros in dez_digitos:
    numeros = int(numeros)
    numeros = numeros * contagem
    contagem -= 1
    numero_final_2 += numeros


segundo_digito = numero_final_2 % 11

segundo_digito = 0 if segundo_digito < 2 else 11 - segundo_digito

print(f'Os numeros finais do CPF são {primeiro_digito} e {segundo_digito}')

###### VALIDANDO O CPF #######

ultimos_numeros_cpf = cpf[len(cpf)-2:len(cpf)]

primeiro_digito = str(primeiro_digito)
segundo_digito = str(segundo_digito)

if ultimos_numeros_cpf == primeiro_digito + segundo_digito:
    print('CPF válido!')
else:
    print('CPF inválido')

