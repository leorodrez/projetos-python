lista_compras = []
respostas_permitidas = 'ial'

while True:
    resposta = input('Selecione uma opção: ' + '\n' + '[i]nserir [a]pagar [l]istar ')
    if (resposta in respostas_permitidas) and (len(resposta) == 1):
        if (resposta == 'l') and (int(len(lista_compras)) == 0):
            print('Ainda não há itens para exibir')
        if resposta == 'i':
            valor = input('Valor: ')
            lista_compras.append(valor)
        if resposta == 'l':
            for indice,produto in enumerate(lista_compras):
                print(indice,produto)
        if resposta == 'a':
            indice_produto = input("Digite o índice do produto que deseja excluir: ")
            try:
                lista_compras.pop(int(indice_produto))
            except:
                print('Você deve indicar apenas números correspondentes da lista!')

    elif resposta == 'encerrar':
        break

    else:
        print("Selecione apenas uma das respostas possíveis")
        continue


print('O programa foi encerrado com sucesso')