"""
Vogais.py - Conta a quantidade de vogais em uma palavra

Descrição:
    Este script conta quantas vogais existem em uma palavra
    ou frase informada pelo usuário. Considera tanto vogais
    maiúsculas quanto minúsculas.

Vogais consideradas:
    a, e, i, o, u (e suas versões maiúsculas)

Autor: Projeto PLCP - 1º Semestre
"""


def contar_vogais(palavra):
    """
    Conta a quantidade de vogais em uma palavra ou frase.
    
    Parâmetros:
        palavra (str): A palavra ou frase a ser analisada.
    
    Retorno:
        int: A quantidade de vogais encontradas.
    """
    # Define as vogais (minúsculas e maiúsculas)
    vogais = 'aeiouAEIOU'
    
    # Inicializa o contador de vogais
    contador = 0
    
    # Percorre cada letra da palavra
    for letra in palavra:
        # Verifica se a letra é uma vogal
        if letra in vogais:
            contador += 1
    
    return contador


def main():
    """
    Função principal do programa.
    
    Solicita uma palavra ao usuário e exibe a quantidade de vogais.
    """
    # Entrada: solicita a palavra ao usuário
    palavra = input('Digite uma palavra: ')
    
    # Processamento: conta as vogais
    qtd_vogais = contar_vogais(palavra)
    
    # Saída: exibe o resultado
    print(f'A palavra contém {qtd_vogais} vogais.')


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()
