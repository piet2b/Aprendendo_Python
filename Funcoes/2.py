'''Faça um programa, com uma função que necessite de três argumentos, 
e que forneça a soma desses três argumentos.'''


def soma_tres_numeros(a, b, c):
    return a + b + c


def main():
    try:
        # Solicita ao usuário para fornecer três números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        num3 = float(input("Digite o terceiro número: "))

        # Chama a função e imprime o resultado
        resultado = soma_tres_numeros(num1, num2, num3)
        print(f"A soma dos três números é: {resultado}")

    except ValueError:
        print("Por favor, insira números válidos.")


if __name__ == "__main__":
    main()
