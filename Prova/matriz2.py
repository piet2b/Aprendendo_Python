# Defina a matriz 3x3
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Exiba a matriz
print("A matriz 3x3 é:")
for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=" ")
    print()  # Quebra de linha para imprimir a próxima linha da matriz
