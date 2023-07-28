import os

palavra_secreta = 'cavalo'
chances = 0
letras_acertadas = ''

while True:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        chances += 1
        continue

    if len(letra_digitada) == 1:

        #posicao_letra = palavra_secreta.find(letra_digitada)

        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada

        palavra_formada = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'

    print(palavra_formada)

    chances += 1

    if palavra_formada == palavra_secreta:
        break

os.system('clear') #comando para limpar o Terminal

print('VOCÊ GANHOU PARABÉNS' + '\n' + 'A palavra era ' + palavra_secreta + '\n' + f'Tentativas: {chances}x')
