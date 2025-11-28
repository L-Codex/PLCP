"""
primo.py - Verifica se um número é primo

Descrição:
    Este script verifica se um número inteiro informado pelo usuário
    é um número primo. Utiliza um algoritmo otimizado que verifica
    divisores apenas até a raiz quadrada do número.

Conceito:
    Um número primo é aquele que possui exatamente dois divisores:
    1 e ele mesmo. Exemplos: 2, 3, 5, 7, 11, 13, 17, 19, 23...

Complexidade:
    O(√n) - Otimizado para verificar apenas até a raiz quadrada

Autor: Projeto PLCP - 1º Semestre
"""


def e_primo(n):
    """
    Verifica se um número é primo.
    
    Parâmetros:
        n (int): O número a ser verificado.
    
    Retorno:
        bool: True se o número for primo, False caso contrário.
    """
    # Números menores que 2 não são primos
    if n < 2:
        return False
    
    # 2 é o único número primo par
    if n == 2:
        return True
    
    # Números pares maiores que 2 não são primos
    if n % 2 == 0:
        return False
    
    # Verifica divisores ímpares até a raiz quadrada de n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def main():
    """
    Função principal do programa.
    
    Solicita um número ao usuário e verifica se é primo.
    """
    try:
        # Entrada: solicita o número ao usuário
        n = int(input('Digite um número: '))
        
        # Processamento e Saída: verifica e exibe o resultado
        if e_primo(n):
            print('É primo!')
        else:
            print('Não é primo!')
            
    except ValueError:
        # Tratamento de erro para entrada inválida
        print("Erro: Por favor, digite um número inteiro válido.")


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()