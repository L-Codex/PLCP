def calcular_media(numero1, numero2, numero3):
    return (numero1 + numero2 + numero3) / 3

def main():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    numero3 = float(input("Digite o terceiro número: "))
    
    media = calcular_media(numero1, numero2, numero3)
    print(f'A média é: {media}')

if __name__ == '__main__':
    main()
