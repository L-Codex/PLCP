"""
Ola.py - Programa básico de saudação (Hello World)

Descrição:
    Este script demonstra um programa simples de saudação em Python.
    É o primeiro programa que muitos estudantes aprendem,
    mostrando como definir funções e imprimir texto na tela.

Autor: Projeto PLCP
"""


def saudacao(nome):
    """
    Exibe uma mensagem de saudação personalizada.
    
    Parâmetros:
        nome (str): O nome da pessoa a ser saudada.
    
    Retorno:
        None - A função apenas imprime a mensagem na tela.
    """
    # Imprime a saudação utilizando f-string para formatação
    print(f"Olá, {nome}")


def main():
    """
    Função principal do programa.
    
    Define um nome padrão e chama a função de saudação.
    """
    # Define o nome a ser usado na saudação
    nome = "Lucas"
    
    # Chama a função que exibe a saudação
    saudacao(nome)


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()
