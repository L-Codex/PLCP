def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    numero = int(input("Digite um número para ver sua tabuada: "))
    print(f"\nTabuada de {numero}:")
    tabuada(numero)

if __name__ == '__main__':
    main()
