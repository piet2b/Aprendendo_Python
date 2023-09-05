'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

letra = input("Digite uma letra: ").lower()

if letra.isalpha() and len(letra) == 1:
    if letra in 'aeiou':
        print("É uma vogal.")
    else:
        print("É uma consoante.")
else:
    print("Por favor, digite apenas uma única letra.")
