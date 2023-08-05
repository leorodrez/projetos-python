def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

resultado = multiplica(4,5,7,8,4,3)
print(resultado)

print(4*5*7*8*4*3)



def par_impar(numero):
    if numero % 2 == 0:
        return 'É par!'
    else:
        return 'É ímpar!'

print(par_impar(7885297))