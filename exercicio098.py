from time import sleep
def contagem(i, f, p):

    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for c in range(i, f + 1, p):
            sleep(0.5)
            print(f'{c} ', end='')
            c += p
    else:
        for c in range(i , f -1, -p):
            sleep(0.5)
            print(f'{c} ', end='')
            c -= p

    print()
    print('-=' * 20)

contagem(1, 10, 1)
contagem(10, 0, 2)

print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contagem(i, f, p)