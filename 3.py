'''Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um número: "))
numero3 = float(input("Digite um número: "))
numero4 = float(input("Digite um número: "))
media = (numero1 + numero2 + numero3 + numero4)/4
print("as notas sao {} {} {} {} e a media eh {:.2f}".format(
    numero1, numero2, numero3, numero4, media))
