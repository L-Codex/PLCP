def e_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()  
    return palavra == palavra[::-1]  
def main():
    palavra = input('Digite uma palavra: ')
    
    if e_palindromo(palavra):
        print('A palavra é um palíndromo!')
    else:
        print('A palavra não é um palíndromo!')

if __name__ == '__main__':
    main()
