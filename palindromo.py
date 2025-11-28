"""
palindromo.py - Verifica se uma palavra é um palíndromo

Descrição:
    Este script verifica se uma palavra ou frase informada pelo usuário
    é um palíndromo. Um palíndromo é uma sequência de caracteres que
    pode ser lida da mesma forma de trás para frente.

Exemplos de palíndromos:
    - "ana"
    - "arara"
    - "radar"
    - "socorram me subi no onibus em marrocos"

Autor: Projeto PLCP - 1º Semestre
"""


def e_palindromo(palavra):
    """
    Verifica se uma palavra ou frase é um palíndromo.
    
    Parâmetros:
        palavra (str): A palavra ou frase a ser verificada.
    
    Retorno:
        bool: True se for palíndromo, False caso contrário.
    """
    # Remove espaços e converte para minúsculas para comparação
    palavra = palavra.replace(" ", "").lower()
    
    # Compara a palavra com sua versão invertida
    return palavra == palavra[::-1]


def main():
    """
    Função principal do programa.
    
    Solicita uma palavra ao usuário e verifica se é palíndromo.
    """
    # Entrada: solicita a palavra ao usuário
    palavra = input('Digite uma palavra: ')
    
    # Processamento e Saída: verifica e exibe o resultado
    if e_palindromo(palavra):
        print('A palavra é um palíndromo!')
    else:
        print('A palavra não é um palíndromo!')


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()
