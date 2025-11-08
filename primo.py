def e_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input('Digite um número: '))

    if e_primo(n):
        print('É primo!')
    else:
        print('Não é primo!')

if __name__ == '__main__':
    main()