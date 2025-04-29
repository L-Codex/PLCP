numero = int(input("Digite um número para ver sua tabuada: "))

print(f"\nTabuada de {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
