'''Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.'''


def vetor1():
    vetor = []

    for i in range(10):
        numero = int(input(f"Digite o {i+1}° numero: "))
        vetor.append(numero)

    print("Numeros (ordem inversa): ")

    for numero in reversed(vetor):
        print(numero)


vetor1()
