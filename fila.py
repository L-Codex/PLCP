from collections import deque

def main():
    
    fila = deque()
    print("Fila inicial:", list(fila))

    fila.append("3")
    print("Após adicionar '3':", list(fila))

    fila.append("5")
    print("Após adicionar '5':", list(fila))

    fila.append("7")
    print("Após adicionar '7':", list(fila))

    removido = fila.popleft()
    print(f"Após remover '{removido}':", list(fila))

    removido = fila.popleft()
    print(f"Após remover '{removido}':", list(fila))

    fila.append("11")
    print("Após adicionar '11':", list(fila))

    removido = fila.popleft()
    print(f"Após remover '{removido}':", list(fila))

if __name__ == "__main__":
    main()
