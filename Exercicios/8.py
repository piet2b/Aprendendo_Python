'''Faça um Programa que pergunte quanto você ganha por hora e 
o número de horas trabalhadas no mês. Calcule e mostre o total 
do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
faça um programa que nos dê:
- salário bruto.
- quanto pagou ao INSS.
- quanto pagou ao sindicato.
- o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : 
- IR (11%) : 
- INSS (8%) : 
- Sindicato ( 5%) : 
= Salário Liquido : 
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

horas = float(input("Horas trabalhadas: "))
valor = float(input("Quanto voce ganha por hora: "))

salario_bruto = horas * valor

inss = 0.11 * salario_bruto
ir = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto

descontos = inss + ir + sindicato
salario_liquido = salario_bruto - descontos

print(f"+ Salário Bruto: R${salario_bruto:.2f}")
print(f"- IR (11%): R${ir:.2f}")
print(f"- INSS (8%): R${inss:.2f}")
print(f"- Sindicato (5%): R${sindicato:.2f}")
print(f"= Salário Líquido: R${salario_liquido:.2f}")
