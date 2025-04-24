def fib(n):
    anter = 0
    atual = 1
    print(anter)
    print(atual)
    for _ in range(n - 1):
        prox = anter + atual
        print(prox)
        anter = atual
        atual = prox

def main():
    n = int(input('Digite um número: '))
    fib(n)

if __name__ == '__main__':
    main()