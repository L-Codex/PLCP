def main():

    pilha = []
    print("Pilha inicial:", pilha)
    
    pilha.insert(0,3)
    print("Após adicionar '3':", pilha)

    pilha.insert(0,5)
    print("Após adicionar '5':", pilha)

    pilha.insert(0,7)
    print("Após adicionar '7':", pilha)

    removido = pilha.pop()
    print(f"Após remover '{removido}':", pilha)

    removido = pilha.pop()
    print(f"Após remover '{removido}':", pilha)

    pilha.insert(0,11)
    print(f"Após adicionar '11':", pilha)

    removido = pilha.pop(0)
    print(f"Após remover '{removido}':", pilha)

if __name__ == "__main__":
    main()  
