# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


def problema_matematica(num_pergunta):
    pergunta = perguntas[num_pergunta]
    pergunta = pergunta['Pergunta']
    print(pergunta)

    opcoes = perguntas[num_pergunta]
    opcoes = opcoes['Opções']
    for indice,numero in enumerate(opcoes):
        print(f'{indice}) {numero}')

    resposta = input('Escolha uma opção: ')
    resposta_correta = perguntas[num_pergunta]
    resposta_correta = resposta_correta['Resposta']
    if resposta == resposta_correta:
        print('Acertou!')
    else:
        print('Errou!')


problema_matematica(0)
problema_matematica(1)
problema_matematica(2)