'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

num1 = float(input("Digite numero 1: "))
num2 = float(input("Digite numero 2: "))
num3 = float(input("Digite numero 3: "))

# Cria uma lista com os números
numeros = [num1, num2, num3]

# Ordena a lista em ordem decrescente
numeros.sort(reverse=True)

print("Números em ordem decrescente:")
#  loop For
for numero in numeros:
    # Percorre a lista numeros
    print(numero)
