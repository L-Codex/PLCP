"""
pilha.py - Implementação de Pilha (Stack) em Python

Descrição:
    Este script demonstra a implementação de uma estrutura de dados
    do tipo PILHA (stack) usando listas Python. Uma pilha segue
    o princípio LIFO (Last In, First Out) - o último a entrar
    é o primeiro a sair.

Operações:
    - append(): Adiciona elemento ao topo da pilha (push)
    - pop(): Remove elemento do topo da pilha (pop)

Complexidade:
    - append(): O(1)
    - pop(): O(1)

Autor: Projeto PLCP - 1º Semestre
"""


def main():
    """
    Função principal do programa.
    
    Demonstra as operações básicas de uma pilha.
    """
    # Cria uma pilha vazia usando lista
    pilha = []
    print("Pilha inicial:", pilha)
    
    # Adiciona elementos ao topo da pilha (push)
    pilha.append(3)
    print("Após adicionar '3':", pilha)

    pilha.append(5)
    print("Após adicionar '5':", pilha)

    pilha.append(7)
    print("Após adicionar '7':", pilha)

    # Remove elementos do topo da pilha (pop) - LIFO
    removido = pilha.pop()
    print(f"Após remover '{removido}':", pilha)

    removido = pilha.pop()
    print(f"Após remover '{removido}':", pilha)

    # Continua demonstrando operações
    pilha.append(11)
    print(f"Após adicionar '11':", pilha)

    removido = pilha.pop()
    print(f"Após remover '{removido}':", pilha)


# Bloco que permite a execução direta do script
if __name__ == "__main__":
    main()  
