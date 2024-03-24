'''
numeros = list()
pares = list()
impares = list()

for c in range(1, 8):
    n = (int(input(f'Digite o {c}o. valor: ')))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    numeros.append(pares)
    numeros.append(impares)

print("-=" * 30)

print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores impares digitados foram: {impares}')
'''

numeros = [[], []]

for c in range(1, 8):
    n = (int(input(f'Digite o {c}o. valor: ')))

    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print("-=" * 30)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')
