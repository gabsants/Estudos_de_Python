'''
    Esse programa possui uma calculadora de expressões frequentemente utilizadas onde o usuário pode escolher entre 3 opções: Regra de Três, Média e Porcentagem, dentre outras sub_opções. O programa é interativo e proporciona que o usuário realize os cálculos de forma dinâmica ao isnerir os valores desejados. O programa também lida com entradas inválidas para evitar erros durante a execução.

'''
'''
    O programa foi estruturado utilizando funções para cada opção do menu.
    Foram importados o 'time' para pausas em determinadas áreas do código e 'statistics' para otimização de cálculos de média. O loop 'while' permite o retorno ao menu principal após a execução de cada operação e finalizado ao escolher o [0] para sair da execução.
    As listas criadas dentro de determinadas operações facilitam a manipulação e o cálculo dos valores inseridos pelo usuário. Dentre outras diversas melhorias que foram implementadas para otimizar o código e proporcionar uma melhor experiência ao usuário.

    '''
from time import sleep
import statistics 

def opcao_1():# Regra de Três Simples
    print("\n" + "="*50)
    print("REGRA DE TRÊS SIMPLES")
    print("="*50)
    print("\nConsidere que : A está para B assim como C está para X.\n")

    try:
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        c = float(input("Digite o valor de C: "))
       
        print("\n" + "-"*50)
        if a == 0:
            print("❌ ERRO: O valor de A não pode ser zero!")
            print("-"*50)
            return
        
        resultado = (b * c) / a
        print(f"✓ O valor de X é: {resultado:.2f}")
        print("-"*50 + "\n")

    except ValueError:
        print("\n" + "-"*50)
        print("❌ ERRO: Entrada inválida. Por favor, insira apenas números.")
        print("-"*50 + "\n")

def opcao_2():# Média
    try:
        print("\n" + "="*50)
        print("CÁLCULO DE MÉDIAS")
        print("="*50)
        print("\nEscolha o tipo de média:")
        print(" 1 - Média Aritmética")
        print(" 2 - Média Ponderada")
        print(" 3 - Mediana\n")

        escolha = int(input("Digite a opção desejada: "))

        if escolha not in [1, 2, 3]:
            print("\n" + "-"*50)
            print("❌ Opção inválida. Por favor, escolha uma opção válida.")
            print("-"*50 + "\n")
            return
        
        n = int(input("\nQuantos números deseja calcular a média? "))

        if n <= 0:
            print("\n" + "-"*50)
            print("❌ ERRO: A quantidade de números deve ser maior que zero.")
            print("-"*50 + "\n")
            return

        notas = []

        for i in range(n):
            num = float(input(f"Digite o {i + 1}° número: "))
            notas.append(num)

        print("\n" + "-"*50)
        if escolha == 1: 
            media_aritmetica = statistics.mean(notas)
            print(f"✓ Média Aritmética: {media_aritmetica:.2f}")
        elif escolha == 2:
            pesos = []
            print("\nAgora digite os pesos correspondentes:")
            for i in range(n):
                peso = float(input(f"Peso do {i + 1}° número: "))
                pesos.append(peso)

            media_ponderada = statistics.fmean(notas, weights=pesos)
            print(f"✓ Média Ponderada: {media_ponderada:.2f}")
        elif escolha == 3:
            mediana = statistics.median(notas)
            print(f"✓ Mediana: {mediana:.2f}")
        
        print("-"*50 + "\n")
       
    except ValueError:
        print("\n" + "-"*50)
        print("❌ ERRO: Entrada inválida. Por favor, insira apenas números.")
        print("-"*50 + "\n")

def opcao_3():# Porcentagem
    try:
        print("\n" + "="*50)
        print("CÁLCULO DE PORCENTAGEM")
        print("="*50)
        print("\nEscolha o tipo de cálculo:")
        print(" 1 - Desconto")
        print(" 2 - Aumento")
        print(" 3 - Apenas a porcentagem\n")
        
        escolha = int(input("Digite a opção desejada: "))

        if escolha not in [1, 2, 3]:
            print("\n" + "-"*50)
            print("❌ Opção inválida. Por favor, escolha uma opção válida.")
            print("-"*50 + "\n")
            return 
        
        valor = float(input("\nDigite o valor: R$ "))
        porcentagem = float(input("Digite a porcentagem (%): "))

        print("\n" + "-"*50)
        if escolha == 1:
            desconto = valor * porcentagem / 100
            print(f"Valor original: R$ {valor:.2f}")
            print(f"Desconto ({porcentagem}%): R$ {desconto:.2f}")
            print(f"✓ Valor final: R$ {valor - desconto:.2f}")
        elif escolha == 2:
            aumento = valor * porcentagem / 100
            print(f"Valor original: R$ {valor:.2f}")
            print(f"Aumento ({porcentagem}%): R$ {aumento:.2f}")
            print(f"✓ Valor final: R$ {valor + aumento:.2f}")
        elif escolha == 3:
            resultado = porcentagem * valor / 100
            print(f"✓ {porcentagem}% de R$ {valor:.2f} = R$ {resultado:.2f}")
        
        print("-"*50 + "\n")

    except ValueError:
        print("\n" + "-"*50)
        print("❌ ERRO: Entrada inválida. Por favor, insira apenas números.")
        print("-"*50 + "\n")   

      
def menu():
    opcao = None
    while opcao != 0:
        try:
            print("\n" + "#"*50)
            print("#" + " "*48 + "#")
            print("#" + "  CALCULADORA DE EXPRESSÕES".center(48) + "#")
            print("#" + " "*48 + "#")
            print("#"*50)
            print("\n Opções disponíveis:")
            print("\n  1 - Regra de Três")
            print("  2 - Média (Aritmética, Ponderada, Mediana)")
            print("  3 - Porcentagem (Aumento, Desconto)")
            print("\n  0 - Sair do Programa")
            print("\n" + "#"*50)

            opcao = int(input("\n➤ Digite a opção desejada: "))

            match opcao:
                case 1:
                    opcao_1()
                case 2:
                    opcao_2()
                case 3:
                    opcao_3()
                case 0:
                    print("\n" + "="*50)
                    print("Obrigado por usar a calculadora!")
                    print("="*50)
                    print("\nSaindo do programa...\n")
                    sleep(1)
                    break
                case _:
                    print("\n" + "-"*50)
                    print("❌ Opção inválida. Por favor, escolha uma opção válida.")
                    print("-"*50)
        
        except ValueError:
            print("\n" + "-"*50)
            print("❌ ERRO: Entrada inválida. Por favor, insira apenas números.")
            print("-"*50)

    return

if __name__ == "__main__":
        menu()
