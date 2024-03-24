
numeros = list()
mai = men = 0
maiores = list()
menores = list()

for c in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = numeros[c]
    else:
        if numeros[c] > mai:
            mai = numeros[c]
        if numeros[c] < men:
            men = numeros[c]

print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == men:
        print(f'{i}... ', end='')
print()

