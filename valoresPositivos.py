valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite um valor: '))
valor3 = float(input('Digite um valor: '))
valor4 = float(input('Digite um valor: '))
valor5 = float(input('Digite um valor: '))
valor6 = float(input('Digite um valor: '))

numeros = [valor1, valor2, valor3, valor4, valor5, valor6]

total = 0

for num in numeros:
    if num > 0:
        total += 1
        
print(f'{total} valores positivos')