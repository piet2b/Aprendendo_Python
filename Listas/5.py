'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.'''


def vetor1():
    vetor = []
    par = []
    impar = []

    for i in range(20):
        numero = int(input(f"Digite o {i+1}° numero: "))
        vetor.append(numero)

        if numero % 2 == 0:
            par.append(numero)
        else:
            impar.append(numero)

    print("Todos os números:", vetor)
    print("Números pares:", par)
    print("Números ímpares:", impar)


vetor1()
