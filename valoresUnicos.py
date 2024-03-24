numeros = list()
cont = "s"
while cont == 's':
    n = (int(input('Digite um valor: ')))
    if n in numeros:
        print('Valor duplicado! não vou adicionar...')
    else:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    cont = str(input('Quer continuar? [S/N] ')).lower()
    numeros.sort()
print(numeros)

