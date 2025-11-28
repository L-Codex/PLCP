"""
Area-Circulo.py - Cálculo da Área de um Círculo

Descrição:
    Este script calcula a área de um círculo a partir do raio
    informado pelo usuário. Utiliza a constante pi do módulo math
    para maior precisão nos cálculos.

Fórmula:
    Área = π × raio²

Autor: Projeto PLCP
"""

import math


def calcular_area_circulo(raio):
    """
    Calcula a área de um círculo dado o raio.
    
    Parâmetros:
        raio (float): O raio do círculo (deve ser positivo).
    
    Retorno:
        float: A área do círculo calculada.
    """
    # Aplica a fórmula: área = pi * raio²
    area = math.pi * (raio ** 2)
    return area


def main():
    """
    Função principal do programa.
    
    Solicita o raio ao usuário, valida a entrada e exibe a área calculada.
    """
    try:
        # Entrada: solicita o valor do raio ao usuário
        raio = float(input("Digite o valor do raio: "))
        
        # Validação: verifica se o raio é positivo
        if raio < 0:
            print("Erro: O raio deve ser um valor positivo.")
            return
        
        # Processamento: calcula a área do círculo
        area = calcular_area_circulo(raio)
        
        # Saída: exibe o resultado formatado
        print(f"A área do círculo é: {area:.4f}")
        
    except ValueError:
        # Tratamento de erro para entrada inválida
        print("Erro: Por favor, digite um número válido para o raio.")


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()
