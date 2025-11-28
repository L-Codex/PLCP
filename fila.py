"""
fila.py - Implementação de Fila (Queue) em Python

Descrição:
    Este script demonstra a implementação de uma estrutura de dados
    do tipo FILA (queue) usando collections.deque. Uma fila segue
    o princípio FIFO (First In, First Out) - o primeiro a entrar
    é o primeiro a sair.

Operações:
    - append(): Adiciona elemento ao final da fila (enqueue)
    - popleft(): Remove elemento do início da fila (dequeue)

Complexidade:
    - append(): O(1)
    - popleft(): O(1) (usando deque)

Autor: Projeto PLCP - 1º Semestre
"""

from collections import deque


def main():
    """
    Função principal do programa.
    
    Demonstra as operações básicas de uma fila.
    """
    # Cria uma fila vazia usando deque (double-ended queue)
    fila = deque()
    print("Fila inicial:", list(fila))

    # Adiciona elementos ao final da fila (enqueue)
    fila.append("3")
    print("Após adicionar '3':", list(fila))

    fila.append("5")
    print("Após adicionar '5':", list(fila))

    fila.append("7")
    print("Após adicionar '7':", list(fila))

    # Remove elementos do início da fila (dequeue) - FIFO
    removido = fila.popleft()
    print(f"Após remover '{removido}':", list(fila))

    removido = fila.popleft()
    print(f"Após remover '{removido}':", list(fila))

    # Continua demonstrando operações
    fila.append("11")
    print("Após adicionar '11':", list(fila))

    removido = fila.popleft()
    print(f"Após remover '{removido}':", list(fila))


# Bloco que permite a execução direta do script
if __name__ == "__main__":
    main()
