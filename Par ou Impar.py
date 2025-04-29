def verificar_paridade(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

def main():
    numero = int(input("Digite um número inteiro: "))
    resultado = verificar_paridade(numero)
    print(f"O número é {resultado}.")

if __name__ == '__main__':
    main()
