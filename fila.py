def main():
    
    fila = []
    print("Fila inicial:", fila)

    fila.append("3")
    print("Após adicionar '3':", fila)

    fila.append("5")
    print("Após adicionar '5':", fila)

    fila.append("7")
    print("Após adicionar '7':", fila)

    removido = fila.pop(0)
    print(f"Após remover '{removido}':", fila)

    removido = fila.pop(0)
    print(f"Após remover '{removido}':", fila)

    fila.append("11")
    print("Após adicionar '11':", fila)

    removido = fila.pop(0)
    print(f"Após remover '{removido}':", fila)

if __name__ == "__main__":
    main()
