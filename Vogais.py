def contar_vogais(palavra):
    vogais = 'aeiouAEIOU' 
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador

def main():
    palavra = input('Digite uma palavra: ')
    qtd_vogais = contar_vogais(palavra)
    print(f'A palavra contém {qtd_vogais} vogais.')

if __name__ == '__main__':
    main()
