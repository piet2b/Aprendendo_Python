'''Faça um Programa para uma loja de tintas. O programa deverá pedir 
o tamanho em metros quadrados da área a ser pintada. Considere que a 
cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a 
tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões
de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os 
respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
considere latas cheias.'''

import math

# Definir constantes
METROS_POR_LITRO = 6
CAPACIDADE_LATA = 18
CAPACIDADE_GALAO = 3.6
PRECO_LATA = 80.00
PRECO_GALAO = 25.00
FOLGA = 1.10

# Solicitar a área a ser pintada em metros quadrados
area_a_ser_pintada = float(
    input("Digite o tamanho em metros quadrados da área a ser pintada: "))

# Calcular a quantidade de tinta necessária em litros
quantidade_tinta_litros = (area_a_ser_pintada / METROS_POR_LITRO) * FOLGA

# Calcular a quantidade de latas necessárias e o custo
latas_necessarias = math.ceil(quantidade_tinta_litros / CAPACIDADE_LATA)
custo_latas = latas_necessarias * PRECO_LATA

# Calcular a quantidade de galões necessários e o custo
galoes_necessarios = math.ceil(quantidade_tinta_litros / CAPACIDADE_GALAO)
custo_galoes = galoes_necessarios * PRECO_GALAO

# Calcular a combinação ideal de latas e galões para minimizar o custo
comb_latas = math.floor(quantidade_tinta_litros / CAPACIDADE_LATA)
resto_litros = quantidade_tinta_litros - (comb_latas * CAPACIDADE_LATA)
comb_galoes = math.ceil(resto_litros / CAPACIDADE_GALAO)
custo_combinacao = (comb_latas * PRECO_LATA) + (comb_galoes * PRECO_GALAO)

print(
    f"Quantidade necessária de tinta em litros: {round(quantidade_tinta_litros):.2f}L")
print(
    f"Opção 1: Comprar {latas_necessarias} latas de 18 litros por R$ {custo_latas:.2f}")
print(
    f"Opção 2: Comprar {galoes_necessarios} galões de 3,6 litros por R$ {custo_galoes:.2f}")
print(
    f"Opção 3: Misturar {comb_latas} latas e {comb_galoes} galões por R$ {custo_combinacao:.2f}")
