'''Tendo como dado de entrada a altura (h) de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

sexo = input("Seu sexo (Digite 'M' para masculino ou 'F' para feminino): ")
altura = float(input("Sua altura em metros: "))

if sexo.upper() == 'F':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = (72.7*altura) - 58

print("Seu peso ideal é {:.1f} kg".format(peso_ideal))
