def e_primo(n):
    soma = 0
    for i in range(1, n + 1):
        if n % 1 == 0:
            soma += 1
    return soma == 2

def main():
    n = int(input('Digite um número: '))

    if e_primo(n):
        print('É primo!')
    else:
        print('Não é primo!')

if __name__ == '__main__':
    main()