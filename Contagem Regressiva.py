"""
Contagem Regressiva.py - Realiza uma contagem regressiva

Descrição:
    Este script solicita um número inteiro positivo ao usuário
    e exibe uma contagem regressiva desde esse número até zero.
    Demonstra o uso de laços for com range decremental.

Autor: Projeto PLCP - 1º Semestre
"""


def contagem_regressiva(numero):
    """
    Realiza a contagem regressiva de um número até zero.
    
    Parâmetros:
        numero (int): O número inicial da contagem (deve ser positivo).
    
    Retorno:
        None - A função apenas imprime os números na tela.
    """
    # Verifica se o número é negativo
    if numero < 0:
        print("Por favor, insira um número positivo.")
    else:
        # Usa range com passo -1 para contar de numero até 0
        for i in range(numero, -1, -1):
            print(i)


def main():
    """
    Função principal do programa.
    
    Solicita um número ao usuário e inicia a contagem regressiva.
    """
    try:
        # Entrada: solicita um número inteiro positivo
        numero = int(input("Digite um número inteiro positivo para a contagem regressiva: "))
        
        # Processamento e Saída: realiza a contagem regressiva
        contagem_regressiva(numero)
        
    except ValueError:
        # Tratamento de erro para entrada inválida
        print("Erro: Por favor, digite um número inteiro válido.")


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()
