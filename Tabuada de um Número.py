# Solicita que o usuário insira um número
numero = int(input("Digite um número para ver sua tabuada: "))

# Exibe a tabuada do número
print(f"\nTabuada de {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")