'''Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido'''

# Lista com os nomes dos dias da semana
dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

# Solicita número de 1 a 7
numero = int(
    input("Digite um número (1 a 7) para representar o dia da semana: "))

if numero >= 1 and numero <= 7:
    # Acessa o dia correspondente na lista
    dia_correspondente = dias[numero - 1]
    # Exibe o número e o nome do dia correspondente
    print(f"{numero} - {dia_correspondente}")
else:
    # Número estiver fora do intervalo
    print("Valor inválido. Por favor, digite um número de 1 a 7 para representar o dia da semana.")
