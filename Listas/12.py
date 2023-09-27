'''Sua organização acaba de contratar um estagiário para trabalhar no 
Suporte de Informática, com a intenção de fazer um levantamento nas 
sucatas encontradas nesta área. A primeira tarefa dele é testar todos 
os cerca de 200 mouses que se encontram lá, testando e anotando o estado 
de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. 
O programa deverá receber um número indeterminado de entradas, cada uma contendo: 
um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; 
a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. 
Ao final o programa deverá emitir o seguinte relatório:'''


def relatorio_sucatas():
    defeitos = {
        "necessita da esfera": 0,
        "necessita de limpeza": 0,
        "necessita troca do cabo ou conector": 0,
        "quebrado ou inutilizado": 0
    }

    while True:
        identificacao = int(
            input("Número de identificação do mouse (ou 0 para encerrar): "))

        if identificacao == 0:
            break

        print("Tipos de defeito:")
        print("1 - Necessita da esfera")
        print("2 - Necessita de limpeza")
        print("3 - Necessita troca do cabo ou conector")
        print("4 - Quebrado ou inutilizado")

        opcao = int(input("Informe o número correspondente ao defeito: "))

        if opcao == 1:
            defeitos["necessita da esfera"] += 1
        elif opcao == 2:
            defeitos["necessita de limpeza"] += 1
        elif opcao == 3:
            defeitos["necessita troca do cabo ou conector"] += 1
        elif opcao == 4:
            defeitos["quebrado ou inutilizado"] += 1
        else:
            print("Opção inválida. Tente novamente.")

    print("\nRelatório de Sucatas:")
    for defeito, quantidade in defeitos.items():
        print(f"{defeito}: {quantidade} unidades")


relatorio_sucatas()
