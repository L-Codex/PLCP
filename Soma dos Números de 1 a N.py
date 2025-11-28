"""
Soma dos Números de 1 a N.py - Calcula a soma dos números de 1 até N

Descrição:
    Este script calcula a soma de todos os números inteiros
    de 1 até um número N informado pelo usuário.
    Demonstra o uso de laços for e acumuladores.

Fórmula alternativa:
    Soma = N × (N + 1) / 2 (Fórmula de Gauss)

Autor: Projeto PLCP - 1º Semestre
"""


def calcular_soma(n):
    """
    Calcula a soma dos números de 1 até N.
    
    Parâmetros:
        n (int): O número limite superior da soma.
    
    Retorno:
        int: A soma de todos os números de 1 até N.
    """
    # Inicializa o acumulador da soma
    soma = 0
    
    # Percorre todos os números de 1 até N (inclusive)
    for i in range(1, n + 1):
        soma += i  # Adiciona cada número ao acumulador
    
    return soma


def main():
    """
    Função principal do programa.
    
    Solicita um número N ao usuário e exibe a soma de 1 até N.
    """
    try:
        # Entrada: solicita o número N ao usuário
        n = int(input("Digite um número N para calcular a soma de 1 até N: "))
        
        # Validação: verifica se N é positivo
        if n < 1:
            print("Erro: Por favor, digite um número positivo.")
            return
        
        # Processamento: calcula a soma
        resultado = calcular_soma(n)
        
        # Saída: exibe o resultado
        print(f"A soma dos números de 1 até {n} é: {resultado}")
        
    except ValueError:
        # Tratamento de erro para entrada inválida
        print("Erro: Por favor, digite um número inteiro válido.")


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()
