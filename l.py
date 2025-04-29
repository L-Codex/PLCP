numeros = [1,2,3,4,5]
for num in numeros:
    print(num)
    
numeros [2]=6    
for num in numeros:
    print(num)
    
numeros.append(10)
for num in numeros:
    print(num)
    
print(len(numeros))

print(numeros)
numeros.insert(2,8)
print(numeros[2])
print(numeros)

print(numeros[3])
numeros.remove(4)
print(numeros)
numeros.pop()
print(numeros)

del numeros[3]
print(numeros)

numeros.pop(3)
print(numeros)

if __name__ == '__main__':
    main()
