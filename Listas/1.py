'''Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.'''


def vetor1():
    vetor = []

    for i in range(5):
        numero = int(input(f"Digite o {i + 1}° numero: "))
        vetor.append(numero)

    print("numeros no vetor: ")

    for numero in vetor:
        print(numero)


vetor1()
