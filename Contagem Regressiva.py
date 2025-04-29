numero = int(input("Digite um número inteiro positivo para a contagem regressiva: "))

# Verifica se o número é positivo
if numero < 0:
    print("Por favor, insira um número positivo.")
else:
    # Exibe a contagem regressiva
    for i in range(numero, -1, -1):
        print(i)
