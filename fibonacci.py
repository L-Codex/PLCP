"""
fibonacci.py - Gera a sequência de Fibonacci

Descrição:
    Este script gera os primeiros N números da sequência de Fibonacci.
    A sequência começa com 0 e 1, e cada número seguinte é a soma
    dos dois anteriores.

Sequência:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

Fórmula:
    F(n) = F(n-1) + F(n-2)
    F(0) = 0, F(1) = 1

Autor: Projeto PLCP - 1º Semestre
"""


def fib(n):
    """
    Gera e exibe a sequência de Fibonacci até o n-ésimo termo.
    
    Parâmetros:
        n (int): Quantidade de termos a gerar (além dos dois primeiros).
    
    Retorno:
        None - A função apenas imprime os números na tela.
    """
    # Inicializa os dois primeiros termos
    anterior = 0
    atual = 1
    
    # Exibe os dois primeiros termos
    print(anterior)
    print(atual)
    
    # Gera os próximos n-1 termos
    for _ in range(n - 1):
        # Calcula o próximo número (soma dos dois anteriores)
        proximo = anterior + atual
        print(proximo)
        
        # Atualiza os valores para a próxima iteração
        anterior = atual
        atual = proximo


def main():
    """
    Função principal do programa.
    
    Solicita a quantidade de termos e exibe a sequência de Fibonacci.
    """
    try:
        # Entrada: solicita a quantidade de termos
        n = int(input('Digite quantos termos deseja gerar: '))
        
        # Validação: verifica se n é positivo
        if n < 1:
            print("Erro: Por favor, digite um número positivo.")
            return
        
        # Processamento e Saída: gera e exibe a sequência
        print("\nSequência de Fibonacci:")
        fib(n)
        
    except ValueError:
        # Tratamento de erro para entrada inválida
        print("Erro: Por favor, digite um número inteiro válido.")


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()