'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
Imprima as consoantes.'''


def vetor1():
    vetor = []

    for i in range(10):
        charact = input(f"Digite o {i+1}° charactere: ")
        vetor.append(charact)

    consoantes = [c for c in vetor if c.isalpha() and c.lower() not in 'aeiou']

    print(f"Consoantes: {consoantes}")
    print(f"Total de consoantes: {len(consoantes)}")


vetor1()
