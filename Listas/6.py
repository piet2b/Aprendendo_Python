'''Faça um Programa que peça as quatro notas de 10 alunos, 
calcule e armazene num vetor a média de cada aluno, imprima 
o número de alunos com média maior ou igual a 7.0.'''


def vetor1():
    notas = []
    alunos = []
    alunos_aprovados = []

    for i in range(10):
        nome = input("Digite nome do aluno: ")
        alunos.append(nome)

        for i in range(4):
            nota = float(input(f"Digite {i+1}° nota: "))
            notas.append(nota)

        media = sum(notas)/len(notas)

        if media >= 7:
            print(f"aluno {nome} foi aprovado")
            alunos_aprovados.append(nome)
        else:
            print(f"aluno {nome} nao foi aprovado")

    print("Total de alunos aprovados:", len(alunos_aprovados))
    print("Lista de alunos aprovados:", alunos_aprovados)


vetor1()
