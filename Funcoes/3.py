'''Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.'''


def pn(n):
    if n > 0:
        print('Positivo')
    elif n == 0:
        print('Nulo')
    else:
        print('Negativo')


print('POSITIVO OU NEGATIVO')
n = int(input('digite um número: '))
print('Este número é', end=' ')
pn(n)
