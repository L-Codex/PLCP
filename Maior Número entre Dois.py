def maior_numero(numero1, numero2):
    if numero1 > numero2:
        return f"O maior número é: {numero1}"
    elif numero2 > numero1:
        return f"O maior número é: {numero2}"
    else:
        return "Os números são iguais."

def main():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    resultado = maior_numero(numero1, numero2)
    print(resultado)

if __name__ == '__main__':
    main()
