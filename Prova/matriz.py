# Inicialize uma matriz 3x3 com zeros
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Solicite os elementos da matriz do usuário
for i in range(3):
    for j in range(3):
        matriz[i][j] = float(
            input(f"Digite o elemento da linha {i + 1}, coluna {j + 1}: "))

# Exiba a matriz
print("A matriz 3x3 digitada é:")
for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=" ")
    print()  # Quebra de linha para imprimir a próxima linha da matriz
