'''Faça um Programa que leia um vetor de 5 números inteiros, 
mostre a soma, a multiplicação e os números.'''


def vetor1():
    vetor = []

    for i in range(5):
        numero = int(input(f"Digite o {i+1}° numero: "))
        vetor.append(numero)

    soma = sum(vetor)

    mult = 1
    for num in vetor:
        mult *= num

    print(f"Soma dos números: {soma}")
    print(f"Multiplicação dos números: {mult}")
    print(f"Números: {vetor}")
    print(f"Quantidade de números: {len(vetor)}")


vetor1()
