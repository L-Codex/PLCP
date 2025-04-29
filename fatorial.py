def fatorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def main():
    n = int(input('Digite um número: '))
    res = fatorial(n)
    print(f'O resultado é: {res}')

if __name__ == '__main__':
    main()
