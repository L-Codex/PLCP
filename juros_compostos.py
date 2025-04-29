def calcular_montante(p, r, t):
    m = p * (1 + r) ** t
    return m

def main():
    p = float(input("Digite o valor inicial (capital): "))
    r = float(input("Digite a taxa de juros mensal (em decimal): "))
    t = int(input("Digite o tempo em meses: "))
    montante = calcular_montante(p, r, t)
    print(f"O montante final é: {montante:.2f}")

if __name__ == '__main__':
    main()
