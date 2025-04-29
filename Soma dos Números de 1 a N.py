def calcular_soma(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma

def main():
    n = int(input("Digite um número N para calcular a soma de 1 até N: "))
    resultado = calcular_soma(n)
    print(f"A soma dos números de 1 até {n} é: {resultado}")

if __name__ == '__main__':
    main()
