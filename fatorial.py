"""
fatorial.py - Calcula o fatorial de um número

Descrição:
    Este script calcula o fatorial de um número inteiro não-negativo
    informado pelo usuário. O fatorial é o produto de todos os
    inteiros positivos menores ou iguais a n.

Fórmula:
    n! = n × (n-1) × (n-2) × ... × 2 × 1
    0! = 1 (por definição)

Exemplos:
    5! = 5 × 4 × 3 × 2 × 1 = 120
    3! = 3 × 2 × 1 = 6

Autor: Projeto PLCP - 1º Semestre
"""


def fatorial(n):
    """
    Calcula o fatorial de um número.
    
    Parâmetros:
        n (int): O número para calcular o fatorial (deve ser >= 0).
    
    Retorno:
        int: O valor do fatorial de n.
    """
    # Inicializa o resultado como 1 (valor neutro da multiplicação)
    res = 1
    
    # Multiplica todos os números de 1 até n
    for i in range(1, n + 1):
        res *= i
    
    return res


def main():
    """
    Função principal do programa.
    
    Solicita um número ao usuário e exibe seu fatorial.
    """
    try:
        # Entrada: solicita o número ao usuário
        n = int(input('Digite um número: '))
        
        # Validação: verifica se o número é não-negativo
        if n < 0:
            print("Erro: O fatorial não é definido para números negativos.")
            return
        
        # Processamento: calcula o fatorial
        res = fatorial(n)
        
        # Saída: exibe o resultado
        print(f'O resultado é: {res}')
        
    except ValueError:
        # Tratamento de erro para entrada inválida
        print("Erro: Por favor, digite um número inteiro válido.")


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()
