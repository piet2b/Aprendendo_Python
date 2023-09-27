'''Faça um Programa que leia dois vetores com 10 elementos cada. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser 
compostos pelos elementos intercalados dos dois outros vetores.'''


def vetorIntercalado(vetor1, vetor2):
    vetorIntercalado = []

    for i in range(10):
        vetorIntercalado.append(vetor1[i])
        vetorIntercalado.append(vetor2[i])

    return vetorIntercalado


vetor1 = []
vetor2 = []

print("Primeiro vetor")
for i in range(10):
    num = int(input("Digite o numero: "))
    vetor1.append(num)

print("Segundo vetor")
for i in range(10):
    num = int(input("Digite numero: "))
    vetor2.append(num)

vetor_intercalado = vetorIntercalado(vetor1, vetor2)

print("Vetores intercalados: ", vetor_intercalado)
