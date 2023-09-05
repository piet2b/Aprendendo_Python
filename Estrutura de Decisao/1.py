'''Faça um Programa que peça dois números e imprima o maior deles.'''

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite um numero: "))

if num1 > num2:
    print(f"Maior numero: {num1:.2f}")
else:
    print(f"Maior numero: {num2:.2f}")
