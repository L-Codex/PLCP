"""
l.py - Operações com Listas em Python

Descrição:
    Este script demonstra as principais operações que podem ser
    realizadas com listas em Python, incluindo criação, acesso,
    modificação, adição e remoção de elementos.

Operações demonstradas:
    - Iteração com for
    - Modificação de elementos por índice
    - append(): Adiciona elemento ao final
    - insert(): Insere elemento em posição específica
    - remove(): Remove primeira ocorrência de um valor
    - pop(): Remove e retorna elemento (por índice ou último)
    - del: Remove elemento por índice
    - len(): Retorna o tamanho da lista

Autor: Projeto PLCP - 1º Semestre
"""


def demonstrar_operacoes_lista():
    """
    Demonstra as principais operações com listas.
    """
    # Cria uma lista inicial
    numeros = [1, 2, 3, 4, 5]
    print("Lista inicial:", numeros)
    
    # Iteração: percorre e imprime cada elemento
    print("\n--- Iterando sobre a lista ---")
    for num in numeros:
        print(num)
    
    # Modificação: altera o elemento no índice 2
    print("\n--- Modificando elemento no índice 2 ---")
    numeros[2] = 6
    for num in numeros:
        print(num)
    
    # append(): adiciona elemento ao final da lista
    print("\n--- Após append(10) ---")
    numeros.append(10)
    for num in numeros:
        print(num)
    
    # len(): retorna o tamanho da lista
    print("\nTamanho da lista:", len(numeros))
    
    # insert(): insere elemento em posição específica
    print("\n--- Após insert(2, 8) ---")
    print("Lista antes:", numeros)
    numeros.insert(2, 8)
    print("Elemento no índice 2:", numeros[2])
    print("Lista após:", numeros)
    
    # remove(): remove primeira ocorrência de um valor
    print("\n--- Após remove(4) ---")
    print("Elemento no índice 3:", numeros[3])
    numeros.remove(4)
    print("Lista após:", numeros)
    
    # pop(): remove e retorna o último elemento
    print("\n--- Após pop() ---")
    numeros.pop()
    print("Lista após:", numeros)
    
    # del: remove elemento por índice
    print("\n--- Após del numeros[3] ---")
    del numeros[3]
    print("Lista após:", numeros)
    
    # pop(índice): remove e retorna elemento em índice específico
    print("\n--- Após pop(3) ---")
    numeros.pop(3)
    print("Lista final:", numeros)


def main():
    """
    Função principal do programa.
    """
    demonstrar_operacoes_lista()


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()
