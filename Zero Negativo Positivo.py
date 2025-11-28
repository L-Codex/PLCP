"""
Zero Negativo Positivo.py - Classifica um número como zero, negativo ou positivo

Descrição:
    Este script classifica um número informado pelo usuário
    como positivo, negativo ou zero. Demonstra o uso de
    estruturas condicionais (if/elif/else) para tomada de decisão.

Autor: Projeto PLCP - 1º Semestre
"""


def verificar_sinal(numero):
    """
    Verifica o sinal de um número.
    
    Parâmetros:
        numero (float): O número a ser classificado.
    
    Retorno:
        str: "positivo", "negativo" ou "zero" conforme o valor.
    """
    # Verifica se o número é positivo, negativo ou zero
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "zero"


def main():
    """
    Função principal do programa.
    
    Solicita um número ao usuário e exibe sua classificação.
    """
    try:
        # Entrada: solicita o número ao usuário
        numero = float(input("Digite um número: "))
        
        # Processamento: verifica o sinal do número
        resultado = verificar_sinal(numero)
        
        # Saída: exibe a classificação do número
        print(f"O número é {resultado}.")
        
    except ValueError:
        # Tratamento de erro para entrada inválida
        print("Erro: Por favor, digite um valor numérico válido.")


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()
