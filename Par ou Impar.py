"""
Par ou Impar.py - Verifica se um número é par ou ímpar

Descrição:
    Este script verifica se um número inteiro informado pelo usuário
    é par ou ímpar. Utiliza o operador módulo (%) para determinar
    a paridade do número.

Conceito:
    - Um número é PAR se o resto da divisão por 2 é igual a 0
    - Um número é ÍMPAR se o resto da divisão por 2 é diferente de 0

Autor: Projeto PLCP - 1º Semestre
"""


def verificar_paridade(numero):
    """
    Verifica se um número é par ou ímpar.
    
    Parâmetros:
        numero (int): O número inteiro a ser verificado.
    
    Retorno:
        str: "par" se o número for par, "ímpar" caso contrário.
    """
    # Usa o operador módulo para verificar o resto da divisão por 2
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"


def main():
    """
    Função principal do programa.
    
    Solicita um número ao usuário e exibe se é par ou ímpar.
    """
    try:
        # Entrada: solicita um número inteiro ao usuário
        numero = int(input("Digite um número inteiro: "))
        
        # Processamento: verifica a paridade do número
        resultado = verificar_paridade(numero)
        
        # Saída: exibe o resultado
        print(f"O número é {resultado}.")
        
    except ValueError:
        # Tratamento de erro para entrada inválida
        print("Erro: Por favor, digite um número inteiro válido.")


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()
