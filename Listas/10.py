'''Utilizando listas faça um programa que faça 5 perguntas para 
uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime. Se a pessoa responder positivamente a 2 questões 
ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" 
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''


def interrogatorio():
    perguntas = [
        "Telefonou para a vítima?",
        "Esteve no local do crime?",
        "Mora perto da vítima?",
        "Devia para a vítima?",
        "Já trabalhou com a vítima?"
    ]
    respostas = []

    for pergunta in perguntas:
        resposta = input(pergunta + " (S/N): ").lower()
        if resposta == "s":
            respostas.append(1)
        else:
            respostas.append(0)

    pontuacao = sum(respostas)

    if pontuacao == 2:
        print("Você é Suspeito(a)!")
    elif 3 <= pontuacao <= 4:
        print("Você é Cúmplice!")
    elif pontuacao == 5:
        print("Você é o Assassino!")
    else:
        print("Você é Inocente!")


interrogatorio()
