def contagem_regressiva(numero):
    if numero < 0:
        print("Por favor, insira um número positivo.")
    else:
        for i in range(numero, -1, -1):
            print(i)

def main():
    numero = int(input("Digite um número inteiro positivo para a contagem regressiva: "))
    contagem_regressiva(numero)

if __name__ == '__main__':
    main()
