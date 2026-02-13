"""
     Este programa solicita ao usuário um dos Ângulos Notáveis (30°, 45°, 60°) para o cálculo de Seno, Cosseno e Tangente. 
     Utilizando o módulo 'math' para realizar os cálculos trigonométricos de forma dinâmica, evitando o uso de valores fixos (hardcoding).

"""
import math

def calcular_trigonometria():
# Def para otimizar a organização do código.
    print("--- Calculadora de Ângulos Notáveis (30°, 45°, 60°) ---")
    
    try:
        # Try / Except para tratamento de erros na entrada do usuário.
        angulo_graus = int(input("Digite o ângulo desejado (30, 45 ou 60): "))
        
        # Validar através de if/else se o ângulo está entre os 'notáveis'.
        if angulo_graus not in [30, 45, 60]:
            print("Aviso: Este programa é otimizado para os ângulos 30, 45 e 60.")

        # O Python trabalha internamente com Radianos para cálculos trigonométricos.
        # math.radians() é a forma mais precisa de converter graus para radianos.
        angulo_rad = math.radians(angulo_graus)
 
        # Evitamos 'hardcoding' para permitir a escalabilidade do código.
        seno = math.sin(angulo_rad)
        cosseno = math.cos(angulo_rad)
        tangente = math.tan(angulo_rad)

        # Formatação de casas decimais utilizando '.2f'. 
        # Melhorando a experiência do usuário final (UX).
        print(f"\nResultados para {angulo_graus}°:")
        print(f"  - Seno:     {seno:.2f}")
        print(f"  - Cosseno:  {cosseno:.2f}")
        print(f"  - Tangente: {tangente:.2f}")

    except ValueError:
        # Caso o usuário digite texto em vez de números, o erro é capturado aqui.
        print("Erro: Por favor, digite apenas um dos números citados (30, 45 ou 60).")

if __name__ == "__main__":
    """ O bloco 'if __name__ == "__main__":'  funciona como uma trava de segurança para não executar as demonstrações ou testes deixados no arquivo original, 
        proporcionando um ambiente mais limpo e organizado para o usuário final."""

    calcular_trigonometria()
