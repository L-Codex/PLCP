"""
Maior Número entre Dois.py - Encontra o maior entre dois números

Descrição:
    Este script compara dois números informados pelo usuário
    e determina qual deles é o maior, ou se são iguais.
    Demonstra o uso de estruturas condicionais (if/elif/else).

Autor: Projeto PLCP - 1º Semestre
"""


def maior_numero(numero1, numero2):
    """
    Compara dois números e retorna qual é o maior.
    
    Parâmetros:
        numero1 (float): O primeiro número a ser comparado.
        numero2 (float): O segundo número a ser comparado.
    
    Retorno:
        str: Mensagem indicando qual número é maior ou se são iguais.
    """
    # Compara os dois números usando estrutura condicional
    if numero1 > numero2:
        return f"O maior número é: {numero1}"
    elif numero2 > numero1:
        return f"O maior número é: {numero2}"
    else:
        return "Os números são iguais."


def main():
    """
    Função principal do programa.
    
    Solicita dois números ao usuário e exibe qual é o maior.
    """
    try:
        # Entrada: solicita os dois números ao usuário
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        
        # Processamento: compara os números
        resultado = maior_numero(numero1, numero2)
        
        # Saída: exibe o resultado da comparação
        print(resultado)
        
    except ValueError:
        # Tratamento de erro para entrada inválida
        print("Erro: Por favor, digite valores numéricos válidos.")


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()
