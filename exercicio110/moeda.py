def metade(n=0, formato=False):
    res = n - (n / 2)
    return res if not formato else formatacao(res)

def dobro(n=0, formato=False):
    res = n * 2
    return res if not formato else formatacao(res)

def aumento(n=0, taxa=0, formato=False):
    res = n + ((taxa / 100) * n)
    return res if not formato else formatacao(res)

def diminuir(n=0, taxa=0, formato=False):
    res = n - ((taxa / 100) * n)
    return res if not formato else formatacao(res)


def formatacao(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(p=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{formatacao(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{taxaa}% de aumento: \t{aumento(p, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(p, taxar, True)}')
    print('-' * 30)




