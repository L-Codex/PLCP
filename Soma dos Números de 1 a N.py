# Solicita que o usuário insira um número
N = int(input("Digite um número N para calcular a soma de 1 até N: "))

# Inicializa a soma
soma = 0

# Calcula a soma dos números de 1 a N
for i in range(1, N + 1):
    soma += i

# Exibe o resultado
print(f"A soma dos números de 1 até {N} é: {soma}")