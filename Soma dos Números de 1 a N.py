N = int(input("Digite um número N para calcular a soma de 1 até N: "))

soma = 0

for i in range(1, N + 1):
    soma += i

print(f"A soma dos números de 1 até {N} é: {soma}")
