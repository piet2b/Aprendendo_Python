'''Utilize uma lista para resolver o problema a seguir. Uma empresa paga 
seus vendedores com base em comissões. O vendedor recebe $200 por semana 
mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um 
vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 
por cento de $3000, ou seja, um total de $470. Escreva um programa (usando 
um array de contadores) que determine quantos vendedores receberam salários 
nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante'''


def calcular_salario(vendas_brutas):
    salario_fixo = 200
    comissao_percentual = 0.09
    salario_total = salario_fixo + (comissao_percentual * vendas_brutas)

    return salario_total


def categorizar_salarios(salarios):
    intervalos = [0] * 9

    for salario in salarios:
        if 200 <= salario <= 299:
            intervalos[0] += 1
        elif 300 <= salario <= 399:
            intervalos[1] += 1
        elif 400 <= salario <= 499:
            intervalos[2] += 1
        elif 500 <= salario <= 599:
            intervalos[3] += 1
        elif 600 <= salario <= 699:
            intervalos[4] += 1
        elif 700 <= salario <= 799:
            intervalos[5] += 1
        elif 800 <= salario <= 899:
            intervalos[6] += 1
        elif 900 <= salario <= 999:
            intervalos[7] += 1
        else:
            intervalos[8] += 1

    return intervalos


num_vendedores = int(input("Digite o número de vendedores: "))
vendas_vendedores = []

for i in range(num_vendedores):
    vendas = float(input("Digite as vendas brutas do vendedor: "))
    salario = calcular_salario(vendas)
    vendas_vendedores.append(salario)

intervalos_salarios = categorizar_salarios(vendas_vendedores)

print("\nRelatório de Salários:")
for i in range(9):
    inicio_intervalo = i * 100 + 200
    fim_intervalo = inicio_intervalo + 99
    print(
        f"${inicio_intervalo} - ${fim_intervalo}: {intervalos_salarios[i]} vendedores")
