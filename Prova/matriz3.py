# Defina a matriz 3x3
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Solicite ao usuário a linha e a coluna do item desejado
linha = int(input("Digite o número da linha (1 a 3): "))
coluna = int(input("Digite o número da coluna (1 a 3): "))

# Verifique se as entradas do usuário estão dentro dos limites válidos
if 1 <= linha <= 3 and 1 <= coluna <= 3:
    item_desejado = matriz[linha - 1][coluna - 1]
    print(
        f"O item da matriz na linha {linha} e coluna {coluna} é: {item_desejado}")
else:
    print("Entradas inválidas. Certifique-se de digitar números de linha e coluna de 1 a 3.")
