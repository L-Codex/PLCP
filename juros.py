def juros_compostos(p, r, t):
    return p * (1 + r) ** t

def main():
    c = float(input('Digite o capital inicial: '))
    i = float(input('Digite a taxa de juros: ')) / 100
    t = int(input('Digite o tempo de rendimento: '))

    print(f'O montante é: {juros_compostos(c, i, t):,.2f}')

if __name__ == '__main__':
    main()