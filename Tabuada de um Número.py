"""
Tabuada de um Número.py - Exibe a tabuada de multiplicação

Descrição:
    Este script exibe a tabuada de multiplicação de um número
    informado pelo usuário, mostrando as multiplicações de 1 a 10.
    Demonstra o uso de laços for e formatação de strings.

Autor: Projeto PLCP - 1º Semestre
"""


def tabuada(numero):
    """
    Exibe a tabuada de multiplicação de um número.
    
    Parâmetros:
        numero (int): O número cuja tabuada será exibida.
    
    Retorno:
        None - A função apenas imprime a tabuada na tela.
    """
    # Percorre os números de 1 a 10 para formar a tabuada
    for i in range(1, 11):
        # Calcula o resultado da multiplicação
        resultado = numero * i
        # Exibe a operação formatada
        print(f"{numero} x {i} = {resultado}")


def main():
    """
    Função principal do programa.
    
    Solicita um número ao usuário e exibe sua tabuada completa.
    """
    try:
        # Entrada: solicita o número ao usuário
        numero = int(input("Digite um número para ver sua tabuada: "))
        
        # Saída: exibe o cabeçalho e a tabuada
        print(f"\nTabuada de {numero}:")
        tabuada(numero)
        
    except ValueError:
        # Tratamento de erro para entrada inválida
        print("Erro: Por favor, digite um número inteiro válido.")


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()
