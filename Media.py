"""
Media.py - Calculadora de Média Aritmética

Descrição:
    Este script calcula a média aritmética de três números
    informados pelo usuário. A média aritmética é a soma dos
    valores dividida pela quantidade de valores.

Fórmula:
    Média = (n1 + n2 + n3) / 3

Autor: Projeto PLCP
"""


def calcular_media(numero1, numero2, numero3):
    """
    Calcula a média aritmética de três números.
    
    Parâmetros:
        numero1 (float): O primeiro número.
        numero2 (float): O segundo número.
        numero3 (float): O terceiro número.
    
    Retorno:
        float: A média aritmética dos três números.
    """
    # Soma os três números e divide por 3 (quantidade de números)
    return (numero1 + numero2 + numero3) / 3


def main():
    """
    Função principal do programa.
    
    Solicita três números ao usuário e exibe a média aritmética.
    """
    try:
        # Entrada: solicita os três números ao usuário
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        numero3 = float(input("Digite o terceiro número: "))
        
        # Processamento: calcula a média dos três números
        media = calcular_media(numero1, numero2, numero3)
        
        # Saída: exibe o resultado da média
        print(f'A média é: {media}')
        
    except ValueError:
        # Tratamento de erro para entrada inválida
        print("Erro: Por favor, digite valores numéricos válidos.")


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()
