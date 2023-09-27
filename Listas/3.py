'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela.'''


def notas1():
    notas = []

    for i in range(4):
        nota = float(input(f"{i+1}° nota: "))
        notas.append(nota)

    print(f"Essas sao suas notas: {notas}")

    media = sum(notas)/len(notas)
    print(f"Essa é sua media: {media}")


notas1()
