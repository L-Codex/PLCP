def verificar_sinal(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "zero"

def main():
    numero = float(input("Digite um número: "))
    resultado = verificar_sinal(numero)
    print(f"O
