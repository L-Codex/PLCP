def main():

    pilha = []
    print("Pilha inicial:", pilha)
    
    pilha.append(3)
    print("Após adicionar '3':", pilha)

    pilha.append(5)
    print("Após adicionar '5':", pilha)

    pilha.append(7)
    print("Após adicionar '7':", pilha)

    removido = pilha.pop()
    print(f"Após remover '{removido}':", pilha)

    removido = pilha.pop()
    print(f"Após remover '{removido}':", pilha)

    pilha.append(11)
    print(f"Após adicionar '11':", pilha)

    removido = pilha.pop()
    print(f"Após remover '{removido}':", pilha)

if __name__ == "__main__":
    main()  
