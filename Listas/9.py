'''Foram anotadas as idades e alturas de 30 alunos. Faça um 
Programa que determine quantos alunos com mais de 13 anos 
possuem altura inferior à média de altura desses alunos.'''


def vetor1():
    idades = []
    alturas = []

    for i in range(30):
        idade = int(input("Digite sua idade: "))
        idades.append(idade)

        altura = float(input("Digite sua altura: "))
        alturas.append(altura)

    media = sum(alturas)/len(alturas)

    contagem = 0
    for i in range(30):
        if idades[i] > 13 and alturas[i] < media:
            contagem += 1

    print(
        f"Quantidade de alunos com mais de 13 anos e altura abaixo da media: {contagem}")


vetor1()
